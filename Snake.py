import pygame
import os
import sys
import random

#add difficulty level and sounds and draw an algorithm
 
 #INITIALIZING PYGAME
pygame.init()

#SETTING UP THE WINDOW
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("SNAKES")
black = (0,0,0)
colour1 = (255,0,0)
colour2=(0,255,0)
FPS = 3
right=(30,0)
left=(-30,0)
up=(0,-30)
down=(0,30)

font = pygame.font.SysFont("Comic Sans MS", 40)
#LOAD THE GAME BACKGROUND AND SNAKE FOOD
background = pygame.transform.scale(pygame.image.load("s.jpeg"), (WINDOW_WIDTH, WINDOW_HEIGHT))



#SNAKE CLASS
class Snake:
    def __init__(self,colour,direction,x_position,y_position):
        self.colour = colour
        self.direction = direction
        self.x_position = x_position
        self.y_position = y_position
        self.body= [(x_position,y_position)]
        self.score = 0
    
    def draw(self,display):
        #DRAWS THE SNACK BODY SHAPE
        for x,y in self.body:
            pygame.draw.rect(display,self.colour,[x,y,30,30])
    def move(self):
        #MOVES THE SNAKE BODY, CHECKS FOR BOUNDARY FIRST THO
        new_x = self.x_position + self.direction[0]
        new_y = self.y_position + self.direction[1]
        if (new_x >= 10 and new_x <= WINDOW_WIDTH - 30) and (new_y >= 10 and new_y <= WINDOW_HEIGHT - 30):
             self.x_position = new_x
             self.y_position = new_y
             self.body.insert(0, (self.x_position, self.y_position))
             self.body.pop()
    def increase(self):
        #INCREASES SIZE OF SNAKE
        self.score += 10
        new_x = self.x_position + self.direction[0]
        new_y = self.y_position + self.direction[1]
        if (new_x >= 10 and new_x <= WINDOW_WIDTH - 30) and (new_y >= 10 and new_y <= WINDOW_HEIGHT - 30):
            self.x_position = new_x
            self.y_position = new_y
            self.body.insert(0, (self.x_position, self.y_position))

class Food():
    def __init__(self):
        self.food_x = random.randrange(30,WINDOW_WIDTH-30,30)
        self.food_y = random.randrange(30,WINDOW_HEIGHT-30,30)
        self.food = pygame.transform.scale(pygame.image.load("food.png"),(30,30))

    def draw(self, display):
        display.blit(self.food,(self.food_x,self.food_y))




def main():
   result= None
   result1 = None
   game_over=False
   
   player1 = Snake(colour1,left,600,600)
   player2 = Snake(colour2,right,210,510)
   food = Food()
   run = True
   clock = pygame.time.Clock()
   while run:
       clock.tick(FPS)
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
       
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player1.direction != down and len(player1.body) > 0 and player1.body[0][1]> 10:
                    player1.direction= up
                if event.key == pygame.K_DOWN and player1.direction != up and len(player1.body) > 0 and player1.body[0][1]< WINDOW_HEIGHT - 10:
                    player1.direction = down
                if event.key == pygame.K_RIGHT and player1.direction != left and len(player1.body) > 0 and player1.body[0][0]< WINDOW_WIDTH -10:
                    player1.direction = right
                if event.key == pygame.K_LEFT and player1.direction != right and len(player1.body) > 0 and player1.body[0][0]> 10:
                    player1.direction = left
                if event.key == pygame.K_w and player2.direction != down and len(player2.body) > 0 and player2.body[0][1]> 10:
                    player2.direction= up
                if event.key == pygame.K_s and player2.direction != up and len(player2.body) > 0 and player2.body[0][1]< WINDOW_HEIGHT-10:
                    player2.direction = down
                if event.key == pygame.K_d and player2.direction != left and len(player2.body) > 0 and player2.body[0][0]< WINDOW_WIDTH-10:
                    player2.direction = right
                if event.key == pygame.K_a and player2.direction != left and len(player2.body) > 0 and player2.body[0][0]> 10:
                    player2.direction = left
                elif event.key ==pygame.K_r:
                    if game_over:
                         main()

    

       
       player1.move()
       player2.move()
       #CHECKS FOR WHEN SNAKE COMES IN CONTACT WITH THE FOOD, INCREASES IN SIZE AND SCORE INCREASES
       if len(player1.body) > 0 and (player1.body[0][0] == food.food_x and player1.body[0][1] == food.food_y):
             player1.increase()
             food = Food()
       if len(player2.body) > 0 and (player2.body[0][0] == food.food_x and player2.body[0][1] == food.food_y):
             player2.increase()
             food = Food()
       if len(player1.body) > 0 and player1.body[0] in player1.body[1:]:
            result = True  # Player1 dies 
            player1.body = []
       if len(player2.body) > 0 and player2.body[0] in player2.body[1:]:
            result1 = True  # Player2 dies
            player2.body = []
       if len(player1.body) > 0 and player1.body[0] in player2.body:
           if len(player1.body) < len(player2.body):
               result = True  # Player1 dies because it's smaller
               player1.body = []
           elif len(player1.body) == len(player2.body):
               result = True 
               result1 = True # Player1 dies because it's smaller
               player1.body = []
               player2.body = []
           else:
               result1 = True  # Player2 dies because it's smaller
               player2.body = []
       elif len(player2.body) > 0 and player2.body[0] in player1.body:
            if len(player2.body) < len(player1.body):
                result1 = True  # Player2 dies because it's smaller
                player2.body = []
            else:
                result = True  # Player1 dies because it's smaller
                player1.body = []
       
    #CHECKS FOR IF THE SNAKE COMES IN CONTACT WITH ITS OWN BODY OR THE BODY OF THE OTHER SNAKE
    #    if player1.body[0] in player2.body or player1.body[0] in player1.body[1:]:
    #        result = True  # Snake 1 is out
    #    if player2.body[0] in player1.body or player2.body[0] in player2.body[1:]:
    #         result1 = True  # Snake 2 is out

       #HANDLE DRAWING SNAKES ON SNAKE ONLY IF THEY HAVEN'T EATING THEMSELVES OR TRIED TO BITE THIER TEAMMATES OR SLAMMED HEAD AGAINST THE WALL
       #PUT INTO CONSIDERATION THAT I CAN ALSO MAKE THE GAME WORK IN A WAY THAT IT IS SNAKE 1 THAT DIES IF SNAKE 2 COLLIDES INTO SNAKE 1
       display.blit(background,(0,0))
       if (result is None) :
          player1.draw(display)
       if (result1 is None) :
          player2.draw(display)
       food.draw(display)
       #DISPLAY THE PLAYERS SCORE ON THE SCREEN
       
       score1= font.render(f"player 1: {player1.score}", False, (225,225,225))
       display.blit(score1, (10,10))
       score2= font.render(f"player 2: {player2.score}", False, (225,225,225))
       display.blit(score2, (700,10))
       if result is not None and result1 is not None:
            if player2.score > player1.score:
                game_over_text = font.render(f"Game Over! Player2 Wins!", True, (255, 0, 0))
            elif player1.score == player2.score:
                game_over_text = font.render(f"Game Over! You snooze You lose!", True, (255, 0, 0))
            else:
                game_over_text = font.render(f"Game Over! Player1 Wins!", True, (255, 0, 0))
            restart_text = font.render("Press R to Restart", True, (255, 255, 255))
            display.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 20))
            display.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 20))
            game_over=True
       
       pygame.display.update()
   display.fill(black)
   pygame.display.update()
   pygame.time.wait(500)
   pygame.quit()
   sys.exit()

   


if __name__ == "__main__":
    main()