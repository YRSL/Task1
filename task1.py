import argparse
import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as xml


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

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Student:
    def __init__(self, id, name, room):
        self.id = id
        self.name = name
        self.room = room

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'room': self.room}


class Room_Student(Room):
    def __init__(self, id, name, students):
        Room.__init__(self, id, name)
        self.students = students

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'students': [student.to_dict() for student in self.students]}


class Writer(ABC):

    @abstractmethod
    def writeq(*args):
        pass


class JSON_Writer(Writer):

    @staticmethod
    def writeq(list_objects):
        data_result = [i.to_dict() for i in list_objects]
        with open('result.json', 'w', encoding='UTF-8') as file:
            json.dump(data_result, file, ensure_ascii=False)


class XML_Writer(Writer):

    @staticmethod
    def writeq(root):
        tree = xml.ElementTree(root)
        with open('updated22.xml', 'wb') as f:
            tree.write(f, encoding="utf-8")


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
    def create_objects(*args):
        pass


class Room_Creator(Object_Creator):

    def create_objects(self, dict_room, list_object_rooms):
        room = Room(id=dict_room["id"], name=dict_room["name"])
        list_object_rooms.append(room)


class Student_Creator(Object_Creator):

    def create_objects(self, dict_students, list_object_students):
        student = Student(id=dict_students["id"], name=dict_students["name"], room=dict_students["room"])
        list_object_students.append(student)


class Room_Student_Creator(Object_Creator):

    def create_objects(self, room, list_object_students, list_object_rooms_students):
        room_student = Room_Student(id=room.id, name=room.name, students=Logic.find_students(list_object_students, room))
        list_object_rooms_students.append(room_student)


class Parser:

    @staticmethod
    def parse(*args):
        pass

class XML_Parser(Parser):

    @staticmethod
    def parse_students(list_students, root):

        students = xml.Element("students")
        root.append(students)
        for student in list_students:
            id = xml.SubElement(students, "id")
            id.text = str(student.id)
            name = xml.SubElement(students, "name")
            name.text = str(student.name)
            room = xml.SubElement(students, "room")
            room.text = str(student.room)
        return students


    @staticmethod
    def parse(list_objects):

        root = xml.Element("room")
        for i in list_objects:
            el = xml.Element("a")

            id = xml.SubElement(el, "id")
            id.text = str(i.id)
            name = xml.SubElement(el, "name")
            name.text = str(i.name)

            XML_Parser.parse_students(i.students, root)
        return root




class Logic:

    @staticmethod
    def find_students(list_students, room):
        list_students_in_room = []

        for student in list_students:
            if student.room == room.id:
                list_students_in_room.append(student)

        return list_students_in_room


def main():

    rooms = JSON_Reader()

    data_rooms = rooms.read(p.rooms_file)

    list_object_rooms = []

    rooms_object = Room_Creator()

    for room in data_rooms:
        rooms_object.create_objects(room, list_object_rooms)

    # print(list_object_rooms)
    # fres = [i.to_dict() for i in list_object_rooms]
    # print(fres)

# ----------------------------------------

    students = JSON_Reader()

    data_students = students.read(p.student_file)

    list_object_students = []

    students_object = Student_Creator()

    for student in data_students:
        students_object.create_objects(student, list_object_students)

# ----------------------------------------
    list_object_rooms_students = []

    rooms_students_object = Room_Student_Creator()

    for room in list_object_rooms:
        rooms_students_object.create_objects(room, list_object_students, list_object_rooms_students)

    # print(list_object_rooms_students)
    # fres = [i.to_dict() for i in list_object_rooms_students]
    # print(fres)

# ----------------------------------------

    JSON_Writer.writeq(list_object_rooms_students)
    XML_Writer.writeq(XML_Parser.parse(list_object_rooms_students))

# ----------------------------------------



if __name__ == "__main__":
        main()
