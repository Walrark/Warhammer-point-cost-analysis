# What I want to do is take the information off of wahapedia to make a system which
# ranks units by their stat/cost ratio with a weight given by some arbitrary value
import webbrowser

# What do I need to do this?

# scrape wahapedia
# creat data sheets as an array
# assign weight values to stats (ideally by a probability)
# compare the arrays based on their point to ability cost

# test:  https://wahapedia.ru/wh40k9ed/factions/aeldari/Corsair-Voidscarred
import numpy as np
import linalg as la
#give save as percent to save and chances to hit
#Want to use dictionaries for the statblocks instead of these arrays


Heading = ['Points','M','WS','BS','STR','T','W','A','LD','SV']
Weight_Vector = [1 ,0.4 ,0.6 ,0.6 ,0.4,0.8,0.8,0.6,0.3,2 ]
#Example_stat = ['Example Unit',10,6,4,4,3,3,1,1,8,2/6]

#Guardian_Defenders= np.array([['Guardian_Defenders',9 ,7 ,3 ,3 ,3 ,3 ,1 ,1 ,7 ,3/6 ],
#                        ['Heavy_Weapon_Platfrom',20 ,7 ,6 ,3 ,3,3 ,2 ,1 ,7 ,4/6 ]])

wraithlord = {'Points': 100,
    'M': 8,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 7,
    'T': 8,
    'W': 9,
    'A': 4,
    'LD': 9,
    'SV': 4/6}

Heavy_Weapon_Platfrom = {'Points': 20,
    'M': 7,
    'WS': 1/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 2,
    'A': 1,
    'LD': 7,
    'SV': 4/6}

Guardian_Defender = {
    'Points': 9,
    'M': 7,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 1,
    'A': 1,
    'LD': 7,
    'SV': 3/6}
WraithLord = [wraithlord]
Guardian_Defenders =[Guardian_Defender,Heavy_Weapon_Platfrom]


Eldar = [WraithLord,Guardian_Defenders]


#with new data type we should be able to simplify a lot of our functions
#want a function which takes the army list and hands off the units to another function which
#hands off to another function to use the weights for each unit



def army_list_value(army):
    #this function takes an army list and returns a list by highest point to cost ratio to the lowest
    for i in range(0,len(army)):
        #unit_handle(army[i])
        return None



def unit_handle(unit):
    #this function take the unit given from the army and returns a list of the point to cost ratio of each member
    for i in range(0,len(unit)):
        #member_value(unit[i])
        return  None

#'Points','M','WS','BS','STR','T','W','A','LD','SV'

def member_value(member):
    #This function adds the values of each stat and divides by the cost
    x = ((m_cost(member)
    + ws_cost(member)
    + bs_cost(member)
    + str_cost(member)
    + t_cost(member)
    + w_cost(member)
    + a_cost(member)
    + ld_cost(member)
    + sv_cost(member))/member['Points'])
    return None

def m_cost(val):
    #given a move value returns a weighted value
    x = val['M']
    w = 2
    return w * x

def ws_cost(val):
    #given a ws value returns a weighted value
    x = val['WS']
    w = (val['STR'] * 0.8 + val['A'] * 2)/2
    return x * w

def bs_cost(val):
    #given a bs value returns a weighted value
    x = val['BS']
    w = 18
    return x * w

def str_cost(val):
    #given a str value returns a weighted value
    x = val['STR']
    w = (val['WS'] + val['A'])
    return 0

def t_cost(val):
    #given a t value returns a weighted value
    x = val['T']
    w = val['W']
    return (x * w)/2

def w_cost(val):
    #given a w value returns a weighted value
    x = val['W']
    w = val['T']
    return (x * w)/2

def a_cost(val):
    #given a a value returns a weighted value
    x = val['A']
    return 0

def ld_cost(val):
    #given a ld value returns a weighted value
    x = val['LD']
    return 0

def sv_cost(val):
    #given a sv value returns a weighted value
    x = val['SV']
    return 0