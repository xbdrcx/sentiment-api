import requests, json, uuid

def send_test_event():
    url = "http://localhost:8000/analyze"

    event_data = {
        "text": "I love using FastAPI for building AI apps!",
    }

    headers = {
        "Content-Type": "application/json",
    }

    # Send POST request to the endpoint
    response = requests.post(url=url, data=json.dumps(event_data), headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print(f"Full Response Headers: {response.headers}")

if __name__ == "__main__":
    send_test_event()
