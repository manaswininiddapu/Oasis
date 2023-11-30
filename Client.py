import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive and print messages from the server
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received from server: {message}")
        except:
            break

def main():
    # Set up the client
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # Send messages to the server
    while True:
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
