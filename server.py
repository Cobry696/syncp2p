import socket
import threading

class Server:
    
    """
    nodeID: Unique ID generated from mac address and account details
    resyncPaths: paths that will be pulled from when broadcasting data to sync
    nodes: dict of known nodes in the network. In the form {nodePublicID, addr}
    """

    def __init__(nodeID : int, resyncPaths : tuple, nodes : dict, port=7070) -> None:
        self.nodeID = nodeID
        self.resyncPaths = resyncPaths
        self.nodes
        self.port = port
        self.comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # comm as in communication which is the attribute that stores the socket itself

    # Method that connects this node as a server to the network
    def connect(self):

        """
        Method that connects this node as a server to the network
        """

        self.comm.bind(("0.0.0.0", self.port)) # binds it to listen on all local addresses on user specified port
        acceptingThread = threading.Thread(target=self.acceptIncoming) # defines a thread for accepting incoming connections
        acceptingThread.start() # starts the accepting thread
        while True:
            pass

    def acceptIncoming(self):
        pass

    