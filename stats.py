def get_num_words(file_contents):
    words = file_contents.split()
    total_words = 0
    for word in words:
        total_words += 1
    return total_words