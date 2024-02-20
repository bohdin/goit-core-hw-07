from AddressBook import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact doesn't exists."
        except IndexError:
            return "Invalid contact."
        
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook) -> str:
    # Розбиваємо список
    name, phone = args
    # Робим щоб імена починалися з великої літери
    name = name.capitalize()
    # Якщо такою людини ще немає в словнику додаємо
    if name not in  book.data.keys():        
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."
    else:
        return "Contact already exists." # В іншому випадку виводимо, що вже контакт існує

@input_error
def change_contact(args, book: AddressBook):
    
    #  Розбиваємо список
    name, phone = args
    # Робим щоб імена починалися з великої літери
    name = name.capitalize()
    record = book.delete(name)
    if record:
        record.edit_phone(str(record.phones[0].value), phone)
        book.add_record(record)        
        return "Contact change."
    else:
        raise(KeyError)

@input_error
def show_phone(args, book: AddressBook):  
    # Приводимо ім'я до потрібної нам форми
    name = args[0].capitalize()
    return str(book.find(name))
    

@input_error
def show_all(contacts):
    # Якщо словник не пустий, виводимо контакти через enter
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts."
    
@input_error
def add_birthday(args, book):
    # реалізація
    pass

@input_error
def show_birthday(args, book):
    # реалізація
    pass

@input_error
def birthdays(args, book):
    # реалізація
    pass

    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
