import sys
from textwrap import wrap

result = 0


def get_ids_list(id_range_str: str) -> list[int]:
    min, max = id_range_str.split("-")
    return list(range(int(min), int(max) + 1))


def is_invalid_id(id: str) -> bool:
    if len(id) == 1:
        return False

    if len(set(id)) == 1:
        return True

    for i in range(2, len(id)):
        if len(id) % int(i) == 0:
            if len(set(list(wrap(id, int(i))))) == 1:
                return True

    return False


def get_invalid_ids(ids: list[int]) -> list[int]:
    result = []
    for id in ids:
        id_str = str(id)
        if is_invalid_id(id_str):
            result.append(id)
    return result


def get_sum_invalid_ids(invalid_ids: list[int]) -> int:
    sum = 0
    for id in invalid_ids:
        sum += id

    return sum


def get_input_data() -> list[str]:
    input_data = []

    try:
        file_path = sys.argv[1]
        with open(file_path, "r") as file:
            content = file.read()
            input_data = content.strip().split(",")
    except IndexError:
        print("Need file with input data")
    except FileNotFoundError:
        print(f"File {file_path} not found!")

    return input_data


if __name__ == "__main__":
    id_ranges = get_input_data()
    all_invalid_ids = []
    for i in id_ranges:
        ids_list = get_ids_list(i)
        invalid_ids = get_invalid_ids(ids_list)
        all_invalid_ids.extend(invalid_ids)
    print(all_invalid_ids)
    print(f"sum: {get_sum_invalid_ids(all_invalid_ids)}")
