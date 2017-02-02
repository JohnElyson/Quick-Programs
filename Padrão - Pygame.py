import pygame,random,time
pygame.init()
Clock = pygame.time.Clock()
TamanhodaTela = (800,600)
Screen = pygame.display.set_mode(TamanhodaTela)
# Cores
BLACK = (0, 0, 0)
GRAY = (100,100,100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255,0,255)
GREEN = (0, 255, 0)
DARKGREEN = (0,100,0)
LIGHTGREEN = (100,255,0)
BLUE = (0, 0, 255)
DARKBLUE = (0,0,100)
LIGHTBLUE = (0,255,255)
YELLOW = (255, 255, 0)

# Variáveis de teste
while True:
    PosicaoMouse = pygame.mouse.get_pos()
    Clock.tick(30)
# Tela de testes
    Screen.fill(BLACK)
    pygame.draw.rect(Screen,WHITE,[125,100,25,25])
# Fim da Tela de testes
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            break
    #print pygame.mouse.get_pos()
    pygame.display.flip()
pygame.quit()
