import unittest
import io
import sys
import os
from main import students_report

class TestStudentsPerformance(unittest.TestCase):

    def test_output(self):

        test_file = "test.csv"
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("""student_name,subject,teacher_name,date,grade
Иванов Иван,Математика,Сидоров,2023-10-10,5
Иванов Иван,Физика,Сидоров,2023-10-11,3
Петров Петр,Физика,Иванова,2023-10-11,4
""")

        captured_output = io.StringIO()
        sys.stdout = captured_output

        students_report(["test.csv"])

        output = captured_output.getvalue()

        self.assertIn("Иванов Иван", output)
        self.assertIn("Петров Петр", output)
        self.assertNotIn("grid", output)

        os.remove(test_file)

    def test_empty_file(self):
        empty_file = "empty.csv"
        with open(empty_file, "w", encoding="utf-8") as f:
            f.write("")

        captured_output = io.StringIO()
        sys.stdout = captured_output

        students_report(["empty.csv"])

        output = captured_output.getvalue()

        self.assertNotIn("Иванов", output)
        self.assertNotIn("Петров", output)

        self.assertIn("student_name", output)
        self.assertIn("grade", output)

        os.remove(empty_file)


if __name__ == "__main__":
    unittest.main()
