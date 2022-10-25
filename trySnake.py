import pygame, sys, random
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.crunch = pygame.mixer.Sound('Sound/eat-sounds.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
            # #create rectangle
            # x_pos = int(block.x * cell_size)
            # y_pos = int(block.y * cell_size)
            # block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            # #draw rectangle
            # pygame.draw.rect(screen,(121,111,199),block_rect)
            #1. We still need a rect for the positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            #2. Create head direction
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index+1] - block
                next_block = self.body[index -1] -block
                if previous_block.x == next_block.x: # create body of snake when the snake moving along
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:# create body of snake when the snake moving sideway
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x ==1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x ==1:
                        screen.blit(self.body_br,block_rect)
                    elif previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x ==-1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x ==-1:
                        screen.blit(self.body_bl,block_rect)
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0) : self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, -1): self.head = self.head_down
        elif head_relation == Vector2(0, 1): self.head = self.head_up
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1):self.tail = self.tail_down
    def move_snake(self):
        if self.new_block== True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)  # insert to end of snake
            self.body = body_copy[:]  # Update new body for snake
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)# insert to end of snake
            self.body = body_copy[:] # Update new body for snake
    def add_block(self):
        self.new_block = True
    def play_sound(self):
        self.crunch.play()
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
class FRUIT:

    def __init__(self):
        self.randomize()
        self.blueberry = pygame.image.load('Graphics/blueberry.png').convert_alpha()
        self.items = pygame.image.load('Graphics/rasberry.png').convert_alpha()
    def randomize(self):
        # create an X and Y position
        # draw a square
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)

        self.x1 = random.randint(0, cell_number - 1)
        self.y1 = random.randint(0, cell_number - 1)
        self.pos_i = pygame.math.Vector2(self.x1,self.y1)
    def draw_fruit(self):
        #create rectangle
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int( self.pos.y*cell_size),cell_size,cell_size)
        # demo fruit by draw rectangle
        # pygame.draw.rect(screen,(191,115,114),fruit_rect)
        # create graphics for fruit

        screen.blit(self.blueberry,fruit_rect)
        """I want to change graphics of fruit when snake eat itself but I can't
        Because  When I use method choice of random then it change image very fast"""
        # rasberry = pygame.image.load('Graphics/rasberry.png').convert_alpha()
        # list_fruit = [blueberry,rasberry]
        # choice_item = random.choice(list_fruit)
        # screen.blit(choice_item,fruit_rect)
    def draw_items(self):
        items_rect = pygame.Rect(int(self.pos_i.x*cell_size),int( self.pos_i.x*cell_size),cell_size,cell_size)
        screen.blit(self.items,items_rect)
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.draw_score()
        self.set_speed()
        # self.check_item()
    def draw_element(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        # self.fruit.draw_items()
    def check_collision(self): # check when snake through the fruit
        if self.fruit.pos == self.snake.body[0]:
            #reposition for fruit
            self.fruit.randomize()
            # add anothor block to the snake
            self.snake.add_block()
            self.snake.play_sound()

        #check when fruit appear but it's on top of the Snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    def game_over(self):
        self.snake.reset()
    def check_fail(self):
         # if snake hits to wall
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def draw_grass(self):
        for col in range(cell_number):
            if col %2 == 0:
                for row in range(cell_number):
                    if row % 2 == 0:
                        grass_rect = pygame.Rect(int(row * cell_size),int(col*cell_size),cell_size,cell_size)
                        pygame.draw.rect(screen,(111,215,70),grass_rect)
                        # grass_image = pygame.image.load('Graphics/grass.png').convert_alpha()
                        # screen.blit(grass_image,grass_rect)
            else:
                for row in range(cell_number):
                    if row % 2 != 0:
                        grass_rect = pygame.Rect(int(row * cell_size), int(col * cell_size), cell_size, cell_size)
                        pygame.draw.rect(screen, (111, 215, 70), grass_rect)
                        # grass_image = pygame.image.load('Graphics/grass.png').convert_alpha()
                        # screen.blit(grass_image, grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body) -3)
        score_surface = game_font.render(score_text,True,(50,77,48))
        score_x = int(cell_size*cell_number -120)
        score_y = int(cell_size*cell_number -40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = self.fruit.blueberry.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width+score_rect.width,apple_rect.height)

        pygame.draw.rect(screen,(167,70,81),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(self.fruit.blueberry,apple_rect)
        pygame.draw.rect(screen,(56,74,125),bg_rect,2)

    def check_level(self):
        level_text = 'LEVEL UP!'
        level_surface = game_font.render(level_text, True, (150, 77, 48))
        lv_x = int((cell_size * cell_number) / 2)
        lv_y = int((cell_size * cell_number) / 2)
        level_rect = level_surface.get_rect(center=(lv_x, lv_y))
        screen.blit(level_surface, level_rect)
    def set_speed(self):

        score_point = int(len(self.snake.body) -3)
        if score_point < 5:
            pygame.time.set_timer(SCREEN_UPDATE, 120)  # set up speed for snake
            self.check_level()
        elif 5 <= score_point < 10:
            pygame.time.set_timer(SCREEN_UPDATE, 100)  # set up speed for snake
        else:
            pygame.time.set_timer(SCREEN_UPDATE, 80)  # set up speed for snake

    ''''I want to add some attribute for snake such as : speed up'''
    # def check_item(self):
    #     score_point = int(len(self.snake.body) -3)
    #     if score_point == score_point+3:
    #         self.fruit.draw_items()
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_number = 20
cell_size = 40
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,200)
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) # tạo screen
pygame.display.set_caption('Snake 1.0')
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',25)
main_game = MAIN()
while True:
    for event in pygame.event.get(): #run all of  event
        if event.type == pygame.QUIT:# quit
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1: # check snake can't reverse itself
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

    screen.fill((115,195,70))
    main_game.draw_element()
    pygame.display.update()
    clock.tick(60)