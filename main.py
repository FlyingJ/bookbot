import sys
from stats import get_word_count, get_character_counts, get_sorted_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    book_text = get_book_text(book_filepath)
    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_counts = get_character_counts(book_text)
    sorted_character_counts = get_sorted_character_counts(character_counts)
    for entry in sorted_character_counts:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
