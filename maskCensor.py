# A file contains the word “Donkey” multiple times.
# You need to write a program which replaces this word with ******
# BY UPDATING THE SAME FILE.

def mask_censor(fname, cenwords):
    # Opening the file to read the data
    with open(fname) as f:
        data = f.read()

    # Replacing each Censored word with *****
    for word in cenwords:
        if word in data:
            data = data.replace(word, "*****")

    # Writing the masked data back to file
    with open(fname, 'w') as f:
        f.write(data)



mask_censor("data.txt", ['asshole', 'fuck', 'bastard'])
