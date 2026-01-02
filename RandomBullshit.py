import pickle
from WordleNarrower import load_word_list

allowed_solutions = load_word_list("allowed_solutions.txt")
allowed_guesses = load_word_list("allowed_guesses.txt")

with open("pattern_freq_db_updated1.pkl", "rb") as f:
    pattern_freq_db = pickle.load(f)

def number_of_patterns(word, pattern_freq_db):
    """
    Return the number of distinct patterns that occur
    for this word (i.e., nonzero-count patterns).
    """
    return len(pattern_freq_db[word])

def words_ordered_by_pattern_count(words, pattern_freq_db, descending=True):
    """
    Return a list of (word, pattern_count) ordered by pattern_count.
    """

    results = []

    for word in words:
        count = number_of_patterns(word, pattern_freq_db)
        results.append((word, count))

    results.sort(key=lambda x: x[1], reverse=descending)
    return results

ordered = words_ordered_by_pattern_count(allowed_solutions, pattern_freq_db)

for word, count in ordered[:2315]:
    print(word, count)

def pattern_set_contained(word_a, word_b, pattern_freq_db):
    """
    Return True if all patterns of word_a
    are also possible for word_b.
    """
    return set(pattern_freq_db[word_a].keys()).issubset(
        pattern_freq_db[word_b].keys()
    )

def build_pattern_sets(words, pattern_freq_db):
    """
    Precompute pattern sets for efficiency.
    """
    return {
        word: set(pattern_freq_db[word].keys())
        for word in words
    }

def find_contained_pattern_pairs_fast(words, pattern_freq_db):
    """
    Efficient containment detection.
    """

    pattern_sets = build_pattern_sets(words, pattern_freq_db)
    results = []

    for a in words:
        set_a = pattern_sets[a]
        for b in words:
            if a == b:
                continue
            if set_a.issubset(pattern_sets[b]):
                results.append((a, b))

    return results
def count_unique_containers_and_contained(containment_pairs):
    """
    containment_pairs: list of (contained_word, container_word)

    Returns:
        num_unique_containers
        num_unique_contained
        set_of_containers
        set_of_contained
    """

    contained_words = set()
    container_words = set()

    for contained, container in containment_pairs:
        contained_words.add(contained)
        container_words.add(container)

    return (
        len(container_words),
        len(contained_words),
        container_words, 
        contained_words
    )
print(count_unique_containers_and_contained(find_contained_pattern_pairs_fast(allowed_solutions, pattern_freq_db)))

def total_unique_patterns(pattern_freq_db):
    """
    Return the total number of distinct pattern IDs
    that appear anywhere in the database.
    """

    all_patterns = set()

    for word_patterns in pattern_freq_db.values():
        all_patterns.update(word_patterns.keys())

    return len(all_patterns)

print("Total unique patterns:", total_unique_patterns(pattern_freq_db))

def count_times_word_is_contained(word, containment_pairs):
    """
    Return the number of times `word` appears as the contained
    element in containment_pairs.
    """

    count = 0
    for contained, _ in containment_pairs:
        if contained == word:
            count += 1

    return count

pairs = find_contained_pattern_pairs_fast(allowed_solutions, pattern_freq_db)

print(count_times_word_is_contained("batch", pairs))