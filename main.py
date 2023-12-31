from collections import UserDict
from datetime import datetime


# Клас для книги контактів
class ADDRESSBOOK(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index < len(self.data):
            keys = list(self.data.keys())
            key = keys[self._iter_index]
            self._iter_index += 1
            return self.data[key]
        else:
            raise StopIteration


# Базовий клас для полів (ім'я, телефон, емейл)
class Field:
    def __init__(self, value):
        self.value = value


# Клас для телефону
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        # Перевірка та форматування телефонного номера
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number")

    # Перевірка коректності номера телефону
    def is_valid_phone(self, value):
        # Тут можна додати додаткові перевірки, наприклад, на довжину або формат
        return True


# Клас для імені
class Name(Field):
    def __init__(self, value):
        super().__init__(value)


# Клас для електронної адреси
class Email(Field):
    def __init__(self, value):
        super().__init__(value)


# Клас для запису контакту
class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.birthday = birthday

    # Додати номер телефону
    def add_phone(self, number: Phone):
        phone_number = Phone(number)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    # Оновити номер телефону
    def update_phone(self, old_number, new_number):
        old_phone = Phone(old_number)
        # Перевірка наявності та оновлення всіх входжень номера телефону
        for i in range(len(self.phones)):
            if self.phones[i] == old_phone:
                self.phones[i] = Phone(new_number)

    # Видалити номер телефону
    def delete_phone(self, value):
        # Видалити всі входження номера телефону
        self.phones = [phone for phone in self.phones if phone.value != value]

    # Додати електронну адресу
    def add_email(self, email: Email):
        email_address = Email(email)
        if email_address not in self.emails:
            self.emails.append(email_address)

    # Оновити електронну адресу
    def update_email(self, old_email, new_email):
        index = self.emails.index(old_email)
        self.emails[index] = new_email

    # Видалити електронну адресу
    def delete_email(self, value):
        # Видалити всі входження електронної адреси
        self.emails = [email for email in self.emails if email.value != value]

    # Підрахувати дні до дня народження
    def calculate_days_to_birthday(self):
        if self.birthday:
            today = datetime.today()
            next_birthday = datetime(
                today.year, self.birthday.value.month, self.birthday.value.day
            )
            if next_birthday < today:
                next_birthday = datetime(
                    today.year + 1, self.birthday.value.month, self.birthday.value.day
                )
            days_remaining = (next_birthday - today).days
            return days_remaining
        else:
            return None


# Клас для дня народження
class Birthday(Field):
    def __init__(self, value):
        self.value = value

    def is_valid_birthday(self, value):
        # Тут можна додати перевірки на коректність дня народження
        return True

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not self.is_valid_birthday(value):
            raise ValueError("Incorrect Birthday")
        self.value = value


address_book = ADDRESSBOOK()

record1 = Record("Art")
phone1 = Phone("023456789")
email1 = Email("Art@example.com")
record1.add_phone(phone1)
record1.add_email(email1)
birthday1 = Birthday(datetime(1991, 5, 13))
record1.birthday = birthday1

record2 = Record("Nick")
phone2 = Phone("987654321")
email2 = Email("nick@example.com")
record2.add_phone(phone2)
record2.add_email(email2)
birthday2 = Birthday(datetime(1997, 8, 9))
record2.birthday = birthday2

record3 = Record("Alice")
phone3 = Phone("555555555")
email3 = Email("alice@example.com")
birthday3 = Birthday(datetime(1995, 10, 20))
record3.add_phone(phone3)
record3.add_email(email3)
record3.birthday = birthday3
address_book.add_record(record3)


address_book.add_record(record1)
address_book.add_record(record2)
address_book.add_record(record3)

# Перевірки та виведення результатів
for record in address_book:
    print("Name:", record.name.value)
    print("Phones:", record.phones)
    print("Emails:", [email.value for email in record.emails])
    print("Birthday:", record.birthday.value if record.birthday else "N/A")
    print("Days to Birthday:", record.calculate_days_to_birthday())
    print()
