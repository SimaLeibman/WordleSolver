from WordleNarrower import *
from NaiveGuesser import *
from BayesianProbability import *
from SurpriseCalculator import *
import pickle
from collections import defaultdict



allowed_solutions = load_word_list("allowed_solutions.txt")
allowed_guesses = load_word_list("allowed_guesses.txt")


with open("pattern_freq_db_updated1.pkl", "rb") as f:
    pattern_freq_db = pickle.load(f)



patterns = [
    (2,0,1,0,0), #sima
    (1,1,0,0,0),
    (0,1,0,0,0), #kaddical     
    (0,0,2,0,2), 
    (0,0,0,1,0), #fare 
    (1,1,0,0,0), 
    (0,1,0,0,0), #anabanana 
    (2,0,0,0,0),
    (2,0,2,1,0),  
    (0,0,0,0,0), #tyler 
    (1,1,2,0,1), 
    (2,2,2,0,2),
    (2,2,2,0,0), #hopper
    (2,2,2,0,0), 
    (2,2,2,2,0),
    (0,1,0,1,0),#jp
    (2,0,2,0,1), 
    (2,2,2,2,0),
    (0,0,0,0,1), #tony
    (2,0,2,0,0), 
    (2,0,2,0,2),
    (0,0,0,2,1), #thinking
    (2,0,1,2,0),
    (2,1,2,2,1), 
    (0,0,0,0,0), #pangolin
    (1,0,1,1,0),
    (1,0,1,1,0), 
    (0,0,2,0,0), 
    (0,1,2,1,1)
    # (0,2,0,0,2), #
    # (1,0,1,0,0), #thinking
    # (0,1,1,2,0)
    # (0,0,0,1,1),
    # (0,2,0,1,0),
    # (0,2,2,2,2),
    # (0,0,0,0,0), 
    # (0,0,0,1,1),
    # (0,2,0,1,0),
    # (0,2,2,2,2)
]
patterns = convert_patterns(patterns)
valid_words = filter_solutions_by_patterns(allowed_solutions, patterns, pattern_freq_db)

#print(valid_words)

next_guess, score = best_guess(valid_words, allowed_guesses)
print("recommended guess:", next_guess)

print(most_likely_words(patterns, valid_words, pattern_freq_db, 5))
print("Number of valid words: " + str(len(valid_words)))
#print(filter_possible_words(valid_words, "inert", compare("inert","spool")))

#plot_word_probabilities_with_slider(word_probability_tuples(patterns, valid_words, pattern_freq_db), "glint")
plot_all_word_probabilities(word_probability_tuples(patterns, valid_words, pattern_freq_db), "glint")

print(probability_of_word_given_patterns(patterns, "spool", valid_words, pattern_freq_db))
print(probability_of_word_given_patterns(patterns, "stoop", valid_words, pattern_freq_db))

