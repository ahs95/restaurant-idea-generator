# 🍽️ Restaurant Idea Generator

An intelligent, dual-powered AI application that generates creative restaurant concepts, complete with catchy names, curated menus, and professional logo designs.

Built by combining the privacy and speed of **Local LLMs** with the visual creativity of **Cloud-based Image Generation**.

![Demo](https://img.shields.io/badge/Status-Stable-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

*   **Creative Text Generation:** Powered by **LFM2.5-1.2B-Instruct** to generate unique restaurant names and 3-item menus.
*   **Visual Logo Creation:** Integrated with **Pollinations AI** (Flux model) to generate high-quality, minimalist logo concepts based on the restaurant name.
*   **Hybrid Architecture:** Runs text generation locally on your CPU (Offline & Private) while fetching images via API (Cloud).
*   **Interactive UI:** Built with **Gradio** for a seamless, user-friendly experience.
*   **Customizable Control:** A creativity slider to adjust the randomness of the text generation.
*   **Markdown Output:** Concepts are displayed with rich formatting (bolding, emojis) for better readability.
*   **Downloadable Assets:** Generated logos are ready to be saved to your device with a single click.

## 🛠️ Tech Stack

- **🤗 Model:** [LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct) (Liquid AI) - Optimized for fast CPU inference.
- **🎨 Image:** Pollinations AI (Flux Model) - High-quality, free image generation.
- **⚡ Framework:** Gradio (Web UI) & Transformers (Model Inference).
- **🐍 Language:** Python 3.8+

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ahs95/restaurant-idea-generator.git
cd restaurant-idea-generator
```

### 2. Install Dependencies
Ensure you have Python installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```
*(Or manually install: `pip install torch transformers gradio requests pillow`)*

### 3. Download the Model
The application is configured to use the **LFM2.5-1.2B-Instruct** model.

1.  Visit the [Model Page](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct).
2.  Download the model weights using `git lfs` or the "Download" button.
3.  **Important:** Place the downloaded model files into a folder named `LFM2.5-1.2B-Instruct` inside your project directory.
    *   *Alternatively, update the `model_dir` path in `main.py` to point to where you saved the model on your machine.*

## 💻 Usage

Run the application using Python:

```bash
python app.py
```

The interface will launch locally (usually at `http://127.0.0.1:7860`).

### How to Use
1.  **Select Cuisine:** Choose a type of food (e.g., Turkish, Japanese, Fusion).
2.  **Adjust Creativity:** Move the slider to change how "wild" the ideas are.
3.  **Generate:** Click the button to see your concept.
4.  **Save:** Click the download icon on the logo image to save the high-res file.

## 🧠 How It Works

1.  **Text Engine:** The app runs `LFM2.5-1.2B-Instruct` locally on your CPU. It creates a structured response containing a Name and a Menu.
2.  **Image Engine:**
    *   The app intelligently extracts the Restaurant Name from the text (removing emojis and taglines).
    *   It sends a prompt to Pollinations AI requesting a minimalist symbol based on the name's style.
    *   The result is displayed side-by-side with the text.

## 📁 Project Structure

```text
restaurant-idea-generator/
├── main.py               # Model logic, text generation, and image processing
├── app.py                # Gradio interface setup
├── LFM2.5-1.2B-Instruct/ # Folder containing the local LLM weights
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 📝 Future Improvements

- [ ] Add a "Regenerate" button for images only.
- [ ] Support for custom negative prompts.
- [ ] Multi-language support for the UI.

## 🤝 Credits

- **Text Model:** [Liquid AI](https://huggingface.co/LiquidAI)
- **Image Model:** [Pollinations AI](https://pollinations.ai/)
- **UI:** [Gradio](https://www.gradio.app/)

***

### Suggestion
You might want to create a `requirements.txt` file to match your README so users can install dependencies easily. Here is the content for that file:

```text
torch
transformers
gradio
requests
Pillow
huggingface_hub
```
