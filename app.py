import streamlit as st
import re
import random
import string


blacklist = {"password123", "12345678", "qwerty", "abc123", "password", "admin", "letmein", "welcome"}

def generate_strong_password(length=12):
    """Generates a random strong password ensuring inclusion of each required character type."""
    if length < 8:
        length = 8  
   
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password_chars += random.choices(all_chars, k=length - 4)
    random.shuffle(password_chars)
    return ''.join(password_chars)

def check_password_strength(password):
    """
    Checks the password against multiple criteria:
      - Minimum length (>= 8): 2 points
      - Contains both uppercase and lowercase letters: 1 point
      - Contains at least one digit: 1 point
      - Contains at least one special character: 1 point
      
    Total maximum score: 5.
    
    If the password is in a blacklist of common passwords, an error is returned.
    """
    
    if password.lower() in {p.lower() for p in blacklist}:
        return 0, "❌ This is a common password. Please choose a more secure one.", []

    score = 0
    feedback = []
    
    
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    return score, None, feedback

def get_strength_rating(score):
    """Returns a rating message based on the custom score."""
    if score == 5:
        return "✅ Strong Password!"
    elif 3 <= score < 5:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions above."



st.title("Password Strength Meter")


tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

with tab1:
    st.header("Check Your Password")
    user_password = st.text_input("Enter your password:", type="password")
    if st.button("Check Password"):
        if not user_password:
            st.warning("Please enter a password to check.")
        else:
            score, blacklist_warning, feedback = check_password_strength(user_password)
            if blacklist_warning:
                st.error(blacklist_warning)
            else:
                rating = get_strength_rating(score)
                st.write(f"**Score:** {score} / 5")
                st.write(rating)
                if feedback:
                    st.write("**Suggestions:**")
                    for tip in feedback:
                        st.write("- " + tip)

with tab2:
    st.header("Generate a Strong Password")
    length = st.number_input("Password Length:", min_value=8, max_value=32, value=12)
    if st.button("Generate Password"):
        generated_password = generate_strong_password(length)
        st.code(generated_password, language="plaintext")
        st.write("Evaluating the generated password:")
        score, blacklist_warning, feedback = check_password_strength(generated_password)
        rating = get_strength_rating(score)
        st.write(f"**Score:** {score} / 5")
        st.write(rating)
        if feedback:
            st.write("**Suggestions:**")
            for tip in feedback:
                st.write("- " + tip)
