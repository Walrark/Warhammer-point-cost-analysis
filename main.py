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
#give save as percent to save

Heading = ['Name','Points','M','WS','BS','STR','T','W','A','LD','SV']
Weight_Vector = [1 ,0.4 ,0.6 ,0.6 ,0.4,0.8,0.8,0.6,0.3,2 ]
Example_stat = ['Example Unit',10,6,4,4,3,3,1,1,8,2/6]

Guardian_Defenders = np.array([['Guardian_Defenders',9 ,7 ,3 ,3 ,3 ,3 ,1 ,1 ,7 ,3/6 ],
                         ['Heavy_Weapon_Platfrom',20 ,7 ,6 ,3 ,3,3 ,2 ,1 ,7 ,4/6 ]])

WraithLord = np.array([['Wraithlord',100 ,8 ,3 ,3 ,7 ,8 ,9 ,4 ,9 ,4/6]])

Eldar = [WraithLord,Guardian_Defenders]


def matrix_trim(matrix):
    #Gives a trimmed statblock and the original statblock
    x0 = np.zeros(shape= [len(matrix),10])
    y0 = np.matrix([''])
    for i in range(0,len(matrix)):
        x0[i] = np.array(( matrix[i][1:]))
    return x0

#print(matrix_trim(Guardian_Defenders))

def weight_solve(m1):
    #returns a weight@statblock and the name of the statblock
    w = Weight_Vector * m1
    return w

#print(weight_solve(matrix_trim(WraithLord )))

def point_stat(stat):

    for j in range(0,len(stat)):
        x = 0
        for i in range(1,8):
         x = stat[j][i] + x
         print(x)
    return x/stat[j][0]


print(point_stat(weight_solve(matrix_trim(Guardian_Defenders))))

#want a function which takes the name of the stat block and gives the accociated value in an ordered list

def value_assess(matrix):
    #want y to be the value of the unit
    #x will be the name of the unit
    #z will be an n by 2 matrix
    y = point_stat(weight_solve(matrix_trim(WraithLord)))
    x = None
    z = None
    return z