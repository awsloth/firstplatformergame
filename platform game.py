#Whole game loop
while 1:
    import pygame, sys, time, random, math
    from pygame.locals import *
    pygame.init()
    pygame.display.set_caption("Platform Game")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    #Images
    player1_image = pygame.image.load("stick.png").convert()
    player1_image2 = pygame.image.load("stick2.png").convert()
    player1_image = pygame.transform.scale(player1_image,(40,40))
    player1_image2 = pygame.transform.scale(player1_image2,(40,40))
    #Variables
    holding = 0
    jump = 0
    n = 0
    x = 18
    air = 0
    Game = "Menu"
    #Fonts
    font = pygame.font.SysFont("couriernew",120)
    font2 = pygame.font.SysFont("couriernew",60)
    font3 = pygame.font.SysFont("couriernew",20)
    #Creating player

    class Player:
        def __init__(self,x,y,ctrls,img):
            self.x = x
            self.y = y
            self.ctrls = ctrls
            self.img = img
            self.air = air
            self.direction = "Right"
            self.airtime = 0
            self.fallspeed = 5
            self.room = "Menu1"
            self.rucksack = 0
            self.sleeping_bag = 0
            self.coat = 0
            self.time = 0
            self.score = 0
            self.rucksackscore = 0
            self.sleeping_bagscore = 0
            self.coatscore = 0

        def move(self, height):
            self.y -= height

        def gravity(self):
            self.y += 5   
            
        def run(self):
            if pressed_keys[self.ctrls[1]]:
                self.x += 10
                self.direction = "Right"
                
            if pressed_keys[self.ctrls[2]]:
                self.x -= 10
                self.direction = "Left"
                
        def draw(self):
            if self.direction == "Right":
                screen.blit(self.img[0],(self.x,self.y))
            if self.direction == "Left":
                screen.blit(self.img[1],(self.x,self.y))
            


        def offscreen(self):
            #(Menu 1)Object detection
            if self.room == "Menu1":
                if self.x < 0:
                    self.x += 10
                if self.y > 560:
                    self.y -= 5
            
            #(Menu 2)Object detection
            if self.room == "Menu2":
                if self.x > 760:
                    self.x -= 10
                if self.y > 560:
                    self.y -= 5

            #(Room 1)Object detection
            if self.room == "Room1":
                if self.x > 760:
                    self.x -= 10
                if self.x < 0:
                    self.x += 10

                #all TOP hitboxes
                if (
                    (self.y > 540 and self.x < 150) or
                    (self.y > 510 and self.x > 100 and self.x < 300) or
                    (self.y > 410 and self.x > 310 and self.x < 400) or
                    (self.y > 310 and self.x > 460 and self.x < 750) or
                    (self.y > 220 and self.x > 240 and self.x < 400 and self.y < 260) or
                    (self.y > 180 and self.x > 180 and self.x < 340 and self.y < 230) or
                    (self.y > 100 and self.x > 150 and self.x < 210 and self.y < 120) or
                    (self.y > 50 and self.x < 190 and self.y < 100)
                    ):
                    self.y -= 5

                #all RIGHT hitboxes
                if (
                    (self.x < 300 and self.y > 510 and self.x > 120) or
                    (self.x < 400 and self.y > 410 and self.x > 320) or
                    (self.x < 750 and self.y > 310 and self.x > 470) or
                    (self.y < 280 and self.x < 400 and self.y > 220 and self.x > 380) or
                    (self.y < 240 and self.x < 340 and self.y > 180 and self.x > 180) or
                    (self.y < 200 and self.x < 210 and self.y > 100 and self.x > 150) or
                    (self.y < 200 and self.x < 190 and self.y > 50)
                    ):
                    self.x += 10
                    
                #all LEFT hitboxes
                if (
                    (self.x > 110 and self.y > 510 and self.x < 290) or
                    (self.x > 310 and self.y > 410 and self.x < 390) or
                    (self.x > 460 and self.y > 310 and self.x < 740)
                    ):
                    self.x -= 10

                #all BOTTOM hitboxes
                if self.x < 400 and self.y < 280 and self.y > 260:
                    self.y += 5

            #(Room 2)Object detection
            if self.room == "Room2":
                if self.x > 760 and self.y > 90:
                    self.x -= 10
                if self.x < 0:
                    self.x += 10

                #all TOP hitboxes
                if (
                    (self.y > 510 and self.x < 50) or
                    (self.y > 410 and self.x > 60 and self.x < 150) or
                    (self.y > 360 and self.x > 160) or
                    (self.y > 330 and self.x > 620) or
                    (self.y > 190 and self.x > 360 and self.x < 600 and self.y < 210) or
                    (self.y > 40 and self.x > 610 and self.y < 60)
                    ):
                    self.y -=5

                #all RIGHT hitboxes
                if (
                    (self.x < 50 and self.y > 510 and self.x > 0) or
                    (self.x < 150 and self.y > 410 and self.x > 100) or
                    (self.x < 600 and self.y > 190 and self.x > 550 and self.y < 250)
                    ):
                    self.x += 10
                    
                #all LEFT hitboxes
                if (
                    (self.x > 60 and self.y > 410 and self.x < 140) or
                    (self.x > 160 and self.y > 360 and self.x < 260) or
                    (self.x > 160 and self.y > 430 and self.x < 260) or
                    (self.x > 620 and self.y > 330 and self.x < 720) or
                    (self.x > 360 and self.y > 190 and self.x < 460 and self.y <  240) or
                    (self.x > 610 and self.y > 40 and self.x < 710 and self.y <  90)
                    ):
                    self.x -= 10

                #all BOTTOM hitboxes
                if ((self.x < 600 and self.y < 250 and self.y > 190 and self.x > 360) or
                    (self.y < 100 and self.y > 40 and self.x > 610)
                    ):
                    self.y += 5

                    

            #(Room 2b)Object detection
            if self.room == "Room2b":
                if self.x > 760:
                    self.x -= 10
                if self.x < 0 and self.y > 90:
                    self.x += 10

                #all TOP hitboxes
                if (
                    (self.y > 40 and self.x < 100 and self.y < 60) or
                    (self.y > 260 and self.x > 210 and self.x < 400 and self.y < 280) or
                    (self.y > 160 and self.x > 360 and self.x < 450 and self.y < 180) or
                    (self.y > 90 and self.x > 510 and self.y < 750 and self.y < 110)
                    ):
                    self.y -= 5

                #all RIGHT hitboxes
                if (
                    (self.x > 40 and self.y > 40 and self.x < 100 and self.y < 90) or
                    (self.x > 420 and self.y > 290 and self.x < 450 and self.y <  340) or
                    (self.x > 420 and self.y > 160 and self.x < 450 and self.y <  320)
                    ):
                    self.x += 10

                #all LEFT hitboxes
                if (
                    (self.x > 210 and self.y > 260 and self.x < 260 and self.y <  320 ) or
                    (self.x > 210 and self.y > 290 and self.x < 260 and self.y <  340 ) or
                    (self.x > 360 and self.y > 160 and self.x < 410 and self.y <  320 ) or
                    (self.x > 510 and self.y > 90 and self.x < 560 and self.y <  140 )
                    ):
                    self.x -= 10

            #(Room 3)Object detection
            if self.room == "Room3":
                if self.x > 760 and self.y > 170:
                    self.x-= 10
                if self.x < 0:
                    self.x += 10

                #all TOP hitboxes
                if (
                    (self.x > -40 and self.y > 510 and self.x < 200) or
                    (self.x > 310 and self.y > 360 and self.x < 600) or
                    (self.x > 510 and self.y > 210) or 
                    (self.x > 530 and self.y > 160)
                    ):
                    self.y -= 5
                


                # all RIGHT hitboxes
                if (self.y > 510 and self.x < 200):
                    self.x += 10

                #all LEFT hitboxes
                if (
                    (self.x > 310 and self.y > 360 and self.x < 360) or
                    (self.x > 510 and self.y > 210 and self.x < 560) or
                    (self.x > 530 and self.y > 160 and self.x < 580)
                    ):
                    self.x -= 10


            #(Room 3b)Object detection
            if self.room == "Room3b":
                if self.x > 760:
                    self.x -= 10
                if self.x < 0 and self.y > 190:
                    self.x += 10

                #all TOP hitboxes
                if (
                    (self.y > 210 and self.x < 100) or
                    (self.x > 60 and self.y > 410 and self.x < 600) or
                    (self.x > 410 and self.y > 360 and self.x < 600) or
                    (self.x > 560 and self.y > 210 and self.x < 700) or
                    (self.x > 660 and self.y > 510 and self.x < 800)
                    ):
                    self.y -= 5

                #all RIGHT hitboxes
                if (
                    (self.x > 40 and self.y > 210 and self.x < 100) or
                    (self.x > 640 and self.y > 210 and self.x < 700)
                    ):
                    self.x += 10

                #all LEFT hitoxes
                if (
                    (self.x > 410 and self.y > 360 and self.x < 460) or
                    (self.x > 560 and self.y > 210 and self.x < 610)
                    ):
                    self.x -= 10
                    

                
                                    

        def touched(self):
            if self.room == "Menu1" or self.room == "Menu2":
                if self.y == 560:
                    self.air = 0
                else:
                    self.air = 1

            if self.room == "Room1":
                if (
                    (self.y == 540 and self.x < 150) or
                    (self.y == 510 and self.x > 110 and self.x < 300) or
                    (self.y == 410 and self.x > 310 and self.x < 400) or
                    (self.y == 310 and self.x > 460 and self.x < 750) or
                    (self.y == 220 and self.x > 240 and self.x < 400 and self.y < 290) or
                    (self.y == 180 and self.x > 180 and self.x < 340 and self.y < 230) or
                    (self.y == 160 and self.x > 100 and self.x < 160 and self.y < 230) or
                    (self.y == 100 and self.x > 150 and self.x < 210 and self.y < 120) or
                    (self.y == 50 and self.x < 190 and self.y < 100)
                    ):
                    self.air = 0

                else:
                    self.air = 1

            if self.room == "Room2":

                if (
                    (self.y == 510 and self.x < 50) or
                    (self.y == 410 and self.x > 60 and self.x < 150) or
                    (self.y == 360 and self.x > 160) or
                    (self.y == 330 and self.x > 620) or
                    (self.y == 190 and self.x > 360 and self.x < 600 and self.y < 210) or
                    (self.y == 40 and self.x > 610 and self.y < 60)
                    ):
                    self.air = 0

                else:
                    self.air = 1

            if self.room == "Room2b":

                if (
                    (self.y == 40 and self.x < 100 and self.y < 60) or
                    (self.y == 260 and self.x > 210 and self.x < 400 and self.y < 280) or
                    (self.y == 160 and self.x > 360 and self.x < 450 and self.y < 180) or
                    (self.y == 90 and self.x > 510 and self.y < 750 and self.y < 110)
                    ):
                    self.air = 0

                else:
                    self.air = 1

            if self.room == "Room3":

                if (
                    (self.x > -40 and self.y > 500 and self.x < 200) or
                    (self.x > 310 and self.y > 350 and self.x < 600) or
                    (self.x > 510 and self.y > 200) or 
                    (self.x > 530 and self.y > 150)
                    ):
                    self.air = 0

                else:
                    self.air = 1

            if self.room == "Room3b":

                if (
                    (self.y > 200 and self.x < 100) or
                    (self.x > 60 and self.y > 400 and self.x < 600) or
                    (self.x > 410 and self.y > 350 and self.x < 600) or
                    (self.x > 560 and self.y > 200 and self.x < 700) or
                    (self.x > 660 and self.y > 500)
                    ):
                    self.air = 0

                else:
                    self.air =1
                    

        def dead(self):
            if self.y > 570:
                if self.room == "Room1":
                    self.x = 0
                    self.y = 530
                if self.room == "Room2":
                    self.x = 0
                    self.y = 500
                if self.room == "Room2b":
                    self.x = 0
                    self.y = 40
                if self.room == "Room3":
                    self.x = 0
                    self.y = 500
                if self.room == "Room3b":
                    self.x = 0
                    self.y = 210

        def switchscreen(self):
            if self.room == "Menu1":
                if self.x > 800:
                    self.room = "Menu2"
                    self.x = 0
                    self.y = 560
            if self.room == "Menu2":
                if self.x < 0:
                    self.room = "Menu1"
                    self.x = 800
                    self.y = 560

            if self.room == "Room2":
                if self.x > 800:
                    self.room = "Room2b"
                    self.x = 0
                    self.y = 40

            if self.room == "Room2b":
                if self.x < 0:
                    self.room = "Room2"
                    self.x = 800
                    self.y = 40

            if self.room == "Room3":
                if self.x > 800:
                    self.room = "Room3b"
                    self.x = 0
                    self.y = 210

            if self.room == "Room3b":
                if self.x < 0:
                    self.room = "Room3"
                    self.x = 800
                    self.y = 210

        def enterdoor(self):
            if self.room == "Menu1":
                if (self.y > 400 and self.x > 260 and self.x < 400) and pressed_keys[self.ctrls[0]]:
                    self.room = "Room1"
                    self.x = 0
                    self.y = 520
                    self.time = time.time()

                if (self.y > 400 and self.x > 470 and self.x < 590) and pressed_keys[self.ctrls[0]]:
                    self.room = "Room2"
                    self.x = 0
                    self.y = 500
                    self.time = time.time()

                if (self.y > 400 and self.x > 580 and self.x < 7800) and pressed_keys[self.ctrls[0]]:
                    self.room = "Room3"
                    self.x = 0
                    self.y = 500
                    self.time = time.time()

        def touchitem(self):
            if self.room == "Room1":
                if self.y < 100 and self.x < 10 and self.y > 40:
                    self.room = "Menu1"
                    self.x = 0
                    self.y = 560
                    if self.rucksack == 0:
                        self.score += 100-round((time.time()-self.time),1)
                        self.rucksackscore = 100-round((time.time()-self.time),1)
                    elif self.rucksackscore < 100-round((time.time()-self.time),1):
                        self.score -= self.rucksackscore
                        self.score += 100-round((time.time()-self.time),1)
                    self.rucksack = 1

            if self.room == "Room2b":
                if self.y < 100 and self.x > 700 and self.y > 40:
                    self.room = "Menu1"
                    self.x = 0
                    self.y = 560
                    if self.sleeping_bag == 0:
                        self.score += 100-round((time.time()-self.time),1)
                        self.sleeping_bagscore = 100-round((time.time()-self.time),1)
                    elif self.sleeping_bagscore < 100-round((time.time()-self.time),1):
                        self.score -= self.sleeping_bagscore
                        self.score += 100-round((time.time()-self.time),1)
                    self.sleeping_bag = 1


            if self.room == "Room3b":
                if self.y > 500 and self.x > 700:
                    self.room = "Menu1"
                    self.x = 0
                    self.y = 560
                    if self.coat == 0:
                        self.score += 100-round((time.time()-self.time),1)
                        self.coatscore = 100-round((time.time()-self.time),1)
                    elif self.coatscore < 100-round((time.time()-self.time),1):
                        self.score -= self.coatscore
                        self.score += 100-round((time.time()-self.time),1)
                    self.coat = 1


    class Item:
        def __init__(self,x,y,item):
            self.x = x
            self.y = y
            self.item = item
            self.colour1 = 200,200,200
            self.colour2 = 200,200,200
            self.colour3 = 200,200,200

        def draw(self):
            if player.room == "Room1" and self.item == 1:
                pygame.draw.rect(screen,(150,150,150),(self.x,self.y,30,30))
                
            if player.room == "Room2b" and self.item == 2:
                pygame.draw.rect(screen,(150,150,150),(self.x,self.y,30,30))

            if player.room == "Room3b" and self.item == 3:
                pygame.draw.rect(screen,(150,150,150),(self.x,self.y,30,30))

            if self.item == 1:
                pygame.draw.rect(screen,(self.colour1),(660,20,30,30))
                
            if self.item == 2:
                pygame.draw.rect(screen,(self.colour2),(710,20,30,30))

            if self.item == 3:
                pygame.draw.rect(screen,(self.colour3),(760,20,30,30))

            if player.rucksack == 1:
                self.colour1 = 100,100,100

            if player.sleeping_bag == 1:
                self.colour2 = 100,100,100

            if player.coat == 1:
                self.colour3 = 100,100,100

    class Door:
        def __init__(self,x,room):
            self.x = x
            self.room = room

        def draw(self):
            if self.room == 1 and player.room == "Menu1":
                pygame.draw.rect(screen,(100,0,0),(self.x,400,100,200))

            if self.room == 2 and player.room == "Menu2":
                pygame.draw.rect(screen,(100,0,0),(self.x,400,100,200))

    class Testline:
        def __init__(self,x,y,width,height,room):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.room = room

        def draw(self):
            if player.room == "Room1" and self.room == 1:
                pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))

            if player.room == "Room2" and self.room == 21:
                pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))

            if player.room == "Room2b" and self.room == 22:
                pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))

            if player.room == "Room3" and self.room == 31:
                pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))

            if player.room == "Room3b" and self.room == 32:
                pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height))
                

    #Finishing classes
    player = Player(0,560,(K_UP,K_RIGHT,K_LEFT),(player1_image,player1_image2))
    testlines = ((Testline(0,580,150,20,1)),(Testline(150,550,150,50,1)),(Testline(350,450,50,150,1)),(Testline(500,350,250,250,1)),
                 (Testline(300,260,100,20,1)),(Testline(210,220,130,60,1)),(Testline(190,140,20,140,1)),(Testline(0,90,190,190,1)),
                 (Testline(0,550,50,50,21)),(Testline(100,450,50,150,21)),(Testline(200,400,600,70,21)),(Testline(200,470,50,130,21)),
                 (Testline(750,470,50,130,21)),(Testline(660,370,130,30,21)),(Testline(400,230,200,20,21)),(Testline(650,80,150,20,21)),
                 (Testline(0,80,100,20,22)),(Testline(250,300,150,30,22)),(Testline(250,330,200,20,22)),(Testline(400,200,50,130,22)),(Testline(550,130,240,20,22)),
                 (Testline(0,550,200,100,31)),(Testline(350,450,50,150,31)),(Testline(350,400,250,50,31)),(Testline(550,450,50,150,31)),
                 (Testline(550,250,50,150,31)),(Testline(570,200,230,50,31)),(Testline(750,250,50,150,31)),(Testline(750,400,50,200,31)),
                 (Testline(0,250,100,350,32)),(Testline(100,450,500,150,32)),(Testline(450,400,150,50,32)),(Testline(600,250,100,350,32)),(Testline(700,550,100,50,32))
                 )
    doors = (Door(300,1)),(Door(500,1)),(Door(700,1)),(Door(350,2))
    items = (Item(10,50,1)),(Item(740,90,2)),(Item(760,510,3))

    #Menu
    while Game == "Menu":
        clock.tick(60)

        screen.fill((255,255,255))

        #Add exit button
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()

        txt = font.render("Menu",True,(0,0,0))

        txt_x = 400-txt.get_width()/2
        txt_y = 120-txt.get_height()/2

        screen.blit(txt,(txt_x,txt_y))

        txt2 = font2.render("PLAY",True,(0,0,0))

        txt2_x = 260-txt2.get_width()/2
        txt2_y = 460-txt2.get_height()/2

        pygame.draw.rect(screen,(0,0,0),(260-txt2.get_width()/2,450-txt2.get_height()/2,txt2.get_width()+40,txt2.get_height()+20))

        clickable_rect = pygame.draw.rect(screen,(255,255,255),(270-txt2.get_width()/2,460-txt2.get_height()/2,txt2.get_width()+20,txt2.get_height()))

        screen.blit(txt2,(txt2_x+20,txt2_y))

        if pygame.mouse.get_pressed()[0] and clickable_rect.collidepoint(pygame.mouse.get_pos()):
            Game = "Play"

        txt3 = font3.render("INSTRUCTIONS",True,(0,0,0))

        txt3_x = 550-txt3.get_width()/2
        txt3_y = 460-txt3.get_height()/2

        pygame.draw.rect(screen,(0,0,0),(550-txt3.get_width()/2,450-txt3.get_height()/2,txt3.get_width()+20,txt3.get_height()+20))

        clickable_rect2 = pygame.draw.rect(screen,(255,255,255),(555-txt3.get_width()/2,455-txt3.get_height()/2,txt3.get_width()+10,txt3.get_height()+10))

        screen.blit(txt3,(txt3_x+7,txt3_y))

        if pygame.mouse.get_pressed()[0] and clickable_rect2.collidepoint(pygame.mouse.get_pos()):
            Game = "Instructions"

        pygame.display.update()

    #Instructions
    while Game == "Instructions":
        clock.tick(60)

        #Add exit button and key detection
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()

        #Set background
        screen.fill((255,255,255))

        txt = font3.render("INSTRUCTIONS",True,(0,0,0))

        screen.blit(txt,(10,0))

        txt2 = font3.render("Press the Left and Right arrow keys to move.",True,(0,0,0))

        screen.blit(txt2,(10,100))

        txt3 = font3.render("Press the Up arrow to enter doors.",True,(0,0,0))

        screen.blit(txt3,(10,200))

        txt4 = font3.render("Press the Space Bar to jump.",True,(0,0,0))

        screen.blit(txt4,(10,300))

        

        pygame.display.update()

        

        

    #Game functions
    while Game == "Play":
        clock.tick(60)

        #Add exit button and key detection
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()

        #Set background
        screen.fill((255,255,255))

        
        #Jumping
        if player.air == 0:
            if not player.room == "Menu1" or not player.room == "Menu2":
                if pressed_keys[K_SPACE]:
                    if holding == 0:
                        while n < 20:
                            screen.fill((255,255,255))
                            player.move(x)
                            player.run()
                            player.offscreen()
                            holding = 1
                            time.sleep(0.01)
                            for item in items:
                                item.draw()
                            if player.room == "Menu1" or player.room == "Menu2":
                                for door in doors:
                                    door.draw()
                            for testline in testlines:
                                testline.draw()
                            player.draw()
                            n+=1
                            x-=1
                            player.air = 1
                            player.timer = int(time.time()-player.time)
                            txt = font3.render("Time: "+str(int((time.time()-player.time)*10)/10.),True,(0,0,0))
                            if not (player.room == "Menu1" or player.room == "Menu2"):
                                screen.blit(txt,(0,0))
                            pygame.display.update()
                            
                        time.sleep(0.01)
                else:
                    holding = 0
                    n=0
                    x=18

        if player.room == "Menu1" or player.room == "Menu2":
            for door in doors:
                door.draw()
                                 
        for item in items:
            item.draw()

        #Detect player touching platform or ground
        player.touched()

        #Running player functions
        player.gravity()
                
        player.run()

        player.offscreen()

        player.dead()

        player.switchscreen()

        player.enterdoor()

        player.touchitem()

        if pressed_keys[K_i]:
            print(player.x,player.y)
            if player.rucksack == 1:
                print("rucksack")
            if player.sleeping_bag == 1:
                print("sleeping bag")

        if pressed_keys[K_o]:
            player.rucksack = 1
            player.sleeping_bag = 1
            player.coat = 1

        for testline in testlines:
            testline.draw()

        #Display player over everything
        player.draw()

        if (
            player.room == "Menu2" and (player.y > 400 and player.x > 310 and player.x < 450) and pressed_keys[K_UP] and
            (player.rucksack == 1 and player.coat == 1 and player.sleeping_bag == 1)
            ):
            Game = "End"

        if pressed_keys[K_e]:
            player.room = "Menu1"
            player.x = 0
            player.y = 560

        txt = font3.render("Time: "+str(int((time.time()-player.time)*10)/10.),True,(0,0,0))

        if not (player.room == "Menu1" or player.room == "Menu2"):
            screen.blit(txt,(0,0))

        txt2 = font3.render("Score: "+str(int((player.score)*10)/10.),True,(0,0,0))

        if player.room == "Menu1" or player.room == "Menu2":
            screen.blit(txt2,(0,0))

        player.timer = int(time.time()-player.time)

        #Diplay everything
        pygame.display.update()


    #End of game
    while Game == "End":
        
        #Add exit button and key detection
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()

        screen.fill((255,255,255,))
        
        txt2 = font3.render("You have completed the game",True,(0,0,0))
        txt3 = font2.render("Menu",True,(0,0,0))
        txt4 = font3.render("Your score is:",True,(0,0,0))
        txt5 = font3.render(str(player.score),True,(0,0,0))

        txt3_x = 630-txt3.get_width()/2
        txt3_y = 450-txt3.get_height()/2

        pygame.draw.rect(screen,(0,0,0),(610-txt3.get_width()/2,440-txt3.get_height()/2,txt3.get_width()+40,txt3.get_height()+20))

        pygame.draw.rect(screen,(255,255,255),(620-txt3.get_width()/2,450-txt3.get_height()/2,txt3.get_width()+20,txt3.get_height()))

        clickable_rect = pygame.draw.rect(screen,(255,255,255),(620-txt3.get_width()/2,450-txt3.get_height()/2,txt3.get_width()+20,txt3.get_height()))

        screen.blit(txt2,(240,200))
        screen.blit(txt3,(txt3_x,txt3_y))
        screen.blit(txt4,(100,400))
        screen.blit(txt5,(270,400))

        if pygame.mouse.get_pressed()[0] and clickable_rect.collidepoint(pygame.mouse.get_pos()):
            Game = "Menu"

        pygame.display.update()
         
            
