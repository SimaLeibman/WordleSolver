from WordleNarrower import *
from NaiveGuesser import *
from BayesianProbability import *
from SurpriseCalculator import *
from input import load_data

allowed_solutions, allowed_guesses, pattern_freq_db, agg_df = load_data()

# Run all experiments
for ind in range(len(agg_df)):

    tuple_patterns = agg_df['tuples'].iloc[ind]
    answer = agg_df['secret'].iloc[ind]
    experiment_index = agg_df['ind'].iloc[ind]
    
    print(f"\n==> Running experiment #{experiment_index}, answer = {answer}\n")

    patterns = convert_patterns(tuple_patterns)
    valid_words = filter_solutions_by_patterns(allowed_solutions, patterns, pattern_freq_db)
    valid_words = most_likely_words(patterns, valid_words, pattern_freq_db, len(valid_words))

    print(valid_words)
    print("Number of bayesian guesses: " + str(bayesian_number_of_guesses(patterns, valid_words, pattern_freq_db, answer)))
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

