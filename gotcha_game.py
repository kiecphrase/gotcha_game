import random as r
import doggies_data as dog

def rollCheck(rolled, success):
    if rolled >= success:
        return True
    return False

def pull(cap):
    return(r.randint(0, cap))

def success():
    roll = r.randint(1, dog.dogSuccess["max"])

    if rollCheck(roll, dog.dogSuccess["deity"]):
        rarity_alert = '[DEITY]'
        pulled_item = str(dog.dogDeity[pull(len(dog.dogDeity)-1)])

    elif rollCheck(roll, dog.dogSuccess["legendary"]):
        rarity_alert = '[LEGENDARY]'
        pulled_item = str(dog.dogLegendary[pull(len(dog.dogLegendary)-1)])
    
    elif rollCheck(roll, dog.dogSuccess["ultra"]):
        rarity_alert = '[ULTRA]'
        pulled_item = str(dog.dogUltra[pull(len(dog.dogUltra)-1)])

    elif rollCheck(roll, dog.dogSuccess["rare"]):
        rarity_alert = '[RARE]'
        pulled_item = str(dog.dogRare[pull(len(dog.dogRare)-1)])

    elif rollCheck(roll, dog.dogSuccess["uncommon"]):
        rarity_alert = '[UNCOMMON]'
        pulled_item = str(dog.dogUncommon[pull(len(dog.dogUncommon)-1)])

    else:
        rarity_alert = '[COMMON]'
        pulled_item = str(dog.dogCommon[pull(len(dog.dogCommon)-1)])

    s = rarity_alert + '\nyou got a ' + pulled_item

    return s


def fail():
    return "Oh no! You got nothing :("

def gotcha_pull():
    x = r.randint(0, 100)

    if x > 60:
        return success()
    else:
        return fail()