import matplotlib.pyplot as plt
def bresenham_algo(x1,x2,y1,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x_plot_points=[]
    y_plot_points=[]
    if dx!=0:
        slope=dy/dx
    else:
        slope=9999
    if slope<=1:
        pk=2*dy-dx
        if x2>x1:
            x=x1
            y=y1
            x_final=x2
            y_final=y2
        else:
            x=x2
            y=y2
            x_final=x1
            y_final=y1 
        while x<=x_final:
            plt.plot(x,y,color="blue",marker="o")
            x_plot_points.append(x)
            y_plot_points.append(y)
            x=x+1
            if pk<0:
                pk=pk+2*dy
            else:
                pk=pk+2*dy-2*dx
                y=y+1
    else:
        pk=2*dx-dy
        if y2>y1:
            x=x1
            y=y1
            x_final=x2
            y_final=y2
        else:
            x=x2
            y=y2
            x_final=x1
            y_final=y1  
        while y<=y_final:
            plt.plot(x,y,color="blue",marker="o")
            x_plot_points.append(x)
            y_plot_points.append(y)
            y=y+1
            if pk<0:
                pk=pk+2*dx
            else:
                pk=pk+2*dx-2*dy
                x=x+1
    plt.plot(x_plot_points,y_plot_points)
    plt.xlabel('<----X---->')
    plt.ylabel('<----Y---->')
    plt.title('Line using Bresenham algorithm')
    plt.show()
x1=int(input('Enter first point x coordinate: '))
y1=int(input('Enter first point y coordinate: '))
x2=int(input('Enter second point x coordinate: '))
y2=int(input('Enter second point y coordinate: '))
bresenham_algo(x1,x2,y1,y2)
