import math

ttx = 34.0206
tty = -118.2854

r = 1
R = 6
a = 8

n = 14

xt = 0
yt = 0

t = 0.00

coor = ''


while t < n*math.pi:
    xt = ((R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t))*0.00025+ttx
    yt = ((R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t))*0.00025+tty
    #print(yt,xt,sep=',')
    coor+=(f'{yt},{xt},0.') + '\n'
    t+=0.01

with open('spiro.txt','w') as f:
    f.write(coor)