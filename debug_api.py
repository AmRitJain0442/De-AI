import requests
import json

try:
    response = requests.post(
        "http://localhost:8000/api/generate-lesson",
        json={"topic": "Tic Tac Toe"}
    )
    with open("debug_output.txt", "w") as f:
        f.write(response.text)
    print("Response written to debug_output.txt")
except Exception as e:
    print(f"Request failed: {e}")
