import argparse
import writer
import reader
import object_creator
import my_parser


def main():

    parser = argparse.ArgumentParser()
    # parser.add_argument('students_file', type=str, help='Path to file "students.json"')
    # parser.add_argument('rooms_file', type=str, help='Path to file "rooms.json"')
    # parser.add_argument('format_file', type=str, choices=['json', 'xml'], help='Format JSON or XML')
    p = parser.parse_args()

    p.student_file = "students.json"
    p.rooms_file = "rooms.json"

    data_from_rooms_file = reader.JSON_Reader().read(p.rooms_file)

    list_object_rooms = []

    for room in data_from_rooms_file:
        object_creator.Room_Creator().create_objects(room, list_object_rooms)

# ----------------------------------------

    data_from_students_file = reader.JSON_Reader().read(p.student_file)

    list_object_students = []

    for student in data_from_students_file:
        object_creator.Student_Creator().create_objects(student, list_object_students)

# ----------------------------------------
    list_students_in_room_object = []

    for room_object in list_object_rooms:
        object_creator.Students_In_Room_Creator().create_objects(room_object, list_object_students,
                                                                 list_students_in_room_object)

# ----------------------------------------

    writer.JSON_Writer.write(list_students_in_room_object)
    writer.XML_Writer.write(my_parser.XML_Parser.parse(list_students_in_room_object))

if __name__ == "__main__":
        main()
