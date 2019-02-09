from config import HOST, PORT, NICK, PSWD
import socket


class TwitchSocket():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        self.send("PASS " + PSWD)
        self.send("NICK " + NICK)
        self.send("JOIN #" + NICK)
        self.send("Test post")
        while "End of /NAMES list" not in self.recv():
            pass

    def send(self, text):
        self.sock.send(bytes(text + "\r\n", "UTF-8"))

    def recv(self):
        return str(self.sock.recv(1024))

    def recv_lines(self):
        return self.recv().split("\\r\\n")
