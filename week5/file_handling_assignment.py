
def create_file():
    """Create a new text file and write initial content to it."""
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is my file.\n")
            file.write("Here is a number: 42\n")
            file.write("Python file handling is interesting!\n")
        print("File created and written to successfully.")
    except (PermissionError, OSError) as e:
        print(f"Error occurred while creating the file: {e}")
    finally:
        print("Finished attempting to create file.")

def read_file():
    """Read the contents of the file and display them on the console."""
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    finally:
        print("Finished attempting to read file.")

def append_to_file():
    """Append additional content to the existing file."""
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending a new line.\n")
            file.write("Here is another number: 100\n")
            file.write("End of file handling assignment.\n")
        print("Additional lines appended successfully.")
    except (PermissionError, OSError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("Finished attempting to append to file.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show appended content
