"""
Game made to test out how to parctice : Data manipulation,
Resize and Events.

Goal Features :

 - Resize (with black bars and stuff)
 - Collision events when leaving body

"""


import pyglet, random
from pyglet.gl import*
from pyglet import resource
import pyglet.clock as clock
from pyglet.math import Vec2
from pyglet.window import key

import src.font_data as fd
from src.fixed_resolution import FixedResolution #Aspect ratio

#Display
window  = pyglet.window.Window(500, 600, "Bouncy Square", resizable=True, vsync = True)
viewport= FixedResolution(window, 500, 600)
window.set_minimum_size(500, 600)

ASPECT_SIZE = 500,600

greetings = [
    '"Totally not a Flappy Bird clone"',
    "Can you beat my record? It's 9 billions.",
    "Having trouble? Just Git Gud."
]

def CreateSolidImage(width, height, color):
    return pyglet.image.SolidColorImagePattern(color).create_image(width, height)

class Player(pyglet.sprite.Sprite):
    def __init__(self, batch=None, **kwargs):
        self.sheet = resource.image('player_sheet.png')
        img = self.sheet.get_region(0,0,50,50)
        
        super(Player, self).__init__(img, batch=batch, **kwargs)
        
        
        
        self.image.anchor_x = self.width//2
        self.image.anchor_y = self.height//2
        
        self.x, self.y = window.width//2, window.height//2
        self.dy = 0
        
    def set_status(self, status=None):
        image = self.sheet.get_region(0,0,50,50)
        
        if status == "dead": image = self.sheet.get_region(100,0,50,50)
        if status == "chill": image = self.sheet.get_region(50,0,50,50)
        
        image.anchor_x = self.width//2
        image.anchor_y = self.height//2
        self.image = image
    
    def get_rect(self):
        Position    = Vec2(self.x-self.width/2, self.y-self.height/2)
        Size        = Vec2(self.width, self.height)
        return Position, Size
        
    def on_key_press(self, symbol, mod):
        if symbol == key.SPACE: 
            self.dy = 300
            JUMP_Player.queue(J_SFX)
            JUMP_Player.play()
        
    def update(self, dt):
        self.y += self.dy*dt
        
class Background:
    def __init__(self, img, batch=None, **kwargs):
        self.x   = 0
        self.y   = 0
        self.dx  = 0.03
        
        self.img = img
        
    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glMatrixMode(GL_TEXTURE)
        glPushMatrix()
        glTranslatef(self.x, self.y, 0)

        self.img.blit(0, 0, width=ASPECT_SIZE[0], height=ASPECT_SIZE[1])
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        
    def update(self, dt):
        self.x += self.dx*dt
        
class Pipe:
    def __init__(self, img, y, color=(255,255,255), batch=None):
        
        #Image adjustment
        self.top    = pyglet.sprite.Sprite(img, batch=batch)
        self.bottom = pyglet.sprite.Sprite(img, batch=batch)
        self.top.color = color
        self.bottom.color = color
        
        self.top.y      = ASPECT_SIZE[1]//2 + 40 + (y-ASPECT_SIZE[1]/2)
        self.bottom.y   = -self.bottom.height + ASPECT_SIZE[0]//2 - 40 + (y-ASPECT_SIZE[1]/2)
        
        self.top.x      = ASPECT_SIZE[0]
        self.bottom.x   = ASPECT_SIZE[0]
        
        #Physics
        self.dx         = -200
        self.counted    = False
    
    @property
    def x(self): return self.top.x
    
    @property
    def width(self): return self.top.width
    
    def get_rect(self):
        Position1    = Vec2(self.top.x, self.top.y)
        Size1        = Vec2(self.top.width, self.top.height)
        
        Position2    = Vec2(self.bottom.x, self.bottom.y)
        Size2        = Vec2(self.bottom.width, self.bottom.height)
        return Position1, Size1, Position2, Size2
        
    def update(self, dt):
        self.top.x += self.dx*dt
        self.bottom.x += self.dx*dt
        
def CheckCollision(rect1, rect2):
    P1, S1 = rect1[0], rect1[1]
    P2, S2 = rect2[0], rect2[1]
    
    if P1.x + S1.x > P2.x and P1.x < P2.x + S2.x:
        if P1.y + S1.y > P2.y and P1.y < P2.y + S2.y:
            return True
    return False
        
   
#---------------------------------------------------
#User Interface
#---------------------------------------------------

resource.path.append('res')

