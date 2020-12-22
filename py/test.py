import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("51.11.50.70", 5050))



while True:
    full_msg = ''
    new_msg = True
    while True:
        # time.sleep(2)
        # s.send("Hello".encode('utf-8'))
        msg = s.recv(16)
        if new_msg:
            # print("new msg len:", msg[:HEADERSIZE])
            msglen = msg
            new_msg = False

        # print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")
        # if len(full_msg) > 335:
        #     # print(full_msg)
        #     break
        if len(full_msg) == 349:
            print("Mathew")
            s.sendall(b"Mathew\n")            
            print(s.recv(1024).decode('utf-8'))
            break

    print("here")
    break
s.close()
