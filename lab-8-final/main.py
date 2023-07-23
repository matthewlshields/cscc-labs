# FOR TESTING
sample_text = '''
Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge's name was good upon 'Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail.

Mind! I don't mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country's done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail.

Scrooge knew he was dead? Of course he did. How could it be otherwise? Scrooge and he were partners for I don't know how many years. Scrooge was his sole executor, his sole administrator, his sole assign, his sole residuary legatee, his sole friend, and sole mourner. And even Scrooge was not so dreadfully cut up by the sad event, but that he was an excellent man of business on the very day of the funeral, and solemnised it with an undoubted bargain.

The mention of Marley's funeral brings me back to the point I started from. There is no doubt that Marley was dead. This must be distinctly understood, or nothing wonderful can come of the story I am going to relate. If we were not perfectly convinced that Hamlet's Father died before the play began, there would be nothing more remarkable in his taking a stroll at night, in an easterly wind, upon his own ramparts, than there would be in any other middle-aged gentleman rashly turning out after dark in a breezy spot—say Saint Paul's Churchyard for instance—literally to astonish his son's weak mind.
'''


# Open text file


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

# List top X words

# Document modification

# List positions of provided word

# Replace a word. One or all instances

# Save as new file. Do not allow to overwrite.


if __name__ == '__main__':
    common_words = ['a', 'an', 'and']
    print(sample_text)
    cleaned_text = text_scrubber(sample_text, excluded_words=common_words)
    print("Total words:", total_words(cleaned_text))
    print("Count per word:", word_counter(cleaned_text))
    print("Word proportion:", word_proportion(cleaned_text))
