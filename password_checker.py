import re 

# char = (r"[A-Z]", r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", "Hello@123")
def password_checker():

    password =input("Enter the password:- ")

    if len(password)<8:
        return "Weak: Password must be at least 8 charecters."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must including at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must be including at least one Uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must be including at least one lowerercase letter."
    
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]" ,password):
        return "Medium: Add some special charecter to make password strong."


    return "Stroge: your password is strong and secure",password
print(password_checker())

