import os
with open("diary.txt", "w" , encoding="utf-8") as f:
    f.write("today was a good day\n")
    f.write("the sun was shinning \n")
    f.write("motherfucker\n")
    print("file created successfully")

with open("diary.txt", "r") as f:
    print(f.read())

def add_entry(filename, date, content):
    with open(filename, "a", encoding= "utf-8") as f:
        f.write(f"{date}: {content}")


def search_diary(filename, keyword):
    entry = ""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for row in f:
                if keyword in row:
                    entry += row + "\n"
        return entry.strip()


    
with open("result.txt", "r") as f:
    print(f.read().split("\n"))

