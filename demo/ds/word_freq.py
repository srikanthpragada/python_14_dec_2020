s = "how do you do how did you do yesterday"

words = s.split()    # Split to get words
word_freq = {}
for w in set(words): # Take all unique words
    word_freq[w] = s.count(w)   # Add word as key and count as value

# Print word and key in sorted order of key
for w, c in sorted(word_freq.items()):
    print(f"{w:10} {c:2}")
