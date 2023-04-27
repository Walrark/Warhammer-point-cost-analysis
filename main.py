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



#The melee weapons will need to be changed to 'STR':+2 or 'STR':*2 to account for different weapon profiles
GGCrush = {'Points': 15,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':2,
                  'AP':4,
                  'D(rand)':3,
                  'D(con)':3,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}
GGSweep = {'Points': 15,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':0,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(rand)': 0,
                  'A(con)': 1,
                  'AB':'None'}
GhostGlave = [GGSweep,GGCrush]
Wraithbone_Fists = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':0,
                  'AP':3,
                  'D(rand)':0,
                  'D(con)':3,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}
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
Power_Glaive = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':2,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}
Banshee_Blade = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':1,
                  'AP':4,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}
Star_Glaive = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'*',
                  'STR':2,
                  'AP':3,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'None'}
Diresword = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':1,
                  'AP':0,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(rand)': 0,
                  'A(con)': 0,
                  'AB':'*'}
Paired_Hekatarii_Blades = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':0,
                  'AP':3,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':0,
                  'AB':'None'}
Witch_Staff ={'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':0,
                  'AP':1,
                  'D(rand)':3,
                  'D(con)':0,
                  'A(con)':0,
                  'A(rand)':0,
                  'AB':'None'}
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
Shuriken_Catapult = {'Points': 0,
                  'R':18,
                  'Type':'Assault',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':2,
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
Dragon_Breath_Flamer = {'Points': 0,
                  'R':12,
                  'Type':'Assault',
                  'STR':6,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':6,
                  'AB':'None'}
Fire_pike ={'Points': 10,
                  'R':18,
                  'Type':'Assault',
                  'STR':9,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':4,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}
Flamer ={'Points': 5,
                  'R':12,
                  'Type':'Assault',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':6,
                  'AB':'None'}
Fury_of_the_Tempest ={'Points': 0,
                  'R':24,
                  'Type':'Assault',
                  'STR':9,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':2,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}
Scatter_Laser = {'Points': 0,
                  'R':6,
                  'Type':'Heavy',
                  'STR':6,
                  'AP':0,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':6,
                  'A(rand)':0,
                  'AB':'None'}
Star_Cannon = {'Points': 5,
                  'R':36,
                  'Type':'Heavy',
                  'STR':7,
                  'AP':3,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(con)':2,
                  'A(rand)':0,
                  'AB':'None'}
StarSwarm = {'Points': 0,
                  'R':48,
                  'Type':'Heavy',
                  'STR':5,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(con)':2,
                  'A(rand)':0,
                  'AB':'None'}
StarShotReaper = {'Points': 0,
                  'R':48,
                  'Type':'Heavy',
                  'STR':8,
                  'AP':2,
                  'D(rand)':0,
                  'D(con)':3,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}
Reaper_Launcher = [StarShotReaper,]
Corsair_Shredder = {'Points': 5,
                  'R':18,
                  'Type':'Assualt',
                  'STR':6,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':6,
                  'A(rand)':0,
                  'AB':'None'}
Neuro_Disrupter = {'Points': 5,
                  'R':12,
                  'Type':'Pistol',
                  'STR':6,
                  'AP':3,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'*'}
Ranger_Long_Rifle = {'Points': 0,
                  'R':36,
                  'Type':'Heavy',
                  'STR':4,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'*'}
Aeldari_Power_Sowrd = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':1,
                  'AP':3,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':0,
                  'A(rand)':0,
                  'AB':'None'}
Scorpion_Chainsword = {'Points': 0,
                  'Type':'Melee',
                  '*/+':'+',
                  'STR':0,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}
Eldar_Melee_Weapons = [Diresword,Power_Glaive]
Eldar_Ranged_Weapons = [Fusion_Pistol,Shuriken_Cannon,Shuriken_Rifle,Wraithcannon,Avenger_Shuriken_Catapult,
                        Shuriken_Pistol,Plasma_Grenade,Aeldari_Missle_Launcher,Dragon_Fusion_Gun,Bright_Lance,
                        Doomweaver,Death_Spinner,D_Scythe,D_Cannon,Dragon_Breath_Flamer,Fire_pike,
                        Flamer,Fury_of_the_Tempest,Shuriken_Catapult,Scatter_Laser,Star_Cannon,Ranger_Long_Rifle,
                        Neuro_Disrupter,Corsair_Shredder,Reaper_Launcher]

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
    'SV': 4/6,
    'Weap':[Bright_Lance,Scatter_Laser,Shuriken_Cannon,Star_Cannon,Aeldari_Missle_Launcher,Aeldari_Flamer,
            Shuriken_Catapult,GhostGlave,Wraithbone_Fists]}

Heavy_Weapon_Platfrom = {'Points': 20,
    'M': 7,
    'WS': 1/6,
    'BS': 4/6,
    'STR': 3,
    'T': 3,
    'W': 2,
    'A': 1,
    'LD': 7,
    'SV': 4/6,
    'Weap':[Bright_Lance,Scatter_Laser,Shuriken_Cannon,Star_Cannon,Aeldari_Missle_Launcher]}

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
    'SV': 3/6,
    'Weap':[Shuriken_Catapult,Plasma_Grenade]}

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
    'SV': 4/6,
    'Weap':[Fusion_Pistol,Shuriken_Pistol,Death_Spinner,Dragon_Fusion_Gun,Reaper_Launcher,
            Banshee_Blade,Star_Glaive,Scorpion_Chainsword,Plasma_Grenade]}


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
    'SV': 3/6,
    'Weap':[Shuriken_Pistol,Aeldari_Power_Sowrd,Plasma_Grenade,Shuriken_Rifle,Corsair_Shredder,Corsair_Blaster,
            Shuriken_Cannon,Ranger_Long_Rifle,Fusion_Pistol]}

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
    'SV': 3/6,
    'Weap':[Shuriken_Pistol,Aeldari_Power_Sowrd,Plasma_Grenade,Shuriken_Rifle,Neuro_Disrupter]}

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
    'SV': 3/6,
    'Weap':[Paired_Hekatarii_Blades,Plasma_Grenade]}

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
    'SV': 3/6,
    'Weap':[Aeldari_Power_Sowrd,Plasma_Grenade]}

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
    'SV': 3/6,
    'Weap':[Witch_Staff,Plasma_Grenade]}

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
                  'Weap':[Avenger_Shuriken_Catapult,Plasma_Grenade]}

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
                  'Weap':[Shuriken_Pistol,Avenger_Shuriken_Catapult,Diresword,Power_Glaive,Plasma_Grenade]}

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

