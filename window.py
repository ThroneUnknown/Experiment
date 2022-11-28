# Create a box that has an arm and other properties
class Window:

    def __init__(self, loc, size, console, title='', clear=True, fg=None, bg=None, bg_blend=1, decor="┌─┐│ │└─┘"):
        self.loc = loc
        self.size = size
        self.title = title
        self.clear = clear
        self.fg = fg
        self.bg = bg
        self.bg_blend=1
        self.decoration = decor
        self.console = console

    def display(self):
        self.console.draw_frame(self.loc[0], self.loc[1], self.size[0], self.size[1],
            title=self.title,
            clear=self.clear,
            fg=self.fg,
            bg=self.bg,
            bg_blend=self.bg_blend,
            decoration=self.decoration)

