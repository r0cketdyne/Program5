#Matthew Stephenson
#04/24/2024
#Program 5
#this prog reads a list of grades, computes the average grade, the median grade, the high and low
#grades, and print a histogram where each * represents one of the counted grade types.
#################################################################################################

def grade_counter(grades):
    """
    This func takes a list of grades and returns a list of counts for each grade range (A-F).
    """
    grade_counts = [0] * 5 # Adjusted to 5 to include F
    for grade in grades:
        if 90 <= grade <= 100:
            grade_counts[0] += 1 # A100
        elif 80 <= grade < 90:
            grade_counts[1] += 1 # B
        elif 70 <= grade < 80:
            grade_counts[2] += 1 # C
        elif 60 <= grade < 70:
            grade_counts[3] += 1 # D
        elif 0 <= grade < 60:
            grade_counts[4] += 1 # F
    return grade_counts

def compute_stats(grades):
    """
    This func computes the average, median, highest, and lowest grades from the given list of grades.
    """
    sorted_grades = sorted(grades)
    grade_counts = grade_counter(sorted_grades)
    total = sum(sorted_grades)
    average = total / len(sorted_grades)
    median_index = len(sorted_grades) // 2
    median = (sorted_grades[median_index] + sorted_grades[~median_index]) / 2
    highest = max(sorted_grades)
    lowest = min(sorted_grades)
    return grade_counts, average, median, highest, lowest

def print_histogram(grades):
    """
    This func logs the computed statistics and a histogram of the grades to the standard i/o
    """
    grade_counts, _, _, _, _ = compute_stats(grades)
    print(f"{len(grades)} grades were read in.")
    print("Average:", "{:.2f}".format(compute_stats(grades)[1]))
    print("Median:", "{:.2f}".format(compute_stats(grades)[2]))
    print("Highest:", "{:.2f}".format(compute_stats(grades)[3]))
    print("Lowest:", "{:.2f}".format(compute_stats(grades)[4]))
    print("HISTOGRAM")
    for i, count in enumerate(grade_counts):
        grade_letter = chr(65 + i) if i < 4 else 'F' # Correctly maps to F for the last index
        print(f"{grade_letter}: {'*' * count}")

grades = []
while True:
    grade = input("Please enter a test grade (-1 to quit): ")
    if grade == "-1":
        break
    grades.append(int(grade))

print_histogram(grades)
