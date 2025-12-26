def compare(guess: str, solution: str): #returns a tuple of 5 integers representing the pattern of a guess given a solution. 2 = green 1 = yellow 0 = gray
    assert len(guess) == len(solution) == 5
    
    result = [0]*5
    used = [False]*5

    # Greens first
    for i in range(5):
        if guess[i] == solution[i]:
            result[i] = 2
            used[i] = True

    # Yellows second
    for i in range(5):
        if result[i] == 2:
            continue
        for j in range(5):
            if not used[j] and guess[i] == solution[j]:
                result[i] = 1
                used[j] = True
                break

    return tuple(result)
def filter_solutions_by_patterns(allowed_solutions, pattern_ids, pattern_freq_db):
    # returns words consistent with all wordless patterns
    filtered = []
    
    for word in allowed_solutions:
        ok = True
        word_patterns = pattern_freq_db[word]

        for pid in pattern_ids:
            # pattern must appear at least once
            if word_patterns.get(pid, 0) == 0:
                ok = False
                break
        
        if ok:
            filtered.append(word)
    
    return filtered



def load_word_list(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        # Strip whitespace and ensure lowercase
        return [w.strip().lower() for w in f if len(w.strip()) == 5]


def pattern_tuple_to_int(pattern): #treats tuple as base 3 and converts to corresponding integer
    value = 0
    for p in pattern:
        value = value * 3 + p
    return value


def int_to_pattern_tuple(n): #inverse of pattern_tuple_to_int
    out = [0]*5
    for i in reversed(range(5)):
        out[i] = n % 3
        n //= 3
    return tuple(out)

def filter_possible_words(possible_words, guess, observed_pattern):
    #returns words consistent with guess and observed_pattern
    filtered = []

    for word in possible_words:
        if compare(guess, word) == observed_pattern:
            filtered.append(word)

    return filtered

def convert_patterns(patterns):
    numberPatterns = []
    for pattern in patterns:
        numberPatterns.append(pattern_tuple_to_int(pattern))
    return numberPatterns