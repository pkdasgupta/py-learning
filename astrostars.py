# Program to print Stars (*) in patterns taking user input for no. of rows and a Y/N flag.

from termcolor import cprint


def pstars(r, f):
    if f:
        for i in range(1, r+1):
            cprint("* " * (r + 1 - i), "blue")
    else:
        for i in range(1, r+1):
            cprint("* " * i, "red")


nrows = int(input("\n How many Rows do you want? : "))
flag = input("\n Do you want them upwards? (Y/N) : ")

if flag == "Y":
    fg = True
else:
    fg = False

cprint("\n Here are your stars : \n", "green")
pstars(nrows, fg)
