import turtle
import traceback

def draw_triagle(x1,y1,x2,y2,x3,y3,t):
    t.up()
    t.setpos(x1,y1)
    t.down()
    t.setpos(x2,y2)
    t.setpos(x3,y3)
    t.setpos(x1,y1)



def main():
    try:
        print('drawin triangle')
        t = turtle.Turtle()
        t.hideturtle()
        draw_triagle(-100,0,0,173,100,0,t)
        turtle.mainloop()
    except Exception as e:
        print(f'error drawing the triangle {e}')


if __name__ == '__main__':
    main()

