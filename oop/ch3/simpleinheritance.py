class Contact:
    allContacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.allContacts.append((self.name, self.email))


class Supplier(Contact):
    supplierContacts = []

    def __init__(self, name, email):
        super().__init__(name, email)
        Supplier.supplierContacts.append((self.name, self.email))

    def order(self, order):
        print("\n\n\n\nIf this were a real system we would send "
              "'{}' to '{}'".format(order, self.name))


class Friend(Contact):
    friendContacts = []

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
        Friend.friendContacts.append((self.name, self.email, self.phone))


class MailSender:
    def sendMail(self, message=None):
        print(f"sending mail to {self.email}\n"
              f"Message :\n{message}")


class EmailacleContact(Contact, MailSender):
    pass


def main():
    c = Contact("Jenny", "Jenny@py")
    s = Supplier("Josh", "JoshXie@py")
    f = Friend("Sean", "Sean22@py", "09xxxxxxxx")
    m = EmailacleContact("Daddy", "Daddy@py.com")
    s.order("PocketPy ver.1.0")

    print(Contact.allContacts)
    print(Supplier.supplierContacts)
    print(Friend.friendContacts)

    text = "Hello, Daddy send Money to my Bank Account\nThanks, JoshXie\n2020 08 14"
    m.sendMail(text)


if __name__ == '__main__':
    main()
