# bytes.fromhex('7368616b6564').decode('utf-8')

# import binascii
# import gzip

# s = b'Mathew'
# myWord = binascii.b2a_hex(s)
# print(myWord)
# binascii.a2b_hex(myWord)
# print(myWord)
print(bytearray.fromhex("4d6174686577").decode("latin1"))

# print(gzip.decompress(b""))
# with open('gz.txt', 'rb') as fd:
#     gzip_fd = gzip.GzipFile(fileobj=fd)
#     print(gzip_fd.peek(5))