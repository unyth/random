#In an one time b:1 bet. How much money should you bet?
#According to Kelly Criterion, you should bet f* (% of current bankroll)
#f* = (bp-q)/b
#p = probability of winning
#q = 1 - p
#b = wager
# Let's test it out
#
#b is scale so that the bet is always 1
#e.g. 3:2 => 1.5:1

def kelly_value (p, b):
    #In essence, Kelly Criterion suggest that you should bet % of
    #your assets equal to expected return / potential return

    q = 1 - p

    f = (b * p - q) / b

    if f < 0:
        return 0 #It's a game that's not worth betting

    else:
        return f



