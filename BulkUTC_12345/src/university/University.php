<?php

require_once "AbstractUniversity.php";
require_once "Student.php";
require_once "Subject.php";

/**
 * Class University
 * 
 * Concrete implementation of the AbstractUniversity class for managing university operations.
 */
class University extends AbstractUniversity
{
    private $students = [];
    private $subjects = [];
    private $enrollments = [];

    /**
     * Add a student to the university.
     *
     * @param Student $student The student to add
     */
    public function addStudent(Student $student): void
    {
        $this->students[$student->getId()] = $student;
    }

    /**
     * Remove a student from the university.
     *
     * @param string $studentId The ID of the student to remove
     * @return bool True if the student was removed, false if not found
     */
    public function removeStudent(string $studentId): bool
    {
        if (isset($this->students[$studentId])) {
            unset($this->students[$studentId]);
            // Remove student from all enrollments
            foreach ($this->enrollments as $subjectCode => $enrolledStudents) {
                $this->enrollments[$subjectCode] = array_diff($enrolledStudents, [$studentId]);
            }
            return true;
        }
        return false;
    }

    /**
     * Add a subject to the university.
     *
     * @param Subject $subject The subject to add
     */
    public function addSubject(Subject $subject): void
    {
        $this->subjects[$subject->getCode()] = $subject;
    }

    /**
     * Remove a subject from the university.
     *
     * @param string $subjectCode The code of the subject to remove
     * @return bool True if the subject was removed, false if not found
     */
    public function removeSubject(string $subjectCode): bool
    {
        if (isset($this->subjects[$subjectCode])) {
            unset($this->subjects[$subjectCode]);
            // Remove subject from enrollments
            unset($this->enrollments[$subjectCode]);
            return true;
        }
        return false;
    }

    /**
     * Enroll a student in a subject.
     *
     * @param string $studentId The ID of the student to enroll
     * @param string $subjectCode The code of the subject to enroll in
     * @return bool True if enrollment was successful, false otherwise
     */
    public function enrollStudentInSubject(string $studentId, string $subjectCode): bool
    {
        if (isset($this->students[$studentId]) && isset($this->subjects[$subjectCode])) {
            if (!isset($this->enrollments[$subjectCode])) {
                $this->enrollments[$subjectCode] = [];
            }
            if (!in_array($studentId, $this->enrollments[$subjectCode])) {
                $this->enrollments[$subjectCode][] = $studentId;
                return true;
            }
        }
        return false;
    }

    /**
     * Get all students enrolled in a specific subject.
     *
     * @param string $subjectCode The code of the subject
     * @return array An array of Student objects enrolled in the subject
     */
    public function getEnrolledStudents(string $subjectCode): array
    {
        if (isset($this->enrollments[$subjectCode])) {
            return array_map(function($studentId) {
                return $this->students[$studentId];
            }, $this->enrollments[$subjectCode]);
        }
        return [];
    }

    /**
     * Get all subjects a student is enrolled in.
     *
     * @param string $studentId The ID of the student
     * @return array An array of Subject objects the student is enrolled in
     */
    public function getStudentSubjects(string $studentId): array
    {
        $studentSubjects = [];
        foreach ($this->enrollments as $subjectCode => $enrolledStudents) {
            if (in_array($studentId, $enrolledStudents)) {
                $studentSubjects[] = $this->subjects[$subjectCode];
            }
        }
        return $studentSubjects;
    }
}