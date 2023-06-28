import pygame as pg
import random

from settings import *

# TopPipe class which inherits from pygame's Sprite class
class TopPipe(pg.sprite.Sprite):
  def __init__(self, app, gap_y_pos):
    # Initialize the sprite and add it to the group of pipes and all sprites
    super().__init__(app.pipe_group, app.all_sprites_group)
    self.image = app.top_pipe_image  # Set the image of the pipe
    self.mask = pg.mask.from_surface(self.image)  # Create a mask for collision detection
    self.rect = self.image.get_rect()  # Create a rectangle for position and collision detection
    self.rect.bottomleft = WIDTH, gap_y_pos - HALF_GAP_HEIGHT - GROUND_HEIGHT  # Set initial position

  def update(self):
    self.rect.left -= SCROLL_SPEED  # Move the pipe to the left based on the scroll speed
    if self.rect.right < 0:  # If the pipe is out of screen to the left
      self.kill()  # Remove the pipe

# BottomPipe class which inherits from the TopPipe class
class BottomPipe(TopPipe):
  def __init__(self, app, gap_y_pos):
    super().__init__(app, gap_y_pos)  # Initialize the sprite
    self.image = app.bottom_pipe_image  # Set the image of the pipe
    self.rect.topleft = WIDTH, gap_y_pos + HALF_GAP_HEIGHT - GROUND_HEIGHT  # Set initial position

# PipeHandler class to generate and manage pipes
class PipeHandler:
  def __init__(self, game):
    self.game = game  # The game object that this handler belongs to
    self.pipe_dist = DIST_BETWEEN_PIPES  # The initial distance between pipes
    self.pipes = []  # List to store the current pipes
    self.passed_pipes = 0  # Counter for the pipes that the bird has passed

  def count_passed_pipes(self):
    # Iterate over the current pipes
    for pipe in self.pipes:
      if BIRD_POS[0] > pipe.rect.right:  # If the bird has passed the pipe
        self.game.sound.point_sound.play()  # Play point sound
        self.passed_pipes += 1  # Increase the counter
        self.pipes.remove(pipe)  # Remove the pipe from the list

  def update(self):
    self.generate_pipes()  # Generate new pipes
    self.count_passed_pipes()  # Count the passed pipes

  @staticmethod
  def get_gap_y_position():
    # Get a random y position for the gap between pipes
    return random.randint(GAP_HEIGHT, HEIGHT - GAP_HEIGHT)

  def generate_pipes(self):
    if self.game.bird.first_jump:  # If the bird has made the first jump
      self.pipe_dist += SCROLL_SPEED  # Increase the distance between pipes based on the scroll speed
      if self.pipe_dist > DIST_BETWEEN_PIPES:  # If the distance has reached the threshold
        self.pipe_dist = 0  # Reset the distance
        gap_y = self.get_gap_y_position()  # Get a new gap position

        # Generate a new pair of top and bottom pipes
        TopPipe(self.game, gap_y)
        pipe = BottomPipe(self.game, gap_y)
        self.pipes.append(pipe)  # Add the bottom pipe to the list of current pipes
