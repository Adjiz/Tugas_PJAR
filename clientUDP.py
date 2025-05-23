import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello , UDP Server! Adji Muhammad Zidane 50421051"

client_socket.sendto(message.encode("utf-8"), ('localhost', 9001))
data, address = client_socket.recvfrom(1024)
print(data.decode("utf-8"))