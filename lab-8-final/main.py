import word_replacement as replacer
import document_statistics as stats


class FileEditor:

    def __init__(self):
        self.file_contents = ''
        self.excluded_words = []
        self.scrubbed_text = []

    # Open text file
    def load_file(self, file: str):
        with open(file, "r") as text_file:
            file_contents = text_file.read()
            self.file_contents = file_contents
            self.scrubbed_text = stats.text_scrubber(self.file_contents, excluded_words=self.excluded_words)
            print("Text file has been loaded.")

    def save_file(self, file: str, contents: str):
        with open(file, "w") as text_file:
            text_file.write(contents)


def display_main_menu():
    menu = '''
Hello. Select an option

    L. Load a text document
    E. Exclude common words
    C. Display the total word count
    F. Find a word
    T. Display the top n words
    R. Find and replace text
    Q. Quit
    
    '''
    print(menu)


def process_menu_selection(selection: str):

    if selection == 'L':
        file_path = input("Enter a file name: ")
        fe.load_file(file_path)
        # print(fe.file_contents)
    if selection == 'E':
        words_to_exclude = input("Enter a comma separated list of words to exclude: ")
        fe.excluded_words = str(words_to_exclude).split()
        print(fe.excluded_words)
    if selection == 'C':
        if (fe.file_contents is None) | (fe.file_contents == ''):
            print("Please load a text file")
            return

        total_words = stats.total_words(fe.scrubbed_text)
        print(f"The file contains {total_words} words")
    if selection == 'F':
        word_to_find = input("Enter a word to find: ")
        if (fe.file_contents is None) | (fe.file_contents == ''):
            print("Please load a text file")
            return

        stats.word_finder(word_to_find, fe.scrubbed_text)
    if selection == 'T':
        top_n = input("Enter the top n number of words to be seen: ")
        stats.top_words(fe.scrubbed_text, int(top_n))
    if selection == 'R':
        process_sub_menu_fr()
    if selection == 'Q':
        print("Have a nice day! Good bye!")
        return 'q'


def process_sub_menu_fr():
    # Get the name of the new file

    # Get the word to replace
    old_word = input("What word would you like to replace? ")

    # Display positions
    occurrences_of_old_word = replacer.find_occurrences(old_word, fe.file_contents)
    print(f"The word {old_word} occurs at the following locations: {occurrences_of_old_word}")

    # Get choice
    new_word = input("What is the new word? ")

    # Replace
    location = input("Which location would you like to replace? 'All' or enter a location: ")

    updated_text = ''
    if location.lower() == 'all':
        updated_text = replacer.replace_occurrences(old_word, new_word, fe.file_contents, replace_all=True)
    else:
        updated_text = replacer.replace_occurrences(old_word, new_word, fe.file_contents, int(location))

    # Save
    new_file = input("Enter a new file name: ")
    fe.save_file(new_file, updated_text)

if __name__ == '__main__':
    fe = FileEditor()

    while True:
        display_main_menu()
        user_input = str(input("Enter your choice: "))
        response = process_menu_selection(user_input)

        if response == 'q':
            break

    # the_text = load_file('A_Christmas_Carol_Stave_1.txt')
    # common_words = ['a', 'an', 'and']
    # cleaned_text = stats.text_scrubber(the_text, excluded_words=common_words)
    # print("Total words:", stats.total_words(cleaned_text))
    # print("Count per word:", stats.word_counter(cleaned_text))
    # print("Word proportion:", stats.word_proportion(cleaned_text))
    # print('')
    #
    # stats.word_finder("ancestors", cleaned_text)  # Should be found once
    # stats.word_finder("marley", cleaned_text)  # Should be found multiple times
    # stats.word_finder("lightsaber", cleaned_text)  # Should not be found
    #
    # stats.top_words(cleaned_text, 5)
    #
    # print("Word indexes: ", replacer.find_occurrences("Scrooge", the_text))  # Get the indexes
    # save_file('A_Christmas_Carol_Stave_1-all-replace.txt', replacer.replace_occurrences("Scrooge", "Cratchit", the_text, replace_all=True))  # Replace all
    # save_file('A_Christmas_Carol_Stave_1-one-replace.txt', replacer.replace_occurrences("Scrooge", "Cratchit", the_text, index_to_replace=377))  # Replace the second
    # save_file('A_Christmas_Carol_Stave_1-no-replace.txt', replacer.replace_occurrences("Scrooge", "Cratchit", the_text))  # Nothing to replace, so return the same text
