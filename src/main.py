# import necessary libraries
import pygame as pg
import sys

# import necessary classes from local files
from bird import *
from pipe import *
from game_objects import *
from settings import *

# main class for the game
class FlappyDoom:
  def __init__(self):
    pg.init()  # initialize pygame
    pg.display.set_caption('Flappy Doom') # set window caption
    # create the main screen with resolution from settings
    self.screen = pg.display.set_mode(RES)
    # clock to handle frames per second (FPS)
    self.clock = pg.time.Clock()
    # load game assets (images, etc)
    self.load_assets()
    # load sounds for game
    self.sound = Sound()
    # handle score in the game
    self.score = Score(self)
    # initialize a new game
    self.new_game()

  # this function loads all the necessary game assets
  def load_assets(self):
    # load and resize bird sprites
    self.bird_images = [pg.image.load(f'./assets/bird/{i}.png').convert_alpha() for i in range(5)]
    # get bird size and rescale bird images
    bird_image = self.bird_images[0]
    bird_size = bird_image.get_width() * BIRD_SCALE, bird_image.get_height() * BIRD_SCALE
    self.bird_images = [pg.transform.scale(sprite, bird_size) for sprite in self.bird_images]
    # load and resize background image
    self.background_image = pg.image.load('./assets/images/bg.png').convert()
    self.background_image = pg.transform.scale(self.background_image, RES)
    # load and resize ground image
    self.ground_image = pg.image.load('./assets/images/ground.png').convert()
    self.ground_image = pg.transform.scale(self.ground_image, (WIDTH, GROUND_HEIGHT))
    # load and resize pipe images
    self.top_pipe_image = pg.image.load('./assets/images/top_pipe.png').convert_alpha()
    self.top_pipe_image = pg.transform.scale(self.top_pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
    self.bottom_pipe_image = pg.transform.flip(self.top_pipe_image, False, True)
    # load and resize mask image
    mask_image = pg.image.load('./assets/bird/mask.png').convert_alpha()
    mask_size = mask_image.get_width() * BIRD_SCALE, mask_image.get_height() * BIRD_SCALE
    self.mask_image = pg.transform.scale(mask_image, mask_size)

  # this function initializes a new game
  def new_game(self):
    # initialize game object groups
    self.all_sprites_group = pg.sprite.Group()
    self.pipe_group = pg.sprite.Group()
    # create game objects
    self.bird = Bird(self)
    self.background = Background(self)
    self.ground = Ground(self)
    self.pipe_handler = PipeHandler(self)

  # draw function to render all game objects
  def draw(self):
    # draw background, all sprites, ground, and score
    self.background.draw()
    self.all_sprites_group.draw(self.screen)
    self.ground.draw()
    self.score.draw()
    pg.display.flip()  # update the full display surface to the screen

  # update function to handle logic and update game objects
  def update(self):
    # update background, all sprites, ground, pipe handler, and FPS
    self.background.update()
    self.all_sprites_group.update()
    self.ground.update()
    self.pipe_handler.update()
    self.clock.tick(FPS)  # ensure the program will not run at more than FPS frames per second

  # function to check all pygame events
  def check_events(self):
    # loop through all current events
    for event in pg.event.get():
      if event.type == pg.QUIT:  # if quit event is detected, quit pygame and exit program
        pg.quit()
        sys.exit()
      self.bird.check_event(event)  # check for bird-specific events

  # main game loop
  def run(self):
    while True:  # infinite loop until quit event is detected
      self.check_events()  # check for events
      self.update()  # update game objects
      self.draw()  # draw game objects

# run the game if this script is being run directly
if __name__ == '__main__':
  game = FlappyDoom()
  game.run()
