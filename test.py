import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-handwritten"
headers = {"Authorization": f"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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

    # Example usage with an image file
output = query("backend/fightclub.jpg")
print(output)