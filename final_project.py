import pygame, sys, os, random, math
from pygame.locals import *

# sounds
pygame.mixer.init()
pygame.init()              

# init pygame 
pygame.init()                      
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 800
HEIGHT = 600      
time = 0

# Function to load resources
def load_resource(filename, folder):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resource_path = os.path.join(script_dir, folder, filename)
    return pygame.image.load(resource_path) if filename.endswith(('.png', '.jpg')) else pygame.mixer.Sound(resource_path)

# Canvas declaration
WIDTH, HEIGHT = 1066, 700
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Asteroids')

# Load images
bg = load_resource('bg.jpg', 'images')
debris = load_resource('debris2_brown.png', 'images')
ship = load_resource('ship.png', 'images')
shipWidth, shipHeight = ship.get_width()-1, ship.get_height()-1
ship_thrusted = load_resource('ship_thrusted.png', 'images')
asteroid = load_resource('asteroid.png', 'images')
shot = load_resource('shot2.png', 'images')
shotWidth, shotHeight = shot.get_width(), shot.get_height()
explosion = load_resource('explosion_blue.png', 'images')

# Load sounds
missile_sound = load_resource('missile.ogg', 'sounds')
missile_sound.set_volume(1)

thruster_sound = load_resource('thrust.ogg', 'sounds')
thruster_sound.set_volume(1)

explosion_sound = load_resource('explosion.ogg', 'sounds')
explosion_sound.set_volume(1)

# Background score
def load_resource(filename, folder):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resource_path = os.path.join(script_dir, folder, filename)
    return resource_path

pygame.mixer.music.load(load_resource('game.ogg', 'sounds'))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# set variables
ship_x = WIDTH/2 - 50
ship_y = HEIGHT/2 - 50
ship_angle = 0
ship_is_rotating = False
ship_is_forward = False
ship_is_back = False
ship_direction = 0
ship_speed = 0

asteroid_x = [0,0,0,0,0] #random.randint(0,WIDTH)
asteroid_y = [0,0,0,0,0] #random.randint(0,HEIGHT)
asteroid_angle = []
asteroid_speed = 2
no_asteroids = 8

bullet_x = []
bullet_y = []
bullet_angle = []
no_bullets = 0

score = 0
game_over = False

for i in range(0,no_asteroids):
    asteroid_x.append( random.randint(0,WIDTH) )
    asteroid_y.append( random.randint(0,HEIGHT) )
    asteroid_angle.append( random.randint(0,365) )

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# draw game function
def draw(canvas):
    global time
    global ship_is_forward
    global bullet_x, bullet_y
    global score
    canvas.fill(BLACK)
    canvas.blit(bg,(0,0))
    canvas.blit(debris,(time*.3,0))
    canvas.blit(debris,(time*.3-WIDTH,0))
    time = time + 1

    for i in range(0,no_bullets):
        canvas.blit(shot, (bullet_x[i],bullet_y[i]) )

    for i in range(0,no_asteroids):
        canvas.blit( rot_center(asteroid,time) ,(asteroid_x[i],asteroid_y[i]))

    if ship_is_forward:
        canvas.blit( rot_center(ship_thrusted,ship_angle) , (ship_x, ship_y))
    else:
        canvas.blit( rot_center(ship,ship_angle) , (ship_x, ship_y))

    #draw Score
    myfont1 = pygame.font.SysFont("Comic Sans MS", 40)
    label1 = myfont1.render("Score : "+str(score), 1, (255,255,0))
    canvas.blit(label1, (50,20))
    label = myfont1.render("Done by A.Srayeldine", 1, (255,255,0))
    canvas.blit(label, (20,620))

    if game_over:
        myfont2 = pygame.font.SysFont("Comic Sans MS", 80)
        myfont3 = pygame.font.SysFont("Comic Sans MS", 40)
        label2 = myfont2.render("GAME OVER ", 1, (255,255,255))
        label3 = myfont3.render("Click space bar to try again ", 1, (255,255,255))
        canvas.blit(label2, (WIDTH/2 -230,HEIGHT/2 - 100))
        canvas.blit(label3, (WIDTH/2 -250,HEIGHT/2 -10 ))

