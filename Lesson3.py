import pgzrun
from random import randint
TITLE = "Good Shot Game"
WIDTH = 500
HEIGHT = 500

message = ""
score = 0
game_over = False

mario = Actor("mario")

def draw():
    screen.clear()
    screen.fill((128, 0, 0))

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60,
            color="white"
        )

        screen.draw.text(
            f"Final Score: {score}",
            center=(WIDTH // 2, HEIGHT // 2 + 50),
            fontsize=40,
            color="white"
        )

    else:
        mario.draw()

        screen.draw.text(
            message,
            center=(400, 20),
            fontsize=30,
            color="white"
        )

        screen.draw.text(
            f"Score: {score}",
            topleft=(10, 10),
            fontsize=30,
            color="white"
        )
def place_mario():
    mario.x=randint(50,WIDTH-50)
    mario.y=randint(50,HEIGHT-50)
def end_game():
    quit()
def on_mouse_down(pos):
    global message,score,game_over
    if game_over:
        return
    if mario.collidepoint(pos):
        message="+99 Aura"
        score+=1
        place_mario()
    else:
        message="-99 Aura"
        game_over=True
        clock.schedule_unique(end_game,2)
place_mario()
pgzrun.go()