def FontFromImage(text, x=0, y=0, font_size=25, color=(255,255,255), opacity=255, anchor_x='center', batch=None):
    Characters  = []
    spacing     = 0
    
    text_width = 0
    for l in text:
        try:
            Image = fd.Outlined[l][0]
            width = Image.width
            height = Image.height
            
            
            #Resizing
            transform = 28/font_size
            Image.width /= transform
            Image.height /= transform
            
            #Drawing
            offset_x, offset_y = fd.Outlined[l][1], fd.Outlined[l][2]
            
            sprite = pyglet.sprite.Sprite(Image, x+spacing+offset_x/transform, y+offset_y/transform, batch=batch)
            text_width += sprite.width
            
            spacing += fd.Outlined[l][0].width
            
            
            sprite.opacity = opacity
            sprite.color = color
            
            #Reseting dimensions
            Image.width = width
            Image.height = height
            
            Characters.append(sprite)
            
            
        except: print(l+" is not in list")
    
    return Characters
    
def GetFontImageDimensions(FontImage):
    width, height = 0, 0
    
    for sprite in FontImage:
        width += sprite.width
        if height < sprite.height: height=sprite.height
    
    return width, height
       
class Overlay:
    def update(self, dt): pass
    def draw(self): pass
    def destroy(self): pass
    
class MainMenu(Overlay):
    def __init__(self):
        self._text = [
            FontFromImage('Bouncy Square', y=100, font_size=40, batch=OverlayBatch),
            FontFromImage("Onuelito's Edition", x=5, y=70, font_size=20, batch=OverlayBatch),
            FontFromImage("Press SPACE to start", x=150, y=10, font_size=15, opacity=125, batch=OverlayBatch),
            FontFromImage(random.choice(greetings), x=10, y=580, font_size=12, opacity=30, batch=OverlayBatch),
            FontFromImage(f'Highscore: {Highscore}', color=(153,217,234), x=350, y=160, font_size=16, batch=OverlayBatch),
            
            #FontFromImage('GAME OVER', x=100, y=400, font_size=40, color=(255,0,0), batch=OverlayBatch),
        ]
        
        width, height = GetFontImageDimensions(self._text[0])
        
class LoseOverlay(Overlay):
    def __init__(self):
        super(LoseOverlay, self).__init__()
        self._text = [
            FontFromImage('GAME OVER!', x=100, y=400, font_size=40, color=(255,0,0), batch=OverlayBatch),
        ]
        self.events = []
        self.info()
        
    def info(self):
        
        def add_text(dt, text, font_size=15, x=170, y=200):
            img = FontFromImage(text, x=x, y=y, font_size=font_size, batch=OverlayBatch)
            self._text.append(img)
            
            SCORE_Player.queue(S_SFX)
            SCORE_Player.play()
        
        clock.schedule_once(add_text, 2, text="Pres R to restart", y=200)
        self.events.append(add_text)
        
        def add_text2(dt, text, font_size=15, x=171, y=200):
            img = FontFromImage(text, x=x, y=y, font_size=font_size, batch=OverlayBatch)
            self._text.append(img)
            
            SCORE_Player.queue(S_SFX)
            SCORE_Player.play()
            
        clock.schedule_once(add_text2, 3, font_size=10, text="Press ESC for Main Menu", y=180)
        self.events.append(add_text2)
        
    def destroy(self):
        for event in self.events: clock.unschedule(event)
        self._text = []
    
        
        
class ScoreLabel:
    def __init__(self):
        self._text = f'Score: {0}'
        self._characters = FontFromImage(self._text, y=10, x=190, font_size=18)
        
    @property
    def text(self): return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        self._characters = FontFromImage(value, y=10, x=190, font_size=18)
        
    def draw(self):
        for CHAR in self._characters: CHAR.draw()
        
        
