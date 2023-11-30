import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            print(f"Received message: {message}")

            # Send the message back to the client
            client_socket.send(message.encode('utf-8'))
        except:
            break

    # Close the connection when the client disconnects
    print("Client disconnected")
    client_socket.close()

def main():
    # Set up the server
    host = '127.0.0.1'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Server listening on {host}:{port}")

    while True:
        # Accept incoming connections
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")

        # Create a thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
