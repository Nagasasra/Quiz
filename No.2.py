

with open("data1.txt") as data:
    data_read = data.read()
    print(data_read)


class StaffManagement:
    def __init__(self, id, name, position, salary):
        self.__id = id
        self.__ids = []
        self.__name = name
        self.__position = position
        self.__salary = salary
        self.__staffs = []
        self.__required_position = ["Manager", "Staff", "Officer"]
        self.__required_salary = {"Staff": range(3500000, 7000001), "Officer": range(7000001, 10000000), "Manager": range( salary > 10000000) }

    def add_staff(self):
        new_staff_id = input("Input Staff ID: ")
        if new_staff_id[0] != "S" or len(new_staff_id) > 5 or new_staff_id[1:] != int or new_staff_id in self.__ids:
            print("Incorrect ID")
            new_staff_id = input("Input Staff ID: ")
        data.write("\n" + new_staff_id)
        new_staff_name = input("Input Staff Name: ")
        if len(new_staff_name) > 20:
            print("Names too long")
            new_staff_name = input("Input Staff Name: ")
        data.write("#" + new_staff_name)
        new_staff_position = input("Input Staff Position: ")
        if new_staff_position not in self.__position:
            print("Please input the correct position")
            new_staff_position = input("Input Staff Position: ")
        data.write("#" + new_staff_position)
        new_staff_salary = input("Input Staff Salary: ")
        new_staff = new_staff_id + "#" + new_staff_name + "#" + new_staff_position + "#" + new_staff_salary
        self.__staffs.append(new_staff)
        self.__ids.append(new_staff_id)
        data.write(new_staff + "\n")

    def delete_staff(self):
        deleting_staff = input("Enter Staff ID: ")
        if deleting_staff in self.__staffs:
            self.__staffs.remove(deleting_staff)
        else:
            print("Staff can't be found")
            deleting_staff = input("Enter Staff ID: ")
    
