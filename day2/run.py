import copy
import pathlib
input_file = pathlib.Path(__file__).resolve().parent / 'input.txt'
computer = [int(item) for item in input_file.read_text().split(',')]

def opcode_matic(computer):
    start = 0
    while True:
        if computer[start] == 99:
            return computer[0]

        position1 = computer[start+1]
        position2 = computer[start+2]
        output_location = computer[start+3]

        if computer[start] == 1:
            final = computer[position1] + computer[position2]
        elif computer[start] == 2:
            final = computer[position1] * computer[position2]

        computer[output_location] = final
        start += 4

copy_computer = copy.deepcopy(computer)
copy_computer[1] = 12
copy_computer[2] = 2
print(f"part 1: {opcode_matic(copy_computer)}")

for noun in range(100):
    for verb in range(100):
        copy_computer = copy.deepcopy(computer)
        copy_computer[1] = noun
        copy_computer[2] = verb
        if opcode_matic(copy_computer) == 19690720:
            final_output = (100 * noun) + verb
            print(f"part 2: {final_output}")