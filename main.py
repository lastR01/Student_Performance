import argparse
import csv
from collections import defaultdict
from tabulate import tabulate


def read_csv_files(files):
    rows = []
    for file in files:
        with open(file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows.extend(list(reader))
    return rows


def students_report(files):
    rows = read_csv_files(files)

    grades = defaultdict(list)
    for row in rows:
        grades[row["student_name"]].append(float(row["grade"]))

    averages = {}
    for student, grades in grades.items():
        averages[student] = sum(grades) / len(grades)

    sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    table = []
    for count, (name, grade) in enumerate(sorted_students):
        table.append([count + 1, name, grade])

    print(tabulate(table, headers=["student_name", "grade"], tablefmt="grid"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    if args.report == "students-report":
        students_report(args.files)
    else:
        print(f"Неизвестный отчет: {args.report}")


if __name__ == "__main__":
    main()
