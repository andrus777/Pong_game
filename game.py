import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.2)
        self.change_x = 3.0
        self.change_y = 3.0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = -self.change_x
        if self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y
        if self.top <= 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.2)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.left <= 0:
            self.left = 0


class Brick(arcade.Sprite):
    def __init__(self):
        super().__init__('brick.png', 0.2)


class Game(arcade.Window):
    BRICK_WALL = []

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        for i in range(1,20):
            for j in range(1, 5):
                brick = Brick()
                brick.center_x = i * SCREEN_WIDTH / 20
                brick.center_y = SCREEN_HEIGHT - 20 * j
                self.BRICK_WALL.append(brick)



    def on_draw(self):
        self.ball.update()
        self.clear((255,255,255))
        self.bar.draw()
        self.ball.draw()
        for brick in self.BRICK_WALL:
            brick.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y

        for brick in self.BRICK_WALL:
            if arcade.check_for_collision(brick, self.ball):
                self.ball.change_y = -self.ball.change_y
                self.BRICK_WALL.remove(brick)
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 10
        if key == arcade.key.LEFT:
            self.bar.change_x = -10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0



if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()