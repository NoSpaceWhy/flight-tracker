from flight import flightRQ

# the UI
import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Flight Data Fetcher")


info = pygame.font.Font(None, 50)  # None = default font, 50 = size
# Render the text
info_text = info.render("This is a flight tracker", True, (255, 255, 255))  # White text
# Get the rectangle of the text
text_rect = info_text.get_rect()  # Center on screen


info_2 = pygame.font.Font(None, 50)  # None = default font, 50 = size
# Render the text
info_2_text = info_2.render("To track your flights or just see", True, (255, 255, 255))  # White text
# Get the rectangle of the text
info_2_rect = info_2_text.get_rect()  # Center on screen


# Corner positions
top_left = (0, 0)
top_right = (600 - text_rect.width, 0)
bottom_left = (0, 400 - text_rect.height)
bottom_right = (600 - text_rect.width, 400 - text_rect.height)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # the text to understanding how it works to see the flights
    screen.blit(info_text, top_left)
    screen.blit(info_2_text, (0, 40))

    

    # Update the display
    pygame.display.flip()

pygame.quit()