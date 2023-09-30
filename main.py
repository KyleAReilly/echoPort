import socket


def echo_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('192.X.X.X', port))
        server_socket.listen(1)
        print(f"Echo server listening on port {port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                conn.send(data)
                print(f"Received and echoed: {data.decode('utf-8')}")


if __name__ == "__main__":
    port = 443  # Change this to your desired port
    echo_server(port)
