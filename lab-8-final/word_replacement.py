def find_occurrences(word_to_find: str, text: str):
    word_indexes = []
    if word_to_find in text:
        current_index = 0
        while current_index < len(text):
            found_index = text.find(word_to_find, current_index)

            if found_index == current_index:
                word_indexes.append(current_index)

            current_index += 1

    return word_indexes


# Replace a word. One or all instances
def replace_occurrences(current_word: str, new_word: str, text: str, index_to_replace=-1, replace_all=False):

    if replace_all:
        return text.replace(current_word, new_word)

    if index_to_replace > -1:
        updated_text = text[:index_to_replace] + new_word + text[index_to_replace + len(current_word):]
        return updated_text

    return text
