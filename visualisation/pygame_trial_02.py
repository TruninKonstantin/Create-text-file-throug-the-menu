import pygame, sys, math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def rotate(key, rotation):
    rotation += 1
    if key[pygame.K_LEFT]: glRotate(rotation, 0, 1, 0)
    if key[pygame.K_RIGHT]: glRotate(rotation, 0, -1, 0)
    if key[pygame.K_UP]: glRotate(rotation, 1, 0, 0)
    if key[pygame.K_DOWN]: glRotate(rotation, -1, 0, 0)


def events_mouse_move(event):
    if event.type == pygame.MOUSEMOTION:
        x, y = event.rel
        x /= 10
        y /= 10
        glTranslatef(x,-y,0)


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
    glVertex(0, 0, s)
    for (x, y) in circle_pts:
        z = s
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
    glColor(0, 0, 1)
    glVertex(0, 0, h+s)
    for (x, y) in circle_pts:
        z = h+s
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)  # draw the tube
    glColor(0, 1, 0)
    for (x, y) in circle_pts:
        # z = h / 2.0 + s
        glVertex(x, y, s)
        glVertex(x, y, h+s)
    glEnd()


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(30, (display[0] / display[1]), 1, 1000)
glTranslatef(0, 0, -200)
glRotatef(0, 0, 0, 0)

moveWithMouse = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         glTranslatef(-0.5, 0, 0)
        #     if event.key == pygame.K_RIGHT:
        #         glTranslatef(0.5, 0, 0)
        #     if event.key == pygame.K_UP:
        #         glTranslatef(0, 1, 0)
        #     if event.key == pygame.K_DOWN:
        #         glTranslatef(0, -1, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0, 0, 1.0)
            if event.button == 5:
                glTranslatef(0, 0, -1.0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moveWithMouse = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moveWithMouse = False
        if moveWithMouse == True: events_mouse_move(event)

    # glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_DEPTH_TEST)
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()




    draw_cylinder(5, 10, 20, 0)
    draw_cylinder(3, 0.1, 20, 10)

    pygame.display.flip()
    pygame.time.wait(10)
    key = pygame.key.get_pressed()
    rotate(key, 5)
