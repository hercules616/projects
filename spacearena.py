import turtle
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

scrn = turtle.Screen()
scrn.setup(SCREEN_WIDTH + 220, SCREEN_HEIGHT + 20)
scrn.title("Space Arena")
scrn.bgcolor("black")
scrn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.level = 1

    def start_level(self):
        sprites.clear()

        sprites.append(player)
        sprites.append(missile)

        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, 2)
            sprites.append(Enemy(x, y, "square", "red"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, 2)
            sprites.append(Powerup(x, y, "circle", "blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy

    def render_border(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(3)
        pen.penup()

        left = -self.width/2.0 - x_offset
        right = self.width/2.0 - x_offset
        top = self.height/2.0 - y_offset
        bottom = -self.height/2.0 - y_offset

        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

    def render_info(self, pen, score, active_enemies = 0):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(10, 32, None)
        pen.stamp()

        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)

        pen.penup()
        pen.color("white")
        character_pen.scale = 1.0
        character_pen.draw_string(pen, "SPACE ARENA", 400, 270)
        character_pen.draw_string(pen, "SCORE {}".format(score), 400, 240)
        character_pen.draw_string(pen, "ENEMIES {}".format(active_enemies), 400, 210)
        character_pen.draw_string(pen, "LIVES {}".format(player.lives), 400, 180)
        character_pen.draw_string(pen, "LEVEL {}".format(game.level), 400, 150)

class CharacterPen():
    def __init__(self, color = "white", scale = 1.0):
        self.color = color
        self.scale = scale
        
        self.characters = {}
        self.characters["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
        self.characters["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
        self.characters["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
        self.characters["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
        self.characters["7"] = ((-5, 10), (5, 10), (0, -10))
        self.characters["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
        self.characters["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
        self.characters["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
        self.characters["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
        self.characters["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
        self.characters["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
        self.characters["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
        self.characters["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
        self.characters["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
        self.characters["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
        self.characters["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
        self.characters["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
        self.characters["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
        self.characters["L"] = ((-5, 10), (-5, -10), (5, -10))
        self.characters["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
        self.characters["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
        self.characters["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
        self.characters["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
        self.characters["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
        self.characters["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
        self.characters["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
        self.characters["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
        self.characters["V"] = ((-5, 10), (0, -10), (5, 10)) 
        self.characters["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
        self.characters["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
        self.characters["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))   
        self.characters["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
        self.characters["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))
        self.characters["-"] = ((-3, 0), (3, 0))

    def draw_string(self, pen, str, x, y):
        pen.width(2)
        pen.color(self.color)

        x -= 15 * self.scale * ((len(str)-1) / 2)
        for character in str:
            self.draw_character(pen, character, x, y)
            x += 15 * self.scale

    def draw_character(self, pen, character, x, y):
        scale = self.scale
        character = character.upper()

        if character in self.characters:
            pen.penup()
            xy = self.characters[character][0]
            pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.pendown()
            for i in range(1, len(self.characters[character])):
                xy = self.characters[character][i]
                pen.goto(x + xy[0] * scale, y + xy[1] * scale)
            pen.penup()

character_pen = CharacterPen("red", 3.0)

class Sprite():
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.2
        self.health = 100
        self.maxhealth = 100
        self.width = 20
        self.height = 20
        self.state = "active"
        self.radar = 200

    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy

        self.dx = other.dx
        self.dy = other.dy

        other.dx = temp_dx
        other.dy = temp_dy

    def update(self):
        self.heading += self.da
        self.heading %= 360
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        self.x += self.dx
        self.y += self.dy

        self.border_check()

    def border_check(self):
        if self.x > game.width/2.0 - 10:
            self.x = game.width/2.0 - 10
            self.dx *= -1
        elif self.x < -game.width/2.0 + 10:
            self.x = -game.width/2.0 + 10
            self.dx *= -1
        elif self.y > game.height/2.0 - 10:
            self.y = game.height/2.0 - 10
            self.dy *= -1
        elif self.y < -game.height/2.0 + 10:
            self.y = -game.height/2.0 + 10
            self.dy *= -1
    
    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            self.render_health_meter(pen, x_offset, y_offset)

    def render_health_meter(self, pen, x_offset, y_offset):
        pen.goto(self.x - x_offset - 10, self.y - y_offset + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)

        if self.health/self.maxhealth < 0.3:
            pen.color("red")
        elif self.health/self.maxhealth < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20 * (self.health/self.maxhealth))

        if self.health != self.maxhealth:
            pen.color("grey")
            pen.fd(20 * ((self.maxhealth-self.health)/self.maxhealth))

        pen.penup()

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0

    def rotate_left(self):
        self.da = 5

    def rotate_right(self):
        self.da = -5
    
    def stop_rotation(self):
        self.da = 0

    def accelerate(self):
        self.thrust += self.acceleration

    def decelerate(self):
        self.thrust = 0.0

    def reverse(self):
        self.thrust -= self.acceleration

    def fire(self):
        missile.fire(self.x, self.y, self.heading, self.dx, self.dy)

    def update(self):
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            self.x += self.dx
            self.y += self.dy
            self.border_check()

        if self.health <= 0:
            self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.maxhealth
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.5, 1.0, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            pen.shapesize(1.0, 1.0, None)

            self.render_health_meter(pen, x_offset, y_offset)

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 4.0
        self.maxfuel = 200
        self.fuel = self.maxfuel
        self.height = 4
        self.width = 4

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()
            self.heading += self.da
            self.heading %= 360
            self.x += self.dx
            self.y += self.dy

            self.border_check()

    def reset(self):
        self.fuel = self.maxfuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            pen.shapesize(1.0, 1.0, None)

class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.maxhealth = 20
        self.health = self.maxhealth

    def update(self):
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            self.x += self.dx
            self.y += self.dy

            self.border_check()

        if self.health <= 0:
            self.reset()

    def reset(self):
        self.state = "inactive"

class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

class Camera():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, pen, sprites):
        pen.color("white")
        pen.setheading(90)
        pen.goto(self.x + self.width / 2.0, self.y)
        pen.pendown()
        pen.circle(self.width / 2.0)
        pen.penup()

        for sprite in sprites:
            if sprite.state == "active":
                radar_x = self.x + (sprite.x - player.x) * (self.width / game.width)
                radar_y = self.y + (sprite.y - player.y) * (self.height / game.height)
                pen.goto(radar_x, radar_y)
                pen.color(sprite.color)
                pen.shape(sprite.shape)
                pen.setheading(sprite.heading)
                pen.shapesize(0.2, 0.2, None)
                distance = ((player.x - sprite.x)**2 + (player.y - sprite.y)**2)**0.5
                if distance < player.radar:
                    pen.stamp()

def quit():
    global running
    running = False

game = Game(700, 500)

radar = Radar(400, -200, 200, 200)

player = Player(0, 0, "triangle", "white")
camera = Camera(player.x, player.y)
missile = Missile(0, 100, "classic", "yellow")
powerup = Powerup(0, -100, "circle", "blue")
powerup.dy = 1
powerup.dx = 0.1
powerup2 = Powerup(-100, 100, "circle", "blue")
powerup2.dy = -1
powerup2.dx = -0.1

sprites = []

game.start_level()

scrn.listen()
scrn.onkeypress(player.rotate_left, "Left")
scrn.onkeypress(player.rotate_right, "Right")
scrn.onkeypress(player.accelerate, "Up")
scrn.onkeyrelease(player.decelerate, "Up")
scrn.onkeyrelease(player.stop_rotation, "Left")
scrn.onkeyrelease(player.stop_rotation, "Right")
scrn.onkeypress(player.reverse, "Down")
scrn.onkeyrelease(player.decelerate, "Down")
scrn.onkeypress(player.fire, "space")
scrn.onkeypress(quit, "q")

running = True

while running:
    pen.clear()

    for sprite in sprites:
        sprite.update()

    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state == "active":
            if player.is_collision(sprite):
                sprite.health -= 10
                player.health -= 10
                player.bounce(sprite)

            if missile.state == "active" and missile.is_collision(sprite):
                sprite.health -= 10
                missile.reset()

        if isinstance(sprite, Powerup):
            if player.is_collision(sprite):
                sprite.x = 100
                sprite.y = 100

            if missile.state == "active" and missile.is_collision(sprite):
                sprite.x = 100
                sprite.y = -100
                player.health -= 10
                missile.reset()

    for sprite in sprites:    
        sprite.render(pen, camera.x + 100, camera.y)

    game.render_border(pen, camera.x + 100, camera.y)

    end_of_level = True
    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state == "active":
            end_of_level = False
    if end_of_level:
        game.level += 1
        game.start_level()

    camera.update(player.x, player.y)

    game.render_info(pen, 0, 0)

    radar.render(pen, sprites)

    scrn.update()
scrn.bye()