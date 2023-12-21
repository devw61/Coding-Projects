import pygame 
import math

pygame.init()
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255,255,255)
YELLOW_WHITE = (165,124,27)
YELLOW = (255,255,0)
BLUE = (0,0,255)
RED = (255,0, 5)
DARK_GREY = (105,105,105)
BLACK = (0,0,0)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    AU = (149.6e6 * 1000) # multiply to get meters
    G = 6.67428e-11
    SCALE = 230 / AU # smaller the numbe the closer everything is
    TIMESTEP = 86400 # SECONDS IN A DAY

    def __init__(self, x,y, radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.sun_dist = 0
        self.orbit = []

        self.x_velo = 0
        self.y_velo = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + WIDTH / 2
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + WIDTH / 2
                updated_points.append((x,y))
            pygame.draw.lines(win, self.color, False, updated_points, 2)   

        #render font
        pygame.draw.circle(win, self.color, (x,y), self.radius)
        if not self.sun:
            distance_text = FONT.render(f"{round(self.sun_dist/1000,1)}km",1,WHITE) 
            win.blit(distance_text, (x-distance_text.get_width()/2,y-(distance_text.get_height()/2)-20))
        

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.sun_dist = distance

        force = (self.G * self.mass * other.mass / distance**2) # universal grav equation
        theta = math.atan2(distance_y,distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_pos(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet) #force exerted by each planet
            total_fx += fx
            total_fy += fy

        self.x_velo += total_fx / self.mass * self.TIMESTEP #acceleration per day
        self.y_velo += total_fy / self.mass * self.TIMESTEP #acceleration per day

        self.x += self.x_velo * self.TIMESTEP
        self.y += self.y_velo * self.TIMESTEP
        self.orbit.append((self.x,self.y))



def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,30,YELLOW, 1.98892 * 10**30) # ** means exponent
    sun.sun = True

    earth = Planet(-1*Planet.AU,0,16,BLUE,5.9742 * 10**24)
    earth.y_velo = 29.783 * 1000 #times 1000 to convert to meters

    mars = Planet(-1.524 * Planet.AU, 0,12,RED, 6.39 * 10**23)
    mars.y_velo = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY,3.3*10**23)
    mercury.y_velo = -47.4 * 1000 

    venus = Planet(0.723 * Planet.AU, 0, 14, YELLOW_WHITE, 4.8685 * 10**24)
    venus.y_velo = -35.02 * 1000

    planets = [sun,earth,mars,mercury,venus]

    while run:
        clock.tick(60) #max fps
        win.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets :
            planet.update_pos(planets)
            planet.draw(win)

        pygame.display.update() #allows for white background
    pygame.quit()

main()