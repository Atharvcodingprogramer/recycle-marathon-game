import pgzrun
WIDTH = 1000
HEIGHT = 700
TITLE = "recycle marathon game"
import random
level = 1
endlevel = 5
animations  = []
images = ["batteryimg","chipsimg","bottleimg","bagimg"]
actors = []
def createactors() :
    actorimages = ["paperimg"]
    for i in range(level) :
        image = random.choice(images)
        actorimages.append(image)
    for image in actorimages :
        actor = Actor(image)
        actors.append(actor)
    numberofgap = level + 2 
    gapsize = WIDTH // numberofgap
    actornumber = 1
    random.shuffle(actors)
    for actor in actors :
        actor.pos = actornumber * gapsize,0
        actornumber = actornumber + 1
        animation = animate(actor,duration = 5, y = 700, on_finished = end)
        animations.append(animation)

def end() :
    screen.draw.text("game over",(400,450))


def draw() :
    screen.blit("bground",(0,0))
    for actor in actors :
        actor.draw()

createactors()



def update() :
    pass
pgzrun.go()