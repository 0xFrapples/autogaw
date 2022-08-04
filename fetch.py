import json

# Imports winners.json 
f = open('.winners.json')
data = json.load(f)
n = len(data['winners'])

# Function to fetch winner's data with a given index
def run():
    try:
        if n!=1:
            a=int(input(f"Please enter a winner's index (from 1 to {n}): "))
            if a<1 or a>n:
                print("Index out of range!")
                return run()
        else:
            a=1
    
    except ValueError:
        print("Invalid index!")
        return run()
    
    print(f"\nWinner information: \n{'-'*20} \nIndex: {a} \nWinner: {data['winners'][a-1]} \nTimestamp: {data['datetime'][a-1]} \n{'-'*20}")

# Running the function
try:
    if n==0:
        print("No winners were found. Stopping.")
    else:
        run()
except KeyboardInterrupt:
    print("\nAborted.")