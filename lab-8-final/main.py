import word_replacement as replacer
import document_statistics as stats

# FOR TESTING
sample_text = '''
Marley was dead: to begin with. There is no doubt whatever about that. The register of his burial was signed by the clergyman, the clerk, the undertaker, and the chief mourner. Scrooge signed it: and Scrooge's name was good upon 'Change, for anything he chose to put his hand to. Old Marley was as dead as a door-nail.

Mind! I don't mean to say that I know, of my own knowledge, what there is particularly dead about a door-nail. I might have been inclined, myself, to regard a coffin-nail as the deadest piece of ironmongery in the trade. But the wisdom of our ancestors is in the simile; and my unhallowed hands shall not disturb it, or the Country's done for. You will therefore permit me to repeat, emphatically, that Marley was as dead as a door-nail.

Scrooge knew he was dead? Of course he did. How could it be otherwise? Scrooge and he were partners for I don't know how many years. Scrooge was his sole executor, his sole administrator, his sole assign, his sole residuary legatee, his sole friend, and sole mourner. And even Scrooge was not so dreadfully cut up by the sad event, but that he was an excellent man of business on the very day of the funeral, and solemnised it with an undoubted bargain.

The mention of Marley's funeral brings me back to the point I started from. There is no doubt that Marley was dead. This must be distinctly understood, or nothing wonderful can come of the story I am going to relate. If we were not perfectly convinced that Hamlet's Father died before the play began, there would be nothing more remarkable in his taking a stroll at night, in an easterly wind, upon his own ramparts, than there would be in any other middle-aged gentleman rashly turning out after dark in a breezy spot—say Saint Paul's Churchyard for instance—literally to astonish his son's weak mind.
'''


# Open text file


# Save as new file. Do not allow to overwrite.


if __name__ == '__main__':
    common_words = ['a', 'an', 'and']
    print(sample_text)
    cleaned_text = stats.text_scrubber(sample_text, excluded_words=common_words)
    print("Total words:", stats.total_words(cleaned_text))
    print("Count per word:", stats.word_counter(cleaned_text))
    print("Word proportion:", stats.word_proportion(cleaned_text))
    print('')

    stats.word_finder("ancestors", cleaned_text)  # Should be found once
    stats.word_finder("marley", cleaned_text)  # Should be found multiple times
    stats.word_finder("lightsaber", cleaned_text)  # Should not be found

    stats.top_words(cleaned_text, 5)

    print("Word indexes: ", replacer.find_occurrences("Scrooge", sample_text))  # Get the indexes
    print('')
    print(replacer.replace_occurrences("Scrooge", "Cratchit", sample_text, replace_all=True))  # Replace all
    print('')
    print(replacer.replace_occurrences("Scrooge", "Cratchit", sample_text, index_to_replace=201))  # Replace the second
    print('')
    print(replacer.replace_occurrences("Scrooge", "Cratchit", sample_text))  # Nothing to replace, so return the same text
