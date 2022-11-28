import gui


# Decode building file into a dictionary
def unpack_buildings():
    # Access file and format appropriatly
    with open("buildings.txt", encoding="utf-8") as f:
        file = f.read().split("\n")
    # Loop through file and add to dictionary
    buildings = {}
    fg = bg = dirs = []
    name = ""
    cat = ""
    current = []
    mode = 1
    for line in file:
        if line == "":  # Finished building
            dirs.append(current[:])
            buildings[name] = [fg, bg, dirs, cat]
            name = fg = bg = dirs = []
            current = []
            cat = ""
            mode = ""
            mode = 1
        elif mode == 1:  # Name (1) Foreground (2) Background (3) Category (4)
            name = line
            mode = 2
        elif mode == 2:
            fg = [int(x) for x in line.split(" ")]
            mode = 3
        elif mode == 3:
            bg = [int(x) for x in line.split(" ")]
            mode = 4
        elif mode == 4:
            cat = line
            mode = 5
        elif mode == 5:
            if line == "?`?`?`?":  # New direction
                dirs.append(current[:])
                current = []
            else:
                current.append(line)
    return buildings


buildings = unpack_buildings()


# A parent class for various buildings
class Building:
    
    def __init__(self, name, cat, entry, loc, direction):
        self.name = name  # Key of dicionary
        self.cat = cat  # Building type (entertainment, retail, etc)
        self.entry = entry  # Dictionary entry from above
        self.loc = loc  # Location on map, on screen
        self.direction = direction # direction entrance is facing

    def display(self, loc, console):
        hline = gui.hline
        image = self.entry[2][self.direction]
        console.print(loc[0], loc[1], image[0], self.entry[0], (22,22,22))
        for i in range(len(image)-2):
            # First print the border
            console.print(loc[0], loc[1]+1+i, 
                image[i+1][0]
                + hline(" ", len(image[i+1])-2)
                + image[i+1][len(image[i+1])-1], self.entry[0], (22,22,22))
            # Then print the "meat" of the image, where all the color is shown
            console.print(loc[0]+1, loc[1]+1+i, image[i+1][1:len(image[i+1])-1], self.entry[0], self.entry[1])
        console.print(loc[0], loc[1]+len(image)-1, image[len(image)-1], self.entry[0], (22,22,22))
            
