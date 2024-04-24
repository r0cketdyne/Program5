#Matthew Stephenson
#04/20/2024
#Program 5
#this prog reads a list of grades, computes the average grade, the median grade, the high and low
#grades, and print a histogram where each * represents one of the counted grade types.
#################################################################################################
def grade_counter(grades):
    """
    This function takes a list of grades and returns a list of counts for each grade range (A-F).
    """
    grade_counts = [0] * 5
    for grade in grades:
        grade_counts[grade // 10] += 1
    return grade_counts

def compute_stats(grades):
    """
    This func computes the average, median, highest, and lowest grades from the given list of grades.
    """
    grade_counts = grade_counter(grades)
    total = sum(grades)
    average = total / len(grades)
    median = sorted(grades)[len(grades) // 2]
    highest = max(grades)
    lowest = min(grades)
    return grade_counts, average, median, highest, lowest

def print_histogram(grades):
    """
    This func logs the computed statistics and a histogram of the grades to the standard i/o
    """
    grade_counts, average, median, highest, lowest = compute_stats(grades)
    print("Average:", average)
    print("Median:", median)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("HISTOGRAM")
    for grade in range(10):
        print(f"{chr(grade + 65)}: {'*' * grade_counts[grade // 10]}")

grades = []
while True:
    grade = input("Please enter a test grade (-1 to quit): ")
    if grade == "-1":
        break
    grades.append(int(grade))

print_histogram(grades)