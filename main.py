import sys

from stats import chars_dict_to_sorted_list, get_char_count, get_num_words


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_list = chars_dict_to_sorted_list(get_char_count(text))
    print_report(book_path, num_words, sorted_list)


def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path: str, num_words: int, sorted_list: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {book_path}...")    
    print("----------- Word Count ----------")    
    print(f"Found {num_words} total words")    
    print("--------- Character Count -------")

    for tuple in sorted_list:
        if tuple[0].isalpha():
            print(f"{tuple[0]}: {tuple[1]}")

    print("============= END ===============")


main()
