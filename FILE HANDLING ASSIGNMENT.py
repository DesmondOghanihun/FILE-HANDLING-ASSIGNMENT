try:
    with open("my_file.txt", "w") as file:
        file.write("2024 Fine boys loving Jesus")
        file.write("Happy Easter")
        file.write("Don't forget to pray!")
except FileNotFoundError:
    print("File not found!")
print("File not found!")
try:
    with open("my_file.txt", "w") as file:
        file.write("2024 Fine boys loving Jesus")
        file.write("12345 Happy Easter\n")
        file.write("Another line here\n")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("File creation completed.")
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("File reading completed.")

try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("98765\n")
        file.write("One more line appended\n")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
finally:
    print("File appending completed.")