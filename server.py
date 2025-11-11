import socket
import threading

class Server:
    
    """
    nodeID: public and private id generated per account per device
    resyncPaths: paths that will be pulled from when broadcasting data to sync
    nodes: dict of known nodes in the network. In the form {nodePublicID, addr}
    """

    def __init__(self, nodeID : tuple, resyncPaths : tuple, nodes : dict, port=7070) -> None:
        self.nodeID = nodeID
        self.resyncPaths = resyncPaths
        self.nodes = nodes
        self.port = port
        self.comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # comm as in communication which is the attribute that stores the socket itself

    # Method that connects this node as a server to the network
    def connect(self, allowedConnections=2):

        """
        Method that connects this node as a server to the network
        """
        self.comm.bind(("0.0.0.0", self.port)) # binds the server to listen for incoming connections in the next line
        self.comm.listen() # starts the server listening for incoming connections
        self.acceptIncoming(allowedConnections)

    # Method that closes all client sockets
    def disconnect(self):
        for client in self.clients:
            client.close()

    # method that listens and connects to every incoming request
    def acceptIncoming(self, allowedConnections):
        connections = 0
        addrs = [] # stores all connected addresses to add to address list
        sockets = [] # stores all sockets for communication
        while connections < allowedConnections:
            clientSocket, addr = self.comm.accept()
            print(f"Connection from: {addr}")
            print(clientSocket.recv(1024).decode("UTF-8"))
            addrs.append(addr[0])
            sockets.append(socket)
            connections += 1
            #clientSocket.close()
        self.clients = sockets
        self.addrs = addrs

    # Method that receives data from each client and merges it into one variable
    def sync(self):
        pass

server = Server(("5", "10"), ("",), {6 : "127.0.0.1"})
server.connect()

    