from dataclasses import dataclass

import logthis




@dataclass
class World:

    current_tick: int = 50

    def increment_tick(self):
        msg = "current tick: ", self.current_tick + 1
        logthis.logger.debug(msg)
        self.current_tick = self.current_tick + 1


    def get_bg_color(self):
        logthis.logger.debug("get_bg_color")
        
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