#print(Chance_To_Wound(Shuriken_Cannon))
#print(Chance_To_Wound(Fusion_Pistol))

def Avg_Damage(weap):
    Dr = weap['D(rand)']
    Dc = weap['D(con)']
    #AR = Ar if Ar == 0 else ((Ar / 2) + (Ar / 2) + 1) / 2
    if Dr == 0:
        DR = 0
    else:
        DR = ((Dr / 2) + (Dr / 2) + 1) / 2
    x = (Dc+DR)
    return x

#print(Avg_Damage(Fusion_Pistol))
#print(Avg_Damage(Shuriken_Cannon))


#print(Weapon_Value(Eldar_Ranged_Weapons))
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
    + melee(member)
    + bs_cost(member)
    + t_cost(member)
    + w_cost(member)
    + ld_cost(member)
    + sv_cost(member))/(1*member['Points']))
    return x

def m_cost(val):
    #given a move value returns a weighted value
    x = val['M']
    w = (val['T']*val['W'])+(6*val['WS']+val['A']+val['STR'])/3
    return (w + x)/2

def bs_cost(val):
    #given a member's bs and weapons returns average wounds vs spacemarine with best weapon
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

def melee(memb):
    #given a str value returns a weighted value
    weap_list = memb['Weap']
    result =[]
    for i in range(0,len(weap_list)):
        if type(weap_list[i]) == list:
            for j in range(0,len(weap_list[i])):
               x = melee_wound((weap_list[i])[j],memb)
               result.append(x)
        else:
            x = melee_wound(weap_list[i],memb)
            result.append(x)
    return max(result)

#Avenger_Shuriken_Catapult = {'Points': 0,
#                  'R': 18,
#                  'Type':'Assault',
#                  'STR':4,
#                  'AP':2,
#                  'D(rand)':0,
#                  'D(con)':1,
#                  'A(rand)': 0,
#                  'A(con)': 3,
#                  'AB':'Shuriken'}

def melee_wound(weapon,mem):
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

def ld_cost(val):
    #given a ld value returns a weighted value
    x = val['LD']
    return x/4

def sv_cost(val):
    #given a sv value returns a weighted value
    x = val['SV']
    w = val['W']
    return x * w

print(army_list_value(Eldar))
#print(Weapon_Value(Eldar_Ranged_Weapons))
plot_weapons(Weapon_Value(Eldar_Ranged_Weapons))

