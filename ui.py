import pygame,math,os
pygame.init()

class Text():
    def __init__(self,text,size,x,y,win):
        self.img = pygame.font.SysFont("Arial",size).render(text,True,(222,222,222))
        self.box = self.img.get_rect()
        self.box.center = (x,y)
        self.win = win
    def render(self):
        self.win.blit(self.img,self.box)
    
#slider
class slider:
    def __init__(self):
        self.value =75
    
    def logic(self,x,y,width,height,color,win):
        self.win = win
        self.color = color
        self.width = width
        self.height = height
        self.mousepos = pygame.mouse.get_pos()
        self.touch = pygame.mouse.get_pressed()[0]
        
        self.frame = pygame.Rect(x-width/2,y-height/2,width,height)
        self.slider = pygame.Rect(self.frame.left+10,self.frame.top + 10,width-30,height-20)
        if self.touch and self.frame.collidepoint(self.mousepos) and self.value >= 75:
            self.value = self.mousepos[0]-self.slider.left
        if self.value < 75:
            self.value = 75
        self.ind = pygame.Rect(0,0,self.slider.h-15,self.slider.h-15)

    def render(self):
        if self.value > self.width-20:
           self.value = self.width-20
        if self.value < 20:
            self.value = 20
        self.slider.w = self.value
        self.ind.right = self.slider.right-7
        self.ind.centery = self.slider.centery
        
        pygame.draw.rect(self.win,(255,255,255),self.frame,border_radius=999)
        pygame.draw.rect(self.win,self.color,self.slider,border_radius=999)
        pygame.draw.ellipse(self.win,(255,255,255),self.ind)
        
class button:
    def __init__(self):
        self.clicked = False
        self.action = False
    def logic(self,x,y,width,height,color,win):
        self.win = win
        self.action = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_click = pygame.mouse.get_pressed()[0]
        self.color = color
        self.button = pygame.Rect(0,0,width,height)
        self.button.center = (x,y)
        if self.button.collidepoint(self.mouse_pos) and self.clicked == False and self.mouse_click:
            self.clicked = True
            self.action = True
        if not self.mouse_click:
            self.clicked = False
            
    def render(self):
        pygame.draw.rect(self.win,self.color,self.button,border_radius=25)

def main():
    run = True
    #Making Screen
    screen = pygame.display.get_desktop_sizes()[0]
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen[0]/2-(screen[0]/2-50),screen[1]/2-(screen[1]/2-50))
    win = pygame.display.set_mode((screen[0]-100,screen[1]-100),flags=pygame.RESIZABLE,vsync=1)

    #Change screen name and icon
    pygame.display.set_caption("Keyboard sound configuration")
    icon = pygame.image.load("icon3.png")
    pygame.display.set_icon(icon)

    #Slider here
    volume_slider = slider()

    #Button here
    launch = button()

    #Main code
    while run:
        w,h = pygame.display.get_window_size()
        win.fill((30,30,30))


        #text here
        inst = Text("Drag and drop your keyboard sound here :D",20,w/2,h/4,win)
        vol = Text(f'Volume: {math.floor(0.3278688525*(volume_slider.value-75))}',20,w/2,h/2.5,win)
        f = open("volume.txt","w")
        f.write(str(math.floor(0.3278688525*(volume_slider.value-75))))
        f.close()
        launch_text = Text("Launch app", 20,w/2,h/2,win)
        
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.DROPFILE:
                supported_file_type = ["mp3","wav","ogg"]
                if set(supported_file_type).intersection(str(event.file).split(".")):
                    is_import = Text("Import successful :D",20,w/2,h/2,win)
                    is_import.render()
                    file_name = str(event.file).split("\\")[-1]
                    os.system(f'copy "{str(event.file)}" "{os.getcwd()}"')
                    f = open("song_path.txt","w")
                    f.write(f"{os.getcwd()}\{file_name}")
                    f.close()
                    os.system("taskkill /im pyw.exe /t /f")
                    os.system("start main.pyw")

        #Slider setting
        volume_slider.logic(w/2,h/2.5,400,60,(66,135,245),win)

        #Button Logic
        launch.logic(w/2,h/2,120,40,(66,135,245),win)
        if launch.action:
            os.system("taskkill /im pyw.exe /t /f")
            os.system("start main.pyw")

        #Render
        volume_slider.render()
        inst.render()
        vol.render()
        launch.render()
        launch_text.render()
        pygame.display.flip()
main()