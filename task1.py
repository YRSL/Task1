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


def main():

    rooms = JSON_Reader()

    data_rooms = rooms.read(p.rooms_file)
    # print(data_rooms)

    students = JSON_Reader()

    data_students = students.read(p.student_file)
    # print(data_students)


if __name__ == "__main__":
        main()
