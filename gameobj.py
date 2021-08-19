import pyglet

class GameObject:
    def __init__(self, posx, posy, image=None):
        self.posx=posx
        self.posy=posy
        self.velx=0
        self.vely=0
        if image is not None:
            self.img = pyglet.image.load("res/"+image)
            self.sprite = pyglet.sprite.Sprite(self.img, x=self.posx, y=self.posy)
            self.width= self.sprite.width
            self.height= self.sprite.height


    def draw(self):
        self.sprite.draw()

    def update(self,dt):
        self.sprite.x += self.velx*dt
        self.sprite.y += self.vely*dt
