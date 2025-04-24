from stats import get_num_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = "/home/moridin_zero/workspace/github.com/moridinzero/bookbot/books/frankenstein.txt"
    character_counts = print(count_characters(get_book_text(filepath)))
    return character_counts
main()