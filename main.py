def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_as_string(text)  # Capture the word count
    character_counts = count_characters(text.lower()) 
    create_report(character_counts, word_count, book_path)  # Pass word_count to create_report

def get_book_text(path):
    with open(path) as f:
        return f.read()

def book_as_string(text):
    words = text.split()
    word_count = len(words)
    return word_count  # Return the word count

def count_characters(text):
    character_counts = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic letters
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

def create_report(character_counts, word_count, path):
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")  # Use word_count here
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()