"""Convert a sha256 to base64"""

import hashlib
import base64

mystring = "This is a test"

hashed_value = hashlib.sha256(mystring.encode('utf-8')).digest()
print(hashed_value)

hashed = base64.urlsafe_b64encode(hashed_value)
print(hashed)
print(len(hashed))
decoded = base64.urlsafe_b64decode(hashed)
original_value = decoded.decode('utf-8')
print(decoded)