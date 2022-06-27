#This code i made while learning Allen B. Downey's book.
import turtle
from mypolygon import circle, arc

t = turtle.Turtle()

"""
simple functions which moving turtle. 1st block
"""

#1. Move forward to the distance of attribute 'length'
def fd(t, length):
    t.fd(length)
    

#2. Move backward to the distance of attribute 'length'
def bk(t, length):
    t.bk(length)

#3. Incline turtle to the position 'left'
def lt(t, angle=90):
    t.lt(angle)

#4. Incline turtle to the position 'right'
def rt(t, angle=90):
    t.rt(angle)

#5. Function that makes penup
def pu(t):
    t.pu()

#6. Function that makes pendown
def pd(t):
    t.pd()

"""
Level 1. Functions with simple combinations
"""

#1. forward and left
def fdlt(t, n, angle=90):
    fd(t, n)
    lt(t, angle)

#2. forward and back to the original position
def fdbk(t, n):
    fd(t, n)
    bk(t, n)

#3. lift the pan and move
def skip(t, n):
    pu(t)
    fd(t, n)
    pd(t)

#4. function that draws vertical line, leaves turtle at
    #the top and straight to the right
def stump(t, n, angle=90):
    lt(t)
    fd(t, n)
    rt(t, angle)

#5. function that just move the turtle,
    # which staight to the right, to the top
def hollow(t, n):
    lt(t)
    skip(t, n)
    rt(t)

"""
Level 2. Also simple , but these functions always return the turtle to the
original position and direction
"""

#1. Draws vertical line and goes back to the original position

def post(t, n):
    lt(t)
    fdbk(t, n)
    rt(t)
#2. draws a horizontal line that goes on seted height and return

def beam(t, n, height):
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

#3. draws vertical line at the given height and
    # also horizontal at the given height

def hangman(t, n, height):
    stump(t, n*height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

#4. draws a diagonal from the point x to point y and return
def diagonal(t, x, y):
    from math import atan2, sqrt, pi
    angle = atan2(y, x)*180/pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

#5. draws V-shaped line
def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

#6. draws a bump with ranius n at height*n
def bump(t, n, height):
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)

"""
LETTERS:
"""

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)
    
def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t,n,2)
    fd(t,n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    skip(t, n)
    post(t, 2*n)
    lt(t)
    skip(t, n)
    lt(t)
    fd(t, n)
    lt(t)
    skip(t, n)
    lt(t)
    skip(t, n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)
    
def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    fd(t, n)


def draw_m(t, n):
    post(t, n*2)
    lt(t)
    fd(t, n)
    rt(t)
    skip(t, n)
    vshape(t, 2*n, 0.5)
    skip(t, n)
    rt(t)
    skip(t, n)
    lt(t)
    post(t, n*2)


def draw_n(t, n):
    post(t, n*2)
    skip(t, n)
    post(t, n*2)
    diagonal(t, -n, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)
    
def draw_q(t, n):
    circle(t, n)
    skip(t, n)
    lt(t)
    diagonal(t, n/2, n)
    rt(t)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    fd(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, n*2)
    fd(t, n)
    post(t, n*2)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_y(t, n):
    lt(t)
    fd(t, n)
    rt(t)
    vshape(t, n, 1)
    rt(t)
    skip(t, n)
    lt(t)

def draw_z(t, n):
    lt(t)
    skip(t, n)
    rt(t)
    fd(t, n)
    diagonal(t, -n, -n)
    rt(t)
    skip(t, n)
    rt(t)
    fd(t, n)
    lt(t)
    lt(t)
    skip(t, n)

def draw_(t, n):
    skip(t, n/2)
    
if __name__ == '__main__':

    size = 20
    bob=turtle.Turtle()

    for f in [draw_i, draw_, draw_l, draw_o, draw_v, draw_e, draw_, draw_y, draw_o, draw_u]:
        f(bob, size)
        skip(bob, size)
        t.hideturtle()

t.hideturtle()
turtle.mainloop()
