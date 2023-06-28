# Import necessary libraries and modules
import pygame as pg
from collections import deque

from settings import *

# Define Bird class as a subclass of pygame Sprite
class Bird(pg.sprite.Sprite):
  def __init__(self, game):
    # Initialize the sprite and add it to the group of all sprites
    super().__init__(game.all_sprites_group)
    self.game = game  # The game object that this bird belongs to
    self.image = game.bird_images[0]  # Initial bird image
    self.mask = pg.mask.from_surface(game.mask_image)  # Mask for collision detection
    self.rect = self.image.get_rect()  # Rect for position and collision detection
    self.rect.center = BIRD_POS  # Initial position of the bird

    self.images = deque(game.bird_images)  # Circular buffer of bird images for animation
    self.animation_event = pg.USEREVENT + 0  # Custom event for bird animation
    pg.time.set_timer(self.animation_event, BIRD_ANIMATION_TIME)  # Start timer for bird animation

    self.falling_velocity = 0  # Initial falling velocity
    self.first_jump = False  # Flag to check if bird has jumped for the first time
    self.angle = 0  # Initial rotation angle of the bird

  # Check if bird has collided with a pipe, the ground, or the top of the screen
  def check_collision(self):
    hit = pg.sprite.spritecollide(self, self.game.pipe_group, dokill=False, collided=pg.sprite.collide_mask)
    if hit or self.rect.bottom > GROUND_Y or self.rect.top < -self.image.get_height():
      self.game.sound.hit_sound.play()  # Play hit sound
      pg.time.wait(1000)  # Wait for a second before restarting the game
      self.game.new_game()  # Restart the game

  # Rotate bird image based on falling velocity
  def rotate(self):
    if self.first_jump:
      if self.falling_velocity < -BIRD_JUMP_VALUE:
        self.angle = BIRD_JUMP_ANGLE
      else:
        self.angle = max(-2.5 * self.falling_velocity, -90)
      self.image = pg.transform.rotate(self.image, self.angle)
      mask_image = pg.transform.rotate(self.game.mask_image, self.angle)
      self.mask = pg.mask.from_surface(mask_image)

  # Make bird jump by setting falling velocity to jump value
  def jump(self):
    self.game.sound.wing_sound.play()  # Play wing sound
    self.first_jump = True
    self.falling_velocity = BIRD_JUMP_VALUE

  # Apply gravity to bird by increasing falling velocity
  def use_gravity(self):
    if self.first_jump:
      self.falling_velocity += GRAVITY
      self.rect.y += self.falling_velocity + 0.5 * GRAVITY

  # Update bird state every frame
  def update(self):
    self.check_collision()
    self.use_gravity()

  # Switch to next bird image in the buffer
  def animate(self):
    self.images.rotate(-1)
    self.image = self.images[0]

  # Handle events
  def check_event(self, event):
    if event.type == self.animation_event:
      self.animate()
      self.rotate()
    if event.type == pg.MOUSEBUTTONDOWN:
      if event.button == 1:  # If left mouse button is clicked
        self.jump()
