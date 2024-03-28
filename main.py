from gemini_api import GeminiAPI
from huggingface_api import HuggingFaceAPI

def main():
    # Initialize API instances with your API keys
    gemini_api = GeminiAPI(api_key="your_gemini_api_key")
    huggingface_api = HuggingFaceAPI(api_key="your_huggingface_api_key")

    # Example prompt
    prompt = "Once upon a time, in a faraway land..."

    # Generate text using GEMINI API
    generated_text = gemini_api.generate_text(prompt)
    if generated_text:
        print("Generated Text:", generated_text)

        # Analyze sentiment using Hugging Face API
        sentiment = huggingface_api.analyze_sentiment(generated_text)
        if sentiment:
            print("Sentiment Analysis:", sentiment)
    else:
        print("Failed to generate text.")

if __name__ == "__main__":
    main()
