<?php

require_once "AbstractLibrary.php";
require_once "Book.php";
require_once "Author.php";

class Library extends AbstractLibrary
{
    private $books = [];

    public function addBook(Book $book): void
    {
        $this->books[$book->getIsbn()] = $book;
    }

    public function removeBook(string $isbn): bool
    {
        if (isset($this->books[$isbn])) {
            unset($this->books[$isbn]);
            return true;
        }
        return false;
    }

    public function findBookByTitle(string $title): ?Book
    {
        foreach ($this->books as $book) {
            if (strtolower($book->getTitle()) === strtolower($title)) {
                return $book;
            }
        }
        return null;
    }

    public function listBooks(): array
    {
        return array_values($this->books);
    }

    public function findBooksByAuthor(Author $author): array
    {
        return array_filter($this->books, function($book) use ($author) {
            return $book->getAuthor()->getName() === $author->getName();
        });
    }
}