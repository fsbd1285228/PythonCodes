background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

import pygame
from pygame.locals import *	  # Import some basic functions and constants.
from sys import exit	# To exit the program.

pygame.init()	# Initialize pygame. Prepare to use hard drives.

screen = pygame.display.set_mode((640,480), 0 , 32)		# Generate a screen
pygame.display.set_caption("Hello, World!")		# The title of the screen

# Load and convert the images
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert()

# Main circulation of the game
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()   			    # Exit the program when QUIT received
	screen.blit(background, (0,0))	# Draw the background image
	
	x, y = pygame.mouse.get_pos()	# Get the location of the mouse
	x -= mouse_cursor.get_width()/2
	y -= mouse_cursor.get_height()/2	# Calculate the position of the cursor (top left corner)
	screen.blit(mouse_cursor, (x,y))	# Draw the cursor
	
	pygame.display.update()		# Refresh the picture