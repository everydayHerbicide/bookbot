def main():
    book_path = "books/frankenstein.txt"
    report_on_book(book_path)

def get_book_text(path):
     with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_text_words(text):
    word_list = text.split()
    return len(word_list)

def count_letters(text):
    lower_case = text.lower()
    count_dict = {}
    for char in lower_case:
        if char in count_dict:
            count = count_dict[char] + 1
        else:
            count = 1
        count_dict[char] = count
    return count_dict

def convert_letter_dict_to_list(dictionary):
    letter_list = []
    for letter in dictionary:
        if letter.isalpha():
            letter_list.append((dictionary[letter], letter))
    return letter_list

def report_on_book(path):
    text = get_book_text(path)
    word_count = count_text_words(text)
    letter_count = count_letters(text)
    letter_list = convert_letter_dict_to_list(letter_count)
    letter_list.sort()
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in letter_list:
        l = letter_list.pop()
        print(f"The {l[1]} character was found {l[0]} times")
    print("--- End Report ---")





main()