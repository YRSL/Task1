from argparse import ArgumentParser
from writer import JsonWriter, XmlWriter
from reader import JsonReader
from object_creator import RoomCreator, StudentCreator, StudentsInRoomCreator
from my_parser import XMLParser


def argument_parse():
    parser = ArgumentParser()
    parser.add_argument('students_file', type=str, help='Path to file "students.json"')
    parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
    parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
    p = parser.parse_args()
    return p


def main():

    print("Hello")

    data_from_rooms_file = JsonReader().read(argument_parse().rooms_file)

    list_object_rooms = []

    for room in data_from_rooms_file:
        RoomCreator().create_objects(room, list_object_rooms)
# ----------------------------------------
    data_from_students_file = JsonReader().read(argument_parse().students_file)

    list_object_students = []

    for student in data_from_students_file:
        StudentCreator().create_objects(student, list_object_students)
# ----------------------------------------
    list_object_students_in_room = []

    for room_object in list_object_rooms:
        StudentsInRoomCreator().create_objects(room_object, list_object_students, list_object_students_in_room)
# ----------------------------------------
    if argument_parse().format_file == "json":
        JsonWriter.write(list_object_students_in_room)

    if argument_parse().format_file == "xml":
        XmlWriter.write(XMLParser.parse(list_object_students_in_room))

    print("Please check result file")


if __name__ == "__main__":
        main()
