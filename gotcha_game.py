import random as r
import doggies_data as dog
import elements_data as ele

def rollCheck(rolled, success):
    if rolled >= success:
        return True
    return False

def pull(cap):
    return(r.randint(0, cap))


def dog_pull():
    roll = r.randint(1, dog.Success["max"])

    if rollCheck(roll, dog.Success["deity"]):
        rarity_alert = '[DEITY]'
        pulled_item = str(dog.Deity[pull(len(dog.Deity)-1)])

    elif rollCheck(roll, dog.Success["legendary"]):
        rarity_alert = '[LEGENDARY]'
        pulled_item = str(dog.Legendary[pull(len(dog.Legendary)-1)])

    elif rollCheck(roll, dog.Success["ultra"]):
        rarity_alert = '[ULTRA]'
        pulled_item = str(dog.Ultra[pull(len(dog.Ultra)-1)])

    elif rollCheck(roll, dog.Success["rare"]):
        rarity_alert = '[RARE]'
        pulled_item = str(dog.Rare[pull(len(dog.Rare)-1)])

    elif rollCheck(roll, dog.Success["uncommon"]):
        rarity_alert = '[UNCOMMON]'
        pulled_item = str(dog.Uncommon[pull(len(dog.Uncommon)-1)])

    else:
        rarity_alert = '[COMMON]'
        pulled_item = str(dog.Common[pull(len(dog.Common)-1)])

    return [rarity_alert, pulled_item]

def element_pull():
    roll = r.randint(1, ele.Success["max"])

    if rollCheck(roll, ele.Success["deity"]):
        rarity_alert = '[DEITY]'
        pulled_item = str(ele.Deity[pull(len(ele.Deity)-1)])

    elif rollCheck(roll, ele.Success["legendary"]):
        rarity_alert = '[LEGENDARY]'
        pulled_item = str(ele.Legendary[pull(len(ele.Legendary)-1)])

    elif rollCheck(roll, ele.Success["ultra"]):
        rarity_alert = '[ULTRA]'
        pulled_item = str(ele.Ultra[pull(len(ele.Ultra)-1)])

    elif rollCheck(roll, dog.Success["rare"]):
        rarity_alert = '[RARE]'
        pulled_item = str(ele.Rare[pull(len(ele.Rare)-1)])

    elif rollCheck(roll, ele.Success["uncommon"]):
        rarity_alert = '[UNCOMMON]'
        pulled_item = str(ele.Uncommon[pull(len(ele.Uncommon)-1)])

    else:
        rarity_alert = '[COMMON]'
        pulled_item = str(ele.Common[pull(len(ele.Common)-1)])

    return [rarity_alert, pulled_item]

def success():
    g = r.randint(1,2)

    if g == 1:
        ret = dog_pull()
    
    elif g == 2:
        ret = element_pull()


    s = ret[0] + '\nyou got a ' + ret[1]

    return s


def fail():
    return "Oh no! You got nothing :("

def gotcha_pull():
    x = r.randint(0, 100)

    if x > 60:
        return success()
    else:
        return fail()