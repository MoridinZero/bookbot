from stats import get_num_words
from stats import count_characters
from stats import chars_dict_to_sorted_list
from stats import print_report

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = "/home/moridin_zero/workspace/github.com/moridinzero/bookbot/books/frankenstein.txt"
    word_count = get_num_words(get_book_text(filepath))
    character_counts = count_characters(get_book_text(filepath))
    sorted_chars_list = chars_dict_to_sorted_list(count_characters(get_book_text(filepath)))
    print_report(filepath, word_count, sorted_chars_list)
main()