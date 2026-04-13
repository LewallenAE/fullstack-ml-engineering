from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category': 'science'},
    {'title': 'Title two', 'author': 'Author two', 'category': 'history'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'english'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'math'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'computer science'},
    {'title': 'Title six', 'author': 'Author six', 'category': 'machine learning'},
    {'title': 'Title seven', 'author': 'Author two', 'category': 'quantum physics'},
    {'title': 'Title eight', 'author': 'Author two', 'category': 'renaissance art'},
    {'title': 'Title nine', 'author': 'Author two', 'category': 'manga drawing'},
    {'title': 'Title ten', 'author': 'Author two', 'category': 'teaching'},
]

# all
@app.get("/books")
async def read_all_books():
    return BOOKS

# path parameter
@app.get("/books/category/{category}")
async def read_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Query
@app.get("/books/")
async def read_category_query(category: str = None):
    if category:
        books_to_return = []
        for book in BOOKS:
            if book.get('category').casefold() == category.casefold():
                books_to_return.append(book)
        return books_to_return
    return BOOKS


@app.get("/book/search/")
async def read_author_query(author: str = None):
    if author:
        books_to_return = []
        for book in BOOKS:
            if book.get('author').casefold() == author.casefold():
                books_to_return.append(book)
        return books_to_return
    return BOOKS

@app.get("/book/")
async def read_author_or_category_query(author:str = None, category: str = None):

    books_to_return = BOOKS

    if author:
        books_to_return = [
            book for book in books_to_return
            if book.get('author', "").casefold() == author.casefold()
            ]

    if category:
        books_to_return = [
            book for book in books_to_return
            if book.get('category', "").casefold() == category.casefold()
            ]

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str) -> None:
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get("/books/author/{author}")
async def get_book_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author', "").casefold().strip() == author.casefold().strip():
            books_to_return.append(book)
    return books_to_return

