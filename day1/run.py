import pathlib
input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
content = [int(line) for line in input_file.open()]


def fuel_cost(mass):
    return int(mass / 3) - 2


total = 0
initial_fuel = 0
for mass in content:
    fuel = fuel_cost(mass)
    initial_fuel += fuel
    while fuel > 0:
        total += fuel
        fuel = fuel_cost(fuel)

print(f"part 1: {initial_fuel}")
print(f"part 2: {total}")
