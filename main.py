from pprint import pprint

def count_characters(text):
    alphas = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    characters = dict()
    for c in text:
        lc = c.lower()
        if lc not in alphas:
            continue
        if lc not in characters:
            characters[lc] = 1
        else:
            characters[lc] += 1
    return characters

def count_words(text):
    return len(text.split())

def report(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    characters_list = list(character_count.items())
    characters_list.sort(reverse=True, key=lambda x: x[1])
    for pair in characters_list:
        print(f"The '{pair[0]}' character was found {pair[1]} times")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        count = count_characters(file_contents)
        report(word_count, count)

main()
