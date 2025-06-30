def get_book_words(book_text):
    return len(book_text.split())

def get_character_counts(book_text):
    book_text = book_text.lower()
    char_counts = {}
    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_character_list(char_counts):
    sorted_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list