class Fader(Overlay):
    def __init__(self):
        super(Fader, self).__init__()
        self._transparency = 0
        self._image = CreateSolidImage(ASPECT_SIZE[0], ASPECT_SIZE[1], (0,0,0,self._transparency))
        
        def FI_PlaceHolder(): print("Faded in")
        def FO_PlaceHolder(): print("Faded out")
        
        self._FIEvents = []
        self._FOEvents = []
        
        self._fadeIn    = False
        self._fadeOut   = False
        self.Fading     = False
    
    @property
    def transparency(self): return self._transparency
    
    @transparency.setter
    def transparency(self, value):
        self._transparency = value
        self._image = CreateSolidImage(ASPECT_SIZE[0], ASPECT_SIZE[1], (0,0,0,value))
        
    def fade_in(self, events=[]):
        self._fadeIn = True
        self._FIEvents = events
        
    def fade_out(self, events=[]):
        self._fadeOut = True
        self._FOEvents = events
        
    def draw(self):
        self._image.blit(0,0)
        
    def update(self, dt):
        #Functions played after fade out
        if self._fadeIn and self.transparency != 255: 
            self.transparency = min(self.transparency+10, 255)
            
            if self.transparency == 255:
                self.Fading  = True
                for event in self._FIEvents:
                    function    = event[0]
                    event.pop(0)
                    
                    function(*event)
                self._fadeIn = False
                self.Fading = False
        
        #Functions called after fade out
        if self._fadeOut and self.transparency != 0:
            self.transparency = max(self.transparency-8, 0)
            self.Fading = True
            if self.transparency == 0:
                for event in self._FOEvents:
                    function    = event[0]
                    event.pop(0) 
                    
                    function(*event)
                self._fadeOut = False
                self.Fading = False
                
                
class Spawner:
    time, spawn_time = 0, 2
    _stop = False
    
    def reset(self):
        self.time = 0
        
    def stop(self):
        self._stop = True
        
    def resume(self):
        self._stop = False
    
    def spawn_pipe(self):
        global Highlighted
        y = random.randint(150, ASPECT_SIZE[1]-150)
        image = resource.image('pipe.png')

        if Score == Highscore and not Highlighted and Playing: image= resource.image('pipe_hs.png'); Highlighted=True
        
        Pipes.append(Pipe(image, y=y, batch=WorldBatch))
    
    def update(self, dt):
        if self._stop: return
        self.time += dt
        if self.time > self.spawn_time: self.spawn_pipe(); self.time = 0
        
    
def set_overlay(new_overlay):
    global Overlay
    if Overlay: Overlay.destroy()
    Overlay = new_overlay

fps_display     = pyglet.window.FPSDisplay(window)
#---------------------------------------------------
#Loading resources
#---------------------------------------------------

background  = Background(resource.image('bg.png', atlas=False))
player      = Player()
spawner     = Spawner()
fader = Fader()



#---------------------------------------------------
#Game state values
#---------------------------------------------------
Paused      = False
Playing     = False
GameOver    = False
FadeIn      = False


Overlay     = None
SpawnLoop   = None
Pipes       = []
Score       = 0
Highscore   = 0
Highlighted = False
score_label = ScoreLabel()

#---------------------------------------------------
#Sound
#---------------------------------------------------

L_SFX = resource.media('game_over.wav', streaming=False)
J_SFX = resource.media('jump.wav', streaming=False)
H_SFX = resource.media('hit.wav', streaming=False)
F_SFX = resource.media('fall.wav', streaming=False)
P_SFX = resource.media('points.flac', streaming=False)
S_SFX = resource.media('score.mp3', streaming=False)
HS_SFX = resource.media('highscore.wav', streaming=False)

HIT_Player = pyglet.media.Player(); HIT_Player.volume = .1
JUMP_Player = pyglet.media.Player(); JUMP_Player.volume = .1
SCORE_Player = pyglet.media.Player(); SCORE_Player.volume = .2
PTS_Player = pyglet.media.Player(); PTS_Player.volume = .2
HS_Player = pyglet.media.Player()

MenuThemes = [
    resource.media('res/MenuThemes/Bitstones.wav'),
    resource.media('res/MenuThemes/Twinkle Twinkle Beat Box Star.wav'),
]

MenuPlayer = pyglet.media.Player(); MenuPlayer.queue(MenuThemes[random.randint(0, len(MenuThemes)-1)])
MenuPlayer.volume = .2

#---------------------------------------------------
#Batches
#---------------------------------------------------
WorldBatch  = pyglet.graphics.Batch()
OverlayBatch= pyglet.graphics.Batch()

#---------------------------------------------------
#State fonctions
#---------------------------------------------------

def SpawnPipe(dt):
       y = random.randint(150, ASPECT_SIZE[1]-150)
       Pipes.append(Pipe(resource.image('pipe.png'), y=y, batch=WorldBatch))
       
def start_game():
    global Paused, SpawnLoop
    main_menu()
    
    MenuPlayer.play()
    
