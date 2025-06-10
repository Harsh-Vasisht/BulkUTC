import pytest
from unittest.mock import Mock, patch
from src.library.Library import Library
from src.shopping_cart.Cart import Cart
from src.university.University import University

@pytest.fixture
def library():
    return Library()

@pytest.fixture
def cart():
    return Cart()

@pytest.fixture
def university():
    return University()

def test_library_workflow(library):
    # Add books to the library
    library.add_book("1984", "George Orwell", "9780451524935", 9.99)
    library.add_book("To Kill a Mockingbird", "Harper Lee", "9780446310789", 12.99)
    
    # Search for books
    results = library.search_books("1984")
    assert len(results) == 1
    assert results[0].title == "1984"
    
    results = library.search_books("Harper Lee")
    assert len(results) == 1
    assert results[0].title == "To Kill a Mockingbird"

def test_shopping_cart_workflow(cart):
    # Add products to the cart
    cart.add_product("Laptop", 999.99, 1)
    cart.add_product("Mouse", 19.99, 2)
    
    # Update quantities
    cart.update_quantity("Laptop", 2)
    
    # Check total
    assert cart.get_total() == 2039.97
    
    # Remove a product
    cart.remove_product("Mouse")
    
    # Check updated total
    assert cart.get_total() == 1999.98

def test_university_workflow(university):
    # Add subjects
    university.add_subject("CS101", "Introduction to Computer Science")
    university.add_subject("MATH101", "Calculus I")
    
    # Add students
    university.add_student("Alice", "S001")
    university.add_student("Bob", "S002")
    
    # Enroll students in subjects
    university.enroll_student("S001", "CS101")
    university.enroll_student("S001", "MATH101")
    university.enroll_student("S002", "CS101")
    
    # Check enrollments
    cs101_students = university.get_enrolled_students("CS101")
    assert len(cs101_students) == 2
    assert "Alice" in [s.name for s in cs101_students]
    assert "Bob" in [s.name for s in cs101_students]
    
    math101_students = university.get_enrolled_students("MATH101")
    assert len(math101_students) == 1
    assert math101_students[0].name == "Alice"

def test_library_error_cases(library):
    with pytest.raises(ValueError):
        library.add_book("", "John Doe", "1234567890", 10.99)  # Empty title
    
    with pytest.raises(ValueError):
        library.add_book("Invalid Book", "John Doe", "invalid_isbn", 10.99)  # Invalid ISBN

def test_shopping_cart_error_cases(cart):
    with pytest.raises(ValueError):
        cart.add_product("Invalid Product", -10, 1)  # Negative price
    
    with pytest.raises(ValueError):
        cart.update_quantity("Nonexistent Product", 5)  # Product not in cart

def test_university_error_cases(university):
    with pytest.raises(ValueError):
        university.add_student("", "S003")  # Empty name
    
    with pytest.raises(ValueError):
        university.enroll_student("S999", "CS101")  # Non-existent student

def test_combined_workflow(library, cart, university):
    # Library: Add a textbook
    library.add_book("Python Programming", "John Smith", "9781234567890", 59.99)
    
    # Shopping Cart: Purchase the textbook
    cart.add_product("Python Programming Textbook", 59.99, 1)
    assert cart.get_total() == 59.99
    
    # University: Add a Python course and enroll a student
    university.add_subject("CS202", "Advanced Python Programming")
    university.add_student("Charlie", "S003")
    university.enroll_student("S003", "CS202")
    
    # Verify the flow
    book = library.search_books("Python Programming")[0]
    assert book.title == "Python Programming"
    
    enrolled_students = university.get_enrolled_students("CS202")
    assert len(enrolled_students) == 1
    assert enrolled_students[0].name == "Charlie"
    
    # Simulate book purchase for the course
    cart.add_product("Python Programming Textbook", 59.99, 1)
    assert cart.get_total() == 119.98  # Two textbooks now

if __name__ == "__main__":
    pytest.main()