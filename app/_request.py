import requests, json

def test_analysis():
    url = "http://localhost:8000/analyze"

    text_data = [
        {
            "text": "I love using FastAPI for building AI apps!"
        },
        {
            "text": "This test doesn't seem right."
        },
        {
            "text": "Yet another test for this awesome API"
        }
    ]

    headers = {
        "Content-Type": "application/json",
    }

    # Send POST request to the endpoint
    response = requests.post(url=url, data=json.dumps(text_data), headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print(f"Full Response Headers: {response.headers}")

if __name__ == "__main__":
    test_analysis()
