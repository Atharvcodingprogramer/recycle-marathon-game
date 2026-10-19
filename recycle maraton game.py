import pgzrun
WIDTH = 1000
HEIGHT = 700
TITLE = "recycle marathon game"
import random

level = 1
endlevel = 5
gameover = False
gamecomplete = False
animations  = []
images = ["batteryimg","chipsimg","bottleimg","bagimg"]
actors = []
def stopanimations() :
    global animations
    for animation in animations :
        if animation.running :
            animation.stop()


def createactors() :
    global actors
    actorimages = ["paperimg"]
    actors = []
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
        animation = animate(actor,duration = 5, y = 700, on_finished = endgame)
        animations.append(animation)

def endgame() :
    global gameover
    gameover = True



def draw() :
    screen.blit("bground",(0,0))
    if gameover == True :
        screen.draw.text("Game over" , (400,400),color = "blue")
    elif gamecomplete == True :
        screen.draw.text("Game completed Good job", (400,400),color = "blue")
    else :
        screen.draw.text(f"level {level}", (10,10))
        for actor in actors :
            actor.draw()

createactors()

def on_mouse_down(pos) :
    global level

    global gameover
    global gamecomplete
    for actor in actors :
        if actor.collidepoint(pos) :
            if actor.image == "paperimg" :
                level = level + 1 
                stopanimations()
                if level > endlevel :
                    gamecomplete = True
                else :
                    createactors()
                    
            else :
                gameover = True




def update() :
    pass
pgzrun.go()