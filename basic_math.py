from statistics import median, mode, multimode, mean


test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]
essay_grades = [93, 97, 84, 91, 87, 68, 63, 72, 75, 89]

min_grade = min(test_grades)
median_grade = median(test_grades)
max_grade = max(test_grades)
min_essay = min(essay_grades)
median_essay = median(essay_grades)
max_essay = max(essay_grades)
print(f"The min, median and max test grade is: {min_grade}, {median_grade}, {max_grade}")
print(f"The min, median and max essay grade is: {min_essay}, {median_essay}, {max_essay}")


test_mode = mode(test_grades)
print(f"The most often seen grade is: {test_mode}")

essay_mode = mode(essay_grades)
print(f"The most often seen essay grade is: {essay_mode}")

project_grades = [80, 75, 68, 80, 92, 84, 77, 100, 100, 88, 82]
project_mode = multimode(project_grades)
print(f"The most often seen project grade is: {project_mode}")

test_average = mean(test_grades)
essay_average = mean(essay_grades)

print(f"The average test grade is: {test_average}")
print(f"The average essay grade is: {essay_average}")

test_grades = [98, 100, 54, 70, 83, 83, 75, 68, 83, 91, 75]

passed = 0
total_grades = len(test_grades)

for grade in test_grades:
    if grade >= 70:
        passed += 1

percentage_passed = round(passed / total_grades * 100)

print(f"The number of students who passed: {passed}")
print(f"The number of students who did not pass: {total_grades - passed}")
print(f"The percentage of students who passed: {percentage_passed}")
print(f"The percentage of students who did not pass: {100 - percentage_passed}")
