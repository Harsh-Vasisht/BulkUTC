<?php

declare(strict_types=1);

/**
 * Abstract class representing a university in the University Course Management System.
 */
abstract class AbstractUniversity
{
    /**
     * @var Subject[]
     */
    protected array $subjects = [];

    /**
     * Adds a new subject to the university.
     *
     * @param string $code The subject code
     * @param string $name The subject name
     * @return Subject The newly created subject
     */
    abstract public function addSubject(string $code, string $name): Subject;

    /**
     * Adds a student to a specific subject.
     *
     * @param string $subjectCode The code of the subject
     * @param Student $student The student to be added
     * @return void
     */
    abstract public function addStudentOnSubject(string $subjectCode, Student $student): void;

    /**
     * Retrieves all students enrolled in a specific subject.
     *
     * @param string $subjectCode The code of the subject
     * @return Student[] An array of students enrolled in the subject
     */
    abstract public function getStudentsForSubject(string $subjectCode): array;

    /**
     * Gets the total number of students enrolled in all subjects.
     *
     * @return int The total number of students
     */
    abstract public function getNumberOfStudents(): int;

    /**
     * Prints information about all subjects and their enrolled students.
     *
     * @return void
     */
    abstract public function print(): void;
}