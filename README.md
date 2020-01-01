# CARD WAR Game #
#### Description, assumption and use cases. ####
1. Deck of 52 cards.
2. Number of players is 2.
3. Each player plays a card. Higher card wins. Winner takes both cards.
4. If players tie(war), then each player puts down three cards(bonus cards). 4th card is put down for compete. 
   If tie(war), continue doing this until tie is broken. Winner takes all cards.
   If a player don't have enough cards to complete the war, that player loses. 
   If neither player has enough cards, the one who runs out first loses. If both run out simultaneously, it's a draw.
5. Game is over when a player doesn't have any cards. The player with
   cards remaining is the winner.
   
#### New Can be features: ####
1. Making the game for 3-4 players and different variations like Casino-war
2. Making the game as web app.
3. Hosting as a server less application and hosting on cloud.
4. Creating a DB to keep track of the players all plays history.
5. Make a CICD pipeline for future features.
6. Creating a CT(continuous testing) frame work for the WAR App.
7. At the end creating a mkdoc for the project.

#### How to use the APP? ####
1. Install python3
2. `git clone https://github.com/agnibrata86/WarGamePyProj.git`
3. `cd <gitcloned folder>/WarGamePyProj`
4. Run as below:
```
$ python3 start.py
Enter Names of Player1 and Player2 with comma separated: <Player1_Name>, <Player2_Name>
```
