import praw

reddit = praw.Reddit(
    client_id="gsX9I1clR0zJAYQzeI25KQ",
    client_secret="DQ9QGZrmvHZd3iwjMZOQrq9WHBxTKg",
    user_agent="windows:reddit_reader:1.0.0 (by u/Rich-Dust3014)"
)

def get_posts(sub, count, span):
    subreddit = reddit.subreddit(sub)
    posts = []
    for submission in subreddit.top(span, limit=count):
        if "r/" not in submission.title and "reddit" not in submission.title:
            posts.append(submission)

    return posts


def scrapeComments(subreddit, count, span):
    posts = get_posts(subreddit, count, span)
    postText = []
    #postText = [posts[0],posts[0].selftext]
    for i in range(count):
        try:
            postText.append([posts[i],posts[i].selftext])
        except:
            print("End of comment list")
    return postText

if __name__ == "__main__":
    post = scrapeComments("detrans", 1, "day")
    print(post)
    print(post[0].author)
