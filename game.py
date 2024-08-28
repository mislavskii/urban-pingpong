import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Ping Pong Game'


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('resources/red_bar.png', .1)

    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('resources/orange_ball.png', .1)
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x *= -1
        if self.top >= SCREEN_HEIGHT or self.top <= 0:
            self.change_y *= -1


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 10
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((233, 255, 233))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta_time: float):
        # if arcade.check_for_collision(self.ball, self.bar) and self.ball.change_y < 0:
        #     self.ball.change_y *= -1
        if self.ball_intercepted():
            self.ball.change_y *= -1
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key: int, modifiers: int):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.bar.change_x = 0

    def ball_intercepted(self):
        width_factor = 3
        left_shift = 22
        top_shift = 10
        if (abs(self.ball.center_x - self.bar.center_x) < self.bar.width / width_factor - left_shift
        ) and (self.ball.center_y < self.bar.top - top_shift
        ) and self.ball.change_y < 0:
            return True


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
