from users import register
from users import login
import sys
import socket

def server(host, port):
  listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  listening_socket.bind((host, port))
  listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  listening_socket.listen(5)
  print("starting server")

  while True:
    client_connection, client_address = listening_socket.accept()
    print("listening_socket.accept: ",  listening_socket)
    request_data = client_connection.recv(1024)
    print(f"request data: {request_data.decode()}")
    html_page = """
    <html>
      <head><title>BookReview</title></head>
      <body>
        <h1> this is body</h1>
      </body>
    </html>
    """
    client_connection.sendall(
      f"HTTP/1.1 200 OK\r\nContent-Length: {len(html_page)}\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n{html_page}".encode()
    )
    client_connection.close()
    print("done serving request")

if __name__ == "__main__":
    print("sys.argv: ",sys.argv)
    if('manage.py' and 'user_register' in sys.argv):
        for parameter in sys.argv:
            if 'username' in parameter:
                username = parameter.split('=')[1]
            elif 'password2' in parameter:
                password2 = parameter.split('=')[1]
            elif 'password' in parameter:
                password = parameter.split('=')[1]
            elif 'dateOfBirth' in parameter:
                dateOfBirth = parameter.split('=')[1]
        print(register(username, password, password2, dateOfBirth))

    elif('manage.py' and 'user_login' in sys.argv):
        for parameter in sys.argv:
            if 'username' in parameter:
                username = parameter.split('=')[1]
            elif 'password' in parameter:
                password = parameter.split('=')[1]
        login(username, password)
    elif('manage.py' and 'run_server' in sys.argv):
        server("127.0.0.1", 7001)