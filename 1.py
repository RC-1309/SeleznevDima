class User:
    def __init__(self, first_name, second_name, type_user):
        self.first_name = first_name
        self.second_name = second_name
        self.type_user = type_user

    def __str__(self):
        return f'{self.type_user} {self.first_name} {self.second_name}'


class Teacher(User):
    def __init__(self, first_name, second_name, favorite_joke):
        User.__init__(self, first_name, second_name, 'Teacher')
        self.favorite_joke = favorite_joke

    def __str__(self):
        return f'{self.type_user} {self.first_name} {self.second_name} favorite joke: {self.favorite_joke}'


class Director(User):
    def __init__(self, first_name, second_name, number_of_prizes):
        User.__init__(self, first_name, second_name, 'Director')
        self.number_of_prizes = number_of_prizes

    def __str__(self):
        return f'{self.type_user} {self.first_name} {self.second_name} number of prizes: {self.number_of_prizes}'


class Parent(User):
    def __init__(self, first_name, second_name, number_of_children):
        User.__init__(self, first_name, second_name, 'Parent')
        self.number_of_children = number_of_children

    def __str__(self):
        return f'{self.type_user} {self.first_name} {self.second_name} number of children: {self.number_of_children}'


class Student(User):
    def __init__(self, first_name, second_name, favorite_lesson):
        User.__init__(self, first_name, second_name, 'Student')
        self.favorite_lesson = favorite_lesson

    def __str__(self):
        return f'{self.type_user} {self.first_name} {self.second_name} favorite lesson: {self.favorite_lesson}'


class Room:
    def __init__(self, number, access_level, type_room):
        self.number = number
        self.access_level = access_level
        self.type_room = type_room

    def __str__(self):
        return f'{self.type_room} {self.number}'


class Director_office(Room):
    def __init__(self, number):
        Room.__init__(self, number, ('Director'), 'Director office')


class Assembly_hall(Room):
    def __init__(self, number):
        Room.__init__(self, number, ('Teacher', 'Director', 'Student', 'Parent'), 'Assembly hall')


class Classroom(Room):
    def __init__(self, number):
        Room.__init__(self, number, ('Teacher', 'Director', 'Student'), 'Classroom')


class Teachers_lounge(Room):
    def __init__(self, number):
        Room.__init__(self, number, ('Teacher', 'Director'), 'Teachers_lounge')


def login_attempt(user, room):
    print(f"{user.type_user} {user.first_name} {user.second_name} "
          f"trying to log in to {room.type_room} {room.number}: "
          f"{'success' if user.type_user in room.access_level else 'failure'}")


person1 = Student('Dmitry', 'Seleznev', 'Informatic')
person2 = Parent('Dmitry', 'Seleznev', 2)
person3 = Director('Dmitry', 'Seleznev', 5)
person4 = Teacher('Dmitry', 'Seleznev', 'kolobok hanged himself')

room1 = Director_office(1)
room2 = Teachers_lounge(2)
room3 = Classroom(3)
room4 = Assembly_hall(4)

print(person1)
print(person2)
print(person3)
print(person4)

print(room1)
print(room2)
print(room3)
print(room4)

login_attempt(person2, room1)
login_attempt(person2, room2)
login_attempt(person2, room3)
login_attempt(person2, room4)

login_attempt(person1, room4)
login_attempt(person2, room4)
login_attempt(person3, room4)
login_attempt(person4, room4)

login_attempt(person1, room1)
