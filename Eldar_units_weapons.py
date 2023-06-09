from main import *
# This file contains the units and weapons from the Aeldari faction on Wahapedia.ru
# (incomplete list)

# a member is a part of the unit and is dictionary of stats
# a unit is a dictionary of a name and a list of members


# Weapons
Laser_Lance = {'Points': 0,
                  'R':6,
                  'Type':'Assault',
                  'STR':6,
                  'AP':4,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}
Lasblaster = {'Points': 0,
                  'R':24,
                  'Type':'Assault',
                  'STR':4,
                  'AP':0,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':4,
                  'A(rand)':0,
                  'AB':'None'}
Heavy_Wraith_Cannon = {'Points': 30,
                  'R':36,
                  'Type':'Heavy',
                  'STR':16,
                  'AP':4,
                  'D(rand)':3,
                  'D(con)':6,
                  'A(con)':0,
                  'A(rand)':3,
                  'AB':'None'}
Heavy_Dscythe = {'Points': 0,
                  'R':18,
                  'Type':'Heavy',
                  'STR':12,
                  'AP':4,
                  'D(rand)':0,
                  'D(con)':2,
                  'A(con)':0,
                  'A(rand)':6,
                  'AB':'None'}
Hawks_Talon ={'Points': 0,
                  'R':24,
                  'Type':'Assault',
                  'STR':5,
                  'AP':1,
                  'D(rand)':0,
                  'D(con)':1,
                  'A(con)':4,
                  'A(rand)':0,
                  'AB':'None'}
Guardian_Fusion_Gun = {'Points': 10,
                  'R':12,
                  'Type':'Assault',
                  'STR':8,
                  'AP':4,
                  'D(rand)':6,
                  'D(con)':0,
                  'A(con)':1,
                  'A(rand)':0,
                  'AB':'None'}
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
Wraithcannon = {'Points': 0,
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
Reaper_Launcher = [StarShotReaper,StarSwarm]
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
Eldar_Melee_Weapons = [Diresword,Power_Glaive]
Eldar_Ranged_Weapons = [Fusion_Pistol,Shuriken_Cannon,Shuriken_Rifle,Wraithcannon,Avenger_Shuriken_Catapult,
                        Shuriken_Pistol,Plasma_Grenade,Aeldari_Missle_Launcher,Dragon_Fusion_Gun,Bright_Lance,
                        Doomweaver,Death_Spinner,D_Scythe,D_Cannon,Dragon_Breath_Flamer,Fire_pike,
                        Flamer,Fury_of_the_Tempest,Shuriken_Catapult,Scatter_Laser,Star_Cannon,Ranger_Long_Rifle,
                        Neuro_Disrupter,Corsair_Shredder,Reaper_Launcher,Lasblaster,Laser_Lance,Hawks_Talon,
                        Guardian_Fusion_Gun,Heavy_Dscythe,Heavy_Wraith_Cannon]

# Members
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

# Units
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

# Armies
Eldar = [WraithLord,Guardian_Defenders,Autarch,Corsair_Voidscarred,Dire_Avengers]


Plot_Weapons(Eldar_Ranged_Weapons,wraithlord)
print(Army_List_Value(Eldar,wraithlord))