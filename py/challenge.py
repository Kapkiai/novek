import socket
import gzip


def secretmsg():
    # Create a socket
    # socket.AF_INET - address family, IPv4
    # socket.SOCK_STREAM - TCP, conection-based
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connecting to the server via the address and port
    s.connect(("51.11.50.70", 5050))

    while True:
        # variable to store messgae from the server
        full_msg = ''
        while True:
            # receiving messages from the server with a buffer messgage of 1024
            msg = s.recv(1024)
            # storing the decode stream message to iur variable
            full_msg += msg.decode("utf-8")
            # I used this if statement to check the length of the received messgae in order to determin the end
            # of the incoming message from server. This thus marks the point where I should send the decoded
            # string to the server for validation.
            if len(full_msg) == 349:
                # Once all the message received from the server hs been stored in the variable,
                # I then used the python string operation (splitlines() method) to create a list
                # of string with list boundery being lines. I then accessed the hex encoded string
                # at the -2 position
                print("Hex Encoded Compressed String: ",
                      full_msg.splitlines()[-2])
                # I hex decoded the encoded string to utf-8
                decomMsg = gzip.decompress(
                    bytes.fromhex(full_msg.splitlines()[-2])).decode('utf-8')
                print("Decompressed Message: ", decomMsg)
                # send the decompressed string to the server for validation and apppend the carriage return
                # so that the server can process it
                s.sendall(bytes("{}{}".format(decomMsg, '\n'), 'utf-8'))
                # receiving the secret messgae from the server
                decodedMessage = s.recv(1024).decode('utf-8')
                print("Secret Message: ", decodedMessage)
                # closing the socket
                s.close()

                break

        break


# calling our function
secretmsg()