# handle input function
def handle_input():
    global ship_angle, ship_is_rotating, ship_direction
    global ship_x, ship_y, ship_speed, ship_is_forward, ship_is_back
    global bullet_x, bullet_y, bullet_angle, no_bullets
    global thruster_sound, missile_sound

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ship_is_rotating = True
                ship_direction = 0
            elif event.key == K_LEFT:
                ship_is_rotating = True
                ship_direction = 1
            elif event.key == K_UP:
                ship_is_forward = True
                ship_speed = 8
                thruster_sound.play()
            elif event.key == K_DOWN:  # New: Handle backward movement
                ship_is_back = True
                ship_speed = -8  # Adjust the backward speed
                thruster_sound.play()
            elif event.key == K_SPACE:
                bullet_x.append(ship_x + 50)
                bullet_y.append(ship_y + 50)
                bullet_angle.append(ship_angle)
                no_bullets = no_bullets + 1
                missile_sound.play()

        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                ship_is_rotating = False
            else:
                ship_is_forward = False
                ship_is_back = False
                thruster_sound.stop()

    if ship_is_rotating:
        if ship_direction == 0:
            ship_angle = ship_angle - 10
        else:
            ship_angle = ship_angle + 10

    if ship_is_forward or ship_speed > 0:
        ship_x = (ship_x + math.cos(math.radians(ship_angle))*ship_speed )
        ship_y = (ship_y + -math.sin(math.radians(ship_angle))*ship_speed )
        if ship_is_forward == False:
            ship_speed = ship_speed - 0.2
    if ship_is_back or ship_speed < 0:
        ship_x = (ship_x + math.cos(math.radians(ship_angle))*ship_speed )
        ship_y = (ship_y + -math.sin(math.radians(ship_angle))*ship_speed )
        if ship_is_back == False:
            ship_speed = ship_speed + 0.2

# update the screen
def update_screen():
    pygame.display.update()
    fps.tick(60)

def isCollision(shipX, shipY, shipRadius, asteroidX, asteroidY, asteroidRadius):
    distance = math.sqrt((shipX - asteroidX)**2 + (shipY - asteroidY)**2)
    return distance < (shipRadius + asteroidRadius)


def game_logic():
    global bullet_x, bullet_y, bullet_angle, no_bullets
    global asteroid_x, asteroid_y
    global score, game_over

    ship_radius = max(shipWidth, shipHeight) / 2

    for i in range(0, no_bullets):
        bullet_x[i] = (bullet_x[i] + math.cos(math.radians(bullet_angle[i])) * 10)
        bullet_y[i] = (bullet_y[i] + -math.sin(math.radians(bullet_angle[i])) * 10)

    for i in range(0, no_asteroids):
        asteroid_x[i] = (asteroid_x[i] + math.cos(math.radians(asteroid_angle[i])) * asteroid_speed)
        asteroid_y[i] = (asteroid_y[i] + -math.sin(math.radians(asteroid_angle[i])) * asteroid_speed)

        if asteroid_y[i] < 0:
            asteroid_y[i] = HEIGHT

        if asteroid_y[i] > HEIGHT:
            asteroid_y[i] = 0

        if asteroid_x[i] < 0:
            asteroid_x[i] = WIDTH

        if asteroid_x[i] > WIDTH:
            asteroid_x[i] = 0

        if isCollision(ship_x + shipWidth / 2, ship_y + shipHeight / 2, ship_radius-20,
                       asteroid_x[i] + asteroid.get_width() / 2, asteroid_y[i] + asteroid.get_height() / 2,
                       asteroid.get_width() / 2 -20):
            game_over = True
            pygame.mixer.music.stop()
            pygame.mixer.music.load(load_resource('game_over.mp3', 'sounds'))
            pygame.mixer.music.play()

    for i in range(0, no_bullets):
        for j in range(0, no_asteroids):
            asteroid_radius = max(asteroid.get_width(), asteroid.get_height()) / 2
            if isCollision(bullet_x[i] + shotWidth / 2, bullet_y[i] + shotHeight / 2, shotWidth / 2,
                           asteroid_x[j] + asteroid.get_width() / 2, asteroid_y[j] + asteroid.get_height() / 2,
                           asteroid_radius):
                asteroid_x[j] = random.randint(0, WIDTH)
                asteroid_y[j] = random.randint(0, HEIGHT)
                asteroid_angle[j] = random.randint(0, 365)
                explosion_sound.play()
                score = score + 1

def reset_game():
    global ship_x, ship_y, ship_angle, ship_is_rotating, ship_is_forward, ship_direction, ship_speed, ship_is_back
    global bullet_x, bullet_y, bullet_angle, no_bullets
    global asteroid_x, asteroid_y, asteroid_angle
    global score, game_over
    pygame.mixer.music.stop()
    pygame.mixer.music.load(load_resource('game.ogg', 'sounds'))
    pygame.mixer.music.play()
    ship_x = WIDTH / 2 - 50
    ship_y = HEIGHT / 2 - 50
    ship_angle = 0
    ship_is_rotating = False
    ship_is_forward = False
    ship_is_back = False
    ship_direction = 0
    ship_speed = 0

    asteroid_x = [random.randint(0, WIDTH) for _ in range(no_asteroids)]
    asteroid_y = [random.randint(0, HEIGHT) for _ in range(no_asteroids)]
    asteroid_angle = [random.randint(0, 365) for _ in range(no_asteroids)]

    bullet_x = []
    bullet_y = []
    bullet_angle = []
    no_bullets = 0

    score = 0
    game_over = False
# asteroids game loop
while True:
    draw(window)
    handle_input()
    
    if game_over:
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            reset_game()
    else:
        game_logic()
    
    update_screen()
