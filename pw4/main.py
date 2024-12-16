from domains.manager import MarkManager
import input
import output

def main():
    manager = MarkManager()

    while True:
        print("\nMenu:")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. Display GPA ranking")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            input.input_students(manager)
        elif choice == 2:
            input.input_courses(manager)
        elif choice == 3:
            input.input_marks(manager)
        elif choice == 4:
            output.display_with_curses(manager)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
