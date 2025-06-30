from stats import get_book_words, get_character_counts, get_sorted_character_list
import sys
def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()

def main():
    if not sys.argv[1:]:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_book_words(book_text)
    char_counts = get_character_counts(book_text)
    sorted_list = get_sorted_character_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
