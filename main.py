# main.py

'''
KütüphaneProjesi

- main.py                    # Ana dosya, kullanici etkilesimi burada olacak
- books.py                   # Kitap islemleri (kitap ekleme, odunc verme vb.)
- members.py                 # Uye islemleri (uye ekleme, listeleme vb.)
- users.json                 # Uye verileri burada tutulacak
- kitap.json                 # Kitap verileri burada tutulacak
- taksi.json                 # Odunc alinan kitaplarin takibini yapar)
'''


import json
from members import * 
from books import *
from lend_return import*


# Ana fonksiyon
def main():
    while True:
        print('\nWELCOME TO THE PUBLIC LIBRARY\n'
              '1. Membership Operations\n'
              '2. Book Operations\n'
              '0. EXIT')

        main_choice = input('Please enter the code for the operation you want to access: ')

        if main_choice == '1':
            members_panel()
        elif main_choice == '2':
            book_panel()
        elif main_choice == '0':
            print('Exiting...')
            break
        else:
            print('INVALID SELECTION, PLEASE TRY AGAIN...')


# Üye işlemleri paneli
def members_panel():
    while True:
        print('\nMEMBERSHIP OPERATIONS\n'
              '1. Members\n'
              '2. Add Member\n'
              '3. Search Member\n'
              '4. Delete Member\n'
              '5. Lend Book\n'
              '6. Return Book\n'
              '7. Book Tracking\n'
              '0. EXIT')

        user_choice = input('Please make a selection: ')

        if user_choice == '1':
            users_list()
        elif user_choice == '2':
            users_add()
        elif user_choice == '3':
            users_find()
        elif user_choice == '4':
            users_delete()
        elif user_choice == '5':
            lend_book()
        elif user_choice == '6':
            return_book()
        elif user_choice == '7':
            track_book()
        elif user_choice == '0':
            break
        else:
            print('INVALID SELECTION, PLEASE TRY AGAIN...')

# Kitap işlemleri paneli
def book_panel():
    while True:
        print('\nBOOK OPERATIONS\n'
              '1. List Books\n'
              '2. Add Book\n'
              '3. Search Book\n'
              '4. Delete Book\n'
              '0. Return to Main Menu')

        book_choice = input("Please make a selection: ")

        if book_choice == "1":
            list_books()
        elif book_choice == "2":
            add_book()
        elif book_choice == "3":
            search_book()
        elif book_choice == "4":
            delete_book()
        elif book_choice == "0":
            break
        else:
            print('INVALID SELECTION, PLEASE TRY AGAIN...')


# Ana fonksiyon çağrısı
if __name__ == "__main__":
    main()