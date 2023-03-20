Password Generator with Salting, Hashing, and Estimated Crack Time

This is a Python password generator that uses salting and hashing to create secure passwords. The program generates a random password string of a user-specified length and adds salt to the password before hashing it using BCRYPT. The salt and hash are stored in a SQLite database for later use. The program also calculates an estimated crack time for the password, which is an approximation of how long it would take for a computer to guess the password using brute force methods.


Features:


Generate secure passwords with customizable length and character sets

Salt and hash passwords using BCRYPT

Store salt and hash in a SQLite database

Calculate estimated crack time for password

View stored passwords and their estimated crack times


Tech Stack:


Python

SQLite (for database management)

Time module (for estimating crack time)

