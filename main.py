from flight import flightRQ

# the UI
import pygame

white = (255, 255, 255)
black = (0, 0, 0)


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


# Box setup
refresh_colour = (255, 0, 0)  # Red

# Load a sprite (replace with your image path)
refresh = pygame.image.load("reload.jpeg").convert_alpha()
refresh = pygame.transform.scale(refresh, (80, 80))  # Resize to fit box

refresh_box = refresh.Rect()  # (x, y, width, height)

# Center sprite inside the box
refresh_rect = refresh.get_rect(center=refresh_box.center)



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

    pygame.draw.rect(screen, refresh_colour, refresh_rect, 3)
    
    screen.blit(refresh, refresh_rect)

    mos_pos = pygame.mouse.get_pos()
    refresh_rect_mCollide = refresh_rect.collidepoint(mos_pos)

    if refresh_rect_mCollide:
        if event.type == pygame.MOUSEBUTTONDOWN:
            flightsData = flightRQ()
            print(flightsData)
    # Update the display
    pygame.display.flip()

    print(mos_pos)
    
pygame.quit()