import requests


def lambda_handler(event, context):
    url = event["url"]
    response = requests.get(url)
    if response.status_code == "200":
        return response.json()
    return {
        "status": f"Request failed with status code : {response.status_code}"
    }
