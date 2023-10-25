def count_words(file_contents):
    words = file_contents.split()
    print(len(words))

def count_characters(file_contents):
    dict_char = {}

    for character in file_contents:
        #print(character)
        lowered = character.lower()
        if lowered in dict_char: #if key already exists
            dict_char[lowered] += 1
        else:
            dict_char[lowered] = 1
    
    return dict_char


def generate_report(char_dict):
    for letter in char_dict:
        print(f"The '{letter}' character was found {char_dict[letter]} times")


with open("books/frankenstein.txt") as file:
    file_contents = file.read()


count_words(file_contents)
char_dict = count_characters(file_contents)
generate_report(char_dict)



