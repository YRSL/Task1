class Operations:

    @staticmethod
    def find_students(list_students, room):
        list_students_in_room = []

        for student in list_students:
            if student.room == room.id:
                list_students_in_room.append(student)
        return list_students_in_room
