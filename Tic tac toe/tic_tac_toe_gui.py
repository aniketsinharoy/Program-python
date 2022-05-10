from tkinter import *
e=1
a=[]
b=[]
def cal():
    global e
    if a[0]==9:
        a7["text"]='X'
        a7["bg"]='yellow'
        if e==2:
            e=e+1
        if e>=4:
            if a[1]==4:
                a3["text"]='X'
                a3["bg"]='yellow'
                if e==4:
                    e=e+1
                if e>=6:
                    if a[2]==2:
                        a5["text"]='X'
                        a5["bg"]='yellow'
                        l1.configure(text="YOU LOST")
                    if a[2]==5:
                        a2["text"]='X'
                        a2["bg"]='yellow'
                        l1.configure(text="YOU LOST")
            else:
                a4['text']='X'
                a4["bg"]='yellow'
                l1.configure(text="YOU LOST")
    if a[0]==7:
        a9["text"]='X'
        a9["bg"]='yellow'
        if e==2:
            e=e+1
        if e>=4:
            if a[1]==5:
                a3["text"]='X'
                a3["bg"]='yellow'
                if e==4:
                    e=e+1
                if e>=6:
                    if a[2]==2:
                        a6["text"]='X'
                        a6["bg"]='yellow'
                        l1.configure(text="YOU LOST")
                    if a[2]==6:
                        a2["text"]='X'
                        a2["bg"]='yellow'
                        l1.configure(text="YOU LOST")
            else:
                a5['text']='X'
                l1.configure(text="YOU LOST")
    if a[0]==3:
        a7["text"]='X'
        a7["bg"]='yellow'
        if e==2:
            e=e+1
        if e>=4:
            if a[1]==4:
                a9["text"]='X'
                a9["bg"]='yellow'
                if e==4:
                    e=e+1
                if e>=6:
                    if a[2]==8:
                        a5["text"]='X'
                        a5["bg"]='yellow'
                        l1.configure(text="YOU LOST")
                    if a[2]==5:
                        a8["text"]='X'
                        a8["bg"]='yellow'
                        l1.configure(text="YOU LOST")
            else:
                a4['text']='X'
                a4["bg"]='yellow'
                l1.configure(text="YOU LOST")
    if a[0]==2:
        a5["text"]='X'
        a5["bg"]='yellow'
        if e==2:
            e+=1
        if e>=4:
            e+=1
            if a[1]==9:
                a7["text"]='X'
                a7["bg"]='yellow'
                if e>=6:
                    if a[2]==3:
                        a4["text"]='X'
                        a4["bg"]='yellow' 
                    else:
                        a3["text"]='X'
                        a3["bg"]='yellow'
                    l1.configure(text="YOU LOST")
            else:
                a9["text"]='X'
                a9["bg"]='yellow' 
                l1.configure(text="YOU LOST")
    if a[0]==4:
        a5["text"]='X'
        a5["bg"]='yellow'
        if e==2:
            e+=1
        if e>=4:
            e+=1
            if a[1]==9:
                a3["text"]='X'
                a3["bg"]='yellow'
                if e>=6:
                    if a[2]==2:
                        a7["text"]='X'
                        a7["bg"]='yellow' 
                    else:
                        a2["text"]='X'
                        a2["bg"]='yellow'
                    l1.configure(text="YOU LOST")
            else:
                a9["text"]='X'
                a9["bg"]='yellow' 
                l1.configure(text="YOU LOST")
    if a[0]==6:
        a5["text"]='X'
        a5["bg"]='yellow'
        if e==2:
            e+=1
        if e>=4:
            e+=1
            if a[1]==9:
                a3["text"]='X'
                a3["bg"]='yellow'
                if e>=6:
                    if a[2]==2:
                        a7["text"]='X'
                        a7["bg"]='yellow' 
                    else:
                        a2["text"]='X'
                        a2["bg"]='yellow'
                    l1.configure(text="YOU LOST")
            else:
                a9["text"]='X'
                a9["bg"]='yellow' 
                l1.configure(text="YOU LOST")
    if a[0]==8:
        a5["text"]='X'
        a5["bg"]='yellow'
        if e==2:
            e+=1
        if e>=4:
            e+=1
            if a[1]==9:
                a7["text"]='X'
                a7["bg"]='yellow'
                if e>=6:
                    if a[2]==3:
                        a4["text"]='X'
                        a4["bg"]='yellow' 
                    else:
                        a3["text"]='X'
                        a3["bg"]='yellow'
                    l1.configure(text="YOU LOST")
            else:
                a9["text"]='X'
                a9["bg"]='yellow' 
                l1.configure(text="YOU LOST")
    if a[0]==5:
        a9["text"]='X'
        a9["bg"]='yellow'
        if e==2:
            e=e+1
        if e>=4:
            if a[1]==3:
                a7["text"]='X'
                a7["bg"]='yellow'
            if a[1]==7:
                a3["text"]='X'
                a3["bg"]='yellow'
            if a[1]==2:
                a8["text"]='X'
                a8["bg"]='yellow'
            if a[1]==8:
                a2["text"]='X'
                a2["bg"]='yellow'
            if a[1]==4:
                a6["text"]='X'
                a6["bg"]='yellow'
            if a[1]==6:
                a4["text"]='X'
                a4["bg"]='yellow'
            if e==4:
                e=e+1
            if e>=6:
                if e==6:
                    e=e+1
                if a[2]==8 and a[1]==3:
                    a4["text"]='X'
                    a4["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]!=8 and a[1]==3:
                    a8["text"]='X'
                    a8["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]==6 and a[1]==7:
                    a2["text"]='X'
                    a2["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]!=6 and a[1]==7:
                    a6["text"]='X'
                    a6["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]==7 and a[1]==2:
                    a4["text"]='X'
                    a4["bg"]='yellow'
                    if e>=8:
                        if a[3]==3:
                            a6["text"]='X'
                            a6["bg"]='yellow'
                            l1.configure(text="MATCH TIE")
                        if a[3]==6:
                            a3["text"]='X'
                            a3["bg"]='yellow'
                            l1.configure(text="MATCH TIE")
                if a[2]!=7 and a[1]==2:
                    a7["text"]='X'
                    a7["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]==3 and a[1]==8:
                    a7["text"]='X'
                    a7["bg"]='yellow'
                    if e>=8:
                        if a[3]==4:
                            a6["text"]='X'
                            a6["bg"]='yellow'
                            l1.configure(text="MATCH TIE")
                        if a[3]==6:
                            a4["text"]='X'
                            a4["bg"]='yellow'
                            l1.configure(text="MATCH LOST")
                if a[2]!=3 and a[1]==8:
                    a3["text"]='X'
                    a3["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]==3 and a[1]==4:
                     a7["text"]='X'
                     a7["bg"]='yellow'
                     if e>=8:
                        if a[3]==2:
                            a8["text"]='X'
                            a8["bg"]='yellow'
                            l1.configure(text="YOU LOST")
                        if a[3]==8:
                            a2["text"]='X'
                            a2["bg"]='yellow'
                            l1.configure(text="MATCH TIE")
                if a[2]!=3 and a[1]==4:
                    a3["text"]='X'
                    a3["bg"]='yellow'
                    l1.configure(text="YOU LOST")
                if a[2]==7 and a[1]==6:
                    a3["text"]='X'
                    a3["bg"]='yellow'
                    if e>=8:
                        if a[3]==2:
                            a8["text"]='X'
                            a8["bg"]='yellow'
                            l1.configure(text="MATCH TIE")
                        if a[3]==8:
                            a2["text"]='X'
                            a2["bg"]='yellow'
                            l1.configure(text="YOU LOST")
                if a[2]!=7 and a[1]==6:
                    a7["text"]='X'
                    a7["bg"]='yellow'
                    l1.configure(text="YOU LOST")

def win2(event):
    global e
    if(a2["text"]=='2'):
        a2["text"]='O'
        a2["bg"]='deeppink'
        e=e+1
        a.append(2)
        cal()
def win3(event):
    global e
    if(a3["text"]=='3'):
        a3["text"]='O'
        a3["bg"]='deeppink'
        e=e+1 
        a.append(3)
        cal()
def win4(event):
    global e
    if(a4["text"]=='4'):
        a4["text"]='O'
        a4["bg"]='deeppink'
        e=e+1
        a.append(4)
        cal()
def win5(event):
    global e
    if(a5["text"]=='5'):
        a5["text"]='O'
        a5["bg"]='deeppink'
        e=e+1
        a.append(5)
        cal()
def win6(event):
    global e
    if(a6["text"]=='6'):
        a6["text"]='O'
        a6["bg"]='deeppink'
        e=e+1
        a.append(6)
        cal()
def win7(event):
    global e
    if(a7["text"]=='7'):
        a7["text"]='O'
        a7["bg"]='deeppink'
        e=e+1
        a.append(7)
        cal()
def win8(event):
    global e
    if(a8["text"]=='8'):
        a8["text"]='O'
        a8["bg"]='deeppink'
        e=e+1
        a.append(8)
        cal()
def win9(event):
    global e
    if(a9["text"]=='9'):
        a9["text"]='O'
        a9["bg"]='deeppink'
        e=e+1
        a.append(9)
        cal()
def click1(event):
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,l1,f4
    f=Frame(root,bg="lightgreen")
    f.pack(fill=BOTH)
    f1=Frame(f,bg="lightgreen")
    f1.pack()
    a1=Button(f1,text="X",bg="yellow",font=("bradley hand itc",22,"bold"),width=5)
    a1.pack(side=LEFT,padx=4,pady=3,fill=X)
    a2=Button(f1,text="2",font=("bradley hand itc",22,"bold"),width=5)
    a2.bind("<Button-1>",win2)
    a2.pack(side=LEFT,padx=4,pady=3)
    a3=Button(f1,text="3",font=("bradley hand itc",22,"bold"),width=5)
    a3.bind("<Button-1>",win3)
    a3.pack(side=LEFT,padx=4,pady=3)
    
    f2=Frame(f,bg="lightgreen")
    f2.pack()
    a4=Button(f2,text="4",font=("bradley hand itc",22,"bold"),width=5)
    a4.bind("<Button-1>",win4)
    a4.pack(side=LEFT,padx=4,pady=3,fill=X)
    a5=Button(f2,text="5",font=("bradley hand itc",22,"bold"),width=5)
    a5.bind("<Button-1>",win5)
    a5.pack(side=LEFT,padx=4,pady=3,fill=X)
    a6=Button(f2,text="6",font=("bradley hand itc",22,"bold"),width=5)
    a6.bind("<Button-1>",win6)
    a6.pack(side=LEFT,padx=4,pady=3,fill=X)
    
    f3=Frame(f,bg="lightgreen")
    f3.pack()
    a7=Button(f3,text="7",font=("bradley hand itc",22,"bold"),width=5)
    a7.bind("<Button-1>",win7)
    a7.pack(side=LEFT,padx=4,pady=3,fill=X)
    a8=Button(f3,text="8",font=("bradley hand itc",22,"bold"),width=5)
    a8.bind("<Button-1>",win8)
    a8.pack(side=LEFT,padx=4,pady=3,fill=X)
    a9=Button(f3,text="9",font=("bradley hand itc",22,"bold"),width=5)
    a9.bind("<Button-1>",win9)
    a9.pack(side=LEFT,padx=4,pady=3,fill=X)
    
    f4=Frame(f,bg="lightgreen")
    f4.pack()
    a10=Button(f4,text="Exit",bg="skyblue",font=("bradley hand itc",22,"bold"),width=5,command=root.destroy)
    a10.pack(side=LEFT,anchor="sw",padx=4,pady=3,fill=X) 
    wl1=StringVar()
    a22="Your turn"
    l1=Label(f4,text=a22,bg="lightgreen",font=("bradley hand itc",18,"bold"))
    l1.pack(side=LEFT,padx=4,pady=3,fill=X)
def calm():
    s1=set(a)
    s2=set(b)
    s3={*s1,*s2}
    if s1.issuperset({1,2,3}) or s1.issuperset({4,5,6}) or s1.issuperset({7,8,9}) or s1.issuperset({1,4,7}) or s1.issuperset({2,5,8}) or s1.issuperset({3,6,9}) or s1.issuperset({1,5,9}) or s1.issuperset({3,5,7}):
        l2.configure(textvariable=n1)
        l3.configure(text="Wins")
    elif s2.issuperset({1,2,3}) or s2.issuperset({4,5,6}) or s2.issuperset({7,8,9}) or s2.issuperset({1,4,7}) or s2.issuperset({2,5,8}) or s2.issuperset({3,6,9}) or s2.issuperset({1,5,9}) or s2.issuperset({3,5,7}):
        l2.configure(textvariable=n2)
        l3.configure(text="Wins")
    elif s3.issuperset({1,2,3,4,5,6,7,8,9}):
        l2.destroy()
        l3.configure(text="Match Tie")
def winm1(event):
    global e
    if m1["text"]=="1":
       if(e%2==1):
          m1["text"]='X'
          m1["bg"]='deeppink'
          e=e+1
          a.append(1)
          l2.configure(textvariable=n2)
       else:
          m1["text"]='O'
          m1["bg"]='yellow'
          e=e+1
          b.append(1)
          l2.configure(textvariable=n1)
       calm()
def winm2(event):
    global e
    if m2["text"]=="2":
       if(e%2==1):
          m2["text"]='X'
          m2["bg"]='deeppink'
          e=e+1
          a.append(2)
          l2.configure(textvariable=n2)
       else:
          m2["text"]='O'
          m2["bg"]='yellow'
          e=e+1
          b.append(2)
          l2.configure(textvariable=n1)
       calm()      
def winm3(event):
    global e
    if m3["text"]=="3":
       if(e%2==1):
          m3["text"]='X'
          m3["bg"]='deeppink'
          e=e+1
          a.append(3)
          l2.configure(textvariable=n2)
       else:
          m3["text"]='O'
          m3["bg"]='yellow'
          e=e+1
          b.append(3)
          l2.configure(textvariable=n1)
       calm()
def winm4(event):
    global e
    if m4["text"]=="4":
       if(e%2==1):
          m4["text"]='X'
          m4["bg"]='deeppink'
          e=e+1
          a.append(4)
          l2.configure(textvariable=n2)
       else:
          m4["text"]='O'
          m4["bg"]='yellow'
          e=e+1
          b.append(4)
          l2.configure(textvariable=n1)
       calm()
def winm5(event):
    global e
    if m5["text"]=="5":
       if(e%2==1):
          m5["text"]='X'
          m5["bg"]='deeppink'
          e=e+1
          a.append(5)
          l2.configure(textvariable=n2)
       else:
          m5["text"]='O'
          m5["bg"]='yellow'
          e=e+1
          b.append(5)
          l2.configure(textvariable=n1)
       calm()
def winm6(event):
    global e
    if m6["text"]=="6":
       if(e%2==1):
          m6["text"]='X'
          m6["bg"]='deeppink'
          e=e+1
          a.append(6)
          l2.configure(textvariable=n2)
       else:
          m6["text"]='O'
          m6["bg"]='yellow'
          e=e+1
          b.append(6)
          l2.configure(textvariable=n1)
       calm()
def winm7(event):
    global e
    if m7["text"]=="7":
       if(e%2==1):
          m7["text"]='X'
          m7["bg"]='deeppink'
          e=e+1
          a.append(7)
          l2.configure(textvariable=n2)
       else:
          m7["text"]='O'
          m7["bg"]='yellow'
          e=e+1
          b.append(7)
          l2.configure(textvariable=n1)
       calm()
def winm8(event):
    global e
    if m8["text"]=="8":
       if(e%2==1):
          m8["text"]='X'
          m8["bg"]='deeppink'
          e=e+1
          a.append(8)
          l2.configure(textvariable=n2)
       else:
          m8["text"]='O'
          m8["bg"]='yellow'
          e=e+1
          b.append(8)
          l2.configure(textvariable=n1)
       calm()
def winm9(event):
    global e
    if m9["text"]=="9":
       if(e%2==1):
          m9["text"]='X'
          m9["bg"]='deeppink'
          e=e+1
          a.append(9)
          l2.configure(textvariable=n2)
       else:
          m9["text"]='O'
          m9["bg"]='yellow'
          e=e+1
          b.append(9)
          l2.configure(textvariable=n1)
       calm()
def name(event):
    global n1,n2
    f12=Frame(root,bg="lightgreen")
    f12.pack()
    n1=StringVar()
    la=Label(f12,text="Player 1:",bg="lightgreen",font=("bradley hand itc",22,"bold"))
    la.pack()
    law=Entry(f12,textvariable=n1,font=("bradley hand itc",22,"bold"),bg="yellow",fg="blue")
    law.pack()
    n2=StringVar()
    lb=Label(f12,text="Player 2:",bg="lightgreen",font=("bradley hand itc",22,"bold"))
    lb.pack()
    lbw=Entry(f12,textvariable=n2,font=("bradley hand itc",22,"bold"),bg="yellow",fg="blue")
    lbw.pack()
    Label(f12,text="",bg="lightgreen").pack()
    b60=Button(f12,text="START",bg="orange",font=("braddley hand itc",22,"bold"),width=11,command=f12.destroy)
    b60.bind("<Button-1>",click2)
    b60.pack(side=BOTTOM)
def click2(event):
    global m1,m2,m3,m4,m5,m6,m7,m8,m9,l2,f4,l3
    f=Frame(root,bg="lightgreen")
    f.pack(fill=BOTH)
    f1=Frame(f,bg="lightgreen")
    f1.pack()
    m1=Button(f1,text="1",font=("bradley hand itc",22,"bold"),width=5)
    m1.bind("<Button-1>",winm1)
    m1.pack(side=LEFT,padx=4,pady=3,fill=X)
    m2=Button(f1,text="2",font=("bradley hand itc",22,"bold"),width=5)
    m2.bind("<Button-1>",winm2)
    m2.pack(side=LEFT,padx=4,pady=3)
    m3=Button(f1,text="3",font=("bradley hand itc",22,"bold"),width=5)
    m3.bind("<Button-1>",winm3)
    m3.pack(side=LEFT,padx=4,pady=3)
    
    f2=Frame(f,bg="lightgreen")
    f2.pack()
    m4=Button(f2,text="4",font=("bradley hand itc",22,"bold"),width=5)
    m4.bind("<Button-1>",winm4)
    m4.pack(side=LEFT,padx=4,pady=3,fill=X)
    m5=Button(f2,text="5",font=("bradley hand itc",22,"bold"),width=5)
    m5.bind("<Button-1>",winm5)
    m5.pack(side=LEFT,padx=4,pady=3,fill=X)
    m6=Button(f2,text="6",font=("bradley hand itc",22,"bold"),width=5)
    m6.bind("<Button-1>",winm6)
    m6.pack(side=LEFT,padx=4,pady=3,fill=X)
    
    f3=Frame(f,bg="lightgreen")
    f3.pack()
    m7=Button(f3,text="7",font=("bradley hand itc",22,"bold"),width=5)
    m7.bind("<Button-1>",winm7)
    m7.pack(side=LEFT,padx=4,pady=3,fill=X)
    m8=Button(f3,text="8",font=("bradley hand itc",22,"bold"),width=5)
    m8.bind("<Button-1>",winm8)
    m8.pack(side=LEFT,padx=4,pady=3,fill=X)
    m9=Button(f3,text="9",font=("bradley hand itc",22,"bold"),width=5)
    m9.bind("<Button-1>",winm9)
    m9.pack(side=LEFT,padx=4,pady=3,fill=X)
    
    f4=Frame(f,bg="lightgreen")
    f4.pack()
    m10=Button(f4,text="Exit",bg="skyblue",font=("bradley hand itc",22,"bold"),width=5,command=root.destroy)
    m10.pack(side=LEFT,anchor="sw",padx=4,pady=3,fill=X) 
    wl1=StringVar()
    l2=Label(f4,textvariable=n1,bg="lightgreen",font=("bradley hand itc",18,"bold"))
    l2.pack(side=LEFT,padx=4,pady=3,fill=X)  
    l3=Label(f4,text="Turn",bg="lightgreen",font=("bradley hand itc",18,"bold"))
    l3.pack(side=LEFT,padx=4,pady=3,fill=X)

root=Tk()
root.geometry("400x380")
root.title("Tic Tac Toe")
root.config(bg="lightgreen")
Label(root,text="Tic Tac Toe",font=("bradley hand itc",25," bold"),bg="lightgreen").pack()
f=Frame(root,bg="lightgreen")
f.pack()
Label(f,text="",bg="lightgreen").pack()
y=Button(f,text="Single Player",font=("bradley hand itc",22,"bold"),width=11,command=f.destroy)
y.bind("<Button-1>",click1)
y.pack()
Label(f,text="",bg="lightgreen").pack()
z=Button(f,text="Multi Player",font=("bradley hand itc",22,"bold"),width=11,command=f.destroy)
z.bind("<Button-1>",name)
z.pack()
root.mainloop()
