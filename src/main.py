import socket

HOST = "127.0.0.1"
PORT = 8000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        user_input = input("Input: ")
        s.sendall(user_input.encode())
        data = s.recv(1024)

    print(f"Recived message:\n{data.decode()}")


if __name__ == "__main__":
    main()