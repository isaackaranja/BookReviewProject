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
    request_data = request_data.decode()
    print(f"request data: {request_data}")
    request_headers = request_data.split("\r\n")
    print("request_headers")
    print(request_headers)
    html_page = """
    <html>
      <head><title>BookReview</title></head>
      <body>
        <div>
          <form>
            <lable>username</lable><br>
            <input type"text" name="username" placeholder="username"><br>
            <lable>password</lable>
            <input type="text" name="password" placeholder="password"/><br>
            <lable>password2</lable><br>
            <input type="text" name="password2" placeholder="password2"/><br>
            <lable>Date Of Birth</lable><br>
            <input type="text" name="dateOfBirth" value="2020-01-02"/><br>
            <input type="submit" value="submit"/>
          </form>
        <div/>
      </body>
    </html>
    """
    response_status = "200 OK"
    if request_data.startswith("GET /?username"):
      date_of_birth = request_data.split("\r\n")[0].split("?")[1].split("&")[-1].split(" ")[0].split("=")
      request_data_list = request_data.split("\r\n")[0].split("?")[1].split("&")[:-1]
      register_data = {}
      register_data[date_of_birth[0]] = date_of_birth[1]
      for i in request_data_list:
        data_list = i.split("=")
        register_data[data_list[0]] = data_list[1]
      register(register_data.get("username"), register_data.get("password"), register_data.get("password2"), register_data.get("dateOfBirth"))

      print("request: ", request_data)
      print("hello world")
      response_status = "301 moved permanently\r\nLocation: /user/login"

    if request_data.startswith("GET /user/login"):
      html_page = """
      <html>
        <head><title>BookReview</title></head>
        <body>
          <div>
            <h2> You have been successfully been Registered</h2>
          </div>
        </body>
      </html>
      """
    client_connection.sendall(
      f"HTTP/1.1 {response_status}\r\nContent-Length: {len(html_page)}\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n{html_page}".encode()
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
        for j in sys.argv:
            if 'port' in j:
                port = j.split('=')[1]
        server("127.0.0.1", int(port))