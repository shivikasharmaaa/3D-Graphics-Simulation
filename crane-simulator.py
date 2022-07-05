# Import the header files
from glob import glob
from os import stat
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

"""
Buttons:
x,y,z   :   Rotate about the respective axis
r       :   Reverse the direction of rotation
n       :   Change the target arm of the crane
m       :   Rotate the target arm of the crane
a,w,s,d :   Car-like movement
"""

# Set the global values

# Camera
frustrum_z = -5

x_axis = 0
y_axis = 0
z_axis = 0

# Crane arm movement
centre_x = 0
centre_y = 0
centre_z = -25

crane_values = [0,-45,-90,-20]
crane_pointer = 0

# Wheels parameters
wheel_theta = 0
wheel_theta_rate = 5

turn_theta = 0
turn_theta_rate = 2
turn_theta_cap = 30

# General parameters
angle_step = 2
direction = 1

# Color parameters
colors = [0, 0, 0, 1]

def wired_hollow_rectangle(l,b,h):
    """
    Function to make a cuboid out of cubes, given sides as integers.
    """
    global colors

    glScalef(l, h, b)
    glutSolidCube(1)
    glScalef(1/l, 1/h, 1/b)

# Function to make the vehicle
def draw_crane():
    global colors

    colors = [0.05,0.05,0.05,1]

    # Make the base
    glTranslatef(0, 3, 0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    wired_hollow_rectangle(7, 15, 2)

    # Front left tire
    colors = [0.05, 0.05, 0.05, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(-3.5, -1, -5.5)
    glRotatef(-90-turn_theta,0,1,0)
    glRotatef(wheel_theta,0,0,1)
    glutSolidCylinder(2, 1, 15, 15)

    colors = [0.3, 0.3, 0.3, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(0,0,1.2)
    wired_hollow_rectangle(1,0.4,1)
    glTranslatef(0,0,-1.2)

    glRotatef(-wheel_theta,0,0,1)
    glRotatef(90+turn_theta,0,1,0)

    # Front right tire
    colors = [0.05, 0.05, 0.05, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(7,0,0)
    glRotatef(90-turn_theta,0,1,0)
    glRotatef(-wheel_theta,0,0,1)
    glutSolidCylinder(2, 1, 15, 15)

    colors = [0.3, 0.3, 0.3, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(0,0,1.2)
    wired_hollow_rectangle(1,0.4,1)
    glTranslatef(0,0,-1.2)
    
    glRotatef(wheel_theta,0,0,1)
    glRotatef(-90+turn_theta,0,1,0)

    # Back right tire
    colors = [0.05, 0.05, 0.05, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(0,0,11)
    glRotatef(90,0,1,0)
    glRotatef(-wheel_theta,0,0,1)
    glutSolidCylinder(2, 1, 15, 15)
    
    colors = [0.3, 0.3, 0.3, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(0,0,1.2)
    wired_hollow_rectangle(1,0.4,1)
    glTranslatef(0,0,-1.2)

    glRotatef(wheel_theta,0,0,1)
    glRotatef(-90,0,1,0)

    # Back left tire
    colors = [0.05, 0.05, 0.05, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(-7,0,0)
    glRotatef(-90,0,1,0)
    glRotatef(wheel_theta,0,0,1)
    glutSolidCylinder(2, 1, 15, 15)
    
    colors = [0.3, 0.3, 0.3, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glTranslatef(0,0,1.2)
    wired_hollow_rectangle(1,0.4,1)
    glTranslatef(0,0,-1.2)
    
    glRotatef(-wheel_theta,0,0,1)
    glRotatef(90,0,1,0)

    # Translate to the centre again
    glTranslatef(3.5,2.5,-5.5)

    # Draw the rotating base and the cabin. Translate to the centre of the rotating base
    colors = [1, 0.65, 0, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)

    glRotatef(crane_values[0],0,1,0)
    wired_hollow_rectangle(7, 15, 1)
    glTranslatef(0,2.5,4)
    colors = [1, 0.65, 0, 1]

    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    wired_hollow_rectangle(7, 7, 4)
    glTranslatef(0,-2.5,-4)

    colors = [1, 0.65, 0, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)

    # Draw the first arm
    glTranslatef(0,1.5,-4)
    glutSolidCube(2.2)

    colors = [0.1, 0.1, 0.1, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    glRotatef(crane_values[1],1,0,0)
    glTranslatef(0,5.5,0)
    wired_hollow_rectangle(2, 2, 11)

    # Draw the second arm
    colors = [0.1, 0.1, 0.1, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)

    glTranslatef(0,5.5,0)
    glRotatef(crane_values[2],1,0,0)
    glTranslatef(0,3.5,0)
    wired_hollow_rectangle(1.8, 1.8, 7)

    # Draw the scoop
    colors = [0.4, 0.4, 0.4, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)

    glTranslatef(0,3.5,0)
    glRotatef(crane_values[3],1,0,0)
    glTranslatef(0,1.5,0)
    wired_hollow_rectangle(4, 1, 3)

    glTranslatef(0,2,-1.5)
    wired_hollow_rectangle(4, 4, 1)
    glTranslatef(0,-2,1.5)

    # reverse the rotations and translations
    colors = [0, 0, 1, 1]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)

    glTranslatef(0,-1.5,0)
    glRotatef(-crane_values[3],1,0,0)
    glTranslatef(0,-7,0)
    glRotatef(-crane_values[2],1,0,0)
    glTranslatef(0,-5.5,0)
    glTranslatef(0,-5.5,0)
    glRotatef(-crane_values[1],1,0,0)
    glTranslatef(0,-2.5,4)
    glRotatef(-crane_values[0],0,1,0)
    glTranslatef(0,-3.5,0)

# Drawing routine.
def display():

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glLoadIdentity()  

    # Rotate the set around the centre to position it correctly
    glTranslatef(centre_x, centre_y, centre_z)
    glRotatef(x_axis, 1, 0, 0)
    glRotatef(y_axis, 0, 1, 0)
    glRotatef(z_axis, 0, 0, 1)

    # Create the scene below
    colors = [0.3, 0.3, 0.3, 1]
    glTranslatef(0, -0.5, 0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, colors)
    wired_hollow_rectangle(30, 30, 1)
    glTranslatef(0, 0.5, 0)

    colors = [0, 0, 1]
    draw_crane()

    glPopMatrix()
    glutSwapBuffers()

    glFlush()  

# Initialization routine.
def myInit():
	glClearColor(1.0, 1.0, 1.0, 0.0)  

# OpenGL window reshape routine.
def resize (w, h):
	glViewport(0, 0, w, h)  
	glMatrixMode(GL_PROJECTION)  
	glLoadIdentity()  
	glFrustum(-5.0, 5.0, -5.0, 5.0, -frustrum_z, 100.0)  
	glMatrixMode(GL_MODELVIEW)  
 
# Keyboard input processing routine.
def keyInput (key, x, y):
    global direction, x_axis, y_axis, z_axis, centre_z, crane_values, crane_pointer, wheel_theta, turn_theta, light_y

    if direction == 1:
        # Anticlockwise rotation
        change = angle_step
    else:
        # Clockwise rotation
        change = -angle_step
        
    if key == b'x':
        x_axis += change

    elif key == b'y':
        y_axis += change

    elif key == b'z':
        z_axis += change

    elif key == b'r':
        direction = -direction

    elif key == b'i':
        centre_z += 1
        if centre_z > frustrum_z:
            centre_z = frustrum_z

    elif key == b'o':
        centre_z -= 1
    
    elif key == b'n':
        crane_pointer += 1
        if crane_pointer > 3:
            crane_pointer = 0

    elif key == b'm':
        crane_values[crane_pointer] += change

    elif key == b'a':
        turn_theta -= turn_theta_rate
        if turn_theta < -turn_theta_cap:
            turn_theta = -turn_theta_cap

    elif key == b'd':
        turn_theta += turn_theta_rate
        if turn_theta > turn_theta_cap:
            turn_theta = turn_theta_cap

    elif key == b'w':
        wheel_theta += wheel_theta_rate

    elif key == b's':
        wheel_theta -= wheel_theta_rate

    glutPostRedisplay()

# Main routine.

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("Mini project")
glClearColor(0., 0., 0., 1.)
glShadeModel(GL_SMOOTH)
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)

# Lighting
lightZeroPosition = [0, 5, -5, 1]
lightZeroColor = [0.8,0.8,0.8, 1]
glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.01)
glEnable(GL_LIGHT0)

glutDisplayFunc(display)
glutReshapeFunc(resize)
glutKeyboardFunc(keyInput)  

glMatrixMode(GL_PROJECTION)
glMatrixMode(GL_MODELVIEW)

myInit()
glPushMatrix()
glutMainLoop()
