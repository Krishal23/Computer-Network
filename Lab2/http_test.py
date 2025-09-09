import requests

def send_get_request(url):
    try:
        response = requests.get(url, timeout=5) 
        response.raise_for_status()  # HTTPError for bad responses
        print("\n GET Request")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text, "...")  
    except requests.exceptions.RequestException as e:
        print("GET request failed:", e)


def send_post_request(url, data):
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()
        print("\nPOST Request")
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        print("Body:", response.text[:300], "...")
    except requests.exceptions.RequestException as e:
        print("POST request failed:", e)


if __name__ == "__main__":
    # Using JSONPlaceholder test API (free to use)
    get_url = "https://jsonplaceholder.typicode.com/posts/1"
    post_url = "https://jsonplaceholder.typicode.com/posts"

    # Send GET request
    send_get_request(get_url)

    # Send POST request with sample data
    sample_data = {
        "title": "test",
        "body": "This is a test post TEST TEST TEST",
        "userId": 131
    }
    send_post_request(post_url, sample_data)