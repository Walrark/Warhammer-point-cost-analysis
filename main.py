# What I want to do is take the information off of wahapedia to make a system which
# ranks units by their stat/cost ratio with a weight given by some calculated values
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy import interpolate as int
# Todo(current edition): Add more weapons and units to the Eldar_units_weapons file
#       Improve the move, save, leadership, and toughness functions
#       Order the units in some way (ie by highest average score or highest score)
#       Need a way to take in special abilities of Units:
#           (ie. Reduced Damage Taken, Invul. Saves, Auras, ECT)
#       Need a way to take in special abilities of weapons:
#           (ie. Shuriken, Blast, Auto-Hits, Mortal Wounds, ECT)
#       General clean up and renaming of functions to better reflect their role

# Todo (to get ready for next edition): Remove the BS from the members and put onto weapons,
#       that means that the function for calculating the BS value will depend solely on the weapon.
#       Add new stat "OC" for objective control and evaluate it
#       Remove Str and Attack from member and move to Melee weapons, this will change how much I need the member for.
#       Decide weither to make the graph 3D with chance to hit, chance to wound, and average damage for every weapon,\
#       or if I should instead make it 2D with average damage caused from average hits.
#       Find a way to scrape for the data instead of writing by hand.

# Weapon for weaponless units
Unarmed = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':0,
                  'AP':0,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}
# Default unit for tests
Spacemarine = {'Points': 21,
    'M': 6,
    'WS': 4/6,
    'BS': 4/6,
    'STR': 4,
    'T': 4,
    'W': 2,
    'A': 2,
    'LD': 7,
    'SV': 4/6,
    'Weap':None}

def Weapon_Value(lst , test_unit = Spacemarine):
    # gives back a list of weapons as doubles:
    # (average chance to wound the test unit, average damage to the test unit)
    NA = []
    TU = test_unit
    for i in range(0, len(lst)):
        if type(lst[i]) == list:
            for j in range(0, len(lst[i])):
                x = Make_Double(lst[i][j], TU)
                NA.append(x)
        else:
            x = Make_Double(lst[i], TU)
            NA.append(x)
    return NA

def Make_Double(weap, test_unit = Spacemarine):
    # take a single weapon, gives back a double
    if weap['Type'] == 'Melee':
        return None
    else:
        i = Chance_To_Wound(weap, test_unit)
        j = Avg_Damage(weap, test_unit)
        return (i, j)

def Chance_To_Wound(weap, test_unit = Spacemarine):
    # give the chance to wound with the average number of attacks
    T = test_unit['T']
    SV = test_unit['SV']
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

def Avg_Damage(weap, test_unit = Spacemarine):
    #if test unit has a damage reduction ability, need to take that into account.
    Dr = weap['D(rand)']
    Dc = weap['D(con)']
    # AR = Ar if Ar == 0 else ((Ar / 2) + (Ar / 2) + 1) / 2
    if Dr == 0:
        DR = 0
    else:
        DR = ((Dr / 2) + (Dr / 2) + 1) / 2
    x = (Dc+DR)
    return x

def Plot_Weapons(wlst, test_unit = Spacemarine):
    # take a list of weapons and turn it into a graph using a test unit which is a member
    # want to sort dlist by x values
    step = 1000
    dlst = sorted(Weapon_Value(wlst, test_unit))
    xval = []
    yval = []
    for i in range(0,len(dlst)):
        xval.append(dlst[i][0])
        yval.append(dlst[i][1])
    n = len(xval)
    x = np.array(xval)
    y = np.array(yval)
    xmax = max(xval) + 1
    ymax = max(yval) + 1
    X = np.column_stack([np.ones(n),x,x**2,x**3,x**4,x**5])
    x_rline = np.linspace(0, xmax, step)
    coeff = la.solve((X.T @ X),X.T @ yval)
    y_rline = coeff[0] +coeff[1]*x_rline + coeff[2]*x_rline**2 + coeff[3]* x_rline**3 + coeff[4]* x_rline**4 +\
              coeff[5]* x_rline**5
    plt.scatter(xval,yval)
    plt.plot(x_rline,y_rline,'r')
    plt.axis([0,xmax,0,ymax])
    plt.ylabel('average damage per wound')
    plt.xlabel('average wounds vs {}'.format('unit'))
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

def M_Cost(memb):
    # given a move value returns a weighted value
    # OC in 10th will be combined into move
    x = memb['M']
    w = (memb['T']*memb['W'])+(6*memb['WS']+memb['A']+memb['STR'])/3
    return (w + x)/2

def BS_Cost(memb):
    # given a member's bs and weapons returns average wounds vs spacemarine with best weapon
    mem_bs = memb['BS']
    weap_list = memb['Weap']
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

def T_Cost(memb):
    # given a t value returns a weighted value
    # Ideally I want to feed in some values of weapons and then give distinct T a value
    x = memb['T']
    w = memb['W']
    if x % 2 == 0:
        y = x + 1
    else: y = x + 0.5
    return (y * w)/2

def W_Cost(memb):
    # given a w value returns a weighted value
    x = memb['W']
    w = memb['T']
    return (x * w)/3

def LD_Cost(memb):
    # given a ld value returns a weighted value
    x = memb['LD']
    return x/4

def SV_Cost(memb):
    # given a sv value returns a weighted value
    x = memb['SV']
    w = memb['W']
    return x * w