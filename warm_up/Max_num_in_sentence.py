"Find the sentence with the most words."

def max_num_in_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        if word_count > max_words:
            max_words = word_count
    return max_words