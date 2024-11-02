import random
from DistributionCalculator import initUniformProbabilities, composeProbabilities
from fractions import Fraction
import math


class Player:
    def __init__(self, money, givenBets):
        self.money = money
        self.givenBets = givenBets
    
    def __str__(self):
        return f"Player has ${self.money}"


d6 = initUniformProbabilities(1, 6)
dicePair = composeProbabilities(d6, d6)

def generateRandomDice():
    return random.randint(1, 6)

def playOneRound(player: Player):
    val1, val2, val3, val4 = (generateRandomDice(), generateRandomDice(), generateRandomDice(), generateRandomDice())
    player2Val = val3 + val4
    bet = player.givenBets.get(val1, 0) * player.money
    player1Val = val1 + val2
    if player1Val > player2Val:
        player.money += bet
    if player1Val < player2Val:
        player.money -= bet


def playMultipleRounds(numRounds):
    givenBets = {1: 0, 2: 0, 3: 0, 4: 0.2, 5: 0.4, 6: 0.6}

    player = Player(100, givenBets)

    for i in range(numRounds):
        playOneRound(player)

    return player


average = 0
number = 0
for i in range(100):
    player = playMultipleRounds(1000)
    average = (average * number + math.log(player.money)) / (number + 1)
    number += 1

print(average)

    
    
























# def testGenerateFromDistribution():
#     seen = {}
#     attempts = 100000
#     for i in range(attempts):
#         val = generateRandomFromDistribution()
#         seen[val] = seen.get(val, 0) + 1


#     for key in sorted(seen.keys()):
#         print(f"{key} occured {seen[key]} times. This means it happened with probabiliity {Fraction(seen[key], attempts)} or {seen[key] / attempts}")