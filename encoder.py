from functions import word_swap, remove_non_letters, words_to_shuff, shuffler


def Encoder(x):
    separator = "\n'\\n—weird—\\n’\n"

    print("The original text: \n" + "'" + x + "'" + "\n")

    y = remove_non_letters(x)

    all_words = y.split()

    words_to_shuffle = words_to_shuff(all_words)

    shuffled_words = shuffler(words_to_shuffle)

    word_swap(all_words, shuffled_words)

    encoded_text = ' '.join(all_words)

    print("The encoded text: " + separator + "'" + encoded_text + "'")

    shuffled_sentence = ' '.join(shuffled_words)

    print("Shuffled words only: " + separator + shuffled_sentence)








