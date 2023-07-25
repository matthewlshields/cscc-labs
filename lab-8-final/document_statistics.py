# Remove punctuation
def remove_special_characters(text_list: list, special_characters='.;:?!,\''):
    cleaned_words = []
    for word in text_list:
        cleaned_words.append(word.strip(special_characters))
    return cleaned_words


# Exclude words
def remove_common_words(text_list: list, excluded_words: list, convert_to_lower_case=True):
    working_list = []

    if convert_to_lower_case:
        for word in text_list:
            working_list.append(str(word).lower())
    else:
        working_list = text_list

    if excluded_words is not None:
        for word in working_list:
            if word in excluded_words:
                working_list.remove(word)

    return working_list


def text_scrubber(text: str, special_characters='', excluded_words=None):
    working = str(text)
    the_words = working.split()
    the_words = remove_special_characters(the_words)
    the_words = remove_common_words(the_words, excluded_words)
    return the_words


# Count the total number of words
def total_words(text):
    return len(text)


# Dictionary of count by word
def word_counter(text):
    unique_words = set(text)
    unique_words = list(unique_words)
    unique_words.sort()
    working4 = {}
    for word in unique_words:
        working4[word] = text.count(word)
    return working4


# Dictionary of proportion by work
def word_proportion(text):
    divisor = total_words(text)
    the_counted_words = word_counter(text)
    working_list = {}
    for word in the_counted_words:
        working_list[word] = round(the_counted_words[word] / divisor, 4)
    return working_list


# Accept a user’s query of whether a word exists in the text. If the word search finds a word, state
# the word, the number of times it appears, and the proportion of the total words made up by
# that word. If the word does not find the word, return some information that the word was not
# found in the text.
def word_finder(word_to_find: str, text: list):
    try:
        text.index(word_to_find.lower())
        print(f'The word "{word_to_find}" was found.')
        print(f'It occurs {word_counter(text).get(word_to_find)} times.')
        print(f'That is a proportion of {word_proportion(text).get(word_to_find)} of the total words')
        print("")
    except ValueError:
        print(f'The word "{word_to_find}" was not found.')


# List top X words
def top_words(text: list, show_top_number: int):
    word_count = word_counter(text)

    sorted_by_occurrence = sorted(word_count.items(), key=lambda item_tuple: item_tuple[1], reverse=True)
    sorted_by_occurrence = dict(sorted_by_occurrence)

    counter = 0
    while counter < show_top_number:
        keys = list(sorted_by_occurrence.keys())
        word_finder(keys[counter], text)
        counter += 1