ACCEPTED = [":", ".", " "]  # List of accepted characters to move over


# Setup a map to be used in pathfinding of an entity
def setup_image(file):
    # Prepare the image into 2d list (each char is an element)
    with open(file) as f:
        img = f.read().split("\n")
    img = [list(line) for line in img]
    img.pop()
    
    # Add walls around the border of the map to prevent funky indexing things
    new = [["#" for i in range(len(img[0])+2)]]
    for line in img:
        newl = ["#"] + line + ["#"]
        new.append(newl)
    new.append(new[0])

    return new


# Create a class of a entity that can move and do stuff
class Entity():
    
    def __init__(self, name):
        self.name = name

    def pathfind(self, start, destination, m, accepted):
        nodelocs = [start]  # List of nodes - location : past
        nodedirs = [[]]
        finished = []
        iterations = 0  # Index to keep track of loop iterations
        while True:
            for i in range(len(nodelocs)):
                if nodelocs[i] in finished:
                    continue
                node = nodelocs[i]
                directions = [
                    [node[0], node[1] + 1],  # East
                    [node[0], node[1] - 1],  # West
                    [node[0] + 1, node[1]],  # South
                    [node[0] - 1, node[1]],  # North
                    [node[0] + 1, node[1] + 1],  # Southeast
                    [node[0] + 1, node[1] - 1],  # Southwest
                    [node[0] - 1, node[1] + 1],  # Northeast
                    [node[0] - 1, node[1] - 1],  # Northwest
                ]
                
                paths = []
                for d in directions:
                    if m[d[0]][d[1]] in accepted and d not in nodelocs:
                        paths.append(d)
                for path in paths:
                    nodelocs.append(path)
                    nodedirs.append(node)
                finished.append(node)
                
                if nodelocs[i] == destination:
                    trail = [nodelocs[i]]
                    traceback = trail[0][:]
                    while True:
                        if trail[0] == start:
                            return trail
                        traceback = nodedirs[nodelocs.index(traceback)]
                        trail.insert(0, traceback)


image = setup_image("map.txt")
person = Entity("johnny")
path = person.pathfind([2, 2], [1, 10], image, ACCEPTED)
print(path)
