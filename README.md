# GEMINI and Hugging Face API Integration

This Python script integrates with the GEMINI and Hugging Face APIs to perform text generation and sentiment analysis tasks.

## Purpose and Overview

The purpose of this script is to demonstrate the integration with GEMINI and Hugging Face APIs for text generation and sentiment analysis respectively. It generates text based on a prompt using the GEMINI API and then analyzes the sentiment of the generated text using the Hugging Face API.

## Installation and Usage

1. Clone this repository to your local machine.
2. Install dependencies using pip:
    ```
    pip install requests
    ```
3. Replace `your_gemini_api_key` and `your_huggingface_api_key` in `main.py` with your actual API keys.
4. Run `main.py`:
    ```
    python main.py
    ```

## Prompt Choice and Analysis

For the GEMINI API prompt, the chosen example is "Once upon a time, in a faraway land...". This prompt is selected as it represents a common starting point for creative storytelling and is likely to generate diverse and imaginative text responses. 

After generating text, the sentiment of the generated text is analyzed using the Hugging Face API. The sentiment analysis results provide insights into the overall sentiment of the generated content, whether it's positive, negative, or neutral.

