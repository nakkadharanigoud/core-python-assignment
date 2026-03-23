def calculate_averages(students):
    """Return dictionary of student averages."""
    averages = {}
    for name, marks in students.items():
        averages[name] = round(sum(marks) / len(marks), 2)
    return averages

def find_top_performer(averages):
    """Return the name of the student with the highest average."""
    return max(averages, key=averages.get)


if __name__ == "__main__":
    students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    averages = calculate_averages(students)
    print("Average Marks:", averages)
    print("Top Performer:", find_top_performer(averages))
