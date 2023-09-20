Rhett's Password Manager Readme

Overview

This Python script provides a simple graphical user interface (GUI) for managing passwords. It allows users to store, update, and retrieve login information for various websites and services securely. The script uses the tkinter library for the GUI, json for data storage, and pyperclip for copying passwords to the clipboard.

Features

Password Generation: You can generate strong and random passwords with the click of a button.

Password Storage: Store website URLs, email addresses, and passwords securely in a JSON file named data.json.

Password Update: Change the password for a website and optionally generate a new one if needed.

Password Retrieval: Retrieve stored login information for a specific website and copy the password to the clipboard.

Installation and Requirements

To run this script, you need to have Python 3 installed on your system. Additionally, you'll need to install the following Python libraries:

tkinter: A standard Python interface to the Tk GUI toolkit.

Pillow (PIL): A Python Imaging Library used for displaying the logo image.

pyperclip: A cross-platform clipboard module for copying passwords to the clipboard.

You can install these dependencies using pip:

pip install pillow pyperclip

Usage
1. Run the script using Python by executing python password_manager.py in your terminal.

2. The main window of the Password Manager application will appear.

3. Fill in the "Website," "Email/Username," and "Password" fields. The "Generate Password" button can be used to create a strong password.

4. Click the "Add" button to save the login information for the website.

5. To change the password for a website, fill in the "Website" and "Password" fields, then click the "Change Password" button.

6. To retrieve a stored password, enter the website name and click the "Search" button.

7. If you want to copy the password to the clipboard, click "Yes" when prompted.

File Structure

password_manager.py: The main Python script.

data.json: A JSON file for storing website login information.

RPM.ico: An icon file for the application window.

logo.png: A logo image displayed in the GUI.

Notes
Ensure that you keep the data.json file in the same directory as the script to store and retrieve passwords.

The application's icon (RPM.ico) and logo (logo.png) should also be in the script's directory.

Author
This Password Manager script was created by Rhett Davis.

Disclaimer
This Password Manager is a simple tool intended for personal use. It is not intended for managing critical or highly sensitive passwords. Use it at your own risk and consider using dedicated password management software for more robust security.

Feel free to customize and enhance this script as needed for your personal requirements.

Future Features (Planned Enhancements)
1. Encryption

Currently, the Password Manager script stores passwords in a plain text JSON file (data.json). To enhance security and protect sensitive information, future versions of the Password Manager may implement encryption. This will ensure that stored passwords are encrypted and can only be decrypted with a secure passphrase or key. The encryption feature could include:

AES Encryption: Implementing Advanced Encryption Standard (AES) encryption to secure the stored passwords.

User Authentication: Requiring users to authenticate themselves with a master password or PIN to access their stored passwords.

Secure Key Management: Implementing a secure key management system to protect the encryption keys used for data security.

Key Derivation: Using key derivation functions (such as PBKDF2) to derive encryption keys from user-provided master passwords.

Encryption Algorithms: Allowing users to choose from different encryption algorithms and key lengths for added flexibility.

2. Standalone .exe File
   
To make the Password Manager more accessible to non-technical users and those on Windows systems, future versions may include a standalone executable (.exe) file. Creating a standalone .exe file can simplify the installation process and eliminate the need for users to have Python and additional dependencies installed. This can be achieved with tools like PyInstaller or cx_Freeze.

Steps for creating a standalone .exe file:

Use a packaging tool like PyInstaller to package the Python script and its dependencies into a single .exe file.
Include the necessary icon and logo files in the packaged application.
Provide clear instructions for users on how to run the .exe file on their Windows machines.

3. Password Strength Meter
   
Enhancing password security is crucial. Future versions of the Password Manager may include a password strength meter that evaluates the strength of generated or entered passwords. This feature could include:

Password Complexity Analysis: Analyzing passwords for complexity by checking for a mix of uppercase letters, lowercase letters, numbers, and special characters.

Strength Score: Assigning a strength score to passwords and providing feedback to users on how secure their passwords are.

Password Policy: Allowing users to set their own password complexity requirements and enforcing those policies when generating or updating passwords.

4. Password Expiry and Reminders
   
Enhance security by implementing password expiration policies and reminders. Users could set expiration dates for their stored passwords and receive reminders to update them.

Password Expiry Policies: Allow users to specify how often passwords should expire (e.g., every 90 days).

Password Change Reminders: Send reminders to users when passwords are due for expiration or have not been updated in a while.

Password History: Maintain a history of previously used passwords to prevent reuse.
