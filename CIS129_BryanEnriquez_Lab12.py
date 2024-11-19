# Bryan Enriquez
# 11/18/2024
# Lab - module 12

class Pet:
    def __init__(self):
        self.__name = ""  
        self.__type = ""  
        self.__age = 0    

    def set_name(self, name):
        self.__name = name  
    def get_name(self):
        return self.__name

    def set_type(self, pet_type):
        self.__type = pet_type  

    def get_type(self):
        return self.__type  

    def set_age(self, age):
        self.__age = age  

    def get_age(self):
        return self.__age  

def main():
    animal = Pet()

    input_name = input("Enter a pet name: ")
    animal.set_name(input_name)  # Set the name

    input_type = input("Enter a pet type: ")
    animal.set_type(input_type)  # Set the type

    input_age = int(input("Enter a pet age: "))
    animal.set_age(input_age)  # Set the age

    # Display the pet's information
    print("The pet name is", animal.get_name())
    print("The pet type is", animal.get_type())
    print("The pet age is", animal.get_age())


# Run the program
if __name__ == "__main__":
    main()
