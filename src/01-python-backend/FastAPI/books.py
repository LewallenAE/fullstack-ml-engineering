from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title one', 'author': 'Author one', 'category': 'science'},
    {'title': 'Title two', 'author': 'Author two', 'category': 'history'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'english'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'math'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'computer science'},
    {'title': 'Title six', 'author': 'Author six', 'category': 'machine learning'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{category}")
async def read_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books")
async def read_category_query(category: str = None):
    if category:
        books_to_return = []
        for book in BOOKS:
            if book.get('category').casefold() == category.casefold():
                books_to_return.append(book)
        return books_to_return
    return BOOKS


@app.get("/book/")
async def read_author_query(author: str =None):
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
            if book.get('author').casefold() == author.casefold()
            ]

    if category:
        books_to_return = [
            book for book in books_to_return
            if book.get('category').casefold() == category.casefold()
            ]

    return books_to_return

