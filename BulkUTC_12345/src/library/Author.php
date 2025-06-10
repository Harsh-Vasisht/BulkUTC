<?php

class Author
{
    private string $name;
    private array $books;

    public function __construct(string $name, array $books = [])
    {
        $this->name = $name;
        $this->books = $books;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function setName(string $name): void
    {
        $this->name = $name;
    }

    public function getBooks(): array
    {
        return $this->books;
    }

    public function setBooks(array $books): void
    {
        $this->books = $books;
    }

    public function addBook(string $title, float $price): Book
    {
        $book = new Book($title, $price, $this);
        $this->books[] = $book;
        return $book;
    }
}