from building import Building, buildings
from window import Window


BASE_FG = (125,39,0)
BASE_BG = (22,22,22)
CANVAS_BG = (35,35,35)
DARKWHITE = (200,200,200)
BRIGHTWHITE = (255,255,255)
SELECTED = (48,48,48)


# A function returning a string of a given char for a given length.
def hline(char, length):
    return "".join([char for x in range(length)])


# A function that returns a list of all points in an area
def point_area(start, dimensions):
    all_points = []
    for y in range(dimensions[1]):  # Y coordinate
        for x in range(dimensions[0]):  # X coordinate
            all_points.append([start[0]+x, start[1]+y])
    return all_points


# Graphical user interface function that produces all graphics used in the game
class Gui:
    
    def __init__(self, console, context):
        self.console = console
        self.context = context
        self.locations = []
        self.sector_builder_window = Window([6,4], [110,60], self.console, decor=("╔═╗║ ║╚═╝"))
        self.bs_screen = 1  # bs stands for buildings screen
        self.bs_filter = "F"  # "" is for nothing, 
        self.hover = ""  # Mouse selected place
        self.select = ""
        self.selection = {}  # A dictionary where each key is a hover value (see above) and each value is a list of points that set such key

    def homepage(self):
        # Basic homescreen with color and orange bar
        self.console.clear(fg=[121,35,0], bg=[22,22,22])
        for i in range(68):
            self.console.print(25, i, "│", BASE_FG, BASE_BG)

    # Build a sector using a new window
    def sector_builder(self, engine):
        # Set up a window to be displayed when editing/building a sector
        bar_size = 15  # Height of the bar in which buildings are selected
        selection_x = 25  # X value of selection of building genre bar
        self.sector_builder_window.display()

        # General titles across the page
        for i in range(58):
            self.console.print(99, i+5, "│", BASE_FG, BASE_BG)
        self.console.print(101, 5, "ALL SECTORS", BASE_FG, BASE_BG)
        self.console.print(42, 5, "──             ──", (150,150,150), BASE_BG)
        self.console.print(44, 5, "SECTOR EDITOR", BASE_FG, BASE_BG)

        # X button to close window
        self.selection["x"] = point_area([113, 4], [3, 3])
        self.console.print(113, 4, "╤═╗", BASE_FG, BASE_BG)
        self.console.print(113, 5, "│ ║", BASE_FG, BASE_BG)
        self.console.print(113, 6, "└─╢", BASE_FG, BASE_BG)

        # Hovering x button
        if self.hover == "x":
            self.console.print(114, 5, "x", BRIGHTWHITE, SELECTED)
        else:
            self.console.print(114, 5, "x", DARKWHITE, BASE_BG)
        
        # General category information
        catshorts = ["F", "R", "T", "E"]
        categories = ["Filter All", "Residential", "Retail", "Entertainment"]
        cat_colors = [BASE_BG, (104,0,0), (24,104,0), (0,18,134)]  # Respective color for each category of building
        
        # MOUSE SELECTION
        if self.select in catshorts:
            self.bs_filter = self.select
        elif self.select == "+" or self.select == "-":
            self.bs_screen *= -1
        elif self.select == "x":
            self.bs_screen = 1
            engine.mode = 0
        self.select = ""
        
        # Show or hide the building selection screen
        if self.bs_screen == 1:
            self.console.print(7, 63-bar_size, hline("─", 92), BASE_FG, BASE_BG)
            self.console.print(selection_x+1, 63-bar_size, "Building Selection", DARKWHITE, BASE_BG)
            self.console.print(selection_x, 63-bar_size, "┬", BASE_FG, BASE_BG)  # Selection bar line
            for i in range(55-bar_size): # Canvas screen
                self.console.print(8, 7+i, hline(" ", 90), BASE_FG, CANVAS_BG)
            self.console.print(8, 62-bar_size, hline(" ", 90), BASE_FG, BASE_BG)  # Normal bg screen
            for i in range(bar_size-1):
                self.console.print(8, 64-bar_size+i, hline(" ", 90), BASE_FG, BASE_BG)
            for i in range(bar_size-1):
                self.console.print(selection_x, 64-bar_size+i, "│", BASE_FG, BASE_BG)

            # Hovering of the [-] button
            self.selection["-"] = point_area([90,63-bar_size], [3,1])
            
            # Print [-] button either normal or hovered
            if self.hover == "-":
                self.console.print(90, 63-bar_size, "[-]", DARKWHITE, SELECTED)
            else:
                self.console.print(90, 63-bar_size, "[-]", DARKWHITE, BASE_BG)
            
            # List out all categories correctly on the right
            self.console.print(7, 65-bar_size, "[F] Filter All", DARKWHITE, BASE_BG)
            for i in range(len(categories)):
                self.console.print(7, 65+i-bar_size, "[ ] " + categories[i], DARKWHITE, BASE_BG)
                self.console.print(8, 65+i-bar_size, catshorts[i], DARKWHITE, cat_colors[i])
                self.selection[catshorts[i]] = [[7+x, 65+i-bar_size] for x in range(selection_x-7)]
                self.selection[catshorts[i]] = point_area([7,65+i-bar_size], [selection_x-7,1])
            
            # Place buildings in the building bar at the bottom based on filter and highlight selected category
            dbs = [Building(key, buildings[key][3], buildings[key], [0,0], 0) for key in buildings.keys() if buildings[key][3] == categories[catshorts.index(self.bs_filter)]]  # Display buildings
            if self.bs_filter == "F":
                dbs = [Building(key, buildings[key][3], buildings[key], [0,0], 0) for key in buildings.keys()]  # Display buildings
            self.console.print(11, 65-bar_size+catshorts.index(self.bs_filter), categories[catshorts.index(self.bs_filter)], BRIGHTWHITE, BASE_BG)
            self.console.print(8, 65-bar_size+catshorts.index(self.bs_filter), self.bs_filter, BRIGHTWHITE, cat_colors[catshorts.index(self.bs_filter)])
            
            # Color background different over selected filter
            if self.hover in catshorts:
                index = catshorts.index(self.hover)
                if self.bs_filter == self.hover:
                    fg_color = BRIGHTWHITE
                else:
                    fg_color = DARKWHITE
                self.console.print(7, 65-bar_size+index, "[ ] " + categories[index] + hline(" ", selection_x-11 - len(categories[index])), fg_color, SELECTED)
                self.console.print(8, 65-bar_size+index, catshorts[index], fg_color, cat_colors[index])
            start = [selection_x+1, 65-bar_size]
            for b in dbs:  # Display each of the display buildings next to each other in the bar
                b.display(start, self.console)
                # self.console.print(start[0], start[1]-1, b.name, DARKWHITE, BASE_BG)
                start[0] += len(b.entry[2][0][0]) + 5
                
        else:  # If the building bar is minimized this shows
            self.console.print(90, 62, "[+]", DARKWHITE, BASE_BG)
            for i in range(54):  # Canvas screen
                self.console.print(8, 7+i, hline(" ", 90), BASE_FG, CANVAS_BG)
                
            # Hovering of the [+] button
            self.selection["+"] = point_area([90,62], [3,1])
            
            # Print [+] button either normal or hovered
            if self.hover == "+":
                self.console.print(90, 62, "[+]", DARKWHITE, SELECTED)
            else:
                self.console.print(90, 62, "[+]", DARKWHITE, BASE_BG)

