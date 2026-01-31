import gradio as gr
from main import generate_idea
import requests
import urllib.parse
from PIL import Image
import io
import random 
import re

def generate_logo_image(restaurant_name):
    # Prompt creates a symbol influenced by the name's style
    # We explicitly ask for NO TEXT so the AI focuses purely on the visual icon
    prompt = f"Minimalist restaurant symbol, {restaurant_name} style, icon, white background, vector style, high contrast, NO TEXT, NO LETTERS, NO WORDS"
    
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        
        seed = random.randint(1, 1000000)
        
        params = {
            "width": 1024,
            "height": 1024,
            "seed": seed, 
            "nologo": "true",
            "model": "flux", 
            "negative": "blurry text, misspelled, messy, complex, distorted, words, letters, typography" 
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if "image" in content_type:
                # Simply return the image as is, without drawing text on it
                image = Image.open(io.BytesIO(response.content))
                return image
            else:
                print(f"API returned non-image: {response.text[:200]}")
                return None
        else:
            print(f"HTTP Error: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def format_response(cuisine, temperature):
    idea_text = generate_idea(cuisine, temperature)
    
    # Get all non-empty lines
    lines = [line.strip() for line in idea_text.split('\n') if line.strip()]
    
    clean_name = "The Restaurant" # Fallback default
    
    if lines:
        # Step 1: Find the actual Name line (skip headers)
        name_index = 0
        first_line_lower = lines[0].lower()
        if "name" in first_line_lower or "menu" in first_line_lower or "concept" in first_line_lower:
            if len(lines) > 1:
                name_index = 1
        
        # Step 2: Get the raw name
        raw_name = lines[name_index]
        
        # Remove Markdown bolding
        clean_name = raw_name.replace('*', '').strip()
        
        # Step 3: Remove Taglines/Descriptions
        for separator in [" – ", " — ", " - "]:
            if separator in clean_name:
                clean_name = clean_name.split(separator)[0].strip()
                break

        # Step 4: Remove Emojis from the prompt
        # This regex targets standard Unicode emoji ranges
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # Emoticons
            "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
            "\U0001F1E0-\U0001F1FF"  # Flags
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE
        )
        clean_name = emoji_pattern.sub(r'', clean_name)
        clean_name = clean_name.strip() # Remove any trailing whitespace left behind

    # Generate the image with the cleaned name
    image_pil = generate_logo_image(clean_name)
    
    return idea_text, image_pil

with gr.Blocks() as demo:
    gr.Markdown("# 🍽️ Restaurant Idea Generator")
    gr.Markdown("Powered by **LFM2.5-1.2B-Instruct** & **Pollinations AI**. Click the download icon to save the logo!")
    
    with gr.Row():
        cuisine_dropdown = gr.Dropdown(
            choices=["Bangladeshi", "Arab", "Turkish", "Korean", "Japanese", "Pakistani", "Fusion"], 
            label="Select Cuisine", 
            value="Bangladeshi"
        )
        
        temp_slider = gr.Slider(
            minimum=0.1, 
            maximum=1.0, 
            value=0.8, 
            label="Creativity (Temperature)", 
            info="Higher = More creative/random"
        )
        
    generate_btn = gr.Button("Generate Idea", variant="primary")
    
    with gr.Row():
        with gr.Column():
            output_text = gr.Markdown(label="Generated Concept")
        with gr.Column():
            output_image = gr.Image(label="Generated Logo Concept (Downloadable)", type="filepath")

    generate_btn.click(
        fn=format_response, 
        inputs=[cuisine_dropdown, temp_slider], 
        outputs=[output_text, output_image]
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())