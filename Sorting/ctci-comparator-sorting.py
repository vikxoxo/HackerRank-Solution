"""
https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem
Comparators are used to compare two objects. In this challenge, 
you'll create a comparator and use it to sort an array. 
The Player class is provided in the editor below. It has two fields:

: a string.
: an integer.
Given an array of  Player objects, write a comparator that sorts them in order of decreasing score. 
If  or more players have the same score, sort those players alphabetically ascending by name. 
To do this, you must create a Checker class that implements the Comparator interface, 
then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. 
In short, when sorting in ascending order, a comparator function returns  if ,  if , and  if .

Declare a Checker class that implements the comparator method as described.
It should sort first descending by score, then ascending by name. 
The code stub reads the input, creates a list of Player objects, 
uses your method to sort the data, and prints it out properly.

Example
 

Sort the list as . Sort first descending by score, then ascending by name.

Input Format

The first line contains an integer, , the number of players.
Each of the next  lines contains a player's  and , a string and an integer.
"""

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name}{str(self.score)}"
        
    def comparator(a, b):
        if a.score<b.score:
            return 1
        elif a.score>b.score:
            return -1
        elif a.name>b.name:
            return 1
        elif a.name<b.name:
            return -1
        else:
            return 0

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
