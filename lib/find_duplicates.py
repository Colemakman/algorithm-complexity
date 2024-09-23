def find_duplicates(words):
    found = set()
    duplicate = set() 
    for word in low:
        if word in found and word not in duplicate:
            duplicate.add(word)
        else: found.add(word)
    return list(duplicate)
