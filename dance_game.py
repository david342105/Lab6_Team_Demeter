import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pgzrun
import random
import pygame

WIDTH = 800
HEIGHT = 600

# 背景
stage = Actor("stage")

# 音樂
pygame.mixer.init()
pygame.mixer.music.load("MMV NALYRO x KEAN DYSSO - Here [TubeRipper.cc].ogg")
pygame.mixer.music.play(-1)

# 舞步箭頭位置
move_positions = {
    "up": (150, 100),
    "down": (150, 200),
    "left": (150, 300),
    "right": (150, 400),
    "up2": (650, 100),
    "down2": (650, 200),
    "left2": (650, 300),
    "right2": (650, 400),
}

# 分數與舞步
score1 = 0
score2 = 0
current_move_p1 = random.choice(["up", "down", "left", "right"])
current_move_p2 = random.choice(["up", "down", "left", "right"])
timer = 0
countdown = 30
frame_count = 0
game_over = False

# 小人
dancer1 = Actor("dancer-start", (200, 500))
dancer2 = Actor("dancer-start", (600, 500))
dancer1_timer = 0
dancer2_timer = 0

def draw():
    screen.clear()
    stage.draw()
    dancer1.draw()
    dancer2.draw()

    if not game_over:
        screen.draw.text(f"P1 Score: {score1}", (50, 20), fontsize=40, color="white")
        screen.draw.text(f"P2 Score: {score2}", (600, 20), fontsize=40, color="white")
        screen.draw.text(f"Time Left: {countdown}", center=(400, 30), fontsize=40, color="yellow")

        # Player 1 箭頭
        for move in ["up", "down", "left", "right"]:
            if move == current_move_p1:
                screen.blit(f"{move}-lit", move_positions[move])
            else:
                screen.blit(move, move_positions[move])

        # Player 2 箭頭
        for move in ["up", "down", "left", "right"]:
            move2 = move + "2"
            if move == current_move_p2:
                screen.blit(f"{move}-lit", move_positions[move2])
            else:
                screen.blit(move, move_positions[move2])
    else:
        screen.draw.text("Game Over!", center=(400, 100), fontsize=60, color="orange")
        screen.draw.text(f"P1 Score: {score1}", (100, 200), fontsize=40, color="white")
        screen.draw.text(f"P2 Score: {score2}", (500, 200), fontsize=40, color="white")

        if score1 > score2:
            screen.draw.text("Player 1 Wins!", center=(400, 300), fontsize=50, color="lime")
        elif score2 > score1:
            screen.draw.text("Player 2 Wins!", center=(400, 300), fontsize=50, color="cyan")
        else:
            screen.draw.text("It's a Tie!", center=(400, 300), fontsize=50, color="gray")

def update():
    global timer, current_move_p1, current_move_p2
    global frame_count, countdown, game_over
    global dancer1_timer, dancer2_timer

    if not game_over:
        timer += 1
        frame_count += 1

        if frame_count >= 60:
            countdown -= 1
            frame_count = 0
            if countdown <= 0:
                game_over = True
                dancer1.image = f"dancer-{current_move_p1}"
                dancer2.image = f"dancer-{current_move_p2}"
                return

        if timer >= 60:
            current_move_p1 = random.choice(["up", "down", "left", "right"])
            current_move_p2 = random.choice(["up", "down", "left", "right"])
            timer = 0

    # 動作回復
    if dancer1_timer > 0:
        dancer1_timer -= 1
        if dancer1_timer == 0:
            dancer1.image = "dancer-start"
    if dancer2_timer > 0:
        dancer2_timer -= 1
        if dancer2_timer == 0:
            dancer2.image = "dancer-start"

def on_key_down(key):
    global score1, score2
    global dancer1_timer, dancer2_timer

    if game_over:
        return

    # Player 1 - WASD
    if key == keys.W and current_move_p1 == "up":
        score1 += 1
        dancer1.image = "dancer-up"
        dancer1_timer = 15
    elif key == keys.S and current_move_p1 == "down":
        score1 += 1
        dancer1.image = "dancer-down"
        dancer1_timer = 15
    elif key == keys.A and current_move_p1 == "left":
        score1 += 1
        dancer1.image = "dancer-left"
        dancer1_timer = 15
    elif key == keys.D and current_move_p1 == "right":
        score1 += 1
        dancer1.image = "dancer-right"
        dancer1_timer = 15

    # Player 2 - Arrow Keys
    if key == keys.UP and current_move_p2 == "up":
        score2 += 1
        dancer2.image = "dancer-up"
        dancer2_timer = 15
    elif key == keys.DOWN and current_move_p2 == "down":
        score2 += 1
        dancer2.image = "dancer-down"
        dancer2_timer = 15
    elif key == keys.LEFT and current_move_p2 == "left":
        score2 += 1
        dancer2.image = "dancer-left"
        dancer2_timer = 15
    elif key == keys.RIGHT and current_move_p2 == "right":
        score2 += 1
        dancer2.image = "dancer-right"
        dancer2_timer = 15

pgzrun.go()
