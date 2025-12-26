import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def probability_of_patterns(patterns, valid_words, pattern_freq_db): #P(E) = sum across words P(E|wi)*P(wi)
    p = 0
    for word in valid_words:
        p += probability_of_patterns_given_word(patterns, word, pattern_freq_db)/2315 #2315 is the number of words in the valid list
    return p

def probability_of_patterns_given_word(patterns, word, pattern_freq_db): #P(E|W) = sum across patterns P(E|wi)*P(wi) 
    p = 0
    word_patterns = pattern_freq_db[word]
    for pattern in patterns:
        p += word_patterns.get(pattern, 0)/14855 #14855 is the number of words in the guess list
    return p


def probability_of_word_given_patterns(patterns, word, valid_words, pattern_freq_db): #P(W|E) = P(E|W)*P(W)/P(E)
    return probability_of_patterns_given_word(patterns, word, pattern_freq_db)/2315/probability_of_patterns(patterns, valid_words, pattern_freq_db)

def most_likely_words(patterns, valid_words, pattern_freq_db, num_words):
    probabilities = []
    for word in valid_words:
        p = probability_of_word_given_patterns(patterns, word, valid_words, pattern_freq_db)
        probabilities.append((word, p))
    probabilities.sort(key=lambda x: x[1], reverse=True)
    return [word for word, p in probabilities[:num_words]]

def word_probability_tuples(patterns, valid_words, pattern_freq_db):
    probabilities = []
    for word in valid_words:
        p = probability_of_word_given_patterns(patterns, word, valid_words, pattern_freq_db)
        probabilities.append((word, p))
    probabilities.sort(key=lambda x: x[1], reverse=True)
    return probabilities


def plot_word_probabilities_with_slider(
    word_prob_tuples,
    highlight_word,
    window_size=30,
    padding_frac=0.05
):
    """
    Plot word probabilities with a fixed global y-axis and slider.

    padding_frac : fraction of (max - min) added above and below
    """

    words = [w for w, _ in word_prob_tuples]
    probs = [p for _, p in word_prob_tuples]
    n = len(words)

    # ----- compute global y limits once -----
    ymin = min(probs)
    ymax = max(probs)
    pad = (ymax - ymin) * padding_frac

    ymin -= pad
    ymax += pad

    # ----- find highlighted probability -----
    highlight_prob = next(
        (p for w, p in word_prob_tuples if w == highlight_word),
        None
    )

    start = 0
    end = min(window_size, n)

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    line, = ax.plot(range(start, end), probs[start:end])

    ax.set_xticks(range(start, end))
    ax.set_xticklabels(words[start:end], rotation=90)

    ax.set_xlabel("Word")
    ax.set_ylabel("Probability")
    ax.set_title("Word Probabilities (Descending)")

    # ----- FIXED y-axis -----
    ax.set_ylim(ymin, ymax)

    if highlight_prob is not None:
        ax.axhline(highlight_prob, linestyle=":")

    # ----- slider -----
    ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
    slider = Slider(
        ax=ax_slider,
        label="Scroll",
        valmin=0,
        valmax=max(0, n - window_size),
        valinit=0,
        valstep=1
    )

    def update(val):
        start = int(slider.val)
        end = min(start + window_size, n)

        line.set_xdata(range(start, end))
        line.set_ydata(probs[start:end])

        ax.set_xticks(range(start, end))
        ax.set_xticklabels(words[start:end], rotation=90)
        ax.set_xlim(start - 0.5, end - 0.5)

        # DO NOT touch y-axis here
        fig.canvas.draw_idle()

    slider.on_changed(update)
    plt.show()

def plot_all_word_probabilities(
    word_prob_tuples,
    highlight_word,
    padding_frac=0.05
):
    """
    Plot all word probabilities on a single fixed-scale graph.

    - No word labels
    - All points shown at once
    - Fixed global y-axis with padding
    - Dotted horizontal line at highlight_word probability
    """

    probs = [p for _, p in word_prob_tuples]
    n = len(probs)

    # ----- global y limits -----
    ymin = min(probs)
    ymax = max(probs)
    pad = (ymax - ymin) * padding_frac
    ymin -= pad
    ymax += pad

    # ----- highlighted probability -----
    highlight_prob = next(
        (p for w, p in word_prob_tuples if w == highlight_word),
        None
    )

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(range(n), probs)

    ax.set_xlabel("Word rank (descending probability)")
    ax.set_ylabel("Probability")
    ax.set_title("All Word Probabilities")

    ax.set_ylim(ymin, ymax)
    ax.set_xlim(0, n - 1)

    if highlight_prob is not None:
        ax.axhline(highlight_prob, linestyle=":")

    # Remove word labels entirely
    ax.set_xticks([])

    plt.show()