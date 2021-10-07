import matplotlib.pyplot as plt
def midpoint_ellipse_algo(xc,yc,a,b):
    o1_x=[]
    o1_y=[]
    o2_x=[]
    o2_y=[]
    o3_x=[]
    o3_y=[]
    o4_x=[]
    o4_y=[]
    x=0
    y=b
    pk=round((b*b)+((a*a)/4)-(b*a*a))
    dx=b*b*x
    dy=a*a*y
    while x<=a and y>=0:
        plt.plot(xc+x,yc+y,color="green",marker="o")
        o1_x.append(xc+x)
        o1_y.append(yc+y)
        plt.plot(xc+x,yc-y,color="red",marker="o")
        o4_x.append(xc+x)
        o4_y.append(yc-y)
        plt.plot(xc-x,yc-y,color="yellow",marker="o")
        o3_x.append(xc-x)
        o3_y.append(yc-y)
        plt.plot(xc-x,yc+y,color="blue",marker="o")
        o2_x.append(xc-x)
        o2_y.append(yc+y)
        if dx<dy:
            if pk<0:
                pk=pk+(b*b)*((2*x)+3)
                x=x+1
            else:
                pk=pk+(b*b)*(2*x+3)-2*(a*a)*(y-1)
                x=x+1
                y=y-1
            dx=b*b*x
            dy=a*a*y    
            if dx>=dy:
                pk=round((b*b)*(x+0.5)*(x+0.5)+(a*a)*(y-1)*(y-1)-(a*a*b*b))
        else:
            if pk>0:
                pk=pk+(a*a)*(3-2*y)
                y=y-1
            else:
                pk=pk+2*(b*b)*(x+1)-(a*a)*(2*y-3)
                x=x+1
                y=y-1
    plt.plot(o1_x,o1_y,color="green")
    plt.plot(o2_x,o2_y,color="blue")
    plt.plot(o3_x,o3_y,color="yellow")
    plt.plot(o4_x,o4_y,color="red")
    plt.xlabel('<----X---->')
    plt.ylabel('<----Y---->')
    plt.title('Ellipse using Mid-point ellipse algorithm') 
    plt.gca().set_aspect('equal',adjustable='box')  
    plt.show()
x1=int(input('Enter x coordinate of ellipse center: '))
y1=int(input('Enter y coordinate of ellipse center: '))
a=int(input('Enter major axis of ellipse: '))
b=int(input('Enter major axis of ellipse: '))
midpoint_ellipse_algo(x1,y1,a,b)
