<?php

/**
 * Class Subject
 * 
 * Represents a subject in the University Course Management System.
 */
class Subject
{
    private string $code;
    private string $name;
    /**
     * @var Student[]
     */
    private array $students = [];

    /**
     * Subject constructor.
     *
     * @param string $code The subject code
     * @param string $name The subject name
     */
    public function __construct(string $code, string $name)
    {
        $this->code = $code;
        $this->name = $name;
    }

    /**
     * Get the subject code.
     *
     * @return string
     */
    public function getCode(): string
    {
        return $this->code;
    }

    /**
     * Set the subject code.
     *
     * @param string $code
     */
    public function setCode(string $code): void
    {
        $this->code = $code;
    }

    /**
     * Get the subject name.
     *
     * @return string
     */
    public function getName(): string
    {
        return $this->name;
    }

    /**
     * Set the subject name.
     *
     * @param string $name
     */
    public function setName(string $name): void
    {
        $this->name = $name;
    }

    /**
     * Get the list of students enrolled in this subject.
     *
     * @return Student[]
     */
    public function getStudents(): array
    {
        return $this->students;
    }

    /**
     * Add a student to this subject.
     *
     * @param Student $student
     * @return Student
     */
    public function addStudent(Student $student): Student
    {
        $this->students[] = $student;
        return $student;
    }
}