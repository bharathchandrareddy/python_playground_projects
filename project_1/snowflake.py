import math
import turtle
def snowflake(x1,y1,x2,y2,t):
    d = math.sqrt((x1-x2)*(x1-x2)) + ((y1-y2)*(y1-y2))
    n = ((y1-y2)/d,(x2-x1)/d)
    r = d/3
    h = (math.sqrt(3)/2)*r
    c = ((x1+x2)/2 , (y1+y2)/2)
    p2 = (c[0]+h*n[0],c[1]+h*n[1])
    p1 = ((2*x1+x2)/3 , (2*y1+y2)/3)
    p3 = ((x1+2*x2)/3, (y1+2*y2)/3)

    if d>10:
        #draw 1st snowflake
        #from A -> p1
        snowflake(x1,y1,p1[0],p1[1],t)
        #from p1 -> p2
        snowflake(p1[0],p1[1],p2[0],p2[1],t)
        #from P2 -> p3
        snowflake(p2[0],p2[1],p3[0],p3[1],t)
        #from p3 -> p4
        snowflake(p3[0],p3[1],x2,y2,t)

    else:
        t.up()
        #set positiion at p1
        t.setpos(p1[0],p1[1])
        t.down()
        #draw line from p2 -> p3
        t.setpos(p2[0],p2[1])
        t.setpos(p3[0],p3[1])
        t.up()
        t.setpos(x1,y1)
        t.down()
        t.setpos(p1[0],p1[1])
        t.up()
        t.setpos(p3[0],p3[1])
        t.setpos(x2,y2)

def main():
    print('starting to print the snowflake')
    t = turtle.Turtle()
    #draw snoflake
    snowflake(100,0,0,-175,t)
    #connect snoflake from previous point to other point
    snowflake(0,-175,-100,0,t)
    #connect previous point to the start point
    snowflake(-100,0,100,0,t)
    turtle.mainloop()
    #except Exception as e:
    #print(f'error occured while drawing {e}')


if __name__ == '__main__':
    main()