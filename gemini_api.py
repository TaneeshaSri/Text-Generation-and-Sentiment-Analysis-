import requests

class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://gemini.api.com/generate"

    def generate_text(self, prompt):
        """
        Generate text using the GEMINI API.
        
        Args:
            prompt (str): The prompt for text generation.

        Returns:
            str: The generated text.
        """
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            data = {"prompt": prompt}
            response = requests.post(self.endpoint, headers=headers, json=data)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            return response.json().get("generated_text")
        except requests.RequestException as e:
            print("Error making request to GEMINI API:", e)
            return None
        except Exception as e:
            print("An unexpected error occurred:", e)
            return None
