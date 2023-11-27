def main():
    book_path = "books/frankenstein.txt"
    book_txt = get_book_txt(book_path)
    word_count = get_word_count(book_txt)
    char_count_dict = get_char_count_dict(book_txt)
    char_count_sorted_list = get_char_count_sorted_list(char_count_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")

    for item in char_count_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' was found {item['num']} times")

    print("--- End report ---")


def get_book_txt(path):
    with open(path) as f:
        return f.read()


def get_word_count(source):
    words = source.split()
    return len(words)


def get_char_count_dict(source):
    char_count = {}
    for char in source:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1
    return char_count


def sort_on_num(d):
    return d["num"]


def get_char_count_sorted_list(char_count_dict):
    sorted = []
    for ch in char_count_dict:
        sorted.append({"char": ch, "num": char_count_dict[ch]})

    sorted.sort(key=sort_on_num, reverse=True)
    return sorted


main()
