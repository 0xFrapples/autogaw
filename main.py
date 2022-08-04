import json
import random
import time
import datetime

# A giveaway program which announces the winner and time as soon as it hits 10 entrants 
# (requires a separate program to fetch entrants; can be changed to a larger/lower amount of entrants by editing ln16:col38)
def run():
    try: 
        # Imports address.json data to this script
        f = open('.enter.json')
        data = json.load(f)

        # Waits until json list gets 10 variables
        while len(data["entrants"])<10:
            time.sleep(0.1)
            f = open('.enter.json')
            data = json.load(f)

        # Picks a random variable from the json file and prints it
        a=random.randint(0,len(data["entrants"])-1)
        winner=data["entrants"][a]
        t=datetime.datetime.now()
        print(f"The winner is {winner} -", t)

        # Prepares data to append to winners.json
        w = open('.winners.json')
        wdata = json.load(w)

        wlist = wdata["winners"]
        dtlist = wdata["datetime"]

        wlist.append(winner)
        dtlist.append(str(t))
        
        # Prepared data to be appended
        wl ={
            'winners': wlist,
            'datetime': dtlist
        }

        with open('.winners.json', 'w') as fp:
            json.dump(wl, fp)

        # An empty list to dump to address.json
        l ={
            'entrants': []
        }

        # Clears the json file and writes a newly created dict to it
        with open('.enter.json', 'w') as fp:
            json.dump(l, fp)

    # Prevents KeyboardInterrupt from being raised
    except KeyboardInterrupt: 
        print(f"\nKeyboard interruption called. Shutting down.")
        exit()

    return run()

run()