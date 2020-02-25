from abc import ABC, abstractmethod
from lxml import etree as xml


class Parser(ABC):

    @abstractmethod
    def parse(self, *args):
        pass


class XMLParser(Parser):

    @staticmethod
    def parse(list_objects):

        root = xml.Element("root")
        rooms_xml = xml.Element("Rooms")
        root.append(rooms_xml)

        for i in list_objects:

            room_xml = xml.Element("Room")
            id = xml.Element("id")
            id.text = str(i.id)
            name = xml.Element("name")
            name.text = str(i.name)
            room_xml.append(id)
            room_xml.append(name)

            students = xml.Element("students")

            for student in i.students:
                id_student = xml.Element("id")
                id_student.text = str(student.id)
                name_student = xml.Element("name")
                name_student.text = str(student.name)
                students.append(id_student)
                students.append(name_student)

            room_xml.append(students)
            rooms_xml.append(room_xml)

        result = xml.tostring(root, encoding="utf-8", pretty_print=True)

        return result
