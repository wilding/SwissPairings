

-- create and connect to database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


-- list of players
CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name TEXT
);


-- list of completed matches
CREATE TABLE matches (
	winner INT REFERENCES players(id),
	loser INT REFERENCES players(id),
	PRIMARY KEY(winner, loser)
);


-- list of each player's total wins
CREATE VIEW wins
	AS SELECT players.id, count(matches.winner) AS wins
	FROM players LEFT JOIN matches
	ON matches.winner = players.id
	GROUP BY players.id
	ORDER BY players.id;


-- list of each player's total matches
CREATE VIEW totalmatches
	AS SELECT players.id, count(matches.*) AS matches
	FROM players LEFT JOIN matches
	ON matches.loser = players.id OR matches.winner = players.id
	GROUP BY players.id
	ORDER BY players.id;


-- list of players including both wins and matches played
CREATE VIEW standings
	AS SELECT players.id, players.name, wins.wins, totalmatches.matches
	FROM players JOIN wins ON players.id = wins.id JOIN totalmatches ON wins.id = totalmatches.id
	ORDER BY wins.wins DESC;


-- standings view without wins and matches
CREATE VIEW pairings
	AS SELECT players.id, players.name
	FROM players JOIN wins ON players.id = wins.id JOIN totalmatches ON wins.id = totalmatches.id
	ORDER BY wins.wins DESC;
