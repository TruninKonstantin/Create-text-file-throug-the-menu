import pygame, sys, math


def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x * c - y * s, y * c + x * s


class Cam:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rot[0] += y
            self.rot[1] += x

    def update(self, dt, key):
        s = dt * 10

        # if key[pygame.K_q]: self.pos[1] += s; print("K_q is pressed"); print("dt = " + str(dt) + "s = " + str(s))
        # if key[pygame.K_e]: self.pos[1] -= s; print("K_e is pressed"); print("dt = " + str(dt) + "s = " + str(s))
        #
        # if key[pygame.K_w]: self.pos[2] -= s; print("K_w is pressed"); print("dt = " + str(dt) + "s = " + str(s))
        # if key[pygame.K_s]: self.pos[2] += s; print("K_s is pressed"); print("dt = " + str(dt) + "s = " + str(s))
        #
        # if key[pygame.K_a]: self.pos[0] -= s; print("K_a is pressed"); print("dt = " + str(dt) + "s = " + str(s))
        # if key[pygame.K_d]: self.pos[0] += s; print("K_d is pressed"); print("dt = " + str(dt) + "s = " + str(s))

        if key[pygame.K_q]: self.pos[1] += s; print("K_q is pressed"); print("dt = " + str(dt) + "s = " + str(s))
        if key[pygame.K_e]: self.pos[1] -= s; print("K_e is pressed"); print("dt = " + str(dt) + "s = " + str(s))

        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])

        if key[pygame.K_w]: self.pos[0] += x; self.pos[2] +=y
        if key[pygame.K_s]: self.pos[0] -= x; self.pos[2] -=y

        if key[pygame.K_a]: self.pos[0] -= y; self.pos[2] +=x
        if key[pygame.K_d]: self.pos[0] += y; self.pos[2] -=x


pygame.init()
w, h = 400, 400
cx, cy = w // 2, h // 2
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

verts = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
edges = (0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)

cam = Cam((0, 0, -5))

# pygame.event.get(); pygame.mouse.get_rel()
# pygame.mouse.set_visible(0); pygame.event.set_grab(1)
moveWithMouse = False

while True:

    dt = clock.tick() / 1000


    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE: pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moveWithMouse = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moveWithMouse = False

        if moveWithMouse == True: cam.events(event)

        # if event.type == pygame.KEYDOWN:
        #     key = pygame.key.get_pressed()
        #     cam.update(dt, key)
        #     print("x -= cam.pos[0]" + str(cam.pos[0]))
        #     print("y -= cam.pos[1]" + str(cam.pos[1]))
        #     print("z -= cam.pos[2]" + str(cam.pos[2]))
    screen.fill((255, 255, 255))

    for x, y, z in verts:
        x -= cam.pos[0]
        y -= cam.pos[1]
        z -= cam.pos[2]

        x, z = rotate2d((x, z), cam.rot[1])
        y, z = rotate2d((y, z), cam.rot[0])

        f = 200 / z
        x, y = x * f, y * f
        # points += [(cx + int(x), cy + int(y))]
        pygame.draw.circle(screen, (0, 0, 0), (cx + int(x), cy + int(y)), 6)

    for edge in edges:

        points = []
        for x, y, z in (verts[edge[0]], verts[edge[1]]):
            # z += 5

            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]

            x, z = rotate2d((x, z), cam.rot[1])
            y, z = rotate2d((y, z), cam.rot[0])

            f = 200 / z
            x, y = x * f, y * f
            points += [(cx + int(x), cy + int(y))]
        pygame.draw.line(screen, (0, 0, 0), points[0], points[1], 1)

    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt, key)


    # print("x -= cam.pos[0]" + str(cam.pos[0]))
    # print("y -= cam.pos[1]" + str(cam.pos[1]))
    # print("z -= cam.pos[2]" + str(cam.pos[2]))
