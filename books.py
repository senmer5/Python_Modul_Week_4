import json

FILE_NAME = "kitap.json"

# Kitapları yükle
def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)  # Kitapları liste olarak döndürüyoruz
    except FileNotFoundError:
        print("Books file not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding books JSON file.")
        return []

# Kitapları kaydet
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Kitapları listele
def list_books():
    books = load_books()

    if not books:
        print("No books available.")
    else:
        print("Available Books:")
        for book in books:
            print(f"Barkod: {book['Barkod']}")
            print(f"Title: {book['Kitap_Adi']}")
            print(f"Author: {book['Yazar']}")
            print(f"Publisher: {book['Yayinevi']}")
            print(f"Language: {book['Dil']}")
            print(f"Price: {book['Fiyat']}")
            print("----------------------------")

# Kitap ekle
def add_book():
    books = load_books()

    barkod = int(input("Enter the barcode: "))
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    publisher = input("Enter the publisher: ")
    language = input("Enter the language: ")
    price = float(input("Enter the price: "))

    new_book = {
        "Barkod": barkod,
        "Kitap_Adi": title,
        "Yazar": author,
        "Yayinevi": publisher,
        "Dil": language,
        "Fiyat": price
    }

    books.append(new_book)  # Kitap listesine ekliyoruz
    save_books(books)
    print("Book added successfully.")

# Kitap ara
def search_book():
    books = load_books()

    barkod = int(input("Enter the barcode of the book to search: "))
    
    found = False
    for book in books:
        if book['Barkod'] == barkod:
            print(f"Book found: {book['Kitap_Adi']} by {book['Yazar']}")
            print(f"Barkod: {book['Barkod']}, Publisher: {book['Yayinevi']}, Price: {book['Fiyat']}")
            found = True
            break

    if not found:
        print("Book not found.")

# Kitap sil
def delete_book():
    books = load_books()

    barkod = int(input("Enter the barcode of the book to delete: "))
    
    book_found = False
    for book in books:
        if book['Barkod'] == barkod:
            books.remove(book)  # Kitabı listeden çıkarıyoruz
            book_found = True
            break

    if book_found:
        save_books(books)
        print(f"Book with barcode {barkod} has been deleted.")
    else:
        print("Book not found.")