import pygame,sys,random,time

pygame.init()
SURFACE=pygame.display.set_mode((640,480),pygame.SCALED)
FPSCLOCK=pygame.time.Clock()
pygame.display.set_caption("pymachine,son!")
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            SURFACE.fill((255,255,255))
            pygame.display.update()
            FPSCLOCK.tick(60)
if __name__=='__main__':
    main()