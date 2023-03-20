import bcrypt

def hashAndSaltGen():
    password = input("Enter a password: ")
    salt_len = input("Salt generation (basically bigger num takes more time)")

    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(salt_len)
    hash = bcrypt.hashpw(bytes, salt)

    return(hash)

def check_password(password, hash):
    return bcrypt.checkpw(password, hash)












