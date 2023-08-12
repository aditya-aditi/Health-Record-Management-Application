import time

records_categories = ["food", "checkup", "exercise"]


def add_patient():
    global line_1
    global make_file
    try:
        patient_id = int(input("Write the patient id "))
    except ValueError:
        print("Not a correct input!")
        return
    patient_name = input("Write the patient name ")
    f = open("patient_details.txt", "r")
    lines = f.readlines()
    for line in lines:
        line_1 = line.strip()
        line_1 = line.split(" ")
        if patient_id == int(line_1[0]):
            make_file = False
            break
        else:
            make_file = True

    if make_file == True:
        for category in records_categories:
            open(f"{patient_id}_{category}.txt", "a")
        with open("patient_details.txt", "a") as f:
            f.write(f"{patient_id} {patient_name} \n")
    else:
        print("\nPatient already added! \n")

def new_record():
    try:
        patient_id = int(input("Enter the patient id"))
    except ValueError:
        print("Write a correct patient id")
        return
    for category in records_categories:
        print(category)
    record_category_input = input("In which category do you want to add the record").lower()
    new_record = input("Write the entry")
    record_time = time.strftime("%H:%M")
    with open(f"{patient_id}_{record_category_input}.txt", "a") as f:
        f.write(f"{record_time} : {new_record} \n")


def retrieve_records():
    try:
        patient_id = int(input("Enter the patient id"))
    except ValueError:
        print("Write a correct patient id")
        return
    for category in records_categories:
        print(category)
    record_category_input = input("Of which category do you want to retrieve the records?").lower()
    try:
        f = open(f"{patient_id}_{record_category_input}.txt", "r")
        text = f.read()
        print("\nRecords Found!")
        print(f"\n{text}")
    except Exception:
        print("Records Not Found!")


def retrieve_name():
    f = open("patient_details.txt", "r")
    lines = f.readlines()
    i = 0
    for line in lines:
        line.strip()
        name_id = line.split(" ")
        if i != 0:
            print(f"{name_id[0]} - {name_id[1]}")
        i += 1

while True:
    try:
        user_Options = int(input(
            "Write 1 to add a new patient \nWrite 2 to add a new record to any patient \nWrite 3 to retrieve the records \nWrite 4 to retrieve the name of all the patients\n"))
    except ValueError as e:
        print("Not a valid input")
        continue
    if user_Options == 1:
        add_patient()
    elif user_Options == 2:
        new_record()
    elif user_Options == 3:
        retrieve_records()
    else:
        retrieve_name()
