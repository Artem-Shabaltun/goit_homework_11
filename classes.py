from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self,value):
        super().__init__(value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name: Name, *phones: list, **emails: list):
        self.name = name
        self.phones = list(phones)
        self.emails = emails

    def add_phone(self,number: Phone):
        phone_number = Phone(number)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def update_phone(self, old_number, new_number):
        index = self.phones.index(old_number)
        self.phones[index] = new_number

    def delete_phone(self, value):
        for num in self.phones:
            if num == value:
                self.phones.remove(value)

class ADDRESSBOOK(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)
    
if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    emails = ['bill@example.com']
    rec = Record(name, phone,emails)
    ab = ADDRESSBOOK()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')