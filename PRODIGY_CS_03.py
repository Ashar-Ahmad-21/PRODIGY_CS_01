import re

def assess_password_strength(password):
    # Criteria for a strong password
    min_length = 8
    criteria = {
        'length': len(password) >= min_length,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'\d', password)),
        'special_chars': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    # Calculate strength score
    strength_score = sum(criteria.values())

    # Determine strength level
    if strength_score == 5:
        strength_level = 'Very Strong'
    elif strength_score == 4:
        strength_level = 'Strong'
    elif strength_score == 3:
        strength_level = 'Moderate'
    elif strength_score == 2:
        strength_level = 'Weak'
    else:
        strength_level = 'Very Weak'

    # Provide feedback
    feedback = []
    if not criteria['length']:
        feedback.append(f'Password should be at least {min_length} characters long.')
    if not criteria['uppercase']:
        feedback.append('Password should contain at least one uppercase letter.')
    if not criteria['lowercase']:
        feedback.append('Password should contain at least one lowercase letter.')
    if not criteria['digits']:
        feedback.append('Password should contain at least one digit.')
    if not criteria['special_chars']:
        feedback.append('Password should contain at least one special character.')

    return strength_level, feedback

# Prompt the user to enter their password
password = input("Enter your password to assess its strength: ")

# Assess the strength of the entered password
strength_level, feedback = assess_password_strength(password)

# Display the results
print(f"Password Strength: {strength_level}")
if feedback:
    print("Feedback to improve your password:")
    for item in feedback:
        print(f"- {item}")
else:
    print("Your password is very strong.")

