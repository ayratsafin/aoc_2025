import sys

count_of_zeros = 0

init_value = 50
MIN_VALUE = 0
MAX_VALUE = 99
COUNT = MAX_VALUE + 1


def get_dial_position(position: int, rotation: str):
    direction = rotation[0]
    shift = int(rotation[1:]) % 100
    zero_passes = int(rotation[1:]) // 100
    dial = list(range(MIN_VALUE, COUNT))

    current_position = position - shift if direction == "L" else position + shift

    if current_position < MIN_VALUE:
        new_position = dial[current_position]
        zero_passes = (
            zero_passes + 1 if new_position != 0 and position != 0 else zero_passes
        )
    elif current_position > MAX_VALUE:
        new_position = dial[current_position - COUNT]
        zero_passes = zero_passes + 1 if new_position != 0 else zero_passes
    else:
        new_position = dial[current_position]

    print(
        f"{position} {'+ ' if direction == 'R' else '-'} {rotation} -> {new_position} {zero_passes}"
    )

    return [dial[new_position], zero_passes]


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
    [position, zero_passes] = get_dial_position(position, item)

    if position == 0:
        count_of_zeros += 1

    # only for part 2
    count_of_zeros += zero_passes

print(count_of_zeros)
