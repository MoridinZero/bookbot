def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()

def main():
    filepath = "/home/moridin_zero/workspace/github.com/moridinzero/bookbot/books/frankenstein.txt"
    get_book_text(filepath)
main()