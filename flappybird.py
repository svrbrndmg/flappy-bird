import pygame as pg
import random as rm
import os

ubdir = os.path.dirname(os.path.realpath(__file__))
os.chdir(ubdir)
print(os.getcwd())

pg.init()
pg.font.init()
run = True
WIDTH = 300
HEIGHT = 300
screen = pg.display.set_mode((300, HEIGHT))
pg.display.set_caption("Flappy Bird Clone")
flapper = pg.image.load(r"flapper.png")
pg.display.set_icon(flapper)
clock = pg.time.Clock()
fps = 60
mousedown = False
gamefont = pg.font.SysFont('Calibri', 24)
last = pg.time.get_ticks()
last2 = pg.time.get_ticks()
cooldown = 400
roundcooldown = 10000
roundcount = 1
gameoverflag = False
active = False
name = ''
donenaming = False
debug = False

birdx = 20
birdy = 150
pipe1x = 290
pipe1y = 60
pipe2x = 290
pipe2y = pipe1y + 190
points = 0
strpoints = str(points)

screen.fill("cyan")
bird = pg.draw.circle(screen, "white", [birdx, birdy], 10)
pipe1 = pg.draw.rect(screen, "white", pg.Rect((pipe1x, pipe1y), (40, 100)))
pipe2 = pg.draw.rect(screen, "white", pg.Rect((pipe2x, pipe2y), (40, 100)))
pointbox = pg.draw.rect(screen, "cyan", pg.Rect((20, 0), (5, 300)))
pipe1leftover = pg.draw.rect(screen, "green", pg.Rect((pipe1x, pipe1y - 100), (40, 100)))
pipe2leftover = pg.draw.rect(screen, "green", pg.Rect((pipe2x, pipe2y + 100), (40, 100)))
pipe1top = pg.draw.rect(screen, "green", pg.Rect((pipe1x - 10, pipe1y + 100), (60, 20)))
pipe2top = pg.draw.rect(screen, "green", pg.Rect((pipe2x - 10, pipe2y), (60, 20)))
namebox = pg.draw.rect(screen, "green", pg.Rect((20, 170), (100, 20)))

while run:
      clock.tick(fps)
      screen.fill("cyan")
      
      for event in pg.event.get():
         if event.type == pg.QUIT:
            run = False
         if event.type == pg.MOUSEBUTTONDOWN:
            mousedown = True
            birdy -= 25
            if namebox.collidepoint(event.pos):
                  active = True
            else:
                  active = False
         if event.type == pg.KEYDOWN:
               if event.key == pg.K_SPACE:
                     mousedown = True
                     birdy -= 25
               if event.key == pg.K_d:
                     debug = True
               if active:
                     if event.key == pg.K_RETURN:
                           donenaming = True
                     if event.key == pg.K_BACKSPACE:
                           name = name[:-1]
                     else:
                           name += event.unicode
         if event.type == pg.MOUSEBUTTONUP or event.type == pg.KEYUP:
            mousedown = False
         if pointbox.colliderect(pipe1) or pointbox.colliderect(pipe2):
            if gameoverflag == False:
               now = pg.time.get_ticks()
               if now - last >= cooldown:
                  last = now
                  points += 1
         if not pointbox.colliderect(pipe1) or not pointbox.colliderect(pipe2):
            if gameoverflag == False:
               now2 = pg.time.get_ticks()
               if now2 - last2 >= roundcooldown:
                  last2 = now2
                  roundcount += 1
                  roundcooldown = roundcooldown * 1.5
         if pipe1.colliderect(bird) or pipe2.colliderect(bird):
               if debug == False:
                  gameoverflag = True
         if pipe1leftover.colliderect(bird) or pipe2leftover.colliderect(bird):
               if debug == False:
                  gameoverflag = True
         if pipe1top.colliderect(bird) or pipe2top.colliderect(bird):
               if debug == False:
                  gameoverflag = True
         if debug:
               pass
               
               
      escalation = 3.5
      escalation += roundcount / 5
      pipe1x -= escalation
      pipe2x -= escalation
      if pipe1x < -40:
         pipe1x = 290
         pipe1y = rm.randint(5, 100)
      if pipe2x < -40:
         pipe2x = 290
         pipe2y = pipe1y + 190
      if birdy > 0 and birdy < HEIGHT and mousedown == False:
         birdy += 1.5
      if birdy < 0 or birdy > HEIGHT or birdy == HEIGHT:
         gameoverflag = True

      if debug:
            pointbox = pg.draw.rect(screen, "black", pg.Rect((20, 0), (5, 300)))
      if debug == False:
            pointbox = pg.draw.rect(screen, "cyan", pg.Rect((20, 0), (5, 300)))
      bird = pg.draw.circle(screen, "yellow", [birdx, birdy], 10)
      pipe1 = pg.draw.rect(screen, "green", pg.Rect((pipe1x, pipe1y), (40, 100)))
      pipe2 = pg.draw.rect(screen, "green", pg.Rect((pipe2x, pipe2y), (40, 100)))
      pipe1leftover = pg.draw.rect(screen, "green", pg.Rect((pipe1x, pipe1y - 100), (40, 100)))
      pipe2leftover = pg.draw.rect(screen, "green", pg.Rect((pipe2x, pipe2y + 100), (40, 100)))
      pipe1top = pg.draw.rect(screen, "green", pg.Rect((pipe1x - 10, pipe1y + 100), (60, 20)))
      pipe2top = pg.draw.rect(screen, "green", pg.Rect((pipe2x - 10, pipe2y), (60, 20)))
      strpoints = str(points)
      strroundcount = str(roundcount)
      if points == 0 or points > 1:
         counter = gamefont.render('You have ' + strpoints + ' points', False, "white")
      if points == 1:
         counter = gamefont.render('You have ' + strpoints + ' point', False, "white")
      roundcounter = gamefont.render('Round ' + strroundcount, False, "white")
      screen.blit(counter, (5, 5))
      screen.blit(roundcounter, (5, 280))
      
      if gameoverflag:
            screen.fill("cyan")
            gameover = gamefont.render('GAME OVER. You died at', False, "white")
            gameover2 = gamefont.render('round ' + strroundcount + " with ", False, "white")
            gameover3 = gamefont.render(strpoints + " point(s)!", False, "white")
            gameover4 = gamefont.render("Enter name above! ", False, "white")
            screen.blit(gameover, (20, 110))
            screen.blit(gameover2, (20, 130))
            screen.blit(gameover3, (20, 150))
            screen.blit(gameover4, (60, 230))
            nameboxtext = gamefont.render(name, True, "white")
            namebox = pg.draw.rect(screen, "black", pg.Rect((100, 185), (100, 40)))
            nameboxoutline = pg.draw.rect(screen, "white", pg.Rect(100, 185, 100, 40), 2)
            screen.blit(nameboxtext, (105, 185))
            if name and donenaming:
               if points == 0 or points > 1:
                  highscore = name + " - Round " + str(roundcount) + ", " + str(points) + " points "
               if points == 1:
                  highscore = name + " - Round " + str(roundcount) + ", " + str(points) + " point "
               with open ('highscores.txt', 'a') as save:
                  save.write(str(highscore) + "\n")
               pg.time.delay(1500)
               run = False

      pg.display.flip()

quit()

