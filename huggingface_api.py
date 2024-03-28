import requests

class HuggingFaceAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://huggingface.api.com/sentiment"

    def analyze_sentiment(self, text):
        """
        Analyze sentiment using the Hugging Face API.
        
        Args:
            text (str): The text to analyze.

        Returns:
            str: The sentiment analysis result.
        """
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            data = {"text": text}
            response = requests.post(self.endpoint, headers=headers, json=data)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            return response.json().get("sentiment")
        except requests.RequestException as e:
            print("Error making request to Hugging Face API:", e)
            return None
        except Exception as e:
            print("An unexpected error occurred:", e)
            return None
