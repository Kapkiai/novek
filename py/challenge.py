import socket
import gzip


def unzip(data):
    # This function takes in hex encoded string, decodes it and unzips it to get
    # a string
    # hex decoding
    val = bytes.fromhex(data)
    # unziping
    unzippedVal = gzip.decompress(val).decode('utf-8')
    return unzippedVal


def main():
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
                hexString = full_msg.splitlines()[-2]
                print("Hex Encoded Compressed String: ", hexString)
                # variable to store the decompressed string
                decomMsg = unzip(hexString)
                print("Decompressed String: ", decomMsg)
                # send the decompressed string to the server for validation and apppend the carriage return
                # so that the server can take the input
                s.sendall(bytes("{}{}".format(decomMsg, '\n'), 'utf-8'))
                # receiving the secret messgae from the server
                decodedMessage = s.recv(1024).decode('utf-8')
                print("Secret Message: ", decodedMessage)
                # closing the socket
                s.close()

                break

        break


if __name__ == '__main__':
    main()
