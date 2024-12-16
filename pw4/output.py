import curses

def display_with_curses(manager):
    manager.calculate_gpas()
    manager.sort_students_by_gpa()

    def draw_ui(stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Student GPA Ranking", curses.A_BOLD)
        row = 2
        for student in manager.students:
            stdscr.addstr(row, 0, f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa()}")
            row += 1
        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(draw_ui)
