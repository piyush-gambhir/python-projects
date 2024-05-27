"""
Password Manager
"""

# import the required modules
import random
import string
import sqlite3
import hashlib
import os
import pandas

# creating and connecting to the database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# creating the table
c.execute("""CREATE TABLE IF NOT EXISTS passwords (
            website text NOT NULL,
            nickname text,
            username text NOT NULL,
            password text NOT NULL
            password_health text
            PRIMARY KEY (website, username)
            )""")

conn.commit()
conn.close()

# addPassword Function
# This function adds a password to the database


def addPassword(website: str, username: str, password: str, nickname=""):

    # Add the password to the database
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords (website, nickname, username, password) VALUES (?, ?, ?, ?)",
              (website, nickname, username, password))
    conn.commit()
    conn.close()

# generatePassword Function
# This function generates a random password


def generatePassword(passwordLength: int):
    if (passwordLength > 8):
        # The password variable will contain the generated password
        password = ""

        # Generate a random password containing letters, numbers and symbols
        for i in range(passwordLength):
            password += random.choice(string.ascii_letters +
                                      string.digits + string.punctuation)
        return password

# hashPassword Function
# This function hashes a password


def hashPassword(password: str):

    # Generate a random salt
    salt = os.urandom(16)  # Generate a 16-byte salt

    # Hash the password
    hashedPassword = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000)

    # Return the hashed password
    return hashedPassword, salt

# retrievePassword Function
# This function retrieves a password from the database


def retrievePassword(website: str, username: str):
    # Retrieve the password from the database
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT password FROM passwords WHERE website = ? AND username = ?",
              (website, username))
    password = c.fetchone()
    conn.close()

    # Return the password
    return password

# deletePassword Function
# This function deletes a password from the database


def deletePassword(website: str):
    # Delete the password from the database
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE website = ?", (website,))
    conn.commit()
    conn.close()

# updatePassword Function
# This function updates a password in the database


def updatePassword(website: str, username: str, password: str):
    # Hash the password
    hashedPassword, salt = hashPassword(password)

    # Update the password in the database
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("UPDATE passwords SET username = ?, password = ? WHERE website = ?",
              (username, hashedPassword, salt, website))
    conn.commit()
    conn.close()

# listPasswords Function
# This function lists all the passwords in the database


def listPasswords():
    # Retrieve the passwords from the database
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    passwords = c.fetchall()
    conn.close()

    # Return the passwords
    return passwords

# passwordHealth Function
# This function checks the health of a password


def passwordHealth(password: str):

    points = 0

    # Check if password length is less than 8
    if (len(password) < 8):
        points += 1

    # Check if password contains a lowercase letter
    if not any(char.islower() for char in password):
        points += 1

    # Check if password contains an uppercase letter
    if not any(char.isupper() for char in password):
        points += 1

    # Check if password contains a number
    if not any(char.isdigit() for char in password):
        points += 1

    # Check if password contains a symbol
    if not any(char in string.punctuation for char in password):
        points += 1

    # Check if password contains a repeated character
    if any(password.count(char) > 1 for char in password):
        points += 1

    # Evaluate the password health
    if (points >= 0 and points <= 2):
        return "Weak"

    elif (points >= 3 and points <= 4):
        return "Moderate"

    elif (points >= 5 and points <= 6):
        return "Strong"


# importPasswordsFromCSV Function
# This function imports passwords from a CSV file


def importPasswordsFromCSV():
    # Import the passwords from the CSV file
    df = pandas.read_csv("passwords.csv")

    # Add the passwords to the database
    for index, row in df.iterrows():
        addPassword(row["Website"], row["Username"], row["Password"])

# importPasswordsFromExcel Function
# This function imports passwords from an Excel file


def importPasswordsFromExcel():
    # Import the passwords from the Excel file
    df = pandas.read_excel("passwords.xlsx")

    # Add the passwords to the database
    for index, row in df.iterrows():
        addPassword(row["Website"], row["Username"], row["Password"])

# exportPasswordsToCSV Function
# This function exports all the passwords to a CSV file


def exportPasswordsToCSV():
    # Retrieve the passwords from the database
    passwords = listPasswords()

    # Create a pandas dataframe
    df = pandas.DataFrame(passwords, columns=[
                          "Website", "Username", "Password"])

    # Export the passwords to a CSV file
    df.to_csv("passwords.csv", index=False)

# exportPasswordsToExcel Function
# This function exports all the passwords to an Excel file


def exportPasswordsToExcel():
    # Retrieve the passwords from the database
    passwords = listPasswords()

    # Create a pandas dataframe
    df = pandas.DataFrame(passwords, columns=[
                          "Website", "Username", "Password"])

    # Export the passwords to an Excel file
    df.to_excel("passwords.xlsx", index=False)


def calculateWeakPasswords():
    # Retrieve the passwords from the database
    passwords = listPasswords()

    # Create a pandas dataframe
    df = pandas.DataFrame(passwords, columns=[
                          "Website", "Username", "Password"])

    # Calculate the number of weak passwords
    for password in df["Password"]:
        df["Password Health"] = passwordHealth(password)
    weakPasswords = df["Password Health"].value_counts().to_dict().get("Weak")

    # Return the weak passwords
    return weakPasswords

# calculateReusedPasswords Function
# This function calculates the number of reused passwords


def calculateReusedPasswords():
    # Retrieve the passwords from the database
    passwords = listPasswords()

    # Create a pandas dataframe
    df = pandas.DataFrame(passwords, columns=[
                          "Website", "Username", "Password"])

    # Calculate the number of reused passwords
    reusedPasswords = df["Password"].value_counts().to_dict()

    # Return the reused passwords
    return reusedPasswords

# passwordStats Function
# This function displays the password statistics such as resued passwords, weak passwords, etc.


def passwordStats():
    # Retrieve the passwords from the database
    passwords = listPasswords()

    # Create a pandas dataframe
    df = pandas.DataFrame(passwords, columns=[
                          "Website", "Username", "Password"])

    # Display the password statistics
    print("Reused Passwords: ", calculateReusedPasswords())
    print("Weak Passwords: ", calculateWeakPasswords())
