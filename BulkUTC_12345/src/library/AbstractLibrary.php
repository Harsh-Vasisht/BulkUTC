<?php

/**
 * Abstract class AbstractLibrary
 * 
 * This class defines the structure and common methods for the Library Management System.
 */
abstract class AbstractLibrary
{
    /**
     * @var Author[]
     */
    protected $authors = [];

    /**
     * Add an author to the library.
     *
     * @param string $authorName
     * @return Author
     */
    abstract public function addAuthor(string $authorName): Author;

    /**
     * Add a book for a specific author.
     *
     * @param string $authorName
     * @param Book $book
     */
    abstract public function addBookForAuthor(string $authorName, Book $book): void;

    /**
     * Get books for a specific author.
     *
     * @param string $authorName
     * @return Book[]
     */
    abstract public function getBooksForAuthor(string $authorName): array;

    /**
     * Search for a book by its name.
     *
     * @param string $bookName
     * @return Book|null
     */
    abstract public function search(string $bookName): ?Book;

    /**
     * Print all authors and their books.
     */
    abstract public function print(): void;

    /**
     * Get all authors.
     *
     * @return Author[]
     */
    public function getAuthors(): array
    {
        return $this->authors;
    }

    /**
     * Set authors.
     *
     * @param Author[] $authors
     */
    public function setAuthors(array $authors): void
    {
        $this->authors = $authors;
    }
}