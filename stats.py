def get_word_count(book_string):
    return len(book_string.split())

def get_character_counts(book_string):
    book_string = book_string.lower()
    character_counts = {}
    for character in book_string:
        try:
            character_counts[character] += 1
        except KeyError:
            character_counts[character] = 1
    return character_counts
