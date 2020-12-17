import pgzrun

WIDTH = 1000
HEIGHT = 600

BACKGROUND_IMG = "space_game_background"  # background file name


def draw():
    screen.blit(BACKGROUND_IMG, (0,0))
    
pgzrun.go()
