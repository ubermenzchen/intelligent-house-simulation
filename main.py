import sys
import socket
import events

def main(args):

    PORT = args[0]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', PORT))
    server.listen()

    return 0

if __name__ == '__main__':
    main(sys.argv[1:])