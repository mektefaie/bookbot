def read_book(book_location):
    """This function accepts a relative path (str) to a book in books directory, reads the content and returns the content as a single string.

    Args:
        book_location (str): relative path to books directory (e.g., "books/frankenstein.txt")

    Returns:
        str: the content of the book (e.g., "Once upon a time...") as a single string
    """
    with open(book_location) as f:
        file_content = f.read()
    return file_content


def num_of_words(book_str):
    """This function accepts the content of a book (str), splits it into individual words and returns the word count.

    Args:
        book_str (str): content of an entire book (e.g., "Once upon a time...")

    Returns:
        int: word count (e.g., 1234)
    """
    return len(book_str.split())


def char_count(file_content):
    """This function accepts the content of a book (str) and prints each alphabet from highest occurrence in the book to lowest.

    Args:
        file_content (str): content of an entire book (e.g., "Once upon a time...")

    Returns:
        none.
    """
    file_content = file_content.lower()

    char_count = {}

    for char in file_content:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    sorted_char_count = dict(
        sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_char_count.items():
        print(f"The '{key}' character was found {value} times")


def main():
    book_location = "books/frankenstein.txt"
    file_content = read_book(book_location)
    word_count = num_of_words(file_content)
    print(f"--- Begin report of {book_location} ---")
    print(f"{word_count} words found in the document")
    print()
    character_count = char_count(file_content)
    print(f"--- End report ---")


if __name__ == "__main__":
    main()
