# Flappy DOOM
This project is a Flappy Bird clone game implemented in Python using the Pygame library, with a DOOM style design. The gameplay involves controlling a bird character to avoid pipe obstacles.

# Special Thanks
This project was inspired by the DOOM game series and the Flappy Bird game.

The original "Flappy Bird" game was developed by Dong Nguyen.
The DOOM aesthetic and sounds are inspired by id Software's classic first-person shooter game, DOOM.

# Project Structure
The project has the following file and folder structure:

## src
### This folder contains the source code files for the game:

 * ###### main.py: The main entry point of the game. It controls the game loop, handles events, and manages the rendering and updating of game objects.
* ######  bird.py: This file contains the Bird class that represents the bird character the player controls. It handles the bird's animations, rotations, jumping, gravity, and collision detection.
* ######  pipe.py: Contains the TopPipe, BottomPipe, and PipeHandler classes. TopPipe and BottomPipe handle the movement and removal of the pipe obstacles, while PipeHandler manages the generation of pipes and keeps track of the number of pipes that the bird has passed.
* ######  game_objects.py: This file contains the Score, Sound, Background, and Ground classes. Score handles the drawing of the player's score, Sound manages the game's sound effects, Background handles the scrolling background image, and Ground represents the ground.
* ######  settings.py: This file defines the game's settings and constants.

# Classes

## src/main.py
This file is the main entry point of the game and contains the Game class.

Game: This class controls the game loop, handles events, and manages the rendering and updating of game objects. It also loads the game assets like images and sounds.
## src/bird.py
This file contains the Bird class.

Bird: This class represents the bird character the player controls. It handles the bird's animations, rotations, jumping, gravity, and collision detection.
## src/pipe.py
This file contains the TopPipe, BottomPipe, and PipeHandler classes.

TopPipe and BottomPipe: These classes represent the top and bottom parts of the pipe obstacles, respectively. They handle the movement and removal of the pipes.

PipeHandler: This class manages the generation of pipe obstacles at regular intervals. It also keeps track of the number of pipes that the bird has successfully passed.

## src/game_objects.py
This file contains the Score, Sound, Background, and Ground classes.

Score: This class handles the drawing of the player's score on the screen.

Sound: This class manages the game's sound effects.

Background: This class handles the scrolling background image.

Ground: This class represents the ground and handles its scrolling movement.

## src/settings.py
While this file does not contain any classes, it defines the game's settings and constants which are used by the other classes. For example, it includes settings like the screen resolution, frame rate, scrolling speed, and various bird and pipe parameters.

# assets
This folder contains various resources used in the game:

## bird
This subfolder contains sprite images for the bird character and its mask.

0.png, 1.png, 2.png, 3.png, 4.png: Bird animation frames.
mask.png: Mask image for the bird character.
## font
This subfolder contains font files used in the game.

doom.ttf: Font file used for drawing the score.
## images
This subfolder contains image files used for the game's visuals.

bg.png: Background image.
ground.png: Ground image.
top_pipe.png: Image for the top part of the pipe obstacles.
## sound
This subfolder contains sound files used for sound effects and music.

hit.wav: Sound effect for collision.
point.wav: Sound effect for scoring points.
theme.mp3: Background music theme.
wing.wav: Sound effect for the bird's wing flapping.
## Instructions
To run the project, follow these steps:

Install Python 3 if you haven't already.
Install the Pygame library by running the command: pip install pygame.
Navigate to the project's src directory.
Run the command: python3 main.py.
Make sure you have the required resources (images, sounds, etc.) in the appropriate directories as shown in the folder structure.

Feel free to modify and explore the game to suit your needs.

Enjoy playing!
