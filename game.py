import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCALING = 0.5


class SpaceShooter(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "basic game")
        self.players = None
        self.enemies = None
        #self.player_bullets = None
        #self.enemy_bullets = None
        self.player_sprite = None
        self.enemy_sprite = None
        #self.player_bullet_sprite = None
        #self.enemy_bullet_sprite = None
        self.score = 0
        self.player_dir = 0
        self.player_fire = False
        self.player_speed = 100
        self.set_mouse_visible(False)
        self.sprite_lists = []

        arcade.set_background_color((16, 16, 32))

    def on_draw(self):
        arcade.start_render()

        for sprite_list in self.sprite_lists:
            sprite_list.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dir += -1
        if symbol == arcade.key.RIGHT:
            self.player_dir += 1
        if symbol == arcade.key.SPACE:
            self.player_fire = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dir += 1
        if symbol == arcade.key.RIGHT:
            self.player_dir += -1

    def update(self, d_time):
        for enemy in self.enemies:
            enemy.center_y -= d_time * 10
            if enemy.center_y <= 0:
                enemy.remove_from_sprite_lists()
                self.score -= 5
        for player in self.players:
            player.center_x += self.player_dir * self.player_speed * d_time
        if self.player_fire:
            print("Pew!")
            self.player_fire = False

    def setup(self):
        self.score = 0
        self.players = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        #self.player_bullets = arcade.SpriteList()
        #self.enemy_bullets = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("player.png", SCALING)
        self.enemy_sprite = arcade.Sprite("enemy.png", SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = 25
        self.enemy_sprite.center_x = random.randrange(SCREEN_WIDTH)
        self.enemy_sprite.center_y = random.randrange(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
        #self.player_bullet_sprite = arcade.Sprite("player_bullet.png", SCALING)
        #self.enemy_bullet_sprite = arcade.Sprite("enemy_bullet.png", SCALING)
        self.players.append(self.player_sprite)
        self.enemies.append(self.enemy_sprite)
        self.sprite_lists = [
            self.players,
            self.enemies,
            #self.player_bullets,
            #self.enemy_bullets,
        ]


if __name__ == "__main__":
    window = SpaceShooter()
    window.setup()
    arcade.run()
