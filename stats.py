def get_num_words(text: str) -> int:
    words = text.split()
    num_words = len(words)
    return num_words


def get_char_count(text: str) -> dict[str, int]:
    lowered_text = text.lower()

    chars = {}
    
    for char in lowered_text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
        
    return chars


def sort_on(char: tuple[str, int]) -> int:
    count = char[1]
    return count


def chars_dict_to_sorted_list(text_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list: list[tuple[str, int]] = []

    for char in text_dict:  # noqa: PLC0206
        count = text_dict[char]
        sorted_list.append((char, count))

    return sorted(sorted_list, reverse=True, key=sort_on)