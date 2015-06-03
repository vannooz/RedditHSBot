from HSDictionary import HearthstoneDictionary
from pprint import pprint
from PrettyCardText import PrettyCardText
import praw

def RedditBot
reddit = praw.Reddit(user_agent = "testuseragent")
submissions = reddit.get_subreddit('hearthstone').get_new(limit=10)
for submission in submissions:
    #pprint(vars(submission))
    print submission.title
    print "\n\n\n"

hsDict = HearthstoneDictionary("AllSets.enUS.json")
    #while True:
    #card = raw_input("Enter the card name (quit to exit):");
    #if(card == "quit"):
    #    break
#print(PrettyCardText().getPrettyText(hsDict.getCard(card)))
