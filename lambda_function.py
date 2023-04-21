import requests


def lambda_handler(event, context):
    url = event["url"]
    print("Calling requests")
    response = requests.get(url)
    if response.status_code == "200":
        print("Congrats! So proud of you!")
        return response.json()
    return {
        "status": f"Request failed with status code : {response.status_code}"
    }
