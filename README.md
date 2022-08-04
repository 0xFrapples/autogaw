# Automated Giveaways
A CLI giveaway application/add-on written in Python that announces the winner once amount of entrants has reached a certain amount.

### How does it work?

There is an `.enter.json` file, where all the entrant data is stored at, and `main.py` reads data from it. Once a certain amount of entrants reaches a given number (in this case 10), a random one gets picked as a winner, the winner gets logged into `.winners.json` file (along with the date and time of winning) and entrant list gets erased for the next giveaway all immediately. You can also use `fetch.py` to view the winner history.

### What is the purpose?

This application is useful for people who have a lot to give away but cannot be bothered to set up many small giveaways everytime. It could also be used for smart contracts if you want to set up automated giveaways. 

### Pre-requisites

In order to make automatic giveaways work, you would need the following:

 - An application that would write entrants to the `enter.json` file.
 - `python3`
 - And, obviously, a dedicated host/server to run this on

To run the application, you have to follow the steps below:

- `cd /path/to/dir` in terminal, where you downloaded this app to
- `python main.py` to execute automated giveaways
- `python fetch.py` to fetch winner's information

### Notes

Files `.enter.json` and `.winners.json` are not meant to be modified and it's not recommended editing them unless you know what you are doing.


###### Feel free to modify/redistribute the code for any use. Made with <3 by Frapples

