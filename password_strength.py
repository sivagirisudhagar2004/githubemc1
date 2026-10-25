# password_strength.py
import getpass
import re

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "letmein", "welcome", "admin", "iloveyou",
}


def check_strength(password: str) -> tuple[int, list[str]]:
    """Return a score from 0 to 5 and a list of suggestions."""
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters (12+ is better).")

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add numbers.")

    if re.search(r"[^\w\s]", password):
        score += 1
    else:
        tips.append("Add symbols such as ! @ # $ %.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips.insert(0, "This is a very common password. Choose something else.")

    if re.search(r"(.)\1{2,}", password):
        tips.append("Avoid repeating the same character three or more times in a row.")

    return min(score, 5), tips


LABELS = {0: "Very weak", 1: "Weak", 2: "Fair", 3: "Good", 4: "Strong", 5: "Very strong"}


def main():
    password = getpass.getpass("Enter a password to check (input is hidden): ")
    score, tips = check_strength(password)

    print(f"\nStrength: {LABELS[score]} ({score}/5)")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print(f"  - {tip}")
    else:
        print("Looks good.")


if __name__ == "__main__":
    main()