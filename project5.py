def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Неправильні дані, використовуйте наданий вам формат: додати [ім'я] [номер]"
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Неправильні дані, використовуйте наданий вам формат: змінити [ім'я] [новий номер]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Номер оновлено."
    return "Контакт не знайдено."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Неправильні дані, використовуйте наданий вам формат: номер [ім'я]"
    name = args[0]
    return contacts.get(name, "Контакт не знайдено.")


def show_all(contacts):
    if not contacts:
        return "Список контактів порожній."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Вітаємо вас у нашому боті-асистенті!")
    while True:
        user_input = input("Введіть вашу команду: ")
        command, args = parse_input(user_input)

        if command in ["закрити", "вихід"]:
            print("Дякуємо за використання бота! До побачення!")
            break
        elif command == "вітаю":
            print("Чим я можу вам допомогти?")
        elif command == "додати":
            print(add_contact(args, contacts))
        elif command == "змінити":
            print(change_contact(args, contacts))
        elif command == "номер":
            print(show_phone(args, contacts))
        elif command == "всі":
            print(show_all(contacts))
        else:
            print("Невідома команда. Використайте оду з перелічених команд: додати, змінити, номер, всі, закрити, вихід.")


if __name__ == "__main__":
    main()