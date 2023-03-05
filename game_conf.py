from dataclasses import dataclass
import archive_tests.logthis as logthis    
import pygame




@dataclass
class Game_config:
    running: bool = True
    display_width: int = 1200
    display_height: int = 600
    game_display = pygame.display.set_mode((display_width, display_height))
    white: tuple = (255,255,255)
    bg_color = white
    current_tick: int = 50
    ticks_per_day = 1000
    clock=pygame.time.Clock()
    clock.tick(.5)
    pygame.display.set_caption("clockmaker")


    def increment_tick(self):
        msg = "Current Tick: " + str(self.current_tick + 1)
        logthis.logger.info(msg)
        self.clock.tick(.5)
        self.current_tick = self.current_tick + 1


    def get_bg_color(self):
    
        def get_hund(m):
            n = str(m)

            if len(n) <= 2:
                h = 0
            else:
                h = n[-3]
            return h
        
        n = int(get_hund(self.current_tick))

        def wtf(n):

            if n == 0:  return (25,60,90)
            elif n == 1 or n == 9: return (70,94,104)
            elif n == 2 or n == 8: return (115,128,118)
            elif n == 3 or n == 7: return (160,162,132)
            elif n == 4 or n == 6: return (205,196,146)
            elif n == 5: return (250,230,160)
                
        return wtf(n)
    

    def start_game(self):
        self.running = True
        pygame.init()



g = Game_config()
g.start_game()

