# 2 užduotis. panaudoti P14 paskaitos 4 užduoties kodą(jei neturim savo, yra
# įkeltas į klasės failus). Nustatyti log žinutes Į LOG FAILĄ kai:
# a. bandoma atidaryti pickle failą
# b. kai failo atidarymas nepavyksta
# c. kai įvedamas naujas darbuotojas
# d. kai programa įrašo duomenis į failą
# žinučių tekstas turi atspindėti veiksmą

import pickle
import logging

logger = logging.getLogger()  # sukuriamas logerio objektas

# objektas darbui su zurnalo failu

file_handler = logging.FileHandler("log_the_pickle.log",
                                   encoding="utf-8")

# objektas darbui su terminalu
stream_handler = logging.StreamHandler()

# nustatom zinuciu formata per spec objekta
formatter = logging.Formatter("Thread id is %(thread)d and the path name of the log %(pathname)s ||\n"
                              "You can find it in this module -> %(module)s ||\n"
                              "The numeric loging level for mes is -> %(levelno)s and its %(levelname)s ||\n"
                              "The message is ->>> %(message)s"
                              "\n")

# nustatom formatus handleriam
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# prijungiam handlerius prie pagr logger objekto
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# zinuciu lygis bendras
logger.setLevel(logging.DEBUG)
# lygis konkreciai rasymui i faila
file_handler.setLevel(logging.DEBUG)

all_employee_info = []


def add_employee():
    logger.info("Added new employee")
    name = input("Enter employee's name: ").strip()
    position = input("Enter employee's position: ").strip()
    salary = input("Enter employee's salary: ").strip()
    if not name or not position or not salary:
        logger.warning("Incomplete employee details provided. Name='%s', Position='%s', Salary='%s'", name, position,
                       salary)
        print("\nAll fields (name, position, salary) are required. Please try again.\n")
        return None
    else:
        logger.info(f"Added new employee: %s", name)
        return [name, position, salary]


def read_pickle():
    with open("listas.pickle", mode="rb") as file:
        listas2 = pickle.load(file)

    print("\nAll Employees:")
    if not listas2:
        return "No employee data found..."

    print("\nAll Employees:")
    employee_list = []
    for id, emp in enumerate(listas2, start=1):
        employee_list.append(f"{id}. Name: {emp[0]}, Position: {emp[1]}, Salary: {emp[2]}")
    return "\n".join(employee_list)


while True:

    choice = input("1. Add Employee\n"
                   "2. Read the pickle file\n"
                   "3. Exit\n"
                   "Enter your choice: \n"
                   "> ")

    if choice == '1':
        employee = add_employee()
        if employee:  # Append only if employee data is not None
            all_employee_info.append(employee)
            try:
                with open("listas.pickle", mode="wb") as file:
                    pickle.dump(all_employee_info, file)
                    logger.info("Data successfully written to the pickle file.")
                print("\nEmployee added successfully!")
            except Exception as e:
                logger.critical("Failed to write data to the pickle file: %s", e)
                print("\nFailed to add employee. Please try again.")
        input("Press enter to continue...")
    elif choice == '2':
        print(read_pickle())
        input("Press enter to continue...")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
