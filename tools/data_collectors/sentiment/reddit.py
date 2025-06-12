import praw
import os
from dotenv import load_dotenv

load_dotenv()

print("Client ID:", os.getenv("REDDIT_CLIENT_ID"))
print("Client Secret:", os.getenv("REDDIT_CLIENT_SECRET")[:10] + "..." if os.getenv("REDDIT_CLIENT_SECRET") else "None")
print("User Agent:", os.getenv("REDDIT_USER_AGENT"))


reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def get_reddit_posts(subreddit_names, search_terms, time_filter="week", limit=5):
    print(f"Searching for '{search_terms}' in /r/{subreddit_names}")
    for subreddit_name in subreddit_names:
        subreddit = reddit.subreddit(subreddit_name)
        posts = list(subreddit.search(search_terms, time_filter=time_filter, limit=limit))
        print(f"Found {len(posts)} posts for '{search_terms}' in /r/{subreddit_name}")
        for post in posts:
            print(f"  Score: {post.score:4d} | {post.title[:60]}...")
            print(f"  Upvotes: {post.ups}")
            print(f"  Downvotes: {post.downs}")

    return posts


#posts = get_reddit_posts(["stocks", "investing", "wallstreetbets"], ["Apple", "AAPL", "$AAPL"], time_filter="week", limit=5)






