from stats import get_num_words, get_book_text, get_num_chars, dict_to_sorted_list
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    booktext = get_book_text(book_path)
    num_words = get_num_words(booktext)
    chars_dict = get_num_chars(booktext)
    chars_list = dict_to_sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in chars_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
