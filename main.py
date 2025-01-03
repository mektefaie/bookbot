def main():
    book_location = "books/frankenstein.txt"
    file_content = read_book(book_location)
    word_count = num_of_words(file_content)
    print(f"--- Begin report of {book_location} ---")
    print(f"{word_count} words found in the document")
    print()
    character_count = char_count(file_content)
    print(f"--- End report ---")


def read_book(book_location):
    with open(book_location) as f:
        file_content = f.read()
    return file_content


def num_of_words(book_str):
    return len(book_str.split())


def char_count(file_content):
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


if __name__ == "__main__":
    main()
