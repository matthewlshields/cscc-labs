import word_replacement as replacer
import document_statistics as stats


# Open text file
def load_file(file: str):
    with open(file, "r") as text_file:
        file_contents = text_file.read()
    return file_contents


def save_file(file: str, contents: str):
    with open(file, "w") as text_file:
        text_file.write(contents)


if __name__ == '__main__':
    the_text = load_file('A_Christmas_Carol_Stave_1.txt')
    common_words = ['a', 'an', 'and']
    cleaned_text = stats.text_scrubber(the_text, excluded_words=common_words)
    print("Total words:", stats.total_words(cleaned_text))
    print("Count per word:", stats.word_counter(cleaned_text))
    print("Word proportion:", stats.word_proportion(cleaned_text))
    print('')

    stats.word_finder("ancestors", cleaned_text)  # Should be found once
    stats.word_finder("marley", cleaned_text)  # Should be found multiple times
    stats.word_finder("lightsaber", cleaned_text)  # Should not be found

    stats.top_words(cleaned_text, 5)

    print("Word indexes: ", replacer.find_occurrences("Scrooge", the_text))  # Get the indexes
    save_file('A_Christmas_Carol_Stave_1-all-replace.txt', replacer.replace_occurrences("Scrooge", "Cratchit", the_text, replace_all=True))  # Replace all
    save_file('A_Christmas_Carol_Stave_1-one-replace.txt', replacer.replace_occurrences("Scrooge", "Cratchit", the_text, index_to_replace=377))  # Replace the second
    save_file('A_Christmas_Carol_Stave_1-no-replace.txt', replacer.replace_occurrences("Scrooge", "Cratchit", the_text))  # Nothing to replace, so return the same text
