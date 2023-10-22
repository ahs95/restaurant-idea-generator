# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:28:43 2023

@author: ahs95
"""
import streamlit as st
from main import tokenizer, model
st.title("Restaurant Idea Generator App")
# Streamlit app interface with dropdown menu
selected_cuisine = st.selectbox("Select a cuisine:", ["Bengali", "Indian", "Italian", "Mexican", "Japanese"])
generate_button = st.button("Generate Ideas")

if generate_button:
    if selected_cuisine:
        # Use the selected_cuisine for model input and generate restaurant name
        input_text = f"Create a fancy restaurant name for {selected_cuisine}."
        input_ids = tokenizer.encode(input_text, return_tensors="pt")

        # Generate text for restaurant name
        output_name = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
        generated_name = tokenizer.decode(output_name[0], skip_special_tokens=True)
        st.write("Generated Restaurant Name:")
        st.write(generated_name)

        # Use the selected_cuisine to generate food menus
        # You can create a similar input text with selected_cuisine for menus
        menu_input_text = f"Create a food menu for {selected_cuisine}."
        menu_input_ids = tokenizer.encode(menu_input_text, return_tensors="pt")

        # Generate text for food menus
        output_menus = model.generate(menu_input_ids, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)
        
        st.write("Generated Food Menus:")
        for i, menu_output in enumerate(output_menus):
            generated_menu = tokenizer.decode(menu_output, skip_special_tokens=True)
            st.write(f"Menu {i + 1}:")
            st.write(generated_menu)










