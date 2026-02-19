"""Data input loading utilities for Wordle solver experiments."""

from WordleNarrower import load_word_list
import pickle
import pandas as pd


def convert_bars(lst: list[str]) -> list[tuple]:
    """Convert pipe-separated pattern strings to tuples."""
    res = []
    for el in lst:
        res += [tuple(list(map(int, list(x)))) 
                for x in el.split('|')]
    return res


def load_data():
    """Load all required data files and return them."""
    allowed_solutions = load_word_list("data/allowed_solutions.txt")
    allowed_guesses = load_word_list("data/allowed_guesses.txt")
    
    with open("db/pattern_freq_db_updated1.pkl", "rb") as f:
        pattern_freq_db = pickle.load(f)
    
    experiments_df = pd.read_csv("data/experiments.csv")
    agg_df = experiments_df.groupby(['ind', 'secret'])[['patterns', 'solver']].agg(list).reset_index()
    agg_df['tuples'] = agg_df['patterns'].apply(convert_bars)
    
    return allowed_solutions, allowed_guesses, pattern_freq_db, agg_df
