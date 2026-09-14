import math

import matplotlib.pyplot as plt
x1=0
y1=0
theta=0

x2=0
y2=0

v=0
omega=0
duration=0

trackx=[0.0]
tracky=[0.0]
def motion():
    global x1,x2,y1,y2,theta,v,omega,duration
    x1=x2
    y1=y2
    print()
    v=float(input("enter velocity: "))
    omega=float(input("enter angular velocity: "))
    duration=float(input("enter duration of motion: "))

    curve=int(duration/0.1)
    for i in range(curve):
            x2+=(v*math.cos(theta))*0.1
            y2+=(v*math.sin(theta))*0.1
            theta+=omega*0.1
            trackx.append(x2)
            tracky.append(y2)

    theta%=2*math.pi

    print(str(v)+","+str(omega)+","+str(duration))
    try:
        motion()
    except (KeyboardInterrupt,UnboundLocalError,ValueError):
        plt.plot(trackx,tracky)
        plt.plot(trackx[0], tracky[0],'gs',markersize=10, label="start")
        for i in range (len(trackx)-1):
            plt.annotate("",
                        xy=(trackx[i+1],tracky[i+1]),
                        xytext=(trackx[i], tracky[i]))
        plt.legend()
        plt.show()
        print("command exited")

motion()
