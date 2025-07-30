import pygame

pygame.init()
print("setup Start")
window = pygame.display.set_mode(size=(600, 480))
print("Loop Start")
while True:
    # Check for all evevnts
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quitting...")
            pygame.quit()
            quit()  # end pygame
