# Nove Internship sockets challenge using python
Implements python socket *(client)*

**Main program is in the py folder, i.e py/client.py**

The C folder isn't complete. I opted to do the task with python.

## How the program works
Connects to a server
reads a hex encoded compressed string,
decodes and decompresses the string using gzip,
send the decompresswd string to the server,
the server checks the string, if it is corect, the server returns a secret messgae to the client

## Steps on running the program

```bash 
$ cd path/to/your/dev/folder
$ git clone https://github.com/Kapkiai/novek.git
$ cd py
$ pyton3 client.py
  Hex Encoded Compressed String:  1f8b08003ffae15f02ff55cac10980400c04c056b602abb18153721a249b2309dabe873fbfc3aca760932c0c89ee618dbb406d84df62c282266a9e8ac6d452277ab87d46e7e371290f64b59ac93fffe1f202fcefa41e62000000
  Decompressed Message:  The best performance improvement is the transition from the nonworking state to the working state.
  Secret Message:  
  Nice work padawan, here is you flag: NOVEK{S1MPL1C1TY_1S_THE_SOUL_OF_EFF1C1ENCY}
 
```



