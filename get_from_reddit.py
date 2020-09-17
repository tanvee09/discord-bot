import praw
import random


reddit = praw.Reddit(client_id = '<INSERT CLIENT ID HERE>',
                     client_secret = '<INSERT CLIENT SECRET HERE>',
                     user_agent = '<INSERT USER AGENT HERE>')


def get_posts(subreddit = 'meme') :
    posts = []
    for post in reddit.subreddit(subreddit).hot(limit = 50) :
        if (post.url).endswith(('.jpg', '.png', '.jpeg')) :
            posts.append(post.url)
        else :
            posts.append(post.title + '\n' + post.selftext)
    if len(posts) > 0 :
        return random.choice(posts)
    else :
        return "Aww, seems like we couldn't find anything for you. That's sad."


if __name__ == '__main__' :
    print(get_posts())