import matplotlib.pyplot as plt
import math
x1=0
y1=0
theta=0

x2=0
y2=0

trackx=[0]
tracky=[0]
def motion():
    global x1,x2,y1,y2,theta
    cmnds=["forward","left","right"]
    cmnd=input("enter execution command")
    for word in cmnd.split():
        c=word
        break;

    if c not in cmnds:
        print("command unavailable")
        motion()
    else:
        print("initial pos: ("+str(x2)+","+str(y2)+","+str(theta)+")")
        i=0
        val=0
        for word in cmnd.split():
            if i==0:
                c=word
            else:
                val=int(word)
            i=i+1
        print("executing: "+c)
        if c=="forward":
            y1=y2
            y2+=val
        elif c=="left":
            x1=x2
            x2-=val
        elif c=="right":
            x1=x2
            x2+=val
        trackx.append(x2)
        tracky.append(y2)
        try:
            theta=math.atan2((y2-y1),(x2-x1))
        except ZeroDivisionError:
            theta=0

        print("final pos: ("+str(x2)+","+str(y2)+","+str(theta)+")")
        try:
            motion()
        except KeyboardInterrupt and UnboundLocalError:
            plt.plot(trackx,tracky)
            plt.plot(trackx[0], tracky[0],'gs',markersize=10, label="start")
            for i in range (len(trackx)-1):
                plt.annotate("",
                             xy=(trackx[i+1],tracky[i+1]),
                             xytext=(trackx[i], tracky[i]),
                             arrowprops=dict(arrowstyle="->",color="r"))
            plt.legend()
            plt.show()
            print("command exited")


motion()
