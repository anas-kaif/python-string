from werkzeug.security import generate_password_hash,check_password_hash

stored_password="anaskaif"
hash_password=generate_password_hash(stored_password)

entered_password=input("enter password:")

print(check_password_hash(hash_password,entered_password))