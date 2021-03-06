"""
Application custom exceptions.
"""

class NodeDisconnectException(Exception):
    """
    This exception is thrown when node detects a
    disconnection from the node it is connected.
    """

class InvalidMessageChecksum(Exception):
    """
    This exception is thrown when the checksum for a
    message in a message header doesn't match the actual
    checksum of the message.
    """
