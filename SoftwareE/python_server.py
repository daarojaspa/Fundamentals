import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen(8)
#this is just the part that accepts conections  another socket is need it to  talk to the client and this goes in the while loop
while True:
    client, addres = server.accept()
    response=client.recv(1024).decode()#desirialization from string to byte format because this is tcp
    if response:
        first_line=response.splitlines()[0]
    else:
        first_line=""
    parts=first_line.split()
    print(parts)
    body_bytes = "Funciona mierda".encode()
    length = len(body_bytes)
    method=parts[0].encode()
    path=parts[1]
    if path != "/":
        answer = (
            "HTTP/1.1 404 Notfound\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            f"Content-Length: {length}\r\n"
            "\r\n"
            
            "Error Not found"
        )
    else:   
        answer = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            f"Content-Length: {length}\r\n"
            "\r\n"
            
            "body:Funciona mierda"
        )

    client.sendall(answer.encode() + body_bytes)
    
    ##parsing the first line in to method and path
    ## SEnd back a status line
    ## close the conection 
    client.close()

