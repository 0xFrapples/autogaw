import json
import random
import time
import datetime

# A giveaway program which announces the winner and time as soon as it hits 10 entrants 
# (requires a separate program to fetch entrants; can be changed to a larger/lower amount of entrants by editing ln16:col38)
def run():
    
    try:
        enterfile = open('enter.json')
        enterdata = json.load(enterfile)
    except FileNotFoundError:
        enterwrite = str('{"entrants": []}')
        with open('enter.json', "w") as enterout:
            enterout.write(enterwrite)
        return run()

    try:
        winfile = open('winners.json')
        windata = json.load(winfile)
    except FileNotFoundError:
        winwrite=str('{"winners": [], "datetime": []}')
        with open('winners.json', "w") as winout:
            winout.write(winwrite)
        return run()

    # Waits until json list gets 10 variables
    while len(enterdata["entrants"])<10:
        time.sleep(0.1)
        try:
            enterfile = open('enter.json')
            enterdata = json.load(enterfile)
        except FileNotFoundError:
            enterwrite = str('{"entrants": []}')
            with open('enter.json', "w") as enterout:
                enterout.write(enterwrite)
            return run()

    # Picks a random entrant from the enter.json file and prints it
    randwin=random.randint(0,len(enterdata["entrants"])-1)
    winner=enterdata["entrants"][randwin]
    timern=datetime.datetime.now()
    print(f"The winner is {winner} -", timern)

    winnerlist = windata["winners"]
    datetimelist = windata["datetime"]

    winnerlist.append(winner)
    datetimelist.append(str(timern))
        
    winlist ={
        'winners': winnerlist,
        'datetime': datetimelist
    }

    with open('winners.json', 'w') as fp:
        json.dump(winlist, fp)

    clearlist ={
        'entrants': []
    }

    with open('enter.json', 'w') as fp:
        json.dump(clearlist, fp)


    return run()

try:
    run()
except KeyboardInterrupt: 
    print(f"\nKeyboard interruption called. Shutting down."); exit()