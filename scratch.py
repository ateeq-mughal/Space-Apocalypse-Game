import pyglet

from pyglet.window import key

from gameobj import GameObject


class GameWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.player = GameObject(600, 100, "ship_forward.png")

        self.static_bg = GameObject(0, 0, "static_bg.jpg")

        self.first_bg0 = GameObject(0, 0, "bg0.png")
        self.first_bg0.vely = -100

        self.second_bg0 = GameObject(0, 1080, "bg0.png")
        self.second_bg0.vely = -100

        self.first_bg = GameObject(0, 0, "bg2.png")
        self.first_bg.vely = -50

        self.second_bg = GameObject(0, 1080, "bg2.png")
        self.second_bg.vely = -50

        self.first_bg1 = GameObject(0, 0, "bg3.png")
        self.first_bg1.vely = -30

        self.second_bg1 = GameObject(0, 1080, "bg3.png")
        self.second_bg1.vely = -30

        self.beam_list = []

        self.enemy_list = []
        self.enemy_list2 = []

        self.enemy_fire_list = []
        self.enemy_fire_list2 = []

        self.player_hit_count = 0

        self.high_score = 0
        self.score = 0
        self.enemy_destroyed = 0

        self.score1 = str(self.score)

        with open("high_score.txt", 'r') as file:
            for line in file:
                self.high_score = int(line)
                print(self.high_score)

        self.head_high_score = pyglet.text.Label("High Score", x=1150, y=700)
        self.head_high_score.italic = True
        self.head_high_score.bold = True
        self.head_high_score.font_size = 25

        self.label_high_score = pyglet.text.Label(str(self.high_score), x=1200, y=650)
        self.label_high_score.italic = True
        self.label_high_score.bold = True
        self.label_high_score.font_size = 35

        self.head_score = pyglet.text.Label("Your Score", x=1150, y=500)
        self.head_score.italic = True
        self.head_score.bold = True
        self.head_score.font_size = 25

        self.label_score = pyglet.text.Label(str(self.score), x=1200, y=450)
        self.label_score.italic = True
        self.label_score.bold = True
        self.label_score.font_size = 35

        self.head_enemy_destroyed = pyglet.text.Label("Enemy Destroyed", x=1050, y=300)
        self.head_enemy_destroyed.italic = True
        self.head_enemy_destroyed.bold = True
        self.head_enemy_destroyed.font_size = 25

        self.label_enemy_destroyed = pyglet.text.Label(str(self.enemy_destroyed), x=1200, y=250)
        self.label_enemy_destroyed.italic = True
        self.label_enemy_destroyed.bold = True
        self.label_enemy_destroyed.font_size = 35

    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.player = GameObject(self.player.sprite.x, self.player.sprite.y, "ship_right.png")
            self.player.velx = 200

        if symbol == key.LEFT:
            self.player = GameObject(self.player.sprite.x, self.player.sprite.y, "ship_left.png")
            self.player.velx = -200

        if symbol == key.UP:
            self.player.vely = 100

        if symbol == key.DOWN:
            self.player.vely = -100

        if symbol == key.SPACE:
            sound = pyglet.resource.media('res/fire.wav', streaming=False)
            sound.play()
            self.beam_list.append(GameObject(self.player.sprite.x - 1, self.player.sprite.y + 50, "beam.png"))

        if symbol == key.ESCAPE:
            pyglet.app.exit()

        if symbol == key.SPACE:
            self.beam_list.append(GameObject(self.player.sprite.x + 5, self.player.sprite.y + 50, "beam.png"))

        if symbol == key.ESCAPE:
            self.close()

        if symbol == key.R:
            self.reload()
            self.close()

    def update_beam(self, dt):
        for laser in self.beam_list:
            laser.update(dt)
            laser.vely += 400

    def spawn_enemy(self, dt):
        self.enemy_list.append(GameObject(0, 700, "enemy.png"))

    def spawn_enemy2(self, dt):
        self.enemy_list2.append(GameObject(1300, 700, "enemy2.png"))

    def update_enemy(self, dt):

        for enemy in self.enemy_list:

            enemy.update(dt)

            if enemy.sprite.x >= 1300:
                enemy.sprite.x = 1300
                enemy.velx = -300
            if enemy.sprite.x <= 0:
                enemy.sprite.x = 0
                enemy.velx = 300

            enemy.vely = -10

    def update_enemy2(self, dt):

        for enemy2 in self.enemy_list2:

            enemy2.update(dt)

            if enemy2.sprite.x >= 1300:
                enemy2.sprite.x = 1300
                enemy2.velx = -300
            if enemy2.sprite.x <= 0:
                enemy2.sprite.x = 0
                enemy2.velx = 300

            enemy2.vely = -30

    def enemy_fire(self, dt):

        for enemy in self.enemy_list:
            self.enemy_fire_list.append(GameObject(enemy.sprite.x, enemy.sprite.y, "enemy_beam.png"))
            sound = pyglet.resource.media('res/enemy_fire.wav', streaming=False)
            sound.play()

    def enemy_fire2(self, dt):

        for enemy2 in self.enemy_list2:
            self.enemy_fire_list2.append(GameObject(enemy2.sprite.x, enemy2.sprite.y, "enemy_beam2.png"))
            sound = pyglet.resource.media('res/enemy_fire2.wav', streaming=False)
            sound.play()

    def enemy_hit(self, dt):
        if len(self.enemy_list) != 0:
            for enemy in self.enemy_list:
                for beam in self.beam_list:

                    if beam.sprite.x < enemy.sprite.x + enemy.sprite.width and beam.sprite.x + beam.sprite.width > enemy.sprite.x and \
                            beam.sprite.y < enemy.sprite.y + enemy.sprite.height and beam.sprite.height + beam.sprite.y > enemy.sprite.y:
                        sound = pyglet.resource.media('res/enemy_explode.wav', streaming=False)
                        sound.play()
                        self.beam_list.remove(beam)
                        self.enemy_list.remove(enemy)
                        self.score += 5
                        self.enemy_destroyed += 1
                        print(self.score)
                        print(self.enemy_destroyed)
                        self.label_high_score.text = str(self.high_score)
                        self.label_score.text = str(self.score)
                        self.label_enemy_destroyed.text = str(self.enemy_destroyed)

    def enemy_hit2(self, dt):
        if len(self.enemy_list2) != 0:
            for enemy2 in self.enemy_list2:
                for beam in self.beam_list:
                    if beam.sprite.x < enemy2.sprite.x + enemy2.sprite.width and beam.sprite.x + beam.sprite.width > enemy2.sprite.x and \
                            beam.sprite.y < enemy2.sprite.y + enemy2.sprite.height and beam.sprite.height + beam.sprite.y > enemy2.sprite.y:
                        sound = pyglet.resource.media('res/enemy_explode.wav', streaming=False)
                        sound.play()
                        self.beam_list.remove(beam)
                        self.enemy_list2.remove(enemy2)
                        self.score += 10
                        self.enemy_destroyed += 1
                        print(self.score)
                        print(self.enemy_destroyed)
                        self.label_high_score.text = str(self.high_score)
                        self.label_score.text = str(self.score)
                        self.label_enemy_destroyed.text = str(self.enemy_destroyed)

                    elif beam.sprite.y > 1200:
                        self.beam_list.remove(beam)

    def player_hit(self, dt):
        if self.player_hit_count <= 2:

            for fire in self.enemy_fire_list:

                if fire.sprite.x < self.player.sprite.x + self.player.sprite.width and fire.sprite.x + fire.sprite.width > self.player.sprite.x and \
                        fire.sprite.y < self.player.sprite.y + self.player.sprite.height and fire.sprite.height + fire.sprite.y > self.player.sprite.y:
                    self.enemy_fire_list.remove(fire)
                    sound = pyglet.resource.media('res/explosion.wav', streaming=False)
                    sound.play()
                    self.player = GameObject(self.player.sprite.x, self.player.sprite.y, "ship_hit.png")
                    self.player_hit_count += 1
        else:
            self.player = GameObject(350, 150, 'game_over.png')
            with open("high_score.txt", 'r+') as file:
                for line in file:
                    if self.score > int(line):
                        line = ""
                        file.write(str(self.score))

                        print("written")
                    print('not written')

    def player_hit2(self, dt):
        if self.player_hit_count <= 2:

            for fire2 in self.enemy_fire_list2:

                if fire2.sprite.x < self.player.sprite.x + self.player.sprite.width and fire2.sprite.x + fire2.sprite.width > self.player.sprite.x and \
                        fire2.sprite.y < self.player.sprite.y + self.player.sprite.height and fire2.sprite.height + fire2.sprite.y > self.player.sprite.y:
                    self.enemy_fire_list2.remove(fire2)
                    sound = pyglet.resource.media('res/explosion.wav', streaming=False)
                    sound.play()

                    self.player = GameObject(self.player.sprite.x, self.player.sprite.y, "ship_hit.png")
                    self.player_hit_count += 5

        else:

            self.player = GameObject(350, 150, 'game_over.png')
            with open("high_score.txt", 'r+') as file:
                for line in file:
                    if self.score > int(line):
                        line = ""
                        file.write(str(self.score))

                        print("written")
                    print('not written')

    def update_enemy_fire(self, dt):
        for fire in self.enemy_fire_list:
            fire.update(dt)
            fire.vely = -500

    def update_enemy_fire2(self, dt):
        for fire2 in self.enemy_fire_list2:
            fire2.update(dt)
            fire2.vely = -500

    def on_key_release(self, symbol, modifiers):
        if symbol in (key.RIGHT, key.LEFT):
            self.player = GameObject(self.player.sprite.x, self.player.sprite.y, "ship_forward.png")
            self.player.velx = 0

        if symbol in (key.UP, key.DOWN):
            self.player.vely = 0

    def on_draw(self):
        self.clear()
        self.static_bg.draw()

        self.first_bg0.draw()
        if self.first_bg0.sprite.y <= 1080:
            self.first_bg0 = GameObject(0, 1080 * 2, "bg0.png")
            self.first_bg0.vely = -100

        self.second_bg0.draw()
        if self.second_bg0.sprite.y <= -1080 * 2:
            self.second_bg0 = GameObject(0, 1080 * 2, "bg0.png")
            self.second_bg0.vely = -100

        self.first_bg.draw()
        if self.first_bg.sprite.y <= -1080:
            self.first_bg = GameObject(0, 1080, "bg2.png")
            self.first_bg.vely = -50

        self.second_bg.draw()
        if self.second_bg.sprite.y <= -1080 * 2:
            self.second_bg = GameObject(0, 1080, "bg2.png")
            self.second_bg.vely = -50

        self.first_bg1.draw()
        if self.first_bg1.sprite.y <= -1080:
            self.first_bg1 = GameObject(0, 1080, "bg3.png")
            self.first_bg1.vely = -30

        self.second_bg1.draw()
        if self.second_bg1.sprite.y <= -1080 * 2:
            self.second_bg1 = GameObject(0, 1080, "bg3.png")
            self.second_bg1.vely = -30

        for beam in self.beam_list:
            beam.draw()

        for enemy in self.enemy_list:
            enemy.draw()

        for fire in self.enemy_fire_list:
            fire.draw()

        for beam in self.beam_list:
            beam.draw()

        for enemy in self.enemy_list:
            enemy.draw()

        for fire in self.enemy_fire_list:
            fire.draw()

        for enemy2 in self.enemy_list2:
            enemy2.draw()

        for fire2 in self.enemy_fire_list2:
            fire2.draw()

        self.player.draw()
        self.head_high_score.draw()
        self.label_high_score.draw()
        self.head_score.draw()
        self.label_score.draw()
        self.head_enemy_destroyed.draw()
        self.label_enemy_destroyed.draw()

    def update(self, dt):

        self.static_bg.update(dt)

        self.player.update(dt)

        self.first_bg0.update(dt)
        self.first_bg.update(dt)
        self.first_bg1.update(dt)
        self.second_bg0.update(dt)
        self.second_bg.update(dt)
        self.second_bg1.update(dt)

        self.update_beam(dt)

        self.update_enemy_fire(dt)
        self.update_enemy(dt)
        self.enemy_hit(dt)
        self.player_hit(dt)
        self.update_enemy_fire2(dt)
        self.update_enemy2(dt)
        self.enemy_hit2(dt)
        self.player_hit2(dt)


# if __name__ == '__main__':
window = GameWindow(1100, 500, "Space Apocalypse", resizable=True)
window.set_fullscreen()
icon = pyglet.image.load("res/icon.png")
window.set_icon(icon)
sound = pyglet.resource.media('res/bg_music.wav', streaming=False)
sound.play()
# winsound.PlaySound("res/bg_music.wav", winsound.SND_ASYNC)
pyglet.clock.schedule_interval(window.update, 1 / 120.0)
pyglet.clock.schedule_interval(window.spawn_enemy, 1.5)
pyglet.clock.schedule_interval(window.enemy_fire, 3)
pyglet.clock.schedule_interval(window.spawn_enemy2, 5)
pyglet.clock.schedule_interval(window.enemy_fire2, 5)

pyglet.app.run()
