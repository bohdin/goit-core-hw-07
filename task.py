from AddressBook import AddressBook

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
def add_contact(args, contacts):
    # Розбиваємо список
    name, phone = args
    # Робим щоб імена починалися з великої літери
    name = name.capitalize()
    # Якщо такою людини ще немає в словнику додаємо
    if name not in  contacts.keys():        
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exists." # В іншому випадку виводимо, що вже контакт існує

@input_error
def change_contact(args, contacts):
    
    #  Розбиваємо список
    name, phone = args
    # Робим щоб імена починалися з великої літери
    name = name.capitalize()
    if name in contacts:
        contacts[name] = phone
        return "Contact change."
    else:
        raise(KeyError)

@input_error
def show_phone(args, contacts):  
    # Приводимо ім'я до потрібної нам форми
    name = args[0].capitalize()
    return contacts[name]
    

@input_error
def show_all(contacts):
    # Якщо словник не пустий, виводимо контакти через enter
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts."
    
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
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
             print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
