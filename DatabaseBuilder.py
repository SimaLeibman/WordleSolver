from WordleNarrower import compare, load_word_list
from collections import defaultdict
import pickle

def build_pattern_freq_db(solutions, guesses):
    db = {}  # solution -> pattern frequency counter

    for sol in solutions:
        freq = defaultdict(int)
        for guess in guesses:
            p = compare(guess, sol)  # pattern defined earlier
            freq[p] += 1
        db[sol] = dict(freq)

    return db


def save_pattern_freq_db(db, filename="pattern_freq_db.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(db, f)


def load_pattern_freq_db(filename="pattern_freq_db.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)
    
allowed_solutions = load_word_list("allowed_solutions.txt")
allowed_guesses = load_word_list("allowed_guesses.txt")
    
db = build_pattern_freq_db(allowed_solutions, allowed_guesses)
save_pattern_freq_db(db)
print("stop")