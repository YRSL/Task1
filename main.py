from argparse import ArgumentParser
import writer
import reader
import object_creator
import my_parser


def argument_parse():
    parser = ArgumentParser()
    parser.add_argument('students_file', type=str, help='Path to file "students.json"')
    parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
    parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
    p = parser.parse_args()
    return p

def main():

    print("Hello")

    data_from_rooms_file = reader.JSON_Reader().read(argument_parse().rooms_file)

    list_object_rooms = []

    for room in data_from_rooms_file:
        object_creator.Room_Creator().create_objects(room, list_object_rooms)
# ----------------------------------------
    data_from_students_file = reader.JSON_Reader().read(argument_parse().students_file)

    list_object_students = []

    for student in data_from_students_file:
        object_creator.Student_Creator().create_objects(student, list_object_students)
# ----------------------------------------
        list_object_students_in_room = []

    for room_object in list_object_rooms:
        object_creator.Students_In_Room_Creator().create_objects(room_object, list_object_students,
                                                                 list_object_students_in_room)
# ----------------------------------------
    if argument_parse().format_file == "json":
        writer.JSON_Writer.write(list_object_students_in_room)

    if argument_parse().format_file == "xml":
        writer.XML_Writer.write(my_parser.XML_Parser.parse(list_object_students_in_room))

    print("Please check result file")


if __name__ == "__main__":
        main()
