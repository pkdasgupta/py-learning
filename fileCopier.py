# Write a program to make a copy of a given text file.

def file_copier(fname):
    with open(fname) as f:
        with open(f"copy_of_{fname}", "w") as g:
            g.write(f.read())


def file_detector(f1, f2):
    with open(f1) as f1:
        with open(f2) as f2:
            if f1.read() == f2.read():
                return True


file_copier("data.txt")

fname1 = "data.txt"
fname2 = "copy_of_data.txt"

if file_detector(fname1, fname2):
    print(f"\n Verified that the files {fname1} and {fname2} are identical.")
else:
    print(f"\n Verified that the files {fname1} and {fname2} are NOT identical.")
