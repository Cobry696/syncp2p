import socket
class Client:
    
    """
    nodeID: Unique ID generated from mac address and account details
    resyncPaths: paths that will be overwritten by data retreived from other servers
    nodes: dict of known nodes in the network. In the form {nodePublicID, addr}
    """

    def __init__(nodeID : int, resyncPaths : tuple, nodes : dict, port=7070) -> None: # constructor
        self.nodeID = nodeID
        self.resyncPaths = resyncPaths
        self.port = port
        self.comm = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # comm as in communication which is the attribute that stores the socket itself

    # Method that connects this node as a server to the network
    def connect(self):

        """
        Method that connects this node as a server to the network
        """

        self.comm.bind(("0.0.0.0", self.port))
        while True:
            pass

    def seekNodes(self):
        for node in self.nodes.items():
            self.comm.connect((node[1], port))