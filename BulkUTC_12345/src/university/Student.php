<?php

/**
 * Class Student
 * 
 * Represents a student in the University Course Management System.
 */
class Student
{
    private string $name;
    private string $studentNumber;

    /**
     * Student constructor.
     *
     * @param string $name The name of the student
     * @param string $studentNumber The student number
     */
    public function __construct(string $name, string $studentNumber)
    {
        $this->name = $name;
        $this->studentNumber = $studentNumber;
    }

    /**
     * Get the name of the student.
     *
     * @return string
     */
    public function getName(): string
    {
        return $this->name;
    }

    /**
     * Set the name of the student.
     *
     * @param string $name
     */
    public function setName(string $name): void
    {
        $this->name = $name;
    }

    /**
     * Get the student number.
     *
     * @return string
     */
    public function getStudentNumber(): string
    {
        return $this->studentNumber;
    }

    /**
     * Set the student number.
     *
     * @param string $studentNumber
     */
    public function setStudentNumber(string $studentNumber): void
    {
        $this->studentNumber = $studentNumber;
    }
}