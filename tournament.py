#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


# shortcut for connecting to the database
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


# deletes all rows from 'matches' table and commits the changes to the database
def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches")
    db.commit()
    db.close()
    return


# deletes all rows from 'players' table and commits the changes to the database
def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players")
    db.commit()
    db.close()
    return


# displays the number of rows in the 'players' table
def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) AS num FROM players")
    players = [int(row[0]) for row in c.fetchall()]
    db.close()
    return players[0]


# adds a row to the 'players' table with a unique ID and a user-input name
# commits changes to database
def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    name = bleach.clean(name)
    name = bleach.linkify(name)
    SQL = "INSERT INTO players (name) VALUES (%s);"
    data = (name,)

    db = connect()
    c = db.cursor()
    c.execute(SQL, data)
    db.commit()
    db.close()
    return


# displays a view that ranks players by their wins
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM standings")
    standings = c.fetchall()
    db.close()
    return standings


# adds row to 'matches' table with winner and loser input by user
# commits changes to the database
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    winner = bleach.clean(winner)
    winner = bleach.linkify(winner)
    loser = bleach.clean(loser)
    loser = bleach.linkify(loser)
    SQL = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    data = (winner, loser)

    db = connect()
    c = db.cursor()
    c.execute(SQL, data)
    db.commit()
    db.close()
    return


# displays pairs of names/IDs that are adjacent in the standings
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM pairings")
    pairings = c.fetchall()
    db.close()

    matchups = []
    i = 0
    while i < (countPlayers() / 2):
        matchups.append(pairings.pop() + pairings.pop())
        i += 1

    return matchups
