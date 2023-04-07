from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    unittest_student_name = "UnitTestName"
    unittest_courses_empty_dict = {}
    courses_setup = {"OOP": ["tests", ], }

    def setUp(self):
        self.student = Student("UnitTestName", None)

    def test_initialization(self):
        self.assertEqual(self.unittest_student_name, self.student.name)
        self.assertEqual(self.unittest_courses_empty_dict, self.student.courses)

    def test_enroll_return_course_already_added_notes_are_updated(self):
        course, notes, to_add = "OOP", ["NotToAdd", "ToAdd"], "ToAdd"
        self.student.courses = self.courses_setup
        result = self.student.enroll(course, notes, to_add)
        self.courses_setup[course] += to_add
        self.assertEqual(self.courses_setup, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_return_course_and_notes_added_if_trigger_is_Y_string(self):
        self.student.courses = self.courses_setup
        course_y, notes_y, trigger_y = "WEB", ["NoteToAdd1", "NoteToAdd2"], "Y"

        result = self.student.enroll(course_y, notes_y, trigger_y)

        self.courses_setup[course_y] = notes_y
        self.assertEqual(self.courses_setup, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_return_course_and_notes_added_if_trigger_is_empty_string(self):
        self.student.courses = self.courses_setup
        course_es, notes_es, trigger_es = "JS", ["Note_1", "Note_2"], ""

        result = self.student.enroll(course_es, notes_es, trigger_es)

        self.courses_setup[course_es] = notes_es
        self.assertEqual(self.courses_setup, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_if_course_not_in_courses(self):
        test_course, notes_list, notes_trigger = "OOP", ["must", "not", "be", "added", ], "Z-z-z, wake UP!"
        result = self.student.enroll(test_course, notes_list, notes_trigger)
        self.assertEqual({"OOP": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_method_return_notes_are_added_to_available_course(self):
        self.student.courses = self.courses_setup
        new_notes = "abracdabra"
        result = self.student.add_notes("OOP", new_notes)
        self.courses_setup["OOP"].append(new_notes)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_method_return_exception_of_un_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("OOP", "abrcadabra")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_success_remove(self):
        self.student.courses = {"OOP": []}
        result = self.student.leave_course("OOP")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_raises_exception_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
