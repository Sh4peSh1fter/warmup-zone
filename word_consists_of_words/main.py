def is_word(text: str) -> bool:
    list_of_words = ["dog", "i", "network", "love", "do", "go"]
    for word in list_of_words:
        if word in text:
            return True
    return False

def my_func(text: str) -> bool:
    # input validation - is str
    if not isinstance(text, str):
        raise ValueError("text must be string")
    # input validation - not empty
    if not text:
        raise ValueError("text cant be empty")

    found_words: set[str] = set([])
    uncertain_words: set[str] = set([])


    for starting_index in range(len(text)):
        temp_text: str = ""
        for char in text[starting_index:]:
            if is_word(char):
                found_words.add(char)

            temp_text += char
            if is_word(temp_text):
                found_words.add(temp_text)

    for sus_word in found_words:
        for other_sus_word in found_words:
            if other_sus_word != sus_word and other_sus_word in sus_word:
                uncertain_words.add(sus_word)

    # DEBUG
    # print(f"suspicious words: {found_words}")
    print(f"certain words: {found_words - uncertain_words}")
    print(f"uncertain words: {uncertain_words}")



def main() -> None:
    print(my_func("d"))   # True
    print(my_func("dog"))   # True
    print(my_func("dogo"))  # True
    print(my_func("idog"))  # True
    print(my_func("doig"))  # False
    # print(my_func("lovenetworkingi"))   # False



if __name__ == '__main__':
    main()