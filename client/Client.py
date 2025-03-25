import requests

def add_book(book):
    url = 'http://localhost:5000/add_book'
    response = requests.post(url, json=book)
    print(response.json())

def delete_book(book):
    url = 'http://localhost:5000/delete_book'
    response = requests.delete(url, json=book)
    print(response.json())

if __name__ == '__main__':
    print("CLIENT APPLICATION STARTING")
    print("now")
    print("work")

    book_to_add = {"title": "Python 101", "author": "John Doe"}
    add_book(book_to_add)
    delete_book(book_to_add)