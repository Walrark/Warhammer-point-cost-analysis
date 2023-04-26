# What I want to do is take the information off of wahapedia to make a system which
# ranks units by their stat/cost ratio with a weight given by some arbitrary value
import numpy as np
import matplotlib.pyplot as plt
# What do I need to do this?
# creat data sheets as a dictionary
# assign weight values to stats (ideally by a probability)
# compare the cost to stat in an (ordered) list

#to make things more accurate to the game i must include a list of all the weapons and take some averages to compair survivability
#potential problem with the weapons: different units pay different points for the same weapons

#maybe i can plot average damage vs smlt(space marine like target) against point cost

Example_weapon = {'Points': 10,
                  'R':12,
                  'Type':'Pistol',
                  'STR':8,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A(rand)': 6,
                  'A(con)': 0,
                  'AB':'None'}


#Weapons
#some problems with how im currently doing the weapons
#1: different weapon profiles
#Option 2 (probably better version)
Sunburst = {'Points': 20,
                  'R':48,
                  'Type':'Heavy',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 6,
                  'A(con)': 0,
                  'AB':'Blast'}
Starshot = {'Points': 20,
                  'R':48,
                  'Type':'Heavy',
                  'STR':8,
                  'AP':2,
                  'D(rand)':6,
                  'D(con)':0,
                  'A(rand)': 0,
                  'A(con)': 1,
                  'AB':'None'}
Aeldari_Missle_Launcher = [Sunburst,Starshot]

#2: melee weapons

#option 2:
Example_melee2 = {'Points': 10,
                  'Type':'Melee',
                  'STR':2,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':0,
                  'A(rand)': 0,
                  'A(con)': 1,
                  'AB':'None'}
# if I use range=0 in my melee weapons I can consider them the same as ranged weapons
#otherwise I have to check if the weapon has type melee or not

#I think I will have to check the type either way to use it for weapon skill instead of ballistic skill

#3: In order to accurately construct a value for each unit I need them to have their weapon profiles
#I think the only way to do that properly is to do the following

Example_Unit_With_Weapons = {'Points': 10,
                  'M':6,
                  'WS':4/6,
                  'BS':4/6,
                  'STR':3,
                  'T':3,
                  'W':1,
                  'A':1,
                  'LD':8,
                  'SV':2/6,
                  'Weapon':[Example_melee2,Example_weapon]}
#then I have 2 questions about this style
#1: how does this affect how I calculate my values
#- should I have a list based on the weapons for each member in each unit?


Power_Glaive = {'Points': 0,
                  'Type':'Melee',
                  'STR':2,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}

Diresword = {'Points': 0,
                  'Type':'Melee',
                  'STR':1,
                  'AP':0,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'*'}

Shuriken_Pistol = {'Points': 0,
                  'R':12,
                  'Type':'Pistol',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 0,
                  'A(con)': 1,
                  'AB':'Shuriken'}

Avenger_Shuriken_Catapult = {'Points': 0,
                  'R': 18,
                  'Type':'Assault',
                  'STR':4,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 0,
                  'A(con)': 3,
                  'AB':'Shuriken'}

Plasma_Grenade = {'Points': 0,
                  'R':6,
                  'Type':'Grenade',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 6,
                  'A(con)': 0,
                  'AB':'Blast'}

Fusion_Pistol = {'Points': 10,
                  'R':6,
                  'Type':'Pistol',
                  'STR':8,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}

Shuriken_Rifle = {'Points': 0,
                  'R':24,
                  'Type':'Rapid Fire',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'Shuriken'}

Shuriken_Cannon = {'Points': 10,
                  'R':24,
                  'Type':'Heavy',
                  'STR':6,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(con)':3,
                  'A(rand)':0,
                  'AB':'Shuriken'}

Wraithcannon = {'Points': 15,
                  'R':18,
                  'Type':'Assualt',
                  'STR':10,
                  'AP':4,
                  'D(rand)':3,
                  'D(con)':3,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}

