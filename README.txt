SwissPairings creates an SQL database for players and tournament matches.  It protects against SQL injection attacks using Bleach.  The following functions are provided for interacting with the database and recording tournament data:

deleteMatches() : deletes all matches stored in the database
deletePlayers() : deletes all players stored in the database
countPlayers() : returns the total number of players stored in the database
registerPlayer(name) : adds a new player with the given name
playerStandings() : returns a list of players ranked by their wins
reportMatch(winner, loser) : records a match to the database
swissPairings() : generates player matchups for the next tournament round according to Swiss-system tournament rules

for more info on the Swiss-system: https://en.wikipedia.org/wiki/Swiss-system_tournament

 Instructions:

 to create database:
 1. Install Vagrant and Virtualbox if not previously installed
 2. navigate to SwissPairings folder in the terminal
 3. type 'vagrant up' and 'vagrant ssh' into terminal to enter VM
 4. navigate to folder /vagrant/tournament/ in the terminal
 5. run psql by typing 'psql'
 6. type '\i tournament.sql' to build and connect to database.

 to run tournament.py and tournament_test.py:
 6. exit psql by typing '\q'
 7. run python scripts by typing 'python tournament.py' or 'python tournament_test.py'