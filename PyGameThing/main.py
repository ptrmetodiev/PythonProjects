import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RaceCar')
clock = pygame.time.Clock()  #  defining clock to keep time in the game,  use it to define frames per second

crashed = False

while not crashed:
    for event in pygame.event.get():  # gets any event - mouse click and so on...
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()  #  can update only parts to save time updating the whole display by giving what to update in parameter
    clock.tick(60)  #  defining frames per second

pygame.quit()
quit()
