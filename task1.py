import argparse
from abc import ABC, abstractmethod
import json

parser = argparse.ArgumentParser()
parser.add_argument('students_file', type=str, help='Path to file "students.json"')
parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
p = parser.parse_args()


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
    def read(self):
        pass


class JSON_Reader(Reader):

    def read(self):
        pass


strjsn = '[{"id":990, "name":"Room #990"}, {"id":970, "name":"Room #970"}]'

j = json.loads(strjsn)
print(j)


def main():

    with open('rooms.json', encoding='UTF-8') as file_rooms:
        data1 = json.load(file_rooms)

    print(data1)


if __name__ == "__main__":
        main()
