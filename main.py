from WordleNarrower import *
from NaiveGuesser import *
from BayesianProbability import *
from SurpriseCalculator import *
import pickle


allowed_solutions = load_word_list("data/allowed_solutions.txt")
allowed_guesses = load_word_list("data/allowed_guesses.txt")


with open("pattern_freq_db_updated1.pkl", "rb") as f:
    pattern_freq_db = pickle.load(f)


# Number 6 sample
answer = "abbot"
patterns = [
    (1,0,0,1,0), #tyler
    (0,0,1,1,0),
    (2,2,1,0,2),    
    (0,1,0,0,2), #sima
    (1,0,1,0,0),
    (2,2,1,0,2),
    (2,0,0,0,0),  #fare
    (0,1,0,1,0),
    (1,1,1,2,0),  
    (0,0,0,1,0), #thinking  
    (0,0,1,0,2),
    (0,1,0,0,2),
    (2,2,1,0,2),
    (0,0,1,0,0), #jaiden #1
    (0,1,1,0,0),
    (1,0,0,2,2),
    (0,0,2,2,2),
    (0,1,2,2,2),
    (0,0,1,0,0), #jaiden #2
    (2,0,0,0,1),
    (2,0,0,2,0),
    (2,0,1,2,0),
    (2,0,0,2,2),
    (0,0,1,0,0), #yosef
    (0,1,0,0,0),
    (2,1,1,0,0),
    (2,2,1,0,2),
    (0,1,0,0,2), #sinclair
    (0,1,0,0,2),
    (0,0,1,0,2),
    (0,1,0,0,2),
    (1,0,1,1,0),
    (0,1,1,0,0), #edog
    (1,0,0,2,0),
    (0,0,0,2,2),
    (0,1,0,2,2),
    (2,0,0,2,2),
    (2,0,0,2,2),
    (0,1,0,0,0), #jp
    (0,0,1,0,0),
    (2,0,0,2,2),
    (0,0,1,0,0), #hopper
    (1,1,0,0,0),
    (1,0,0,0,0),
    (0,0,2,2,2)



    # (1,2,1,0,0), #
    # (2,2,0,0,0),
    # (2,2,0,0,0),
    # (2,2,2,0,0),
    # (1,0,1,0,0), #will #4
    # (0,2,1,0,0),
    # (0,2,2,2,2),
    # (0,2,2,2,2),
    # (0,2,2,2,2),
    # (1,0,0,0,0), #jaiden
    # (1,1,1,0,0),
    # (0,0,1,1,2),
    # (1,2,0,0,0),
    # (0,0,0,0,0), #jaiden #2
    # (0,1,1,2,0),
    # (1,2,0,2,0),
    # (0,2,2,2,2),
    # (0,1,1,0,0), #jaiden #3
    # (1,1,1,0,0),  
    # (1,2,2,0,0),
    # (0,2,2,1,0),
    # (0,2,2,2,2)
]


# 1 sample
answer = "conch"
patterns = [(0,1,0,1,0), #bleop
    (2,0,1,0,0),
    (2,0,0,1,0), #kaddical    
    (2,1,0,0,1), 
    (0,0,0,0,0), #caleb
    (0,1,0,0,0), 
    (1,2,0,0,0), #jp
    (0,2,0,2,2),
    (2,2,0,2,2), 
    (0,0,0,0,1), #tony
    (0,0,1,0,0), 
    (0,2,0,0,0),
    (0,0,0,0,1), #nick thinking
    (0,1,0,2,0), 
    (1,2,0,2,2),
    (0,0,0,1,0),#jezztre
    (0,0,0,1,0), 
    (0,0,0,1,0),
    (0,2,0,2,2), 
    (0,0,0,0,0), #tyler
    (0,0,1,0,0),
    (0,2,0,1,0),
    (2,2,2,0,1),
    (0,0,1,0,0), #hopper
    (0,2,2,0,0),
    (0,2,2,0,0),
    (0,0,0,0,0),
    (0,0,0,0,0), #sima
    (0,0,0,1,1),
    (0,2,0,1,0),
    (0,2,2,2,2),
    (2,0,0,0,2), #will
    (0,0,0,0,0), #randbob #1
    (0,2,0,0,2),
    (2,0,0,1,0), #randbob #2
    (2,0,0,0,1),
    (2,2,2,0,0),
    (0,0,0,0,2)]

patterns = convert_patterns(patterns)
valid_words = filter_solutions_by_patterns(allowed_solutions, patterns, pattern_freq_db)
valid_words = most_likely_words(patterns, valid_words, pattern_freq_db, len(valid_words))


print(valid_words)
print("Number of bayesian guesses: " + \
    str(bayesian_number_of_guesses(patterns, valid_words, pattern_freq_db, answer)))
print("Number of best_guess guesses: " + \
    str(best_guess_number_of_guesses(valid_words, allowed_guesses, answer)))
print("Number of hybrid guesses: " + \
    str(hybrid_model_number_of_guesses(patterns, valid_words, pattern_freq_db, allowed_guesses, answer)))
print("Bayesian first guess reduction: " + \
    str((1-len(filter_possible_words(valid_words, valid_words[0], \
        compare(valid_words[0], answer)))/len(valid_words))*100) + "%")
print("Best guess first guess reduction: " + \
    str((1-len(filter_possible_words(valid_words, best_guess(valid_words, allowed_guesses)[0], \
        compare(best_guess(valid_words, allowed_guesses)[0], answer)))/len(valid_words))*100) + "%")

# next_guess, score = best_guess(valid_words, allowed_guesses)
# print("recommended guess:", next_guess)

# print(len(most_likely_words(patterns, valid_words, pattern_freq_db, len(valid_words))))
# print("Number of valid words: " + str(len(valid_words)))
#print(filter_possible_words(valid_words, "trike", compare("trike","prism")))

#plot_word_probabilities_with_slider(word_probability_tuples(patterns, valid_words, pattern_freq_db), "glint")
# plot_all_word_probabilities(word_probability_tuples(patterns, valid_words, pattern_freq_db), "fruit")

# print(probability_of_word_given_patterns(patterns, "spool", valid_words, pattern_freq_db))
# print(probability_of_word_given_patterns(patterns, "stoop", valid_words, pattern_freq_db))

