def is_word(text: str) -> bool:
    words_list = ["dog", "i", "network", "love", "do", "go"]
    for word in words_list:
        if word in text:
            return True
    return False


def find_suspicious_words(found_words: set[str], text: str) -> None:
    for starting_index in range(len(text)):
        temp_text: str = ""
        for char in text[starting_index:]:
            if is_word(char):
                found_words.add(char)

            temp_text += char
            if is_word(temp_text):
                found_words.add(temp_text)


def get_uncertain_words(uncertain_words: set, found_words: set) -> None:
    for sus_word in found_words:
        for other_sus_word in found_words:
            if other_sus_word != sus_word and other_sus_word in sus_word:
                uncertain_words.add(sus_word)


def is_text_consist_of(text: str, words: set[str]) -> bool:
    n: int = len(text)
    dp: list[bool] = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            # # DEBUG
            # print(f"i: {i}, j: {j}, dp[j]: {dp[j]}, text[j:i]: {text[j:i]}, is in: {text[j:i] in (found_words - uncertain_words)}")
            if dp[j] and text[j:i] in words:
                dp[i] = True
                break
        # # DEBUG
        # print(f"dp: {dp}")
    return dp[n]

def my_func(text: str) -> None:
    # input validation - is str
    if not isinstance(text, str):
        raise ValueError("text must be string")
    # input validation - not empty
    if not text:
        raise ValueError("text cant be empty")

    found_words: set[str] = set()       # words that contain words from the words_list
    uncertain_words: set[str] = set()   # words that contain words from the words_list but might not be minimal - can contain other words within them.

    find_suspicious_words(found_words, text)
    get_uncertain_words(uncertain_words, found_words)

    print(f"does \"{text}\" certainly consist of the words in the list?\n"
          f"> {is_text_consist_of(text, found_words - uncertain_words)}")

    print(f"does \"{text}\" consist of words that uncertainly in the list?\n"
          f"> {is_text_consist_of(text, found_words)}")

    # # DEBUG
    # print(f"suspicious words: {found_words}")
    # print(f"certain words: {found_words - uncertain_words}")
    # print(f"uncertain words: {uncertain_words}")


def main() -> None:
    my_func("d")        # False
    my_func("dog")      # True
    my_func("dogo")     # True
    my_func("idog")     # True
    my_func("doig")     # False
    my_func("lovenetworkingi")  # False


if __name__ == '__main__':
    main()