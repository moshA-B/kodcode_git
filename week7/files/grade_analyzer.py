import csv
import os
def create_grades_file(filename):
    students = [
    ("Dan", [85, 90, 78]),
    ("MOMO", [92, 88, 95]),
    ("Yoni", [70, 65, 80]),
    ("Avi", [100, 95, 98]),
    ("Sara", [60, 72, 68]),]

    with open(filename, "w", encoding="utf-8") as f:
        for line in students:
            a,b,c = line[1]
            f.writelines(f"{line[0]}, {a}, {b}, {c} {"\n"}")


def calculate_average(filename):
    averages = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            grades = csv.reader(f)
            for row in grades:
                averages[row[0]] = sum(map(int, row[1::])) / 3
        return averages

def save_result(averages, output_filename):
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("=== student results ===\n")
        count = 1
        for i in sorted(averages,key=averages.get, reverse=True):
            f.write(f"{count}. {i}: {averages[i] :.1f} {"\n"}")
            count += 1
            
    return

def statistics(average, output_filename):
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("===statistics===\n")

        f.write(f"class average {sum(average.values())/len(average):.1f}{"\n"}")

        f.write("highest: {0},{1:.1f}\n".format(*max(average.items(), key=lambda x : x[1])))
        f.write("lowest: {0}, {1:.1f}\n".format(*min(average.items(), key=lambda x : x[1])))
        f.write(f"passing: {str(len([k for k,v in average.items() if v > 60]))}")





av = calculate_average("grades.txt")
save_result(av, "result.txt")
stat = statistics(av, "statistics.txt")
