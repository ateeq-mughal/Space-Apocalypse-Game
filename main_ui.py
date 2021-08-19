import pyglet

from pyglet.window import key

animation = pyglet.image.load_animation('res/ui_bg2.gif')
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width
h = animSprite.height

screen = pyglet.window.Window(w, h, "Space Apocalypse", resizable=True)

icon = pyglet.image.load("res/icon.png")
screen.set_icon(icon)

head = pyglet.image.load("res/ui_head.png")
head_sprite = pyglet.sprite.Sprite(head, x=150, y=500)

start = pyglet.text.Label("Press 'Space' to Start.", x=10, y=420)
# start.color(255,69,0)
start.italic = True
start.bold = True
start.font_size = 35

inst = pyglet.text.Label("INSTRUCTIONS:", x=10, y=350)
inst.italic = True
inst.bold = True
inst.font_size = 35

inst1 = pyglet.text.Label("Press arrow keys to move the spaceship in corresponding directions.\nPress Space to", x=20,
                          y=290)
inst1.italic = True
inst1.bold = True
inst1.font_size = 17

inst2 = pyglet.text.Label("fire. Green enemy scores 5 while black enemy scores 10.\nAvoid enemy fire by moving ", x=20,
                          y=260)
inst2.italic = True
inst2.bold = True
inst2.font_size = 17

inst3 = pyglet.text.Label("spaceship, else you'll be destroyed. Green enemy gives you small damage while black", x=20,
                          y=230)
inst3.italic = True
inst3.bold = True
inst3.font_size = 17

inst4 = pyglet.text.Label("enemy kills you at once.", x=20, y=200)
inst4.italic = True
inst4.bold = True
inst4.font_size = 17

exits = pyglet.text.Label("Press 'Esc' to Exit.", x=10, y=50)
exits.italic = True
exits.bold = True
exits.font_size = 35


@screen.event
def on_key_press(symbol, modifiers):
    if symbol is key.ESCAPE:
        pyglet.app.exit()

    if symbol is key.SPACE:
        import scratch


@screen.event
def on_draw():
    screen.clear()
    animSprite.draw()
    head_sprite.draw()
    start.draw()
    inst.draw()
    inst1.draw()
    inst2.draw()
    inst3.draw()
    inst4.draw()

    exits.draw()


pyglet.app.run()
