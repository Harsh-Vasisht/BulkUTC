import unittest
from typing import List, Dict

# Mock implementations of external dependencies

class Student:
    def __init__(self, id: str, name: str):
        self._id = id
        self._name = name

    def getId(self) -> str:
        return self._id

    def getName(self) -> str:
        return self._name

class Subject:
    def __init__(self, code: str, name: str):
        self._code = code
        self._name = name

    def getCode(self) -> str:
        return self._code

    def getName(self) -> str:
        return self._name

class AbstractUniversity:
    pass

# Implementation of the University class
class University(AbstractUniversity):
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.subjects: Dict[str, Subject] = {}
        self.enrollments: Dict[str, List[str]] = {}

    def addStudent(self, student: Student) -> None:
        self.students[student.getId()] = student

    def removeStudent(self, studentId: str) -> bool:
        if studentId in self.students:
            del self.students[studentId]
            for subjectCode in self.enrollments:
                self.enrollments[subjectCode] = [sid for sid in self.enrollments[subjectCode] if sid != studentId]
            return True
        return False

    def addSubject(self, subject: Subject) -> None:
        self.subjects[subject.getCode()] = subject

    def removeSubject(self, subjectCode: str) -> bool:
        if subjectCode in self.subjects:
            del self.subjects[subjectCode]
            if subjectCode in self.enrollments:
                del self.enrollments[subjectCode]
            return True
        return False

    def enrollStudentInSubject(self, studentId: str, subjectCode: str) -> bool:
        if studentId in self.students and subjectCode in self.subjects:
            if subjectCode not in self.enrollments:
                self.enrollments[subjectCode] = []
            if studentId not in self.enrollments[subjectCode]:
                self.enrollments[subjectCode].append(studentId)
                return True
        return False

    def getEnrolledStudents(self, subjectCode: str) -> List[Student]:
        if subjectCode in self.enrollments:
            return [self.students[studentId] for studentId in self.enrollments[subjectCode]]
        return []

    def getStudentSubjects(self, studentId: str) -> List[Subject]:
        return [self.subjects[subjectCode] for subjectCode, enrolledStudents in self.enrollments.items() if studentId in enrolledStudents]

# Test cases for the University class
class TestUniversity(unittest.TestCase):
    def setUp(self):
        self.university = University()
        self.student1 = Student("S001", "John Doe")
        self.student2 = Student("S002", "Jane Smith")
        self.subject1 = Subject("COMP101", "Introduction to Programming")
        self.subject2 = Subject("MATH201", "Linear Algebra")

    def test_add_and_remove_student(self):
        self.university.addStudent(self.student1)
        self.assertIn(self.student1.getId(), self.university.students)
        
        removed = self.university.removeStudent(self.student1.getId())
        self.assertTrue(removed)
        self.assertNotIn(self.student1.getId(), self.university.students)
        
        removed = self.university.removeStudent("non_existent_id")
        self.assertFalse(removed)

    def test_add_and_remove_subject(self):
        self.university.addSubject(self.subject1)
        self.assertIn(self.subject1.getCode(), self.university.subjects)
        
        removed = self.university.removeSubject(self.subject1.getCode())
        self.assertTrue(removed)
        self.assertNotIn(self.subject1.getCode(), self.university.subjects)
        
        removed = self.university.removeSubject("non_existent_code")
        self.assertFalse(removed)

    def test_enroll_student_in_subject(self):
        self.university.addStudent(self.student1)
        self.university.addSubject(self.subject1)
        
        enrolled = self.university.enrollStudentInSubject(self.student1.getId(), self.subject1.getCode())
        self.assertTrue(enrolled)
        self.assertIn(self.student1.getId(), self.university.enrollments[self.subject1.getCode()])
        
        # Try to enroll the same student again
        enrolled = self.university.enrollStudentInSubject(self.student1.getId(), self.subject1.getCode())
        self.assertFalse(enrolled)
        
        # Try to enroll a non-existent student
        enrolled = self.university.enrollStudentInSubject("non_existent_id", self.subject1.getCode())
        self.assertFalse(enrolled)

    def test_get_enrolled_students(self):
        self.university.addStudent(self.student1)
        self.university.addStudent(self.student2)
        self.university.addSubject(self.subject1)
        
        self.university.enrollStudentInSubject(self.student1.getId(), self.subject1.getCode())
        self.university.enrollStudentInSubject(self.student2.getId(), self.subject1.getCode())
        
        enrolled_students = self.university.getEnrolledStudents(self.subject1.getCode())
        self.assertEqual(len(enrolled_students), 2)
        self.assertIn(self.student1, enrolled_students)
        self.assertIn(self.student2, enrolled_students)
        
        # Test for a subject with no enrollments
        self.university.addSubject(self.subject2)
        enrolled_students = self.university.getEnrolledStudents(self.subject2.getCode())
        self.assertEqual(len(enrolled_students), 0)

    def test_get_student_subjects(self):
        self.university.addStudent(self.student1)
        self.university.addSubject(self.subject1)
        self.university.addSubject(self.subject2)
        
        self.university.enrollStudentInSubject(self.student1.getId(), self.subject1.getCode())
        self.university.enrollStudentInSubject(self.student1.getId(), self.subject2.getCode())
        
        student_subjects = self.university.getStudentSubjects(self.student1.getId())
        self.assertEqual(len(student_subjects), 2)
        self.assertIn(self.subject1, student_subjects)
        self.assertIn(self.subject2, student_subjects)
        
        # Test for a student with no enrollments
        self.university.addStudent(self.student2)
        student_subjects = self.university.getStudentSubjects(self.student2.getId())
        self.assertEqual(len(student_subjects), 0)

    def test_remove_student_from_enrollments(self):
        self.university.addStudent(self.student1)
        self.university.addSubject(self.subject1)
        self.university.enrollStudentInSubject(self.student1.getId(), self.subject1.getCode())
        
        self.university.removeStudent(self.student1.getId())
        enrolled_students = self.university.getEnrolledStudents(self.subject1.getCode())
        self.assertEqual(len(enrolled_students), 0)

    def test_remove_subject_from_enrollments(self):
        self.university.addStudent(self.student1)
        self.university.addSubject(self.subject1)
        self.university.enrollStudentInSubject(self.student1.getId(), self.subject1.getCode())
        
        self.university.removeSubject(self.subject1.getCode())
        student_subjects = self.university.getStudentSubjects(self.student1.getId())
        self.assertEqual(len(student_subjects), 0)

if __name__ == '__main__':
    unittest.main()