import os

print("Starting the try block")
try:
    file_folder = "files/temp" ## "files\\temp" also will work
    #file_name = "dummy1.txt"
    file_name = input("Enter the file name to read : ")
    file_path = os.path.join(file_folder, file_name)

    num = int(input("Enter the division number : "))

    with open(file_path, "r+") as f:
        contents = f.read()
        print("File Contents read successfuly")
        print("*"*60)
        print(contents)
        print("*"*60)

    "AAAA"/2 #type error

    #100/num

    if(int(num) == 0):
        raise ZeroDivisionError("Cannot divide a number with '0'")

except FileNotFoundError:
    print("*"*60)
    print("File Not found in the Specified path")
    #print("Selected Path is : ", os.getcwd()+full_file_path)
    print(f"Current folder is : {os.getcwd()}")
    print(f"List of files in the current directory : {os.listdir(os.path.join(os.getcwd(), file_folder))}")
    print("*"*60)

except ZeroDivisionError as z:
   # print("You have entered '0' which will lead to infinity")
    print("Custom error raised",z)

#except TypeError:
   # print("Incompatible data types used with division operator")

except Exception as e:
    print("Handled in parent", e)

else:
    print("Try block executed successfully")

finally:
    print("Finally block executed successfully")