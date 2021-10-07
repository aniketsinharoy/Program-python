import matplotlib.pyplot as plt
def midpoint_circle_algo(xc,yc,r):
    o1_x=[]
    o2_x=[]
    o3_x=[]
    o4_x=[]
    o5_x=[]
    o6_x=[]
    o7_x=[]
    o8_x=[]
    o1_y=[]
    o2_y=[]
    o3_y=[]
    o4_y=[]
    o5_y=[]
    o6_y=[]
    o7_y=[]
    o8_y=[]
    x=0
    y=r
    plt.plot(xc+x,yc+y,color="blue",marker="o")
    o1_x.append(xc+x)
    o1_y.append(yc+y)
    plt.plot(xc+x,yc-y,color="blue",marker="o")
    o4_x.append(xc+x)
    o4_y.append(yc-y)
    plt.plot(xc+y,yc+x,color="blue",marker="o")
    o2_x.append(xc+y)
    o2_y.append(yc+x)
    plt.plot(xc-y,yc+x,color="blue",marker="o")
    o7_x.append(xc-y)
    o7_y.append(yc+x)
    pk=1-r
    j=0
    while x<y:
        if pk<=0:
            pk=pk+2*x+3
            x=x+1
        else:
            pk=pk+2*x-2*y+5
            x=x+1
            y=y-1
        plt.plot(xc+x,yc+y,color="blue",marker="o")
        j=j+1
        o1_x.append(xc+x)
        o1_y.append(yc+y)
        plt.plot(xc-x,yc+y,color="blue",marker="o")
        o8_x.append(xc-x)
        o8_y.append(yc+y)
        plt.plot(xc+x,yc-y,color="blue",marker="o")
        o4_x.append(xc+x)
        o4_y.append(yc-y)
        plt.plot(xc-x,yc-y,color="blue",marker="o")
        o5_x.append(xc-x)
        o5_y.append(yc-y)
        plt.plot(xc+y,yc+x,color="blue",marker="o")
        o2_x.append(xc+y)
        o2_y.append(yc+x)
        plt.plot(xc-y,yc+x,color="blue",marker="o")
        o7_x.append(xc-y)
        o7_y.append(yc+x)
        plt.plot(xc+y,yc-x,color="blue",marker="o")
        o3_x.append(xc+y)
        o3_y.append(yc-x)
        plt.plot(xc-y,yc-x,color="blue",marker="o")
        o6_x.append(xc-y)
        o6_y.append(yc-x)
    o8_x.insert(0,o1_x[0])
    o8_y.insert(0,o1_y[0])
    o3_x.insert(0,o2_x[0])
    o3_y.insert(0,o2_y[0])
    o5_x.insert(0,o4_x[0])
    o5_y.insert(0,o4_y[0])
    o6_x.insert(0,o7_x[0])
    o6_y.insert(0,o7_y[0])
    plt.plot(o1_x,o1_y,color="blue",marker="o") 
    plt.plot(o2_x,o2_y,color="blue",marker="o")
    plt.plot(o3_x,o3_y,color="blue",marker="o")
    plt.plot(o4_x,o4_y,color="blue",marker="o")
    plt.plot(o5_x,o5_y,color="blue",marker="o")
    plt.plot(o6_x,o6_y,color="blue",marker="o")
    plt.plot(o7_x,o7_y,color="blue",marker="o")
    plt.plot(o8_x,o8_y,color="blue",marker="o")
    plt.xlabel('<----X---->')
    plt.ylabel('<----Y---->')
    plt.title('Circle using Mid-point circle algorithm')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
x1=int(input('Enter x coordinate of circle center: '))
y1=int(input('Enter y coordinate of circle center: '))
r=int(input('Enter radius of circle: '))
midpoint_circle_algo(x1,y1,r)
