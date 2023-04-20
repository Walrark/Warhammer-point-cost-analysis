# What I want to do is take the information off of wahapedia to make a system which
# ranks units by their stat/cost ratio with a weight given by some arbitrary value
import numpy as np

# What do I need to do this?
# creat data sheets as a dictionary
# assign weight values to stats (ideally by a probability)
# compare the cost to stat in an (ordered) list

#to make things more accurate to the game i must include a list of all the weapons and take some averages to compair survivability
#potential problem with the weapons: different units pay different points for the same weapons

#maybe i can plot average damage vs smlt(space marine like target) against point cost

#Weapons
Example_weapon = {'Points': 10,
                  'R':12,
                  'Type':'Pistol',
                  'STR':8,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A':1,
                  'AB':'None'}

Fusion_Pistol = {'Points': 10,
                  'R':6,
                  'Type':'Pistol',
                  'STR':8,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A':1,
                  'AB':'None'}

Shuriken_Rifle = {'Points': 0,
                  'R':24,
                  'Type':'Rapid Fire',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A':1,
                  'AB':'Shuriken'}

Shuriken_Cannon = {'Points': 10,
                  'R':24,
                  'Type':'Heavy',
                  'STR':6,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':2,
                  'A':3,
                  'AB':'Shuriken'}

Wraithcannon = {'Points': 15,
                  'R':18,
                  'Type':'Assualt',
                  'STR':10,
                  'AP':4,
                  'D(rand)':3,
                  'D(con)':3,
                  'A':1,
                  'AB':'None'}

Eldar_Weapons =[Fusion_Pistol,Shuriken_Cannon,Shuriken_Rifle,Wraithcannon]
#members
Example_member = {'Points': 10,
                  'M':6,
                  'WS':4/6,
                  'BS':4/6,
                  'STR':3,
                  'T':3,
                  'W':1,
                  'A':1,
                  'LD':8,
                  'SV':2/6}

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

autarch = {
    'Points': 85,
    'M': 7,
    'WS': 5/6,
    'BS': 5/6,
    'STR': 3,
    'T': 3,
    'W': 5,
    'A': 5,
    'LD': 9,
    'SV': 4/6}

corsair_voidscarred = {
    'Points': 12,
    'M': 7,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 1,
    'A': 3,
    'LD': 7,
    'SV': 3/6}

voidscarred_felarch = {
    'Points': 12,
    'M': 7,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 1,
    'A': 4,
    'LD': 8,
    'SV': 3/6}

shade_runner = {
    'Points': 20,
    'M': 7,
    'WS': 5/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 1,
    'A': 4,
    'LD': 7,
    'SV': 3/6}

soul_weaver = {
    'Points': 20,
    'M': 7,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 1,
    'A': 3,
    'LD': 8,
    'SV': 3/6}

way_seeker = {
    'Points': 25,
    'M': 7,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 1,
    'A': 3,
    'LD': 8,
    'SV': 3/6}


#units
Corsair_Voidscarred = [corsair_voidscarred,voidscarred_felarch,shade_runner,soul_weaver,way_seeker]
Autarch = [autarch]
WraithLord = [wraithlord]
Guardian_Defenders =[Guardian_Defender,Heavy_Weapon_Platfrom]
#army
Eldar = [WraithLord,Guardian_Defenders,Autarch,Corsair_Voidscarred]

#notes for me:
#if T=2*STR for an attack then 1/6 if T>S => 2/6 if T=S => 3/6 if T<S => 4/6 if 2T=S => 5/6
#if 3 A and WS = 3/6 then 1.5 hits


#with new data type we should be able to simplify a lot of our functions
#want a function which takes the army list and hands off the units to another function which
#hands off to another function to use the weights for each unit

def army_list_value(army):
    #this function takes an army list and returns a list by highest point to cost ratio to the lowest
    z = np.zeros((len(army),5))
    for i in range(0,len(army)):
       z[i] = unit_handle(army[i])
    return z


def unit_handle(unit):
    #this function take the unit given from the army and returns a list of the point to cost ratio of each member
    z = np.zeros(5)
    for i in range(0,len(unit)):
        z[i] =  member_value(unit[i])
    return  z

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
    return x

def m_cost(val):
    #given a move value returns a weighted value
    x = val['M']
    w = 2
    return w * x

def ws_cost(val):
    #given a ws value returns a weighted value
    x = val['WS']
    w = (val['STR'] * 0.8 + x * val['A'])/2
    print(w)
    return x * w

def bs_cost(val):
    #given a bs value returns a weighted value
    #This value depends on the ranged weapon but this app. doesn't include weapons
    x = val['BS']
    w = 18
    return x * w

def str_cost(val):
    #given a str value returns a weighted value
    x = val['STR']
    w = (val['A'] * val['WS'])/2
    return x * w

def t_cost(val):
    #given a t value returns a weighted value
    #Ideally I want to feed in some values of weapons and then give distinct T a value
    x = val['T']
    w = val['W']
    if x % 2 == 0:
        y = x + 1
    else: y = x + 0.5
    return (y * w)/2

#print(t_cost(Heavy_Weapon_Platfrom))
#print(t_cost(wraithlord))



def w_cost(val):
    #given a w value returns a weighted value
    x = val['W']
    w = val['T']
    return (x * w)/2

def a_cost(val):
    #given a a value returns a weighted value
    x = val['A']
    w = (val['STR'] * 0.8 + x * val['WS']) / 3
    return w * x

def ld_cost(val):
    #given a ld value returns a weighted value
    x = val['LD']
    return x

def sv_cost(val):
    #given a sv value returns a weighted value
    x = val['SV']
    w = val['W']
    return x * w

print(unit_handle(WraithLord))
print(unit_handle(Guardian_Defenders))
print(army_list_value(Eldar))
