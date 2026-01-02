import numpy as np
from WordleNarrower import compare, most_likely_words, filter_possible_words

def best_guess(candidates, allowed_guesses):
    """
    Return the allowed guess with minimum expected partition size
    equivalent to max entropy split.
    """
    if len(candidates) == 1:
        return candidates[0], 0.0
    best_g = None
    best_score = float("inf")

    cand_arr = np.array(candidates)

    for g in allowed_guesses:

        # hashmap pattern -> count
        counts = {}

        for s in candidates:
            pat = compare(g, s)
            counts[pat] = counts.get(pat, 0) + 1

        # compute expected size metric
        # sum (n/N)^2  (closely tied to entropy)
        N = len(candidates)
        probs = np.array(list(counts.values())) / N
        score = np.sum(probs * probs)

        if score < best_score:
            best_score = score
            best_g = g

    return best_g, best_score


def bayesian_number_of_guesses(patterns, valid_words, pattern_freq_db, correct_word): #calculates number of guesses needed to reach correct_word using the most likely word according to naive bayesian
    count = 0
    while True:
        if valid_words[0] == correct_word:
            count += 1
            break
        valid_words = most_likely_words(patterns, valid_words, pattern_freq_db, len(valid_words))
        valid_words = filter_possible_words(valid_words, valid_words[0], compare(valid_words[0], correct_word))
        count += 1
    return count

def best_guess_number_of_guesses(valid_words, allowed_guesses, correct_word): #calculates number of guesses needed to reach correct_word using the best guess
    count = 0
    while True:
        next_guess, score = best_guess(valid_words, allowed_guesses)
        if next_guess == correct_word:
            count += 1
            break
        valid_words = filter_possible_words(valid_words, next_guess, compare(next_guess, correct_word))
        count += 1
    return count

def hybrid_model_number_of_guesses(patterns, valid_words, pattern_freq_db, allowed_guesses, correct_word): #calculates number of guesses needed to reach correct_word using best_guess first and then bayesian top word
    count = 0
    next_guess, score = best_guess(valid_words, allowed_guesses)
    count += 1
    if next_guess == correct_word:
        return count
    valid_words = filter_possible_words(valid_words, next_guess, compare(next_guess, correct_word))
    while True:
        if valid_words[0] == correct_word:
            count += 1
            break
        valid_words = most_likely_words(patterns, valid_words, pattern_freq_db, len(valid_words))
        valid_words = filter_possible_words(valid_words, valid_words[0], compare(valid_words[0], correct_word))
        count += 1
    return count


