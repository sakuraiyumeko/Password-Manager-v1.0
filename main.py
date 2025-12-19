def register():
    existing_users = []
    try:
        with open("users.txt", "r", encoding="utf-8") as f:
            for line in f:
                existing_users.append(line.split(":")[0])
    except FileNotFoundError:
        pass

    while True:
        new_id = input("Set a name:")
        if new_id in existing_users:
            print("This name already exists")
        for char in [".","/","\\"]:
            if char in new_id:
                print("Can't contain . / \\")
                return
        if new_id == "":
            print("Can't be none")
            return
        else:
            break

    while True:
        user_password = input("Set a password:")
        if " " in user_password:
            print("Can't contain spaces")
        elif user_password == "":
            print("Can't be none")
        else:
            break

    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{new_id}:{user_password}\n")
    print("Completed!")


def login():
    user_db = {}
    try:
        with open("users.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    user_db[parts[0]] = parts[1]
    except FileNotFoundError:
        print("No user file")
        return 0

    input_id = input("Enter your name:")
    if input_id =="":
        print("Can't be none")
        return 0
    input_pw = input("Enter your password:")
    if input_id.strip() in user_db and user_db[input_id.strip()].strip() == input_pw:
        print(f"Welcome {input_id.strip()}! ")
        return input_id.strip()
    else:
        print("Something went wrong")
        return 0

def lobby():
    print("""
    ----------------------------
    Welcome To Password Checker
    1.Register
    2.Login
    3.Exit
    ----------------------------
    """)
    choices = input(">")
    return choices

def main_page():
    print("""
    ----------------------------
    What would you like to do?
    1.Create a new password
    2.Check your password
    3.Change your password
    4.Setting
    5.Log out
    ----------------------------
    """)
    choices = input(">")
    return choices

def create_password(cuser):
    name = input("Enter the name:")
    if name == "":
        print("Can't be none")
        return

    existing_sites = []
    try:
        with open(f"{cuser}.txt", "r", encoding="utf-8") as f:
            for line in f:
                existing_sites.append(line.split(":")[0])
    except FileNotFoundError:
        pass

    if name in existing_sites:
        print(f"Oops! The password for '{name}' already exists!")
        input("Press Enter to return...")
        return

    account = input("Enter your email/phone number/username(choose one):")
    if account == "":
        print("Can't be none")
        return
    password = input("Enter your password:")
    if password == "":
        print("Can't be none")
        return
    note = input("Enter your note:")
    with open(f"{cuser}.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}:{account}:{password}:{note}\n")
    return

def check(cuser,name):
    try:
        with open(f"{cuser}.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":")
                if parts[0] == name:
                    if len(parts) == 4:
                        return parts
                    else:
                        return None
            print("Can't be found")
            return None

    except FileNotFoundError:
        print("No password")
        return None

def check_password(cuser):
    tag = input("Enter which do you want to check:")
    if tag == "":
        print("Can't be none")
        return
    parts=check(cuser,tag)
    if parts:
        print(f"Name:{parts[0]}\nAccount:{parts[1]}\nPassword:{parts[2]}\nNote:{parts[3]}")
        input("\nPress enter to continue...")
    else:
        return

def change_password(cuser):
    print(f"Haven't completed yet,{cuser}")

def options():
    print("""
    ----------------------------
    Options
                WIP
    1.exit
    ----------------------------
    """)
    choices = input(">")
    return choices

def main():
    status1=0
    a=0
    while 1:
        if status1 == 0:
            a = lobby()
            status1 = -1
        elif a == "1" or status1 == 1:
            register()
            status1=-1
            a=0
        elif a == "2" or status1 == 2:
            current_user = login()
            if current_user == 0:
                status1 = 0
                continue
            a=0
            status1=-1
            while 1:
                choice1 = main_page()
                if choice1=="1":
                    create_password(current_user)
                    continue
                if choice1=="2":
                    check_password(current_user)
                    continue
                if choice1=="3":
                    change_password(current_user)
                    continue
                if choice1=="4":
                    #status2=0
                    while 1:
                        choice2 = options()
                        if choice2=="1":
                            break
                if choice1 in ["5","exit","quit"]:
                    break
        elif a == "3":
            quit()
        else:
            status1 = 0
            continue


main()
