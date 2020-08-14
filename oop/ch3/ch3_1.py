class Contact:
    allContacts = []

    def __init__(self, name, email, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.allContacts.append((self.name, self.email))


class AddressHolder:
    AddressDict = {}

    def __init__(self, street, city, state, code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
        AddressHolder.AddressDict[len(AddressHolder.AddressDict)] =  \
            dict(state=state, city=city, street=street, code=code)


class Friend(Contact, AddressHolder):
    """
    need :
    name, email, street, city,
    state, code

    """

    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


def main():
    f1 = Friend(phone='0913555555', name='JoshXie', email='JoshXie@py',
                street='QinHanSt.', city='Tainan', state='Taiwan')

    print(Friend.AddressDict)
    print(Contact.allContacts[0])


if __name__ == '__main__':
    main()
