class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = students
        self.students.sort()
        self.diagram = diagram.split("\n")

    def plants(self, name):
        theirPlants = []
        searchId = (self.students.index(name) * 2)
        theirPlants.append(decode(self.diagram[0][searchId]))
        theirPlants.append(decode(self.diagram[0][searchId+1]))
        theirPlants.append(decode(self.diagram[1][searchId]))
        theirPlants.append(decode(self.diagram[1][searchId+1]))
        return theirPlants

def decode(letter):
    if (letter == "R"):
        return "Radishes"
    if (letter == "C"):
        return "Clover"
    if (letter == "V"):
        return "Violets"
    if (letter == "G"):
        return "Grass"
    return None
