import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

class EmailRewriter:
    """
    Rewrites emails using Hugging Face's Featherless AI Completion API.
    """

    _API_URL = "https://router.huggingface.co/featherless-ai/v1/completions"

    def __init__(self):
        """
        Initializes the API with Hugging Face token from environment or passed explicitly.

        Args:
            hf_token (Optional[str]): Hugging Face access token. If not provided, reads from HF_TOKEN env.
        """
        self.headers = {
            "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
            "Content-Type": "application/json"
        }

    def rewrite(self, draft: str, tone: str, model = "mistralai/Devstral-Small-2507") -> str:
        """
        Rewrite the given draft email into the specified tone.

        Args:
            draft (str): The original email content.
            tone (str): Desired tone ("formal", "friendly", etc.).
            model (Optional[str]): Optional model name to specify. Defaults to router behavior.

        Returns:
            str: The rewritten email.
        """
        prompt = self._build_prompt(draft, tone)

        payload = {
                    "prompt": prompt,
                    "temperature": 0.7,
                    "max_tokens": 300
                  }

        if model:
            payload["model"] = model

        response = requests.post(self._API_URL, headers=self.headers, json=payload)
        return self._parse_response(response)

    def _build_prompt(self, draft: str, tone: str) -> str:
        return (
            f"[INST] You are an expert email writer. "
            f"Rewrite the following email in a {tone} tone:\n\n"
            f"{draft.strip()}\n\n"
            f"Respond only with the rewritten email. [/INST]"
        )


    def _parse_response(self, response: requests.Response) -> str:
        if response.status_code != 200:
            raise RuntimeError(f"Featherless API call failed: {response.status_code}, {response.text}")

        try:
            data = response.json()
            return data["choices"][0]["text"].strip()
        except (KeyError, ValueError) as e:
            raise RuntimeError(f"Unexpected response format: {e}, Content: {response.text}")


# if __name__ == "__main__":
#     rewriter = EmailRewriter()

#     draft = "Hey, are we still on for the meeting tomorrow? Let me know if anything changes."
#     tone = "very polite"

#     try:
#         rewritten = rewriter.rewrite(draft, tone)
#         print("Rewritten Email:\n")
#         print(rewritten)
#     except Exception as e:
#         print(f"Error: {e}")