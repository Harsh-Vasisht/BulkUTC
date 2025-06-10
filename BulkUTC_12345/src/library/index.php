<?php

require_once "Book.php";
require_once "Library.php";
require_once "Author.php";

// Create a new Library instance
$library = new Library();

// Add authors
$jackLondon = $library->addAuthor('Jack London', 'American novelist and journalist');
$markTwain = $library->addAuthor('Mark Twain', 'American writer and humorist');

// Add books for Jack London
$jackLondon->addBook("Martin Eden", 55);
$jackLondon->addBook("The Game", 35);
$library->addBookForAuthor('Jack London', new Book("A Son of the Sun", 25, $jackLondon));

// Add books for Mark Twain
$markTwain->addBook('The Adventures of Tom Sawyer', 65);
$markTwain->addBook('Luck', 12);

// Search for a book and get its author
$book = $library->search('Martin Eden');
if ($book) {
    $author = $book->getAuthor();
    echo "Author of 'Martin Eden': " . $author->getName() . "\n";
} else {
    echo "Book 'Martin Eden' not found.\n";
}

// Print the library catalog
$library->print();

?>