def main_menu():
    global SpawnLoop, Paused, Pipes
    global Playing, GameOver
    
    Playing = False
    GameOver = False
    Paused = False
    
    Pipes = []
    spawner.resume()
    
    #clock.unschedule(SpawnLoop)
    window.remove_handlers(player.on_key_press)
    
    
    set_overlay(MainMenu())
    SpawnLoop = SpawnPipe
    #clock.schedule_interval(SpawnLoop, 2)
    
def play():
    global Playing, Pipes, Score
    global GameOver, Paused, Highlighted
    
    Highlighted = False
    
    Pipes = []
    Score = 0
    player.set_status()
    score_label.text = f'Score: {Score}'
    
    spawner.reset()
    spawner.resume()
    MenuPlayer.pause()
    
    clock
    set_overlay(None)
    Playing = True
    
    player.y = ASPECT_SIZE[1]+30
    player.dy = -300
    
    
    window.push_handlers(player.on_key_press)
    
def restart():
    global GameOver, Paused, Score
    
    GameOver = False
    Paused = False
    
    window.remove_handlers(player.on_key_press)
    play()
    
def pause_game():
    global Paused
    
    Paused = True
    clock.unschedule(SpawnLoop)
    
def resume_game():
    global Paused
    
    Paused = False
    #clock.schedule_interval_soft(SpawnLoop, 2)
    
def game_over():
    global GameOver, Paused, Highscore

    if Score > Highscore: Highscore = Score
    GameOver = True
    spawner.stop()
    player.set_status('dead')
    window.remove_handlers(player.on_key_press)
    if player.y > 0: player.dy = 300
    if player.y < 0: F_SFX.play()
    
    

def on_key_press(symbol, mod):
    global Paused
    
    if symbol == key.F: Paused = not Paused
    
    if symbol == key.SPACE and not Playing and not fader.Fading:
        fader.fade_in(
        events = [
        [fader.fade_out],
        [play],
        ]
        )
        
    if symbol == key.ESCAPE and Playing and not fader.Fading:
        fader.fade_in(
            events = [
                [fader.fade_out],
                [main_menu]
        ])
        
    if symbol == key.R and Playing and not fader.Fading and GameOver:
        fader.fade_in(
            events = [
                [fader.fade_out],
                [restart]
        ])
        
    if symbol == key.ESCAPE and not Playing: pyglet.app.exit()
        
window.on_key_press = on_key_press #Removing default Escape 

@window.event
def on_draw():
    global Overlay
    window.clear()
    background.draw()
    pyglet.graphics.draw
    
    
    
    with viewport:
        WorldBatch.draw()
        
        #score_label.draw()
        if Playing: 
            player.draw()
            score_label.draw()
        if Overlay: OverlayBatch.draw()
        
        fader.draw()
        
    #fps_display.draw()
    
        
           
def update(dt):
    global Score, Playing, Overlay
    
    dt = max(min(dt, 1/60), 1/60) #When holding window
    
    if not Paused:
        background.update(dt)
        if Playing: 
            player.dy -= 10
            player.update(dt)
        PlayerRect = player.get_rect()
        spawner.update(dt)
        #Managing pipes
        if GameOver == False:
            for pipe in Pipes:
                if pipe.x + pipe.width < player.x - player.width//2 and not pipe.counted and Playing:
                    if Score == Highscore: HS_SFX.play()
                    
                    pipe.counted = True; Score += 1
                    score_label.text = f'Score: {Score}'
                    PTS_Player.queue(P_SFX); PTS_Player.play()
                    
                    
                    if Score == 10: player.set_status('chill')
            
                if pipe.x < -pipe.width: Pipes.remove(pipe)
                else: pipe.update(dt)
                
                TopRect = pipe.get_rect()[:2]
                BottomRect = pipe.get_rect()[2:]
                
                if CheckCollision(PlayerRect, TopRect) or CheckCollision(PlayerRect, BottomRect):
                    if Playing and not GameOver: game_over(); HIT_Player.queue(H_SFX); HIT_Player.play()
                    
        if player.y < -player.height and Playing and not GameOver: game_over()
    #print(dt)
    if GameOver and player.y < -100 and Overlay == None: 
        set_overlay(LoseOverlay())
        L_SFX.play()
            
    fader.update(dt)
            
    
Rectangle = pyglet.shapes.Rectangle(window.width//2, window.height//2, 100,100, color=(255,0,0))
Rectangle.anchor_x, Rectangle.anchor_y = 50, 50
   
##Begin game##
clock.schedule_interval(update, 1/144)

##Allowing transparency in images
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable( GL_BLEND )


window.set_icon(resource.image('icon.ico'))
start_game()
pyglet.app.run()