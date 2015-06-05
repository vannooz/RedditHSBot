from HSDictionary import HearthstoneDictionary
from pprint import pprint
from PrettyCardText import PrettyCardText
import praw
import os


def getEnv(name) :
    value = os.environ.get(name)
    if value is None:
        value = raw_input(name+" ")
    return value

reddit = praw.Reddit(user_agent = "testuseragent")
login = getEnv('REDDIT_LOGIN')
passw = getEnv('REDDIT_PASSWORD')
reddit.login(login,passw)



class redditBot :
    def __init__(self):
        pass

    def getLatestPosts(self):
        return reddit.get_subreddit('hsnoobot').get_new(limit=10)

for submission in redditBot().getLatestPosts():
    pprint(vars(submission))
#    print submission.title
    print "\n\n\n"

