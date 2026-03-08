import hashlib

data="anaskaif."
hash_value=hashlib.sha256(data.encode()).hexdigest()

print(data,"\n")
print("Hash valur:",hash_value,"\n")
data="Anaskaif."
hash_value=hashlib.sha256(data.encode()).hexdigest()
print("Hash valur:",hash_value)