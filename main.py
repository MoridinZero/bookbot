from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    filepath = "/home/moridin_zero/workspace/github.com/moridinzero/bookbot/books/frankenstein.txt"
    print(f"{get_num_words(get_book_text(filepath))} words found in the document")
main()