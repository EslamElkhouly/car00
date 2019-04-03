from OpenGL.GL import* #فيها برسم الموديل
from OpenGL.GLUT import*    #
from OpenGL.GLU import *# فيها حاجات جاهزه
import numpy as np
from math import *

'''

def Draw_circle (r=.05,xc=0,yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi,.001 ):
        glColor3f(0,0, 1)
        x = xc+r * cos(theta)  # لو عاوز اغير المركز  هزو على اكس الزياده وكذلك واى
        y = yc+r * sin(theta)

        glVertex(x, y)
    # glVertex(1, 1)
    glEnd()
    '''

def arrowkeys(key,x,y):
    global car_z
    global car_x
    if key==GLUT_KEY_LEFT:
        car_z-=.5
    elif key== GLUT_KEY_RIGHT:
        car_z += .5
    elif key==GLUT_KEY_UP:
        car_x+=.5
    elif key==GLUT_KEY_DOWN:
        car_x-=.5
    display()

def trees():
    glColor3f(.4,.3,0)
    glBegin(GL_POLYGON)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)
    glVertex(-1, -1, 1)
    glVertex(1, -1, 1)
    glEnd()


def my_polygon():

    glBegin(GL_QUADS)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)
    glVertex(-1, 1, 1)
    glVertex(1, 1, 1)
    glEnd()
def sky(x):
    glutSolidSphere(x,100,100)


def myInit():

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90,1,0.1,60)
    gluLookAt(5,10,10,
              0,0,0,
              0,1,0)
    glClearColor(0,0,0,1)
    glClear((GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT))

angle=0
x=0
forward=True
car_z=0
car_x=0
def display():
    #glClearColor(0,0,0,1) # night mood
    glClearColor(0, .6, .1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global car_z
    global angle
    global x
    global forward
    global car_x

    glMatrixMode(GL_MODELVIEW)

    # the Road
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glScale(1000, 0, 4)
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)

    glVertex(-1, -1, 1)
    glVertex(1, -1, 1)
    glEnd()

#the ball
    glColor3f(0,0,0)
    glLoadIdentity()
    glTranslate(0, 3, -1 - ((x * 4) + .01 * x))
    glutWireSphere(1, 10, 10)
    # polygon on road

    glLoadIdentity()
    glColor3f(1, 1, 0)
    glRotate(90, 0, 1, 0)
    glScale(4, 0, .5)
    glTranslate(0-x, 0, 0)
    my_polygon()


    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glScale(4, 0, .5)
    glTranslate(-3-x, 0, 0)
    my_polygon()


    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glScale(4, 0, .5)
    glTranslate(-6-x, 0, 0)
    my_polygon()

    glLoadIdentity()
    glColor3f(1, 1, 0)
    glRotate(90, 0, 1, 0)
    glScale(4, 0, .5)
    glTranslate(6 - x, 0, 0)
    my_polygon()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glScale(4, 0, .5)
    glTranslate(3-x, 0, 0)
    my_polygon()

    # the sky
    # glColor3f(.4,.3,.8) #night mood
    glColor3f(0, .2, 1)
    glLoadIdentity()
    glScale(100, 1, 3)
    glTranslate(0, 10, 0)
    glBegin(GL_POLYGON)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)
    glVertex(-1, -1, 1)
    glVertex(1, -1, 1)
    glEnd()
    glLoadIdentity()

    # the Sky
    # sun
    glColor3f(1, 1, 1)  # night mode
    glColor3f(.8, .4, 0)
    glLoadIdentity()
    glTranslate(-x * .05 + 3, 10, 2)
    sky(.25)

    # First cloud
    # glColor3f(.7,.7,.7) #night mode
    glColor3f(1, 1, 1)
    glLoadIdentity()
    glTranslate(0 + x * .05, 10, 2)
    sky(.45)

    glLoadIdentity()
    glTranslate(.5 + x * .05, 10, 2)
    sky(.25)

    glLoadIdentity()
    glTranslate(-0.5 + x * .05, 10, 2)
    sky(.25)





    # second tree

    glLoadIdentity()
    glColor3f(.4, .3, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(-4, 2, -5)
    glScale(.5, 2, 0)
    trees()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-4.5, 4, -5)
    glColor3f(.4, .6, 0)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-3.5, 4, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-3.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-4.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(-4, 6, -5)
    glutSolidSphere(1, 100, 100)

    # third tree
    glLoadIdentity()
    glColor3f(.4, .3, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(2, 2, -5)
    glScale(.5, 2, 0)
    trees()

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(1.5, 4, -5)
    glColor3f(.4, .6, 0)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5, 4, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(1.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2, 6, -5)
    glutSolidSphere(1, 100, 100)

# المكعب اللى فوق
    glColor3f(1, 0, 0)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(car_x,0+2,car_z)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

#المكعب اللى تحت

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(car_x,.25*5+2,car_z)
    glScale(0.5,.25,.5)
    glutSolidCube(5)



#first wheel
    glLoadIdentity()
    glColor3f(0,0,1)
    glRotate(90, 0, 1, 0)
    glTranslate(2.5+car_x,-2.5*.25+2,.5*2.5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15,.5,12,8)
#second wheel
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(2.5+car_x, -2.5 * .25+2,- .5 * 2.5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, .5, 12, 8)
#third wheel
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-2.5+car_x, -2.5 * .25+2, .5 * 2.5+car_z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, .5, 12, 8)

#forth wheel
    glLoadIdentity()
    glColor3f(0, 0, 1)
    glRotate(90, 0, 1, 0)
    glTranslate(-2.5+car_x, -2.5 * .25+2, -.5 * 2.5+car_z)
    glRotate(angle,0,0,1)
    glutWireTorus(0.15, .5, 12, 8)

#first light

    glColor3f(1,1,0)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5+car_x,-.5*2.5*.25+2,-2.5*.25+car_z)
    glutWireSphere(.25,100,100)

#second light


    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(2.5+car_x, -.5*2.5*.25+2, 2.5*.25+car_z)
    glutWireSphere(.25, 100, 100)




    if forward:
        x+=.05
        angle -= .1
        if x>5:
            forward=False
    else:
        x-=.05
        angle += .1
        if x<-5:
            forward=True







    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)# لو استخدمت
glutInitWindowSize(720,1260)
glutCreateWindow(b"Moving Car")
glutDisplayFunc(display)
glutIdleFunc(display)
glutSpecialFunc(arrowkeys)
myInit()
glutMainLoop()

