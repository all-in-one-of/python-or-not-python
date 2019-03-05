import hou


class _HouNodeMetaclass(type):
    """A simple metaclass used to have the appropriate node by type.
    """

    def __call__( cls, nodeObj ):
        """Function called when the principal is instantiate.

        @param (str) nodeObj:
        Path of the node to instantiate.

        @param (HouNode) nodeObj:
        An instance of HouNode.

        @param (hou.Node) nodeObj:
        A Houdini node.

        @return (hou.Node):
        Returns an instance of hou.Node.
        """

        if isinstance(nodeObj, basestring):
            node = hou.node( nodeObj )
        elif isinstance(nodeObj, HouNode):
            node = hou.node(HouNode.path())
        elif isinstance(nodeObj, hou.Node):
            node = nodeObj
        else:
            raise TypeError('Wrong argument type.')

        return type.__call__(cls, node)

class HouNode(object):
    """Base class for a custom Houdini Node.
    """

    __metaclass__ = _HouNodeMetaclass

    def __init__(self, nodeObj):
        """Initialize the HouNode class.

        @param nodeObj:

        @return (None):
        No return value.
        """
        self.__node__ = nodeObj

    def __getattr__(self, name):
        """Get access to the hou.Node attributes.

        @param (str) name:
        Attribute name.

        @return (variant):
        Returns the attribute result.
        """
        return getattr(self.__node__, name)

    @staticmethod
    def wonderfulFunction():
        """Just a wonderful function.
        And sure... You can remove it if needed. It was
        just a way for me to share with you some happiness !

        @return (str):
        Returns a wonderful answer.
        """
        return "I hope your day is as wonderful as you are ! :)"
