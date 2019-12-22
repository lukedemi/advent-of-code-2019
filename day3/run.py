import pathlib
input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
wires = input_file.read_text().split('\n')

DIRECTIONS = {
    "R":  (0, 1),
    "L":  (0, -1),
    "U":  (1, 0),
    "D":  (-1, 0),
}

class Wire:
    def __init__(self, directions):
        self.instructions = directions.split(',')
        self.places = {}
        self.steps = 0
        self.current = (0, 0)

        self.walk()

    def walk(self):
        for instruction in self.instructions:
            direction = DIRECTIONS[instruction[0]]
            length = int(instruction[1:])

            for _ in range(length):
                self.steps += 1
                self.current = self.step(self.current, direction)
                self.places[(self.current[0], self.current[1])] = self.steps

    def step(self, old, new):
        return [old[0] + new[0], old[1] + new[1]]


wire1 = Wire(wires[0])
wire2 = Wire(wires[1])

commonalities = set(wire1.places.keys()).intersection(wire2.places.keys())

closest = float("inf")
for place in commonalities:
    distance = abs(place[0]) + abs(place[1])
    if distance < closest:
        closest = distance

print(f"part 1: {closest}")

fewest_steps = float("inf")
for place in commonalities:
    distance = wire1.places[place] + wire2.places[place]
    if distance < fewest_steps:
        fewest_steps = distance

print(f"part 2: {fewest_steps}")
