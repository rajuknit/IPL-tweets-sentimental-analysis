import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("output_twoteam/team1res.txt","r").read()
    pullData1 = open("output_twoteam/team2res.txt","r").read()
    lines = pullData.split('\n')
    lines1 = pullData1.split('\n')

    xar = []
    yar = []
    xar1 = []
    yar1 = []

    x = 0
    y = 0
    x1=0
    y1=0

    for l in lines[-200:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 0.5

        xar.append(x)
        yar.append(y)
        
    for l in lines1[-200:]:
        x1 += 1
        if "pos" in l:
            y1 += 1
        elif "neg" in l:
            y1 -= 0.5

        xar1.append(x1)
        yar1.append(y1)    
        
    ax1.clear()
    ax1.plot(xar,yar)
    ax1.plot(xar1,yar1)
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
