from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for books
books = []

# Function to add a book
def add_book_to_list(book):
    """Adds a book to the list."""
    books.append(book)
    return {"message": "Book added successfully!"}, 201

# Function to delete a book
def delete_book_from_list(book):
    """Deletes a book from the list."""
    if book in books:
        books.remove(book)
        return {"message": "Book deleted successfully!"}, 200
    else:
        return {"message": "Book not found!"}, 404


@app.route('/add_book', methods=['POST'])
def add_book():
    book = request.json
    return add_book_to_list(book)

@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    book = request.json
    return delete_book_from_list(book)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
