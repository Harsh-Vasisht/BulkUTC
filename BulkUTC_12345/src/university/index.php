<?php

declare(strict_types=1);

require_once __DIR__ . '/Student.php';
require_once __DIR__ . '/Subject.php';
require_once __DIR__ . '/University.php';

// Create a new University instance
$university = new University();

// Add subjects to the university
$webII = $university->addSubject(new Subject('112', 'Web II', 3));
$webIII = $university->addSubject(new Subject('113', 'Web III', 4));

// Add students to subjects
$university->addStudentToSubject($webII, new Student('George', '123', 'george@example.com'));
$university->addStudentToSubject($webII, new Student('Mary', '234', 'mary@example.com'));
$university->addStudentToSubject($webII, new Student('David', '345', 'david@example.com'));

$university->addStudentToSubject($webIII, new Student('Bob', '456', 'bob@example.com'));
$university->addStudentToSubject($webIII, new Student('Brad', '567', 'brad@example.com'));

// Get the total number of students
echo "Total number of students: " . $university->getNumberOfStudents() . "\n";

// Print all subjects and their students
$university->printSubjectsAndStudents();