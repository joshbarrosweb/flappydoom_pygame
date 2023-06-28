# Define resolution settings
RES = WIDTH, HEIGHT = 1600, 900  # Game screen resolution: 1600 x 900 pixels
FPS = 60  # Frames per second (game update frequency)

# Game dynamics settings
SCROLL_SPEED = 8  # Scrolling speed for moving objects (ground, pipes)
GRAVITY = 1  # Gravity value affecting the bird's fall

# Bird specific settings
BIRD_POS = WIDTH // 4, HEIGHT // 3  # Bird's initial position on the screen
BIRD_SCALE = 1.5  # Scaling factor for bird's size
BIRD_ANIMATION_TIME = 150  # Time interval (in ms) between each bird flap animation
BIRD_JUMP_VALUE = -16  # Velocity value when bird jumps (negative because pygame's y-axis is inverted)
BIRD_JUMP_ANGLE = 25  # Angle of bird's rotation when it jumps

# Ground settings
GROUND_HEIGHT = HEIGHT // 12  # Height of the ground
GROUND_Y = HEIGHT - GROUND_HEIGHT  # y-coordinate of the ground (taking from the top of the screen)

# Pipe settings
PIPE_WIDTH = 250  # Width of the pipes
PIPE_HEIGHT = HEIGHT  # Maximum height of the pipes
DIST_BETWEEN_PIPES = 650  # Horizontal distance between consecutive pipes
GAP_HEIGHT = 320  # Height of the gap between top and bottom pipes
HALF_GAP_HEIGHT = GAP_HEIGHT // 2  # Half of the gap height for easy calculations in other parts of the code
