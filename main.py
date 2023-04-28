# What I want to do is take the information off of wahapedia to make a system which
# ranks units by their stat/cost ratio with a weight given by some calculated values
import numpy as np
import matplotlib.pyplot as plt
# Todo: Make a regression line of the average weapon visible for the weapon graph
#       Add more weapons and units to the Eldar_units_weapons file
#       Improve the move, save, leadership, and toughness functions
#       Order the units in some way (ie by highest average score or highest score)
#       Add a way to compare the to wound of different units:
#           (right now its to wounds a Space Marine but could be a tank or whatever you feed it)
#       Need a way to take in special abilities of Units:
#           (ie. Reduced Damage Taken, Invul. Saves, Auras, ECT)
#       Need a way to take in special abilities of weapons:
#           (ie. Shuriken, Blast, Auto-Hits, Mortal Wounds, ECT)
#       General clean up and renaming of functions to better reflect their role

# Note: The new edition of 40k is coming out this summer so most of this will be obsolete soon,
# but I can't update till its out, so I will keep going anyway


def Weapon_Value(lst):
    # gives back a list of weapons as doubles:
    # (average chance to wound spacemarine, average damage to spacemarine)
    NA = []
    for i in range(0,len(lst)):
        if type(lst[i]) == list:
            for j in range(0,len(lst[i])):
                x = Make_Double((lst[i])[j])
                NA.append(x)
        else:
            x = Make_Double(lst[i])
            NA.append(x)
    return NA

def Make_Double(weap):
    # take a single weapon, gives back a double
    if weap['Type'] == 'Melee':
        return None
    else:
        i = Chance_To_Wound(weap)
        j = Avg_Damage(weap)
        return (i,j)

def Chance_To_Wound(weap):
    # give the chance to wound with the average number of attacks
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
        result = A*((1/6) * (1 - MSV))
    elif S<T:
        result = A*((2/6) * (1 - MSV))
    elif S==T:
        result = A*((3 / 6) * (1 - MSV))
    elif S>=2*T:
        result = A*((5 / 6) * (1 - MSV))
    elif S>T:
        result = A*((4 / 6) * (1 - MSV))
    return result

def Avg_Damage(weap):
    Dr = weap['D(rand)']
    Dc = weap['D(con)']
    # AR = Ar if Ar == 0 else ((Ar / 2) + (Ar / 2) + 1) / 2
    if Dr == 0:
        DR = 0
    else:
        DR = ((Dr / 2) + (Dr / 2) + 1) / 2
    x = (Dc+DR)
    return x

def Plot_Weapons(wlst):
    # take a list of weapons and turn it into a graph (want to call Weapon_Value)
    dlst = Weapon_Value(wlst)
    xval = []
    yval = []
    for i in range(0,len(wlst)):
        xval.append(dlst[i][0])
        yval.append(dlst[i][1])
    plt.plot(xval,yval,'ro')
    plt.axis([0,5,0,8])
    plt.ylabel('average damage per wound')
    plt.xlabel('average wounds vs Marine')
    return plt.show()

def Army_List_Value(army):
    # this function takes an army list and returns a list by highest point to cost ratio to the lowest
    z = np.zeros((len(army),5))
    for i in range(0,len(army)):
       z[i] = Unit_Handle(army[i])
    return np.block([List_Array_Transpose(army),z])

def List_Array_Transpose(army):
    # Gives the names of each unit in 1 by n vector
    new_list = []
    for i in range(len(army)):
        new_list.append('{}'.format(army[i]['Name']))
    return np.array([new_list]).T


def Unit_Handle(unit):
    # this function take the unit given from the army and returns a list of the point to cost ratio of each member
    z = np.zeros(5)
    for i in range(0,len(unit['Member'])):
        z[i] = Member_Value(unit['Member'][i])
    return z


# 'Points','M','WS','BS','STR','T','W','A','LD','SV'

def Member_Value(member):
    # This function adds the values of each stat and divides by the cost
    x = ((M_Cost(member)
    + Melee(member)
    + BS_Cost(member)
    + T_Cost(member)
    + W_Cost(member)
    + LD_Cost(member)
    + SV_Cost(member))/(1*member['Points']))
    return x

def M_Cost(val):
    # given a move value returns a weighted value
    x = val['M']
    w = (val['T']*val['W'])+(6*val['WS']+val['A']+val['STR'])/3
    return (w + x)/2

def BS_Cost(val):
    # given a member's bs and weapons returns average wounds vs spacemarine with best weapon
    mem_bs = val['BS']
    weap_list = val['Weap']
    results = []
    for i in range(0,len(weap_list)):
        weap_vals = Weapon_Value(weap_list)
    for j in range(0,len(weap_vals)):
        if weap_vals[j] == None:
            x=0
            results.append(x)
        else:
            x = weap_vals[j][0]*weap_vals[j][1]*mem_bs*3
            results.append(x)
    return max(results)

def Melee(memb):
    # given a str value returns a weighted value
    weap_list = memb['Weap']
    result =[]
    for i in range(0,len(weap_list)):
        if type(weap_list[i]) == list:
            for j in range(0,len(weap_list[i])):
               x = Melee_Wound((weap_list[i])[j],memb)
               result.append(x)
        else:
            x = Melee_Wound(weap_list[i],memb)
            result.append(x)
    return max(result)

def Melee_Wound(weapon,mem):
    Unarmed = {'Points': 0,
               'Type': 'Melee',
               '*/+': '+',
               'STR': 0,
               'AP': 0,
               'D(rand)': 0,
               'D(con)': 1,
               'A(rand)': 0,
               'A(con)': 0,
               'AB': 'None'}
    if weapon['Type'] == 'Melee':
        weap = weapon
    else:
        weap = Unarmed
    if weap['*/+'] == '+':
        S = mem['STR'] + weap['STR']
    else:
        S = mem['STR'] * weap['STR']
    WS = mem['WS']
    AP = weap['AP']
    Ar = weap['A(rand)']
    Ac = weap['A(con)']
    Am = mem['A']
    Dr = weap['D(rand)']
    Dc = weap['D(con)']
    T = 4
    SV = 4/6
    if Ar == 0:
        AR = 0
    else:
        AR = ((Ar/2)+(Ar/2)+1)/2
    A = Ac + AR + Am
    if  SV - (AP/6)<0:
        MSV = 0
    else:
        MSV = SV - (AP/6)
    if (2*S )<=T:
        wounds = A*((1/6) * (1 - MSV))
    elif S <T:
        wounds = A*((2/6) * (1 - MSV))
    elif S ==T:
        wounds = A*((3 / 6) * (1 - MSV))
    elif S >=2*T:
        wounds = A*((5 / 6) * (1 - MSV))
    elif S >T:
        wounds = A*((4 / 6) * (1 - MSV))
    if Dr == 0:
            DR = 0
    else:
        DR = ((Dr / 2) + (Dr / 2) + 1) / 2
    damage = (Dc + DR)
    #3/6*2.333*2
    return (WS * wounds * damage)*3

def T_Cost(val):
    # given a t value returns a weighted value
    # Ideally I want to feed in some values of weapons and then give distinct T a value
    x = val['T']
    w = val['W']
    if x % 2 == 0:
        y = x + 1
    else: y = x + 0.5
    return (y * w)/2

def W_Cost(val):
    # given a w value returns a weighted value
    x = val['W']
    w = val['T']
    return (x * w)/3

def LD_Cost(val):
    # given a ld value returns a weighted value
    x = val['LD']
    return x/4

def SV_Cost(val):
    # given a sv value returns a weighted value
    x = val['SV']
    w = val['W']
    return x * w
