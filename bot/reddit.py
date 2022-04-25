import praw
import random


reddit = praw.Reddit(client_id = 'AIdL02FNEhNVRw_O3k3row',
                     client_secret = 'k7Dc9eSEtf4lRKnaWXd_UxcF6qIYtQ',
                     user_agent = 'Daves_bot_service')


def get_posts(subreddit) :
    posts = []
    for post in reddit.subreddit(subreddit).hot(limit = 50) :
        if (post.url).endswith(('.jpg', '.png', '.jpeg')) :
            posts.append(post.url)
        
    if len(posts) > 0 :
        return random.choice(posts)
    else :
        return "Aww, asi jsme nemohli nic najít, škoda."


if __name__ == '__main__' :
    print(get_posts())