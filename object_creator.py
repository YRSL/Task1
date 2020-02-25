from abc import ABC, abstractmethod
from objects import Room, Student, StudentsInRoom
from operations import Operations


class ObjectCreator(ABC):

    @abstractmethod
    def create_objects(self, *args):
        pass


class RoomCreator(ObjectCreator):

    @staticmethod
    def create_objects(room: dict, list_object_rooms: list):
        room_object = Room(id=room["id"], name=room["name"])
        list_object_rooms.append(room_object)


class StudentCreator(ObjectCreator):

    @staticmethod
    def create_objects(students: dict, list_object_students: list):
        student_object = Student(id=students["id"], name=students["name"], room=students["room"])
        list_object_students.append(student_object)


class StudentsInRoomCreator(ObjectCreator):

    @staticmethod
    def create_objects(room_object: object, list_object_students: list, list_object_students_in_room: list):
        object_students_in_room = StudentsInRoom(id=room_object.id, name=room_object.name,
                                        students=Operations.find_students(list_object_students, room_object))
        list_object_students_in_room.append(object_students_in_room)
