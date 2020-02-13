class Room:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_info(self):
        print(self.__str__())

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Student:
    def __init__(self, id, name, room):
        self.id = id
        self.name = name
        self.room = room

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'room': self.room}


class Students_In_Room(Room):
    def __init__(self, id, name, students):
        Room.__init__(self, id, name)
        self.students = students

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'students': [student.to_dict() for student in self.students]}
