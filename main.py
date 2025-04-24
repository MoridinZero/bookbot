def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents
def get_num_words(file_contents):
    words = file_contents.split()
    total_words = 0
    for word in words:
        total_words += 1
    return total_words

def main():
    filepath = "/home/moridin_zero/workspace/github.com/moridinzero/bookbot/books/frankenstein.txt"
    print(f"{get_num_words(get_book_text(filepath))} words found in the document")
main()