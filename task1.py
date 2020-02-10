import argparse
from abc import ABC, abstractmethod
import json

parser = argparse.ArgumentParser()
# parser.add_argument('students_file', type=str, help='Path to file "students.json"')
# parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
# parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
p = parser.parse_args()

p.student_file = "students.json"
p.rooms_file = "rooms.json"


class Room:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        return print("ID: " + self.id + " Name: " + self.name)


class Student:
    def __init__(self, id, name, room):
        self.id = id
        self.name = name
        self.room = room


class Room_Student(Room):
    def __init__(self, id, name, students):
        Room.__init__(self, id, name)
        self.students = students


class Writer(ABC):

    @abstractmethod
    def write(self):
        pass


class JSON_Writer(Writer):

    def write(self):
        pass


class XML_Writer(Writer):

    def write(self):
        pass


class Reader(ABC):

    @abstractmethod
    def read(self, json_file):
        pass


class JSON_Reader(Reader):

    def read(self, json_file):
            with open(json_file, encoding='UTF-8') as file:
                data = json.load(file)
            return data


class Object_Creator(ABC):

    @abstractmethod
    def create_objects(self, dict_date, dict_object):
        pass


class Room_Creator(Object_Creator):

    def create_objects(self, dict_room, dict_object_rooms):
        room = Room(id=dict_room["id"], name=dict_room["name"])
        dict_object_rooms.append(room)


class Student_Creator(Object_Creator):

    def create_objects(self, dict_students, dict_object_students):
        student = Student(id=dict_students["id"], name=dict_students["name"], room=dict_students["room"])
        dict_object_students.append(student)


def main():

    rooms = JSON_Reader()

    data_rooms = rooms.read(p.rooms_file)

    dict_object_rooms = []

    rooms_object = Room_Creator()

    dict_rooms = [rooms_object.create_objects(i, dict_object_rooms) for i in data_rooms]

# ----------------------------------------

    students = JSON_Reader()

    data_students = students.read(p.student_file)

    dict_object_students = []

    students_object = Student_Creator()

    dict_students = [students_object.create_objects(i, dict_object_students) for i in data_students]


if __name__ == "__main__":
        main()
