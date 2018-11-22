import pygame, sys, math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def rotate(key,rotation):
    rotation+=1
    if key[pygame.K_LEFT]: glRotate(rotation, 0, 1, 0); print("left is pressed")


def draw_cylinder(radius, height, num_slices, shift):
    s = shift
    r = radius
    h = height
    n = float(num_slices)

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i / n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)

    glBegin(GL_TRIANGLE_FAN)  # drawing the back circle
    glColor(1, 0, 0)
    glVertex(0, 0, h / 2.0)
    for (x, y) in circle_pts:
        z = h / 2.0 + s
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
    glColor(0, 0, 1)
    glVertex(0, 0, h / 2.0)
    for (x, y) in circle_pts:
        z = -h / 2.0 + s
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)  # draw the tube
    glColor(0, 1, 0)
    for (x, y) in circle_pts:
        # z = h / 2.0 + s
        glVertex(x, y, h / 2.0 + s)
        glVertex(x, y, -h / 2.0 + s)
    glEnd()

pygame.init()
w, h = 400, 400
cx, cy = w // 2, h // 2
screen = pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)
clock = pygame.time.Clock()

# pygame.event.get(); pygame.mouse.get_rel()
# pygame.mouse.set_visible(0); pygame.event.set_grab(1)
moveWithMouse = False

# rotation = 0.0

while True:

    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE: pygame.quit(); sys.exit()
            if event.type == pygame.K_RIGHT: glRotate(1,0,0,0);print("right is pressed")
            if event.type == pygame.K_UP: glTranslate(+1,0,0);print("up is pressed")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moveWithMouse = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moveWithMouse = False



    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, float(w) / h, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -50)  # move back far enough to see this object
    glRotate(rotation, 0, 1, 0)  # NOTE: this is applied BEFORE the translation due to OpenGL multiply order

    draw_cylinder(5, 10, 20, 0)
    draw_cylinder(3, 5, 20, 10)


    pygame.display.flip()
    clock.tick(60)

    # key = pygame.key.get_pressed()
    # rotate(key,0)


