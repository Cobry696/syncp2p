class Client:
    
    """
    nodeID: Unique ID generated from session ID
    resyncPaths: paths that will be overwritten by data retreived from other servers
    """

    def __init__(nodeID : int, resyncPaths : tuple) -> None: # constructor
        self.nodeID = nodeID
        self.resyncPaths = resyncPaths

Client()