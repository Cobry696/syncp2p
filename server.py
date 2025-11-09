class Server:
    
    """
    nodeID: Unique ID generated from session ID
    resyncPaths: paths that will be pulled from when broadcasting data to sync
    can only broadcast local data in which the first value of the row is equal to the nodeID
    """

    def __init__(nodeID : int, resyncPaths : tuple) -> None:
        self.nodeID = nodeID
        self.resyncPaths = resyncPaths