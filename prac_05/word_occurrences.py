def word_count():
    string = input("Enter a string: ")
    words = string.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_word_length = max(len(word) for word in word_counts.keys())

    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


word_count()
