import hashlib
string_to_hash = input()
hash_object = hashlib.sha256(str(string_to_hash).encode('utf-8'))
print(hash_object.hexdigest())
