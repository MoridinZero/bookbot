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

def chars_dict_to_sorted_list(char_dict):
    sorted_chars = []

    for char, count in char_dict.items():
        result_dict = {"char": char, "num": count}
        sorted_chars.append(result_dict)

    def sort_on(dict):
        return dict["num"]
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars

def print_report(path, word_count, sorted_chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
