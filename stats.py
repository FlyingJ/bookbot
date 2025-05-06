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

def get_sorted_character_counts(raw_counts):
    character_list = [{"char": x, "num": raw_counts[x]} for x in raw_counts]
    return sorted(character_list, key=lambda record: record["num"], reverse=True)

