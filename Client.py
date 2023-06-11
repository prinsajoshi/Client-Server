import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port to connect to
host = 'localhost'
port = 12345

# Connect to the server
client_socket.connect((host, port))
print("Connected to server.")

# Send data to the server
message = "Hello from the client!!!"
client_socket.send(message.encode())
print("Message sent.")

# Receive the server's response
response = client_socket.recv(1024).decode()
print("Server's response:", response)

# Close the connection
client_socket.close()
