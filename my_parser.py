from abc import ABC, abstractmethod
import xml.etree.ElementTree as xml


class Parser(ABC):

    @abstractmethod
    def parse(self, *args):
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
