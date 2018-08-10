#create a series of possible history of win and losses
#See how well the kv performs
#Compare it to other possible strategies
#
#Strategies:
#
#1 Using expected winning (a previous exp showed that if positive, bet 100%)
#2 Using a fix mount (Need two different constant amount compare)
#3 Random bets
#4 Randomly choosen strategy for each bet
#
#Assumptions:
#
#Starting purse is 100 (100%)
#
#Fixed amounts are: 5 and 25
#
#Random bets ranges (0%-75%)

from kelly_criterion import kelly_value as kv

def game():
    """
    Create a bet with random probability of winning, p and price of b when won
    """

    from random import random

    p, b = random(), random() * 10

    return p, b


def getKV (p, b):

    return kv(p, b)

def sample_history(max_length = 10000):

    from random import random

    history = 0

    while history < max_length:
        yield random()
        history += 1


