
print("\n╔══════════════════════════════════╗")
print("║     🔐 Account Setup 🔐          ║")
print("╚══════════════════════════════════╝\n")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    name = input("👤 Enter Username: ")
    pin = input("🔑 Enter Code: ")

    errors = []

    if len(name) < 3:
        errors.append("❌ Your name is too Small!")
    if not any(n.isupper() for n in name):
        errors.append("❌ Username Should Contain atleast 1 Upper letter!")
    if not any(n in "!@#$" for n in name):
        errors.append("❌ Username Should Contain atleast 1 Special letter!")

    if len(pin) < 3:
        errors.append("❌ Your Pin is too Small!")
    if not any(p.isupper() for p in pin):
        errors.append("❌ Code Should Contain atleast 1 Upper letter!")
    if not any(p in "!@#$" for p in pin):
        errors.append("❌ Pin Should Contain atleast 1 Special letter!")
    
    if not errors:
        print("\n✅ Access Granted 🎉\n")
        break
    else:
        attempts += 1
        print("\n⚠️  Wrong Input!\n")
        
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        
        if attempts < max_attempts:
            print(f"\n {max_attempts - attempts} Attempts Left!\n")
else:
    print(f"\n🚫 Account Locked! {max_attempts - attempts} Attempts Left!\n")
    exit()


# Login System
print("\n╔══════════════════════════════════╗")
print("║     🔐 Login System 🔐           ║")
print("╚══════════════════════════════════╝\n")

login_attempts = 0
max_login_attempts = 3

def check_login(username, password):
    if username == name and password == pin:
        return True
    return False

while login_attempts < max_login_attempts:
    print(f"🔢 {max_login_attempts - login_attempts} attempts left!")
    
    username = input("👤 Enter Username: ")
    password = input("🔒 Enter Password: ")

    if check_login(username, password):
        print("\n✅ Access Granted! Wooh 🎉\n")
        break
    else:
        login_attempts += 1
        if login_attempts < max_login_attempts:
            print(f"\n❌ Wrong! {max_login_attempts - login_attempts} Attempts Left!\n")

if login_attempts == max_login_attempts:
    print(f"\n🚫 0 Attempts Left!! Account Locked\n")
