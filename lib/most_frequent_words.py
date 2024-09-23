def most_frequent_words(words):
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else: counter[word] = 1
    return sorted(counter, key=counter.get, reverse=True)[:2]
