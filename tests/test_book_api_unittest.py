from api.book_api import add_book_to_list, books


# Test the add_book_to_list function
def test_add_book_to_list():
    book = {"title": "Python 101", "author": "John Doe"}
    response, status_code = add_book_to_list(book)

    # Check if the book was added
    assert status_code == 201
    assert response["message"] == "Book added successfully!"
    assert book in books  # Ensure the book is in the list


