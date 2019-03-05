"""
This script is an example of a basic Houdini node class.

It allows to have access to all hou.Node attributes thanks to
the __getattr__ function. As you may have noticed, it is not
possible to create an instance of hou.Node, so if you want to
create a custom class, you have to found a way to get all of
its attributes. So, that's why this class exists. And I found
this idea from from Ryan Bland, which is available freely on
his website.

This is the link : http://www.ryan-bland.com/CodeSamples/
You can found his HouNode and HouParm classes (and many other
scripts).

I just wanted to share with you a simple one. So don't hesitate
to use it too. You can do the same logic with the hou.Parm class
for example.
"""


import hou


class _HouNodeMetaclass(type):
    """A simple metaclass used to have the appropriate node by type.
    """

    def __call__( cls, nodeObj ):
        """Function called when the principal class is instantiate.

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
