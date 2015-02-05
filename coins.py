'''
    Random experiment for question on quora
    x = heads after 99 toss
    y = heads after 100 toss

    What's the probability of x < y

    Link: http://www.quora.com/Person-A-tosses-a-coin-99-times-and-gets-x-heads-Person-B-tosses-a-coin-100-times-and-gets-y-heads-What-is-the-probability-that-x-is-less-than-y
'''

def toss_coin():
    from random import random

    if random() > 0.5: return 1
    else: return 0

def heads(n):
    total = 0
    for x in range(n):
        total += toss_coin()
    return total

def test(n):
    win = 0

    for x in range(n):
        a = heads(99)
        b = heads(100)

        if a < b: win += 1

    return float(win)/n

if __name__== "__main__":
    print test(10000)
