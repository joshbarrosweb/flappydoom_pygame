import pygame as pg

from settings import *

# Score class which handles the score display
class Score:
  def __init__(self, game):
    self.game = game  # The game object that this score display belongs to
    self.font = pg.font.Font('./assets/font/doom.ttf', 150)  # Load the font
    self.font_pos = (WIDTH // 2, HEIGHT // 8)  # Position to display the score on the screen

  def draw(self):
    score = self.game.pipe_handler.passed_pipes  # Get the score from the game
    self.text = self.font.render(f'{score}', True, 'white')  # Render the score
    self.game.screen.blit(self.text, self.font_pos)  # Draw the score on the screen

# Sound class which handles the sounds effects
class Sound:
  def __init__(self):
    self.hit_sound = pg.mixer.Sound('./assets/sound/hit.wav')  # Load the hit sound
    self.point_sound = pg.mixer.Sound('./assets/sound/point.wav')  # Load the point sound
    self.wing_sound = pg.mixer.Sound('./assets/sound/wing.wav')  # Load the wing sound

# Background class which handles the background image
class Background:
  def __init__(self, game):
    self.game = game  # The game object that this background belongs to
    self.x = 0  # Initial x position
    self.y = 0  # Initial y position
    self.speed = SCROLL_SPEED - 2  # Scroll speed of the background (slower than ground and pipes)
    self.image = self.game.background_image  # Load the background image

  def update(self):
    self.x = (self.x - self.speed) % -WIDTH  # Move the background to the left and loop it when it's out of the screen

  def draw(self):
    # Draw the looping background on the screen
    self.game.screen.blit(self.image, (self.x, self.y))
    self.game.screen.blit(self.image, (WIDTH + self.x, self.y))

# Ground class which handles the ground image and inherits from Background
class Ground(Background):
  def __init__(self, game):
    super().__init__(game)  # Initialize the background
    self.y = GROUND_Y  # y-coordinate of the ground
    self.speed = SCROLL_SPEED  # Scroll speed of the ground (same as pipes)
    self.image = self.game.ground_image  # Load the ground image
