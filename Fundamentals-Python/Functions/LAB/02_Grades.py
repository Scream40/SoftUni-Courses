def grade_word (grade: float):

    if 2.00 <= grade <= 2.99:
        grade = "Fail"
    elif 3.00 <= grade <= 3.49:
        grade = "Poor"
    elif 3.50 <= grade <= 4.49:
        grade = "Good"
    elif 4.50 <= grade <= 5.49:
        grade = "Very Good"
    elif 5.50 <= grade <= 6.00:
        grade = "Excellent"

    return grade
grade_input = float(input())

print(grade_word(grade_input))
