from building import Building, buildings
from window import Window


BASE_FG = (125,39,0)
BASE_BG = (22,22,22)
CANVAS_BG = (35,35,35)
DARKWHITE = (220,220,220)
BRIGHTWHITE = (255,255,255)


# A function returning a string of a given char for a given length.
def hline(char, length):
    return "".join([char for x in range(length)])


# Graphical user interface function that produces all graphics used in the game
class Gui:
    
    def __init__(self, console, context):
        self.console = console
        self.context = context
        self.locations = []
        self.sector_builder_window = Window([6,4], [110,60], self.console, decor=("╔═╗║ ║╚═╝"))
        self.bs_screen = 1
        self.bs_filter = 1  # 0 is all, after this each corresponds to the "categories" list

    def homepage(self):
        # Basic homescreen with color and orange bar
        self.console.clear(fg=[121,35,0], bg=[22,22,22])
        for i in range(68):
            self.console.print(25, i, "│", BASE_FG, BASE_BG)

    # Build a sector using a new window
    def sector_builder(self):
        # Set up a window to be displayed when editing/building a sector
        bar_size = 15  # Height of the bar in which buildings are selected
        selection_x = 25  # X value of selection of building genre bar
        self.sector_builder_window.display()
        for i in range(58):
            self.console.print(99, i+5, "│", BASE_FG, BASE_BG)
        self.console.print(102, 5, "ALL SECTORS", BASE_FG, BASE_BG)
        self.console.print(42, 5, "──             ──", (150,150,150), BASE_BG)
        self.console.print(44, 5, "SECTOR EDITOR", BASE_FG, BASE_BG)

        # Show or hide the building selection screen
        if self.bs_screen == 1:
            self.console.print(7, 63-bar_size, hline("─", 92), BASE_FG, BASE_BG)
            self.console.print(90, 63-bar_size, "[-]", DARKWHITE, BASE_BG)
            self.console.print(selection_x+1, 63-bar_size, "Building Selection", DARKWHITE, BASE_BG)
            self.console.print(selection_x, 63-bar_size, "┬", BASE_FG, BASE_BG)  # Selection bar line
            for i in range(55-bar_size): # Canvas screen
                self.console.print(8, 7+i, hline(" ", 90), BASE_FG, CANVAS_BG)
            self.console.print(8, 62-bar_size, hline(" ", 90), BASE_FG, BASE_BG)  # Normal bg screen
            for i in range(bar_size-1):
                self.console.print(8, 64-bar_size+i, hline(" ", 90), BASE_FG, BASE_BG)
            for i in range(bar_size-1):
                self.console.print(selection_x, 64-bar_size+i, "│", BASE_FG, BASE_BG)

            # List out all the categories of buildings on the left
            catshorts = ["R", "T", "E"]
            categories = ["Residential", "Retail", "Entertainment"]
            cat_colors = [(104,0,0), (24,104,0), (0,18,134)]  # Respective color for each category of building
            self.console.print(7, 64-bar_size, "[F] Filter All", DARKWHITE, BASE_BG)
            for i in range(len(categories)):
                self.console.print(7, 66+i-bar_size, "[ ] " + categories[i], DARKWHITE, BASE_BG)
                self.console.print(8, 66+i-bar_size, catshorts[i], DARKWHITE, cat_colors[i])

            # Place buildings in the building bar at the bottom based on filter and highlight selected category
            start = [selection_x+1, 65-bar_size]
            if self.bs_filter == 0:
                dbs = [Building(key, buildings[key][3], buildings[key], [0,0], 0) for key in buildings.keys()]
                self.console.print(7, 64-bar_size, "[F] Filter All", BRIGHTWHITE, BASE_BG)
            else:
                dbs = [Building(key, buildings[key][3], buildings[key], [0,0], 0) for key in buildings.keys() if buildings[key][3] == categories[self.bs_filter-1]]
                self.console.print(11, 66-bar_size+self.bs_filter-1, categories[self.bs_filter-1], BRIGHTWHITE, BASE_BG)
            
            for b in dbs:  # Display each of the display buildings next to each other in the bar
                b.display(start, self.console)
                # self.console.print(start[0], start[1]-1, b.name, DARKWHITE, BASE_BG)
                start[0] += len(b.entry[2][0][0]) + 5
        else:
            self.console.print(90, 62, "[+]", DARKWHITE, BASE_BG)
            for i in range(54):  # Canvas screen
                self.console.print(8, 7+i, hline(" ", 90), BASE_FG, CANVAS_BG)

