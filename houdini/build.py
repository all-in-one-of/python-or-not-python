import hou


def add_tool( name , **kwargs ):
    """Add a new tool on the Houdini shelf.

    @param (str) name:
    Internal name of this object.

    @param (str) label:
    Object's human-readable label.

    @param (hou.scriptLanguage) language:
    Represents the language in which the tool script is written.

    @param (str) script:
    Text of the script to run when the user clicks the tool in the shelf.

    @param (tuple) network_categories:
    A list of categories used to control the visibility of the tool in the TAB menu.

    @param (str) icon:
    Icon string for the tool.

    @return (hou.Tool):
    Returns a new hou.Tool object using the provided options.
    """

    if name in hou.shelves.tools():
        hou.shelves.tool( name ).destroy()

    return hou.shelves.newTool( name , **kwargs )

