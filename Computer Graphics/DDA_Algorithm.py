import matplotlib.pyplot as plt
def DDA_algo(x1,x2,y1,y2):
    if(abs(x2-x1)>=abs(y2-y1)):
        step=int(x2-x1)
    else:
        step=int(y2-y1)
    c=[]
    d=[]
    x_step=(x2-x1)/abs(step)
    y_step=(y2-y1)/abs(step)
    a=x1
    b=y1
    c.append(a)
    d.append(b)
    plt.plot(round(a),round(b),color="blue",marker="o")
    for i in range(0,abs(step)):
        if x1!=x2:
            x=a+x_step
        else:
            x=a
        y=b+y_step
        plt.plot(round(x),round(y),color="blue",marker="o")
        c.append(round(x))
        d.append(round(y))
        a=x
        b=y
    plt.plot(c,d)
    plt.xlabel('<----X---->')
    plt.ylabel('<----Y---->')
    plt.title('Line using DDA algorithm')
    plt.show()
x1=float(input('Enter first point x coordinate: '))
y1=float(input('Enter first point y coordinate: '))
x2=float(input('Enter second point x coordinate: '))
y2=float(input('Enter second point y coordinate: '))
DDA_algo(x1,x2,y1,y2)
