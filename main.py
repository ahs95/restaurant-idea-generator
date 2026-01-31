import torch
import os
import traceback
from transformers import AutoModelForCausalLM, AutoTokenizer

model_dir = r"C:\LFM2.5-1.2B-Instruct"

try:
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
    
    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        model_dir,
        torch_dtype="auto",
        device_map="auto",
        trust_remote_code=True
    )
    print(f"Model loaded successfully on device: {model.device}")
except Exception as e:
    print(f"CRITICAL: Error loading model: {e}")
    traceback.print_exc()
    raise e

def generate_idea(cuisine, temperature=0.7):
    try:
        print(
            f"\n--- Starting Generation for {cuisine} (Temp: {temperature}) ---"
        )

        messages = [{
            "role":
            "system",
            "content":
            ("You are a creative restaurant consultant."
             "Format the output using Markdown."
             "Use a horizontal rule '---' to separate the name from the menu."
             "Use relevant emojis (e.g., 🍝, 🍱) to make the menu look attractive."
	     "Strict Rule: Do NOT include any conversational filler (like 'Let me know...')."
             )
        }, {
            "role":
            "user",
            "content":
            f"Create a catchy name and a short 3-item menu for a {cuisine} restaurant."
        }]

        inputs = tokenizer.apply_chat_template(messages,
                                               return_tensors="pt",
                                               add_generation_prompt=True).to(
                                                   model.device)

        input_ids = inputs['input_ids']

        print(f"Input tensor shape: {input_ids.shape}")

        outputs = model.generate(input_ids,
                                 max_new_tokens=256,
                                 temperature=temperature,
                                 top_p=0.9,
                                 top_k=50,
                                 repetition_penalty=1.05,
                                 do_sample=True)

        generated_text = tokenizer.decode(outputs[0][len(input_ids[0]):],
                                          skip_special_tokens=True)

        print("Generation successful.")
        return generated_text

    except Exception as e:
        print("\n!!! GENERATION FAILED !!!")
        traceback.print_exc()
        return f"Error during generation. Check the terminal for details."