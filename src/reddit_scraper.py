import praw
import os
from src.logger import logging
from src.exception import PersonaException
from dotenv import load_dotenv
load_dotenv()
import sys

# Reddit API credentials

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_AGENT = os.getenv("REDDIT_AGENT", "langgraph persona bot")

# Function to fetch user data from Reddit
def fetch_user_data(username, limit=20):
    """Fetches posts and comments from a Reddit user."""
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_SECRET,
            user_agent=REDDIT_AGENT
        )

        user = reddit.redditor(username)

        posts = []
        comments = []

        for post in user.submissions.new(limit=limit):
            posts.append({
                "type": "post",
                "title": post.title,
                "body": post.selftext,
                "url": post.permalink
            })
        logging.info(f"Fetched {len(posts)} posts for user {username}")

        for comment in user.comments.new(limit=limit):
            comments.append({
                "type": "comment",
                "body": comment.body,
                "url": comment.permalink
            })
        logging.info(f"Fetched {len(posts)} posts and {len(comments)} comments for user {username}")

        return posts + comments
    except Exception as e:
        logging.error(f"Error fetching data for user {username}: {e}")
        raise PersonaException(f"Failed to fetch data for user {username}", sys)
