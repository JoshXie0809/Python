class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
    def play(self):
        if self._age <= 16:
            print('%s plays psp.' % self._name)
        else:
            print('%s plays girls.' % self._name)


