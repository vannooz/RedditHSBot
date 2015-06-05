from HSDictionary import HearthstoneDictionary
from pprint import pprint
from PrettyCardText import PrettyCardText
import praw
import os


reddit = praw.Reddit(user_agent = "testuseragent")
login = os.environ.get('REDDIT_LOGIN')
passw = os.environ.get('REDDIT_PASSWORD')
reddit.login(login,passw)
submissions = reddit.get_subreddit('hsnoobot').get_new(limit=10)

for submission in submissions:
    #pprint(vars(submission))
    print submission.title
    print "\n\n\n"

hsDict = HearthstoneDictionary("AllSets.enUS.json")
pprint(hsDict)
    #while True:
    #card = raw_input("Enter the card name (quit to exit):");
    #if(card == "quit"):
    #    break
#print(PrettyCardText().getPrettyText(hsDict.getCard(card)))


