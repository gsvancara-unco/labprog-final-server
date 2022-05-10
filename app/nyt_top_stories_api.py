import requests

from constants import BASE_URL, PAGINATION
from config import settings
from response_model import Image, Story

def get_top_stories(topic: str, skip: int):
    # default results
    total_results = 0
    results = []
    message = "An error occured in the NYT Top Stories API"

    # execute request to NYT API
    request_url = f"{BASE_URL}/{topic}.json?api-key={settings.API_KEY}"
    response = requests.get(request_url)
    
    # successful response
    if response.status_code == 200:
        # parse response
        response_data = response.json()
        response_results = response_data["results"]

        # reduce results according to pagination
        limited_results = response_results[skip:skip+PAGINATION]

        # assemble results
        total_results = response_data["num_results"]
        for result in limited_results:
            results.append({
                "image_small": Image(**result["multimedia"][2]),
                "image_large": Image(**result["multimedia"][1]),
                "story": Story(**result)
            })
        message = f"NYT {topic} Top Stories"
    
    # return results
    return {
        "total_results": total_results,
        "data": results,
        "message": message
    }