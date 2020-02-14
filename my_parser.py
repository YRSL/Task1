from abc import ABC, abstractmethod
import xml.etree.ElementTree as xml


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
            el = xml.SubElement(ell, "Room: " + str(list_objects.index(i)))

            id = xml.SubElement(el, "id")
            id.text = str(i.id)
            name = xml.SubElement(el, "name")
            name.text = str(i.name)

            students = xml.Element("students")
            el.append(students)

            for student in i.students:
                id_student = xml.SubElement(students, "id")
                id_student.text = str(student.id)
                name_student = xml.SubElement(students, "name")
                name_student.text = str(student.name)
                room_studen = xml.SubElement(students, "room")
                room_studen.text = str(student.room)

        return root
