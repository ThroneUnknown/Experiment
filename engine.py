import tcod

from inputhandler import InputHandler


# Engine class that houses the main game loop
class Engine:
    
    def __init__(self, console, context, gui):
        self.console = console
        self.context = context
        self.gui = gui
        self.inputhandler = InputHandler(gui, self)
        self.mode = 0

    # The run all functions (input handling, gui, etc) necessary for the main game loop"
    def game_loop(self):
        console = self.console
        context = self.context

        self.gui.homepage()

        # Whole game loop consisting of changing screens and more
        while True:
            
            self.inputhandler.handle()
            if self.mode == 0:
                self.gui.homepage()
                self.gui.bs_screen = 1
            elif self.mode == 1:
                self.gui.sector_builder()
            context.present(console)
            
