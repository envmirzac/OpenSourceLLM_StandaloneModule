from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    content: str

@app.post("/process/")
async def process_message(message: Message):
    try:
        # Here, you're posting directly to the Ollama API.
        response = requests.post(
            'http://ollama:11434/api/generate',  # Ollama service URL
            json={
                "model": "tinyllama",
                "prompt": message.content,
                "stream": False  # Assuming you don't need a streaming response
            }
        )
        response.raise_for_status()  # This will raise an HTTPError if the request returned an unsuccessful status code

        result = response.json()
        return {
            "processed_content": result['response'],
            # Include more details if needed
        }
    except requests.HTTPError as e:
        # Log the error for debugging purposes
        print(f"HTTP Error: {e.response.text}")
        # You might want to return a more generic error message to the user
        # depending on the nature of the error and security considerations
        raise HTTPException(status_code=e.response.status_code, detail="Error processing message.")

    except requests.RequestException as e:
        print(f"Request Exception: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")
