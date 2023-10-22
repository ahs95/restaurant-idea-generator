# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:54:01 2023

@author: ahs95
"""
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large", resume_download=True)
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large", resume_download=True)