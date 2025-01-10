from datetime import datetime, timedelta
import json

MEMBERS_FILE = "user.json"
BOOKS_FILE = "kitap.json"

# Kitapları yükle
def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Books file not found.")
        return []
    except json.JSONDecodeError:
        print("Error loading books.")
        return []

# Üyeleri yükle
def load_members():
    try:
        with open(MEMBERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Members file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error loading members.")
        return {}

# Kitap ödünç verme
def lend_book():
    members = load_members()
    books = load_books()

    if not books:
        print("No books available.")
        return

    # Üye bilgilerini al
    member_id = input("Enter member ID for book lending: ")
    if member_id not in members:
        print("Member not found.")
        return

    # Kitapları listele ve seçim yap
    print("Available Books:")
    for book in books:
        print(f"Barkod: {book['Barkod']}, Title: {book['Kitap_Adi']}")

    book_barkod = input("Enter book barcode to lend: ")
    
    # Seçilen kitabın barkodunu doğrula
    selected_book = None
    for book in books:
        if str(book['Barkod']) == book_barkod:
            selected_book = book
            break

    if not selected_book:
        print("Book not found.")
        return

    # Kitap ödünç alma işlemi
    current_date = datetime.now()
    return_date = current_date + timedelta(weeks=2)  # 2 hafta sonra teslim tarihi
    members[member_id]['book_lend_date'] = current_date.strftime('%Y-%m-%d')
    members[member_id]['book_return_date'] = return_date.strftime('%Y-%m-%d')
    members[member_id]['lent_book_barkod'] = book_barkod  # Hangi kitabı ödünç aldı bilgisi

    # Üye bilgilerini kaydet
    with open(MEMBERS_FILE, "w") as file:
        json.dump(members, file, indent=4)

    print(f"Book lent to member {members[member_id]['name']}.")
    print(f"Book must be returned by: {return_date.strftime('%Y-%m-%d')}")

# Kitap iade etme
def return_book():
    members = load_members()

    # Üye bilgilerini al
    member_id = input("Enter member ID for book return: ")
    if member_id not in members:
        print("Member not found.")
        return

    lent_book_barkod = members[member_id].get('lent_book_barkod', None)
    if lent_book_barkod:
        return_date_str = members[member_id].get('book_return_date', None)
        if return_date_str:
            return_date = datetime.strptime(return_date_str, '%Y-%m-%d')
            current_date = datetime.now()

            if current_date > return_date:
                print(f"Book returned late! Returned on: {current_date.strftime('%Y-%m-%d')}")
            else:
                print(f"Book returned on time. Returned on: {current_date.strftime('%Y-%m-%d')}")

            # İade işlemi yapıldıktan sonra teslim tarihi bilgileri siliniyor
            del members[member_id]['book_lend_date']
            del members[member_id]['book_return_date']
            del members[member_id]['lent_book_barkod']

            # Üye bilgilerini kaydet
            with open(MEMBERS_FILE, "w") as file:
                json.dump(members, file, indent=4)

            print(f"Book returned by member {members[member_id]['name']}.")
        else:
            print("No book found to return.")
    else:
        print("No book lent to this member.")

# Kitap takibi
def track_book():
    members = load_members()

    member_id = input("Enter member ID for book tracking: ")
    if member_id not in members:
        print("Member not found.")
        return

    lent_book_barkod = members[member_id].get('lent_book_barkod', None)
    if lent_book_barkod:
        return_date_str = members[member_id].get('book_return_date', None)
        if return_date_str:
            return_date = datetime.strptime(return_date_str, '%Y-%m-%d')
            print(f"Tracking book for member {members[member_id]['name']}.")
            print(f"Book must be returned by: {return_date.strftime('%Y-%m-%d')}")
        else:
            print("No return date found for this book.")
    else:
        print("No book lent to this member.")