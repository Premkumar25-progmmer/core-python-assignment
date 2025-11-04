def find_average(marks):
    avg_marks = {}
    for name, scores in marks.items():
        avg = sum(scores) / len(scores)
        avg_marks[name] = round(avg, 2)
    return avg_marks
def top_student(avg_marks):
    top_name = max(avg_marks, key=avg_marks.get)
    return top_name
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
average_marks = find_average(students)
topper = top_student(average_marks)
print("Average Marks:", average_marks)
print("Top Performer:", topper)
