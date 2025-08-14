## ATM
'''data = {
    '1234': {'balance': 45678, 'pin': 123, 'history': []},
    '5678': {'balance': 56789, 'pin': 123, 'history': []},
    '5690': {'balance': 98760, 'pin': 123, 'history': []},
    '5612': {'balance': 45678, 'pin': 123, 'history': []},
    '2345': {'balance': 19876, 'pin': 123, 'history': []},
    '6789': {'balance': 1999999, 'pin': 123, 'history': []}
}

def check_balance():'''

###
import sys
import platform
import math
import random
import collections

###import sys
print(sys.argv)
print(sys.exit(0))
print(sys.path)

##import platform
print(platform.system)
print(platform.version)
print(platform.processor)

###import math
print(math.sqrt(25))###OUTPUT-->5
print(math.pow(3,2))###OUTPUT-->9
print(math.fabs(-25))###OUTPUT-->25
print(math.floor(25.8))###OUTPUT-->25
print(math.cos(90))
print(math.ceil(25.1))###OUTPUT-->26
print(math.sin(45))
print(math.degrees(25))## radiance to degree
print(math.pi)###OUTPUT-->3.14

###import random
print(random.random(1,6))
print(random.uniform(1,6))
l =["pardhu","dattu","tarak","mounish","hemanth"]
print(random.choice(l))
print(random.choices(l,k=3))
random.shuffle(l)
print(l)

###import collection
import collections
l =["pardhu","dattu","tarak","mounish","hemanth","pardhu"]
c = collections.Counter(l)
print(c)

### PLAYING DICE USING RANDOM
import random

pardhu_score = 0
dattu_score = 0

while pardhu_score < 100 and dattu_score < 100:
    # Pardhu's turn
    Start = input("Pardhu Turn [c]ontinue and [s]top: ")
    if Start == 'c':
        pardhu_turn = random.randint(1, 6)
        pardhu_score += pardhu_turn
        print(f"Pardhu score: {pardhu_score} - Dice: {pardhu_turn}")
        if pardhu_score >= 100:
            print("😎🤩😎 Pardhu is the winner 😎🤩😎")
            break
    else:
        print("Dattu wins by forfeit!")
        break

    # Dattu's turn
    beat = input("Dattu Turn [c]ontinue and [s]top: ")
    if beat == 'c':
        dattu_turn = random.randint(1, 6)
        dattu_score += dattu_turn
        print(f"Dattu score: {dattu_score} - Dice: {dattu_turn}")
        if dattu_score >= 100:
            print("😤🫢🫢 Dattu is the winner 😤🫢🫢")
            break
    else:
        print("Pardhu wins by forfeit!")
        break


## SNAKE AND LADDER GAME
import random

sandy_score = 0
pardhu_score = 0

snakes = {10: 6, 16: 2, 25: 4, 63: 20, 96: 1, 86: 30, 47: 18, 49: 4, 89: 10}
ladders = {3: 22, 5: 8, 11: 26, 20: 29, 27: 56, 36: 44, 51: 67, 71: 92, 78: 98, 87: 94}

while pardhu_score < 100 and sandy_score < 100:
    # Pardhu's turn
    s = input("Pardhu -- [c]ontinue or [e]xit: ")
    if s.lower() == 'c':
        dice = random.randint(1, 6)
        pardhu_score += dice
        if pardhu_score in snakes:
            pardhu_score = snakes[pardhu_score]
            print(f"🐍 Pardhu got bitten by a snake! Score: {pardhu_score} , Dice: {dice}")
        elif pardhu_score in ladders:
            pardhu_score = ladders[pardhu_score]
            print(f"🪜 Pardhu climbed a ladder! Score: {pardhu_score} , Dice: {dice}")
        else:
            print(f"Pardhu's Score: {pardhu_score}, Dice: {dice}")

        if pardhu_score >= 100:
            print("😎🤩😎 Pardhu is the winner! 😎🤩😎")
            break
    else:
        break

    # Sandy's turn
    t = input("Sandy -- [c]ontinue or [e]xit: ")
    if t.lower() == 'c':
        dice = random.randint(1, 6)
        sandy_score += dice
        if sandy_score in snakes:
            sandy_score = snakes[sandy_score]
            print(f"🐍 Sandy got bitten by a snake! Score: {sandy_score} , Dice: {dice}")
        elif sandy_score in ladders:
            sandy_score = ladders[sandy_score]
            print(f"🪜 Sandy climbed a ladder! Score: {sandy_score} , Dice: {dice}")
        else:
            print(f"Sandy's Score: {sandy_score}, Dice: {dice}")

        if sandy_score >= 100:
            print("😎🤩😎 Sandy is the winner! 😎🤩😎")
            break
    else:
        break