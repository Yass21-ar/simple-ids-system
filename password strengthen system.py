import re
import random
import string

# -------------------------------------------
# Password Strengthener
# -------------------------------------------

def is_strong(password):
    """Check if a password meets basic strength rules."""
    if len(password) < 12:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def suggest_improvements(password):
    """Return a list of suggestions to strengthen the password."""
    suggestions = []

    if len(password) < 12:
        suggestions.append("Increase length to at least 12 characters.")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters.")
    if not re.search(r"[0-9]", password):
        suggestions.append("Add numbers.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add special characters (e.g. !, @, #, $).")

    common_patterns = ["password", "1234", "qwerty", "admin"]
    if any(p in password.lower() for p in common_patterns):
        suggestions.append("Remove common weak patterns like 'password', '1234', 'qwerty'.")

    return suggestions


def generate_stronger_password(base_password, target_length=14):
    """Generate a stronger password inspired by the original one."""
    # Start with the original password (cleaned)
    new_pwd = base_password

    # Ensure minimum length
    if len(new_pwd) < target_length:
        extra_len = target_length - len(new_pwd)
        extra_chars = random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*()",
            k=extra_len
        )
        new_pwd += "".join(extra_chars)

    # Ensure character types
    if not re.search(r"[a-z]", new_pwd):
        new_pwd += random.choice(string.ascii_lowercase)
    if not re.search(r"[A-Z]", new_pwd):
        new_pwd += random.choice(string.ascii_uppercase)
    if not re.search(r"[0-9]", new_pwd):
        new_pwd += random.choice(string.digits)
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_pwd):
        new_pwd += random.choice("!@#$%^&*()")

    # Shuffle characters for randomness
    new_pwd_list = list(new_pwd)
    random.shuffle(new_pwd_list)
    return "".join(new_pwd_list)


if __name__ == "__main__":
    print("=== Password Strengthener ===")
    pwd = input("Enter a password to strengthen: ")

    if is_strong(pwd):
        print("\nYour password is already strong ✅")
    else:
        print("\nYour password is NOT strong ❌")
        print("Suggestions:")
        for s in suggest_improvements(pwd):
            print(f"- {s}")

        stronger = generate_stronger_password(pwd)
        print("\nExample of a stronger password (do NOT reuse blindly):")
        print(stronger)
        print("\nUse this as inspiration and create your own unique strong password.")
