from abc import ABC, abstractmethod
from lxml import etree as xml
# import xml.etree.ElementTree as xml


class Parser(ABC):

    @abstractmethod
    def parse(self, *args):
        pass


class XML_Parser(Parser):

    @staticmethod
    def parse(list_objects):

        root = xml.Element("root")
        ell = xml.Element("Room")
        root.append(ell)

        for i in list_objects:

            el = xml.Element("asd")

            id = xml.Element("id")
            id.text = str(i.id)
            name = xml.Element("name")
            name.text = str(i.name)
            el.append(id)
            el.append(name)

            students = xml.Element("students")

            for student in i.students:
                id_student = xml.Element("id")
                id_student.text = str(student.id)
                name_student = xml.Element("name")
                name_student.text = str(student.name)
                # room_student = xml.Element("room")
                # room_student.text = str(student.room)
                students.append(id_student)
                students.append(name_student)
                # students.append(room_student)

            el.append(students)
            ell.append(el)

        result = xml.tostring(root, encoding="utf-8", pretty_print=True)
        # print(et.tostring(root, pretty_print=True).decode("utf-8"))

        return result