Aeldari_Flamer= {'Points': 5,
                  'R':12,
                  'Type':'Assault',
                  'STR':4,
                  'AP':0,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':6,
                  'AB':'None'}
Bright_Lance = {'Points': 10,
                  'R':48,
                  'Type':'Heavy',
                  'STR':8,
                  'AP':4,
                  'D(rand)':3,
                  'D(con)':3,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}

Corsair_Blaster = {'Points': 10,
                  'R':18,
                  'Type':'Assault',
                  'STR':8,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':0,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}

D_Cannon = {'Points': 20,
                  'R':24,
                  'Type':'Heavy',
                  'STR':12,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A(con)':0,
                  'A(rand)':3,
                  'AB':'None'}

D_Scythe = {'Points': 10,
                  'R':12,
                  'Type':'Assault',
                  'STR':10,
                  'AP':4,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':6,
                  'AB':['Blast','*']}
Death_Spinner = {'Points': 0,
                  'R':12,
                  'Type':'Assault',
                  'STR':6,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':6,
                  'AB':'Blast'}
Doomweaver = {'Points': 0,
                  'R':48,
                  'Type':'Heavy',
                  'STR':7,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(con)':0,
                  'A(rand)':12,
                  'AB':'Blast'}
Dragon_Fusion_Gun = {'Points': 0,
                  'R':12,
                  'Type':'Assault',
                  'STR':9,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}


Eldar_Melee_Weapons = [Diresword,Power_Glaive]
Eldar_Ranged_Weapons = [Fusion_Pistol,Shuriken_Cannon,Shuriken_Rifle,Wraithcannon,Avenger_Shuriken_Catapult,
                        Shuriken_Pistol,Plasma_Grenade,Aeldari_Missle_Launcher,Dragon_Fusion_Gun,Bright_Lance,
                        Doomweaver,Death_Spinner,D_Scythe,D_Cannon]

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

dire_avenger = {'Points': 13,
                  'M':7,
                  'WS':4/6,
                  'BS':4/6,
                  'STR':3,
                  'T':3,
                  'W':1,
                  'A':2,
                  'LD':8,
                  'SV':3/6,
                  'Weapon':[Avenger_Shuriken_Catapult,Plasma_Grenade]}

dire_avenger_exarch = {'Points': 10,
                  'M':7,
                  'WS':4/6,
                  'BS':4/6,
                  'STR':3,
                  'T':3,
                  'W':2,
                  'A':3,
                  'LD':8,
                  'SV':3/6,
                  'Weapon':[Shuriken_Pistol,Avenger_Shuriken_Catapult,Diresword,Power_Glaive,Plasma_Grenade]}

#units
Corsair_Voidscarred = {'Name': 'Corsair_Voidscarred',
    'Member':[corsair_voidscarred,voidscarred_felarch,shade_runner,soul_weaver,way_seeker]}
Autarch = {'Name': 'Autarch',
    'Member':[autarch]}
WraithLord = {'Name': 'WraithLord',
    'Member':[wraithlord]}
Guardian_Defenders ={'Name': 'Guardian_Defenders',
    'Member':[Guardian_Defender,Heavy_Weapon_Platfrom]}
Dire_Avengers = {'Name': 'Dire_Avengers',
    'Member':[dire_avenger,dire_avenger_exarch]}

#army
Eldar = [WraithLord,Guardian_Defenders,Autarch,Corsair_Voidscarred,Dire_Avengers]

#notes for me:
#if T=2*STR for an attack then 1/6 if T>S => 2/6 if T=S => 3/6 if T<S => 4/6 if 2T=S => 5/6
#if 3 A and WS = 3/6 then 1.5 hits

#This section will be for the function which gives insight into the weapons of each unit


#doesnt handle multi profile weapons (yet)
def Weapon_Value(lst):
    #Want this function to evaluate ranged weapons (melee needs unit STR)
    #Take a list of weapons and gives back an array of doubles which gives
    #(average chance to wound spacemarine, average damage to spacemarine)
    NA = []
    for i in range(0,len(lst)):
        if type(lst[i]) == list:
            for j in range(0,len(lst[i])):
                x = make_double((lst[i])[j])
                NA.append(x)
        else:
            x = make_double(lst[i])
            NA.append(x)
    return NA

def make_double(weap):
    #take a weapon, gives back a double:(average chance to wound spacemarine, average damage to spacemarine)
    if weap['Type'] == 'Melee':
        return None
    else:
        i = Chance_To_Wound(weap)
        j = Avg_Damage(weap)
        return (i,j)

def Chance_To_Wound(weap):
    #give the chance to wound (after hitting) with the average number of attacks (if there's a random attack char.)
    T=4
    SV=4/6
    S = weap['STR']
    AP = weap['AP']
    Ac = weap['A(con)']
    Ar = weap['A(rand)']
    if Ar == 0:
        AR = 0
    else:
        AR = ((Ar/2)+(Ar/2)+1)/2
    A = Ac + AR
    if  SV - (AP/6)<0:
        MSV = 0
    else:
        MSV = SV - (AP/6)
    if (2*S)<=T:
        x = A*((1/6) * (1 - MSV))
    elif S<T:
        x = A*((2/6) * (1 - MSV))
    elif S==T:
        x = A*((3 / 6) * (1 - MSV))
    elif S>=2*T:
        x = A*((5 / 6) * (1 - MSV))
    elif S>T:
        x = A*((4 / 6) * (1 - MSV))
    return x

#print(Chance_To_Wound(Shuriken_Cannon))
#print(Chance_To_Wound(Fusion_Pistol))

def Avg_Damage(weap):
    Dr = weap['D(rand)']
    Dc = weap['D(con)']
    Ac = weap['A(con)']
    Ar = weap['A(rand)']
    if Ar == 0:
        AR = 0
    else:
        AR = ((Ar / 2) + (Ar / 2) + 1) / 2
    A = Ac + AR
    if Dr == 0:
        DR = 0
    else:
        DR = ((Dr / 2) + (Dr / 2) + 1) / 2
    x = (Dc+DR)
    return x

#print(Avg_Damage(Fusion_Pistol))
#print(Avg_Damage(Shuriken_Cannon))


print(Weapon_Value(Eldar_Ranged_Weapons))
def plot_weapons(wlst):
    #take a list of doubles and turn it into a graph
    xval = []
    yval = []
    for i in range(0,len(wlst)):
        xval.append(wlst[i][0])
        yval.append(wlst[i][1])
    plt.plot(xval,yval,'ro')
    plt.axis([0,5,0,8])
    plt.ylabel('average damage per wound')
    plt.xlabel('average wounds vs Marine')
    return plt.show()

plot_weapons(Weapon_Value(Eldar_Ranged_Weapons))
#This is the function for evaluating units in an army
def army_list_value(army):
    #this function takes an army list and returns a list by highest point to cost ratio to the lowest
    z = np.zeros((len(army),5))

    for i in range(0,len(army)):
       z[i] = unit_handle(army[i])
    return np.block([list_array_transpose(army),z])

def list_array_transpose(army):
    new_list = []
    for i in range(len(army)):
        new_list.append('{}'.format(army[i]['Name']))
    return np.array([new_list]).T


def unit_handle(unit):
    #this function take the unit given from the army and returns a list of the point to cost ratio of each member
    z = np.zeros(5)
    for i in range(0,len(unit['Member'])):
        z[i] =  member_value(unit['Member'][i])
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
    + sv_cost(member))/(2*member['Points']))
    return x

def m_cost(val):
    #given a move value returns a weighted value
    x = val['M']
    w = (val['T']*val['W'])+(6*val['WS']+val['A']+val['STR'])/3
    return (w + x)/2

def ws_cost(val):
    #given a ws value returns a weighted value
    x = val['WS']
    w = (val['STR'] * 0.8 + x * val['A'])/2
    return x * w

def bs_cost(val):
    #given a bs value returns a weighted value
    #This value depends on the ranged weapon but this app doesn't include weapons (yet)
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
    return (x * w)/3

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

print(army_list_value(Eldar))


