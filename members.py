import json
from datetime import datetime, timedelta

FILE_NAME = "user.json"

# Üye verilerini yükle
def load_members():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Dosya yoksa boş bir sözlük döner
    except json.JSONDecodeError:
        return {}  # JSON hatası durumunda boş bir sözlük döner


# Üye verilerini kaydet
def save_members(members):
    with open(FILE_NAME, "w") as file:
        json.dump(members, file, indent=4)


# Üye listesi
def users_list():
    members = load_members()  # Verileri yükle
    if not members:
        print("No members found.")
    else:
        for member_id, member_info in members.items():
            print(f"ID: {member_id}, Name: {member_info['name']}, Phone: {member_info['phone']} ")



# Yeni üye ekleme
def users_add():
    members = load_members()

    # Mevcut üyelerden en yüksek ID'yi bul
    if members:
        member_ids = list(map(int, members.keys()))  # ID'leri sayısal hale getir
        new_id = max(member_ids) + 1  # Yeni ID, mevcut en büyük ID + 1
    else:
        new_id = 1  # İlk üye, ID 1

    name = input("Enter member name: ").upper()
    phone = input("Enter member phone number: ")

    # Yeni üye bilgilerini ekle
    members[str(new_id)] = {"name": name, "phone": phone}
    save_members(members)
    print(f"Member {name} added successfully with ID {new_id}.")


# Üye arama
def users_find():
    members = load_members()
    users_list()
    member_id = input("Enter member ID to search: ")

    # Üyeyi arama
    if member_id in members:
        member_info = members[member_id]
        print(f"ID: {member_id}, Name: {member_info['name']}, phone: {member_info['phone']}")
    else:
        print("Member not found.")


# Üye silme
def users_delete():
    members = load_members()
    users_list()
    member_id = input("Enter member ID to delete: ")

    if member_id in members:
        del members[member_id]
        save_members(members)
        print(f"Member {member_id} deleted successfully.")
    else:
        print("Member not found.")

