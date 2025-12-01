import sys

count_of_zeros = 0

init_value = 50
MIN_VALUE = 0
MAX_VALUE = 99


def get_dial_position(position: int, rotation: str):
    direction = rotation[0]
    shift = int(rotation[1:]) % 100
    dial = list(range(MIN_VALUE, MAX_VALUE + 1))

    current_position = position - shift if direction == "L" else position + shift

    if current_position < MIN_VALUE:
        position = dial[current_position]
    elif current_position > MAX_VALUE:
        position = dial[current_position - 100]
    else:
        position = dial[current_position]

    return dial[position]


position = 50
rotations = list()

if len(sys.argv) == 2:
    file_path = sys.argv[1]
    try:
        with open(file_path, "r") as file:
            for line in file:
                rotations.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")


for item in rotations:
    position = get_dial_position(position, item)

    if position == 0:
        count_of_zeros += 1

print(count_of_zeros)
