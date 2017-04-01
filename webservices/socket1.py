import socket
cnn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cnn.connect(('www.pythonlearn.com', 80))
cnn.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
while True:
    data=cnn.recv(512)
    if len(data)<1:
        break
    print data
cnn.close()
