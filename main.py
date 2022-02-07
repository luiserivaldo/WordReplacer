# Python 3 code to rename multiple files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    folder = input(str("Would you like a custom path? (y/n)"))
    folder.lower()
    if folder == "y":
        folder = input(str("Enter the custom path: "))
        open(folder)
    if folder == "n":
        print("No custom path requested. Executing in source folder.")
    else:
        print("Invalid input. Will execute program in source folder. ")

    find_target = input(str("Enter the word that needs to be replaced: "))
    replace_target = input(str("Enter the desired word to replace the original: "))

    file_renamer(folder, find_target, replace_target)


def file_renamer(folder, find_target, replace_target):
    for file in os.listdir():
        if find_target(main) in file:
            os.rename(os.path.join(folder, file),
                      os.path.join(folder, file.replace(find_target, replace_target)))


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()