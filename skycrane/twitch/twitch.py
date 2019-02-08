import socket


class TwitchSocket():
    def __init__(self, host, port, nick, pswd):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.send("PASS " + pswd)
        self.send("NICK " + nick)
        self.send("JOIN #" + nick)
        self.send("Test post")
        while self.recv() != "End of /NAMES list":
            pass

    def send(self, text):
        self.sock.send(bytes(text + "\r\n", "UTF-8"))

    def recv(self):
        return str(self.sock.recv(1024))

    def recv_lines(self):
        return self.recv().split("\\r\\n")
