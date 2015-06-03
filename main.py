from HSDictionary import HearthstoneDictionary
from pprint import pprint
from PrettyCardText import PrettyCardText

hsDict = HearthstoneDictionary("AllSets.enUS.json")
while True:
    card = raw_input("Enter the card name (quit to exit):");
    if(card == "quit"):
        break
    print(PrettyCardText().getPrettyText(hsDict.getCard(card)))
