# pwmanager

This is a password manager program written in Python that provides a high level of security. The program allows users to view a list of all stored passwords and access them at any time.

The master password is stored as a hashed value in a file called master_password.txt. When a user wants to access the stored passwords, they are prompted to enter their master password. The entered password is hashed and compared to the stored hashed value. If they match, the user is granted access to the stored passwords.

The program also allows users to create a new master password, change their existing master password, view their stored passwords, and add new passwords. The stored passwords are saved in a file called passwords.txt and are separated by website and password.

The program has a menu-driven interface that allows the user to choose what they would like to do by selecting an option from the menu. The program runs continuously until the user chooses to quit.

### Note:
This program is responsible only for the function of the manager. This is not a designed program. You can use the program freely as long as you give credits for it.

# Usage

### Installation:
Download the source code from GitHub and run the pwmanager.py file.

### Creating a Master Password:
Upon launching the program, you have to create a master password to do so click **1**. Make sure to choose a strong and unique password. 

### Menu:
After you enter your master password, the main menu will appear. The menu consists of the following options:

1. Create master password
2. Change master password
3. View passwords
4. Add password
5. Quit

**Change Master Password:**
Select this option to change your existing master password. You will be prompted to enter your current master password and then your new master password.

**View Passwords:**
Select this option to view a Password. You will have to enter the name of the website for which you need a password.

**Add New Password:**
Select this option to add a new password. You will be prompted to enter the website name and password.

**Quit:**
Select this option to exit the program. The stored passwords will remain secure and encrypted.

### Note: 
Make sure to keep your master password safe and secure. Do not share it with anyone. The program uses encryption to ensure the safety of your stored passwords, but if your master password is compromised, your stored passwords will be at risk.
