import hashlib

in_ = input("Введите пароль: ")
hash_object = hashlib.sha256(f"b{in_}")
hex_dig = hash_object.hexdigest()
print(hex_dig)

in1 = 123
hash_object1 = hashlib.sha256(b"in_")
hex_dig1 = hash_object1.hexdigest()

print(hex_dig1)