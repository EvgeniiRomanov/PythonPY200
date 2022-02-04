import hashlib

#in_ = input("Введите пароль: ")
hash_object = hashlib.sha256(b"'123'")
hex_dig = hash_object.hexdigest()
print(hex_dig)

in_ = input("Введите пароль: ")
print(in_)
in_ = bytes(in_, "UTF-8")
print(in_)
hash_object = hashlib.sha256(in_)
hex_dig = hash_object.hexdigest()
print(hex_dig)

hex_ = hashlib.sha256(in_).hexdigest()
print(hex_)


hash_object1 = hashlib.sha256(b"12345").hexdigest()
print(hash_object1)