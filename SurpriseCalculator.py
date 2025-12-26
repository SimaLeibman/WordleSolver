from WordleNarrower import compare, load_word_list
import numpy

def calculate_surprise(patterns, word, pattern_freq_db):
    surprise = 0
    word_patterns = pattern_freq_db[word]

    for pattern in patterns:
        surprise -= word_patterns.get(pattern, 0)/14855 * numpy.log(word_patterns.get(pattern, 0)/14855)
                #this calculation is -p(x)logp(x)
    return surprise

def least_surprising_words(patterns, valid_words, pattern_freq_db, num_words):
    surprises = []
    for word in valid_words:
        s = calculate_surprise(patterns, word, pattern_freq_db)
        surprises.append((word, s))
    surprises.sort(key=lambda x: x[1], reverse=False)
    return [word for word, s in surprises[:num_words]]