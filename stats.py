def get_num_words(file_contents):
    words = file_contents.split()
    total_words = 0
    for word in words:
        total_words += 1
    return total_words

def count_characters(file_contents):
    words = file_contents.lower()
    count_char_dictionary = {}
    for char in words:
        if char not in count_char_dictionary:
            count_char_dictionary[char] = 1
        else:
            count_char_dictionary[char] += 1
    return count_char_dictionary

    