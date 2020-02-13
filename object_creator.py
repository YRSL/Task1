from abc import ABC, abstractmethod
import objects
import operations


class Object_Creator(ABC):

    @abstractmethod
    def create_objects(self, *args):
        pass


class Room_Creator(Object_Creator):

    @staticmethod
    def create_objects(room: dict, list_object_rooms: list):
        room_object = objects.Room(id=room["id"], name=room["name"])
        list_object_rooms.append(room_object)


class Student_Creator(Object_Creator):

    @staticmethod
    def create_objects(students: dict, list_object_students: list):
        student_object = objects.Student(id=students["id"], name=students["name"], room=students["room"])
        list_object_students.append(student_object)


class Students_In_Room_Creator(Object_Creator):

    @staticmethod
    def create_objects(room_object: object, list_object_students: list, list_students_in_room_object: list):
        students_in_room_object = objects.Students_In_Room(id=room_object.id, name=room_object.name,
                                        students=operations.Operations.find_students(list_object_students, room_object))
        list_students_in_room_object.append(students_in_room_object)
