#IMPORT IMPORTANT FILES
import pygame
from sys import exit
from helper.constants import WIDTH, HEIGHT, GRAY, LIGHT_GREEN
from helper.board import Board


#INITIALIZING SCREEN
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
icon = pygame.image.load('pieces/white_knight.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()


#CREATE BOARD
board = Board()


def main():
    print(board.board)
    while True:
        # Main loop, listening to different events/inputs
        for event in pygame.event.get():
            # Quit functionality
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #if event type == start game, run initlize
        

        board.draw_tiles(screen)
        board.update_pieces(screen)

        pygame.display.update()
        clock.tick(60)


main()