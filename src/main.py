import socket


HOST = "0.0.0.0"
PORT = 8000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening on port {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = f"Greetings!!!\nYour message was {data.decode()}"
                conn.sendall(message.encode())


if __name__ == "__main__":
    main()