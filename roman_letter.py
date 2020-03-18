character_dict = {"i": 1, "v": 5, "x": 10, "l": 50}


def get_roman_to_number(str):
    character_list = list(str)
    total_sum = 0
    skip_next_step = False
    for index, character in enumerate(character_list):
        if skip_next_step:
            skip_next_step = False
            continue
        if index + 1 < len(character_list) and (
            character_dict.get(character) < character_dict.get(character_list[index + 1])
        ):
            total_sum += character_dict.get(character_list[index + 1]) - character_dict.get(character)
            skip_next_step = True
        else:
            total_sum += character_dict.get(character)

    return total_sum


def test_roman_integer():
    sample_number = {
        "i": 1,
        "ii": 2,
        "iii": 3,
        "iv": 4,
        "v": 5,
        "vi": 6,
        "vii": 7,
        "viii": 8,
        "ix": 9,
        "x": 10,
        "xi": 11,
        "xii": 12,
        "xii": 12,
        "xiii": 13,
        "xiv": 14,
        "xv": 15,
        "xvi": 16,
        "xvii": 17,
        "xviii": 18,
        "xix": 19,
        "xx": 20,
        "xxi": 21,
    }

    for key, value in sample_number.items():
        print(f"{key} calculate value {get_roman_to_number(key)} {value}")


test_roman_integer()
