
import socket
import sys

def send_request(host, port, request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(request.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")
    client_socket.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python client.py <host> <port> <request_file>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    request_file = sys.argv[3]

    with open(request_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # Validate the request format and size
            parts = line.split()
            if len(parts) < 2:
                print("Invalid request format")
                continue

            cmd = parts[0]
            key = parts[1]
            value = ' '.join(parts[2:]) if len(parts) > 2 else None

            # Check if the combined size of key and value exceeds 970 characters
            if len(key) + (len(value) if value else 0) > 970:
                print("Request too large")
                continue

            # Format the request message
            if cmd == 'PUT':
                msg = f"{len(line)} P {key} {value}"
            elif cmd == 'READ':
                msg = f"{len(line)} R {key}"
            elif cmd == 'GET':
                msg = f"{len(line)} G {key}"
            else:
                print("Invalid command")
                continue

            send_request(host, port, msg)