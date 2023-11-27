from turtle import *
def mycircle(r):
    circle(r)
m=4
x=120
count=0
wishlist_colors=["pink","red","blue","black"]
for i in range(m):
    current_color=wishlist_colors[count]
    color=("red",current_color)
    begin_fill()
    mycircle(x)
    x=x-5
    end_fill()
    count=count+1
    if (count%5==0):
        count=0
        
