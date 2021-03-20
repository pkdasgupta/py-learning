# Write a program to find out the line number where a given string is present.

def word_finder(fname, word):
    with open(fname) as f:
        lines = f.readlines()
    return int(lines.index([l for l in lines if word in l][0])) + 1

print(word_finder("data.txt", ","))
