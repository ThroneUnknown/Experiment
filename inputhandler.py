import tcod


class InputHandler:
    
    def __init__(self, gui, engine):
        self.gui = gui
        self.engine = engine

    def handle(self):
        for event in tcod.event.wait():
            match event:
                case tcod.event.Quit():
                    raise SystemExit()
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_q:
                    # To be removed later, ends program
                    raise SystemExit()
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_1:
                    # Toggles sector building screen
                    if self.engine.mode == 0:
                        self.engine.mode = 1
                    elif self.engine.mode == 1:
                        self.engine.mode = 0
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_ESCAPE:
                    # Returns to homescreen
                    self.engine.mode = 0
                    self.gui.bs_screen = 1
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_s:
                    # Toggles building bar in building screen
                    if self.engine.mode == 1:
                        self.gui.bs_screen *= -1
                        
                # Building screen building bar filters
                # Does NOT reset when going in/out of building bar or building screen
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_f:
                    # Toggles filter all in building screen
                    if self.engine.mode == 1:
                        self.gui.bs_filter = 0
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_r:
                    # Toggles residential filter in building screen
                    if self.engine.mode == 1:
                        self.gui.bs_filter = 1
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_t:
                    # Toggles retail filter in building screen
                    if self.engine.mode == 1:
                        self.gui.bs_filter = 2
                case tcod.event.KeyDown(sym=sym) if sym == tcod.event.K_e:
                    # Toggles entertainment filter in building screen
                    if self.engine.mode == 1:
                        self.gui.bs_filter = 3
