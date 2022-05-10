from fastapi import APIRouter

import nyt_top_stories_api
from constants import TOPICS

router = APIRouter()

@router.get("/topics")
def topics():
    """
    Get all available topics
    """
    return TOPICS

@router.get("/top-stories")
def top_stories(
    topic: str,
    skip: int = 0
):
    """
    Get top stories of a given topic
    """
    return nyt_top_stories_api.get_top_stories(topic, skip)