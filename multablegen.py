# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.
# Place these files in a folder for a 13- year old boy.

def multabgen(n):
    tab = f"Table of {n} \n\n"
    for i in range(1, 11):
        tab += f"{n} X {i} = {n*i}\n"
    return tab


for num in range(2, 21):
    with open(f"tables/table_of_{num}.txt", "w") as f:
        f.write(f"{multabgen(num)}")
