from fastapi import FastAPI

BOOKS = [
    {'id': '1', 'title': 'Book One', 'author': 'Author One', 'rating': 5},
    {'id': '2', 'title': 'Book Two', 'author': 'Author Two', 'rating': 4},
    {'id': '3', 'title': 'Book Three', 'author': 'Author Three', 'rating': 3},
    {'id': '4', 'title': 'Book Four', 'author': 'Author Four', 'rating': 2},
    {'id': '5', 'title': 'Book Five', 'author': 'Author Five', 'rating': 1},
]

app = FastAPI()

@app.get("/books")
def get_all_books():
    return BOOKS

# Path params
@app.get("/books/{book_id}")
def get_book_by_id(book_id: str):        
    return {'book_id': book_id}

# Query params
@app.get("/books/")
def get_book_by_dynamic_query(dynamic_query: str):
    query_value = ""
    for query in BOOKS:         
        query_value = query.get(dynamic_query)            
    return {f'{dynamic_query}': query_value}

