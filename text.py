import pygame
import sys
  
pygame.init()
  
clock = pygame.time.Clock()
  
screen = pygame.display.set_mode([600, 500])
  
base_font = pygame.font.Font(None, 32)

rects = [(40, 200, 140, 32), (40, 264, 140, 32), (40, 328,140,32)]
rects_delete = [(0, 200, 32, 32), (0, 264, 32, 32), (0, 328,32,32)]
user_texts = {"name":"", "first_name":"", "siret":"", }
inputs=[]
deletes=[]
for i in rects:
    inputs.append(pygame.Rect(i))
for i in rects_delete:
    deletes.append(pygame.Rect(i))

color_active = pygame.Color('lightskyblue3')

color_passive = pygame.Color('chartreuse4')
color = color_passive
  
active = [False, False, False]
  
def delete_txt(i):
    change_line(0, "")

def change_line(i, text):
    lines = open("data", 'r').readlines()
    lines[i] = text
    print(lines)
    out = open("data", 'w')
    out.writelines(lines)
    out.close()
    
def read_line(i):
    lines = open("data", 'r').readlines()
    return lines[0]
print(read_line(0))
change_line(0, read_line(0)[:-1])
while True:
    for event in pygame.event.get():
  
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(deletes)):
                if deletes[i].collidepoint(event.pos):
                    delete_txt(i)
                
            for i in range(len(inputs)):
                active = [False, False, False]
                print(active)
                if inputs[i].collidepoint(event.pos):
                    active[i]=True
                    break
                print(active)
                
        if event.type == pygame.KEYDOWN:
            for i in range(len(active)):
                if active[i]:
                    if event.key == pygame.K_BACKSPACE:
                        change_line(i, read_line(i)[:-1])
                    else:
                        change_line(i, read_line(i)+event.unicode)
    screen.fill((0, 0, 0))
    
    def draw_rects():
        for i in range(len(inputs)):
            pygame.draw.rect(screen, color_active if active[i] else color_passive, inputs[i])
            text_surface = base_font.render(read_line(i), True, (255, 255, 255))
            screen.blit(text_surface, (inputs[i].x+5, inputs[i].y+5))
            inputs[i].w = max(100, text_surface.get_width()+10)
            
        for i in range(len(deletes)):
            pygame.draw.rect(screen, pygame.Color('red'), deletes[i])
    draw_rects()
      
    pygame.display.flip()
      
    clock.tick(60)