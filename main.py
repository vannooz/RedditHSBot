from HSDictionary import HearthstoneDictionary
from pprint import pprint
from PrettyCardText import PrettyCardText
from redditBot import RedditBot
from time import sleep


def prerocess(cards):
    cardsToRemove = []
    for card1 in cards:
        for card2 in cards:
            if card1["name"].find(card2["name"]) > 1:
                cardsToRemove.append(card2)
    for card in cardsToRemove :
        cards.remove(card)
    return cards


hsDict = HearthstoneDictionary("AllSets.enUS.json")
latestTimeStamp = 0.0
redditBot = RedditBot()
while True:
    try:
        newLatestTimestamp = latestTimeStamp
        for submission in redditBot.getLatestPosts():
            try:
                cards = []
                submissionCreated = submission.created
                if submissionCreated <= latestTimeStamp :
                    continue
                if submissionCreated > newLatestTimestamp:
                    newLatestTimestamp = submissionCreated

                for key in hsDict.keys() :
                    if key in submission.title.lower() or key in submission.selftext.lower():
                        cards.append(hsDict.getCard(key))
                cards = prerocess(cards)
                if cards:
                    print PrettyCardText().getPrettyPost(cards)
                    #redditBot.postComment(submission, PrettyCardText().getPrettyPost(cards))
                    print "submission done"
            except:
                print "error Processing submission latestTimestamp " + str(latestTimeStamp) + " newtimestamp " + str(newLatestTimestamp) + "\n submission " + submission.title
        latestTimeStamp = newLatestTimestamp
    except:
        print "error in processing batch latest timestamp " + str(latestTimeStamp)
    sleep(15 * 60) #sleep 15 mins
