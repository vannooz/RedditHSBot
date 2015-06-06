def getRarity(card):
    rarity = card.get("rarity")
    if rarity is None:
        return ""
    if rarity == "Free" :
        return "Basic"
    return rarity

def getClass(card):
    playerClass = card.get("playerClass")
    if playerClass is None :
        return "Neutral"
    return playerClass

def getAttack(card):
    if card.get("attack") is None :
       return ""
    return " " + str(card["attack"])

def getHealth(card):
    hp = card.get("health")
    if  hp is not None :
        return "/" + str(hp)
    durability = card.get("durability")
    if durability is not None :
        return "/" + str(durability)
    return ""

NEW_LINE = '  \n'
DISCLAIMER = '^(Created by a BOT to help new players. Reply for suggestions/comments)' + NEW_LINE + "^(Trial run)" + NEW_LINE

def getFistLines(card) :
    return "**" + card["name"] + "**" + NEW_LINE + getRarity(card) + " " + getClass(card) + " card" + NEW_LINE

def getSecondLines(card) :
    return str(card["cost"]) + " mana" + getAttack(card) + getHealth(card) + " " + card["type"]+ NEW_LINE

def getText(card) :
    text = card.get("text")
    if text is None :
       return ""
    return text.replace("<b>", "**").replace("</b>", "**")



def cardPrinter(card) :
    return getFistLines(card) + getSecondLines(card) + getText(card) + " \n"



class PrettyCardText:
    def __init__(self):
        pass

    def getPrettyText(self, card):
        return cardPrinter(card)

    def getPrettyPost(self, cards):
        post = ''

        for card in cards:
            post = post + self.getPrettyText(card);
            post = post + NEW_LINE + '----------------------------------------------' + NEW_LINE

        post = post + DISCLAIMER
        return post



