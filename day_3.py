import sys


def get_input_data() -> list[str]:
    input_data = []

    try:
        file_path = sys.argv[1]
        with open(file_path, "r") as file:
            content = file.read()
            input_data = content.strip().split("\n")
    except IndexError:
        print("Need file with input data")
    except FileNotFoundError:
        print(f"File {file_path} not found!")

    return input_data


def get_overall_amperage(max_batteries_amperage: list[int]) -> int:
    sum = 0
    for battery in max_batteries_amperage:
        sum += int(battery)
    return sum


def get_max_amperage(battery: str) -> int:
    batteries_elements: list[int] = list(map(int, battery))
    batteries_len: int = len(battery)
    ELEMENTS_COUNT = 12

    max_amperage_list: list[str] = []
    max_index = -1

    for cell_num in range(ELEMENTS_COUNT):
        first_index = max_index + 1
        last_index = batteries_len - (ELEMENTS_COUNT - cell_num)

        search_slice = batteries_elements[first_index : last_index + 1]
        max_value = max(search_slice)
        max_index = search_slice.index(max_value) + first_index
        max_amperage_list.append(str(max_value))

    # find second max element
    print(f"{battery} -> {''.join(max_amperage_list)}")
    return int("".join(max_amperage_list))


if __name__ == "__main__":
    batteries = get_input_data()
    max_amp: list[int] = []
    for i in batteries:
        max_amp.append(get_max_amperage(i))

    print(f"result: {get_overall_amperage(max_amp)}")
