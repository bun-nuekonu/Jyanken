import pygame
import math
import random

# 画面サイズ
WIDTH, HEIGHT = 800, 600

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 速度設定
CHASE_SPEED = 1  # 追いかける速度
ESCAPE_SPEED = 0.7  # 逃げる速度
RANDOM_FACTOR = 2 # ランダムな動きを加える
OBJECT_COUNT = 30  # 各オブジェクトの初期数
MIN_DISTANCE = 20  # オブジェクト間の最小距離

# Pygame の初期化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("じゃんけんライフゲーム")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# 画像の読み込み
ROCK_IMAGE = pygame.image.load("assets/rock.png")
SCISSORS_IMAGE = pygame.image.load("assets/hasami.png")
PAPER_IMAGE = pygame.image.load("assets/paper.png")
ROCK_IMAGE = pygame.transform.scale(ROCK_IMAGE, (20, 20))
SCISSORS_IMAGE = pygame.transform.scale(SCISSORS_IMAGE, (20, 20))
PAPER_IMAGE = pygame.transform.scale(PAPER_IMAGE, (20, 20))

# 初期位置（三角形の頂点を形成）
START_POSITIONS = {
    "rock": (WIDTH // 4, HEIGHT // 4),
    "scissors": (3 * WIDTH // 4, HEIGHT // 4),
    "paper": (WIDTH // 2, 3 * HEIGHT // 4),
}

# クラスの定義
class Entity:
    def __init__(self, x, y, entity_type):
        self.x = x + random.randint(-20, 20)
        self.y = y + random.randint(-20, 20)
        self.type = entity_type
        self.image = ROCK_IMAGE if entity_type == "rock" else SCISSORS_IMAGE if entity_type == "scissors" else PAPER_IMAGE

    def move(self, entities):
        target = None
        escape_target = None
        min_dist = float("inf")
        max_dist = 0
        move_x, move_y = 0, 0

        for other in entities:
            if other == self:
                continue
            dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
            
            # 追いかける対象
            if (self.type == "rock" and other.type == "scissors") or \
               (self.type == "scissors" and other.type == "paper") or \
               (self.type == "paper" and other.type == "rock"):
                if dist < min_dist:
                    min_dist = dist
                    target = other
            
            # 逃げる対象
            if (self.type == "rock" and other.type == "paper") or \
               (self.type == "scissors" and other.type == "rock") or \
               (self.type == "paper" and other.type == "scissors"):
                if dist > max_dist:
                    max_dist = dist
                    escape_target = other

        if target:
            dx = target.x - self.x
            dy = target.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > 0:
                move_x += CHASE_SPEED * (dx / distance)
                move_y += CHASE_SPEED * (dy / distance)
        
        if escape_target:
            dx = escape_target.x - self.x
            dy = escape_target.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance > 0:
                move_x -= ESCAPE_SPEED * (dx / distance)
                move_y -= ESCAPE_SPEED * (dy / distance)

        # ランダムな揺らぎ
        move_x += random.uniform(-RANDOM_FACTOR, RANDOM_FACTOR)
        move_y += random.uniform(-RANDOM_FACTOR, RANDOM_FACTOR)

        # 衝突回避
        for other in entities:
            if other == self:
                continue
            dist = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
            if dist < MIN_DISTANCE:
                move_x += (self.x - other.x) * 0.1
                move_y += (self.y - other.y) * 0.1

        self.x = max(0, min(WIDTH, self.x + move_x))
        self.y = max(0, min(HEIGHT, self.y + move_y))

    def draw(self):
        screen.blit(self.image, (int(self.x) - 10, int(self.y) - 10))

def draw_counts(entities):
    rock_count = sum(1 for e in entities if e.type == "rock")
    scissors_count = sum(1 for e in entities if e.type == "scissors")
    paper_count = sum(1 for e in entities if e.type == "paper")
    text = font.render(f"Rock: {rock_count}  Scissors: {scissors_count}  Paper: {paper_count}", True, WHITE)
    screen.blit(text, (10, 10))

def check_collisions(entities):
    for entity in entities:
        for other in entities:
            if entity == other:
                continue
            dist = math.sqrt((entity.x - other.x) ** 2 + (entity.y - other.y) ** 2)
            if dist < 20:
                if entity.type == "rock" and other.type == "scissors":
                    other.type = "rock"
                    other.image = ROCK_IMAGE
                elif entity.type == "scissors" and other.type == "paper":
                    other.type = "scissors"
                    other.image = SCISSORS_IMAGE
                elif entity.type == "paper" and other.type == "rock":
                    other.type = "paper"
                    other.image = PAPER_IMAGE

def main():
    entities = []
    for entity_type, (x, y) in START_POSITIONS.items():
        for _ in range(OBJECT_COUNT):
            entities.append(Entity(x, y, entity_type))

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for entity in entities:
            entity.move(entities)
            entity.draw()
        check_collisions(entities)
        draw_counts(entities)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
