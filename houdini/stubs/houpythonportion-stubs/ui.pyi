# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtGui
import PySide6.QtWidgets
import hou
import typing
from collections.abc import Callable as Callable, Collection, Sequence
from typing import Literal, TypedDict

_NodeDataSelection = TypedDict('_NodeDataSelection', {'Parameters': list[hou.Parm | hou.ParmTuple], 'Attributes': list[tuple[hou.Attrib, int]], 'Transforms': list[tuple[hou.OpNode, str, str | None]], 'Bounding Boxes': list[tuple[hou.OpNode, str]], 'Custom': list[tuple[hou.OpNode, str]]}, total=False)
_NodeDataInitialSelection = TypedDict('_NodeDataInitialSelection', {'Parameters': Sequence[hou.Parm | hou.ParmTuple], 'Attributes': Sequence[tuple[hou.Attrib, int]], 'Transforms': Sequence[tuple[hou.Node, str, str | None]], 'Bounding Boxes': Sequence[tuple[hou.Node, str | None]], 'Custom': Sequence[tuple[hou.Node, str]]}, total=False)

def openTypePropertiesDialog(self: hou.ui, node_or_node_type: hou.Node | hou.NodeType, promote_spare_parms: bool = False, immediately_save: bool = False) -> None:
    """
openTypePropertiesDialog(node_or_node_type, promote_spare_parms=False,
immediately_save=False)

    Given a hou.OpNode or hou.OpNodeType instance, open the type
    properties dialog.


    promote_spare_parms
        If this parameter is True and you passed in a node instance,
        automatically promote any spare parameters on the node into
        parameters on the node type.

    immediately_save
        When true, immediately save the current state of the node type,
        as if you clicked Apply in the type properties dialog.

"""
def selectFile(self: hou.ui, start_directory: str | None = None, title: str | None = None, collapse_sequences: bool = False, file_type: hou.EnumValue[hou.fileType] = ..., file_types: Collection[hou.EnumValue[hou.fileType]] = ..., pattern: str | None = None, default_value: str | None = None, multiple_select: bool = False, image_chooser: bool | None = None, chooser_mode: hou.EnumValue[hou.fileChooserMode] = ..., width: int = 0, height: int = 0) -> str:
    '''
selectFile(start_directory=None, title=None, collapse_sequences=False,
file_type=hou.fileType.Any, file_types: Collection[hou.fileType] = ...,
pattern=None, default_value=None, multiple_select=False,
image_chooser=None, chooser_mode=hou.fileChooserMode.ReadAndWrite,
width=0, height=0) -> str

    Pop up a window with a file chooser dialog and wait for the user to
    choose a file name. Returns the path to the file that was selected.

    To restrict the type of file the user can choose, pass a
    hou.fileType value to the file_type keyword argument. To allow
    multiple different types, you can pass a set of hou.fileType values
    to the file_types keyword argument instead.

    If you want the user to select a directory instead of a file, use
    hou.fileType.Directory as the file_type. If you want to allow the
    user to choose either a file or a directory, pass a file type and
    hom.fileType.Directory to the file_types argument:

  > # Allow the user to choose a file or a directory
  > path = hou.ui.selectFile(
  >     title="Choose the file or directory to save the scene to",
  >     file_type=[hou.fileType.Usd, hou.fileType.Directory],
  >     chooser_mode=hou.fileChooserMode.Write,
  > )

    start_directory`
        The directory the dialog should initially start in. On Windows
        you must use forward slashes (/) in this path instead of
        backslashes (\\). For example, start_directory="D:/temp".

    title
        The window title for the dialog.

    collapse_sequences`
        Whether sequences of files with common numeric patterns should
        be collapsed into patterns containing $F.

    file_type
        A hou.fileType value to control what type of file the user can
        select. The set of visible files is determined by this file type
        and the pattern. To allow multiple types, use the file_types
        argument instead.

    file_types
        A collection of hou.fileType values to control what types of
        file the user can select. This is especially useful if you want
        to allow the user to select a file or a directory. In that case,
        pass a file type and the hou.fileType.Directory value.


        NOTE
            If you pass both file_type and file_types, the function uses
            file_type and ignores the value of file_types.

    pattern
        Only files matching this pattern (and anything restricted by the
        file type) will be listed. By default, everything matches the
        pattern.


        WARNING
            When a default value of None is used, the pattern will be
            the same as what the file dialog of the given <file_type>
            last used. Always use an explicit value for <pattern> if you
            want it to be predictable.

    default_value
        The default contents of the file name field in the dialog.

    multiple_select
        Whether the user may select multiple files.

    image_chooser
        Whether the dialog shows image thumbnails (True/False). If None
        Show Images for Image Files in File Browsers setting (Edit >
        Preferences > General User Interface) will be used.

    chooser_mode
        A hou.fileChooserMode enumeration value to say if the user is
        being prompted for a file to read from, write to, or either.

    width
        The chooser dialog\'s width. If 0, then the chooser dialog uses a
        default width.

    height
        The chooser dialog\'s height. If 0, then the chooser dialog uses
        a default height.

'''
@typing.overload
def selectNode(self: hou.ui, relative_to_node: hou.Node | None = ..., initial_node: hou.Node | None = ..., node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ..., title: str | None = ..., width: int = ..., height: int = ..., multiple_select: Literal[False] = ..., custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...) -> str | None: ...
@typing.overload
def selectNode(self: hou.ui, relative_to_node: hou.Node | None = ..., initial_node: hou.Node | None = ..., node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ..., title: str | None = ..., width: int = ..., height: int = ..., *, multiple_select: Literal[True], custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...) -> tuple[str, ...] | None: ...
@typing.overload
def selectNode(self: hou.ui, relative_to_node: hou.Node | None = ..., initial_node: hou.Node | None = ..., node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = ..., title: str | None = ..., width: int = ..., height: int = ..., multiple_select: bool = ..., custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = ...) -> str | tuple[str, ...] | None: ...
def createQtIcon(self: hou.ui, icon_name: str, width: int | None = None, height: int | None = None) -> PySide6.QtGui.QIcon:
    """
createQtIcon(name, width=32, height=32)

    This method is deprecated. Call hou.qt.Icon instead.

"""
def mainQtWindow(self: hou.ui) -> PySide6.QtWidgets.QWidget | None:
    """
mainQtWindow(self)

    This method is deprecated. Call hou.qt.mainWindow instead.

"""
def qtStyleSheet(self: hou.ui) -> str:
    """
qtStyleSheet()

    This method is deprecated. Call hou.qt.styleSheet instead.

"""
def selectAttrib(self: hou.ui, initial_selection: Sequence[tuple[hou.Attrib, int]] | None = None, multiple_select: bool = False, expand_components: bool = True, width: int = 0, height: int = 0) -> list[tuple[hou.Attrib, int]] | tuple[()]:
    '''
selectAttrib(initial_selection=(), multiple_select=False,
expand_components=True, width=0, height=0) -> tuple of
([Hom:hou.Attrib], int)

    Pop up a chooser dialog that prompts the user to select a geometry
    attribute in the scene. Return a tuple of the selected attributes
    represented as pairs of hou.Attrib and integer values. Return an
    empty tuple if the selection operation was canceled.


    initial_selection
        Optionally set this argument to a tuple of attributes to be pre-
        selected when the chooser dialog opens. The tuple must contain
        pairs of hou.Attrib and integer pairs. This matches the
        structure of the tuple that is returned by the function. If
        expand_components is set to True then the integer values in the
        tuple must be set to -1.

    multiple_select
        If set to True then the user can select multiple attributes from
        the chooser dialog.

    expand_components
        If set to True then the chooser dialog displays the components
        of the attributes (i.e. P[0], P[1], P[2]) and the user is
        prompted to select an attribute component. In this case the
        integer values in the returned tuple are set to selected
        component indices.

        If set to False then the user is prompted to select attributes
        and the integer values in the returned tuple are set to -1.

    width
        The chooser dialog\'s width. If 0, then the chooser dialog uses a
        default width.

    height
        The chooser dialog\'s height. If 0, then the chooser dialog uses
        a default height.

    Example:

  > # Pre-select the 2nd component of the \'myAttr\' point attribute on the
  > # /obj/geo1/OUT Sop node.
  > attrib = hou.node("/obj/geo1/OUT").geometry().findPointAttrib("myAttr")
  > attrib_component_index = 1
  > preselected_attribs=((attrib, attrib_component_index), )
  > 
  > # Prompt the user to select an attribute.
  > selected_attribs = hou.ui.selectAttrib(
  >     initial_selection=preselected_attribs)
  > 
  > # Output the selected attribute.
  > print selected_attribs

    Example with expand_components set to False:

  > # Pre-select the \'myAttr\' point attribute on the
  > # /obj/geo1/OUT Sop node.
  > attrib = hou.node("/obj/geo1/OUT").geometry().findPointAttrib("myAttr")
  > attrib_component_index = -1
  > preselected_attribs=((attrib, attrib_component_index), )
  > 
  > # Prompt the user to select an attribute.
  > selected_attribs = hou.ui.selectAttrib(
  >     initial_selection=preselected_attribs,
  >     expand_components=False)
  > 
  > # Output the selected attribute.
  > print selected_attribs
'''
def setApplicationTheme(self: hou.ui, name: str, save: bool = True) -> None:
    '''
setApplicationTheme(name: str, save=True) -> str

    Switches the current color theme in the new UI (since Houdini 22).


    name
        The name of the theme to switch to. This is the name as
        displayed in the theme list in the theme editor (Edit > Color
        Theme).

    save
        If True, the theme is set as the user preference. If False,
        Houdini uses the theme but doesn\'t change the preference, so if
        you quit and restart the theme will revert to your preferred
        theme. This option may be useful for previewing a different
        theme or changing the theme temporarily.

  > hou.ui.setApplicationTheme("Mech Pilot", save=False)
'''
def selectNodeData(self: hou.ui, title: str | None = None, message: str | None = None, width: int = 0, height: int = 0, initial_selection: _NodeDataInitialSelection | None = None, node_type_filter: hou.EnumValue[hou.nodeTypeFilter] | None = None, multiple_select: bool = False, include_data_type_headers: bool = True, include_parms: bool = True, include_object_transforms: bool = True, include_geometry_bounding_boxes: bool = True, include_geometry_attributes: bool = True, expand_components: bool = True, custom_data_callback: Callable[[hou.OpNode], Sequence[str]] | None = None, custom_node_filter_callback: Callable[[hou.OpNode], bool] | None = None, help_url: str | None = None) -> _NodeDataSelection:
    '''
selectNodeData(title=None, message=None, width=0, height=0,
initial_selection=0, node_type_filter=None, multiple_select=False,
include_data_type_headers=True, include_parms=True,
include_object_transforms=True, include_geometry_bounding_boxes=True,
include_geometry_attributes=True, expand_components=True,
custom_data_callback=None, custom_node_filter_callback=None,
help_url=None) -> dict

    Pop up a chooser dialog that prompts the user to select data from a
    node. The data can be a parameter, a component from an object node\'s
    transform, a geometry node\'s bounding box property, a geometry
    attribute, or even custom data defined by the custom_data_callback
    argument. Return a dictionary of selected data organized by the
    following keys :

  * Parameters

        Contains a tuple of selected parameters. The elements in the
        tuple are hou.Parm objects. If expand_components is False then
        the elements are hou.ParmTuple objects.

  * Transforms

        Contains a tuple of selected object node transforms or transform
        components. The elements in the tuple are 3-tuples of the form
        (node, transform_type, transform_component) where node is the
        hou.OpNode object that the selected transform is pulled from,
        transform_type is the type of transform (either Local or World),
        and transform_component is the specific component selected from
        the transform (i.e. Rotate[X]). If the whole transform is
        selected instead of a component then transform_component is
        None.

  * Bounding Boxes

        Contains a tuple of selected geometry node bounding box
        properties. The elements in the tuple are 2-tuples of the form
        (node, bbox_property) where node is the hou.OpNode object that
        the selected bounding box property is pulled from, and
        bbox_property is the specific bounding box property (i.e.
        Size[X]).

  * Attributes

        Contains a tuple of selected geometry attributes or attribute
        components. The elements in the tuple are 2-tuples of the form
        (attrib, attrib_index) where attrib is the selected hou.Attrib
        object and attrib_index is the index of the selected attribute
        component. If expand_components is False then attrib_index is
        always -1.

  * Custom

        Contains a tuple of selected custom data as specified by the
        custom_data_callback argument. The elements in the tuple are
        2-tuples of the form (node, custom_data) where node is the
        selected hou.OpNode object that the custom data is attached to
        and custom_data is the actual data.


    NOTE
        If no data is selected for a specific key then the key does not
        exist in the dictionary. For example, if no parameters are
        selected then the Parameters key does not exist.


    title
        The chooser dialog\'s window title. If set to None then the
        window title defaults to Choose Node Data.

    message
        Optional messaging to appear in the chooser dialog below the
        node data tree.

    width
        The chooser dialog\'s width. If 0, then the chooser dialog uses a
        default width.

    height
        The chooser dialog\'s height. If 0, then the chooser dialog uses
        a default height.

    initial_selection
        Optionally set this argument to a dictionary of node data to be
        pre-selected when the chooser dialog opens. The dictionary must
        contain at least one of the Parameters, Transforms, Attributes,
        Custom keys. The values of the keys must be tuples of elements
        that match the elements of the returned dictionary. For example,
        the Parameters tuple must contain hou.Parm or hou.ParmTuple
        objects. The Transforms tuple must contain (node,
        transform_type, transform_component) tuples. The Attributes
        tuple must contain (attrib, attrib_index) tuples. The Custom
        tuple must contain (node, custom_data) tuples.

    node_type_filter
        An optional hou.nodeTypeFilter enumerated value that determines
        which types of nodes appear in the tree view.

    multiple_select
        If set to True then the user can select multiple node data from
        the chooser dialog.

    include_data_type_headers
        If set to True then headers appear in the node data tree for
        each of the data types (i.e. Parameters, Transforms, Attributes)
        except for the Custom data type.

    include_parms
        Include parameters in the node data tree.

    include_object_transforms
        Include object transforms in the node data tree.

    include_geometry_bounding_boxes
        Include geometry bounding boxes in the node data tree.

    include_geometry_attributes
        Include geometry attributes in the node data tree.

    expand_components
        If set to True then the chooser dialog displays the sub-
        components of parameters (i.e. tx instead of t), transforms
        (i.e. Rotate[X] instead of Rotate) and attributes (i.e. P[0]
        instead of P). The user is prompted to select sub-components
        instead of the complete data.

    custom_data_callback
        A Python callback function that is invoked for each node in the
        chooser dialog. The callback accepts a single hou.OpNode
        argument and returns a string tuple of custom data to appear in
        the node.

        You can specify subpaths for the custom data to organize them
        into a tree hierarchy. For example, if the callback returns
        ("Fruits/Apples", "Fruits/Bananas", "Fruits/Oranges") then a
        Fruits row will appear in the node with Apples, Bananas and
        Oranges inside of Fruits.

        Note that the non-leaf parts of a custom data path are not
        selectable. If you want those parts to be selectable then return
        them as separate entries in the tuple. For example, if you want
        Fruits to also be selectable then the callback should return
        ("Fruits", "Fruits/Apples", "Fruits/Bananas", "Fruits/Oranges").

    custom_node_filter_callback
        A Python callback function that is invoked for each node in the
        chooser dialog. The callback accepts a single hou.OpNode
        argument and returns a boolean of whether or not the node should
        be shown in the chooser dialog.

    help_url
        Optional argument for associating a help page with the node data
        chooser. If this argument is specified then a \'?\' help button
        appears in the chooser dialog.

    Basic Example:

  > # Prompt to select node data.  Show all types of data.
  > selected_data = hou.ui.selectNodeData()
  > 
  > # Print out selected parameters (if any).
  > if "Parameters" in selected_data:
  >     for parm in selected_data["Parameters"]:
  >         print "Selected Parm: ", parm
  > 
  > # Print out selected object transforms (if any).
  > if "Transforms" in selected_data:
  >     for xform_info in selected_data["Transforms"]:
  >         print "Selected Node: ", xform_info[0]
  >         print "Selected Transform Type: ", xform_info[1]
  >         print "Selected Transform Component: ", xform_info[2]
  > 
  > # Print out selected geometry bounding boxes (if any).
  > if "Bounding Boxes" in selected_data:
  >     for bbox_info in selected_data["Bounding Boxes"]:
  >         print "Selected Node: ", bbox_info[0]
  >         print "Selected Bounding Box Property: ", bbox_info[1]
  > 
  > # Print out selected geometry attributes (if any).
  > if "Attributes" in selected_data:
  >     for attr_info in selected_data["Attributes"]:
  >         print "Selected Attribute: ", attr_info[0]
  >         print "Selected Attribute Index: ", attr_info[1]

    Here is an example of setting an initial selection:

  > # Pre-select the \'tx\', \'ty\' and \'tz\' parameters on /obj/geo1.
  > preselected_parms = (
  >     hou.parm("/obj/geo1/tx"), hou.parm("/obj/geo1/ty"), 
  >     hou.parm("/obj/geo1/tz"))
  > 
  > # Pre-select the scale z world transform component on /obj/geo1.
  > preselected_xforms = (
  >     (hou.node("/obj/geo1"), "World", "Scale[Z]"),
  > )
  > 
  > # Pre-select the centroid y bounding box property on /obj/geo1/OUT.
  > preselected_bboxes = (
  >     (hou.node("/obj/geo1/OUT"), "Centroid[Y]"),
  > )
  > 
  > # Pre-select the 2nd component of the \'myAttr\' point attribute on the
  > # /obj/geo1/OUT Sop node.
  > attrib = hou.node("/obj/geo1/OUT").geometry().findPointAttrib("myAttr")
  > attrib_component_index = 1
  > preselected_attribs=((attrib, attrib_component_index), )
  > 
  > # Build up the initial selection dictionary.
  > initial_selection = {
  >     "Parameters" : preselected_parms,
  >     "Transforms" : preselected_xforms,
  >     "Bounding Boxes" : preselected_bboxes,
  >     "Attributes" : preselected_attribs,
  > }
  > 
  > # Prompt the user to select node data.
  > selected_data = hou.ui.selectNodeData(
  >     initial_selection=initial_selection,
  >     multiple_select=True)
  > 
  > # Output the selected data.
  > print selected_data

    Here is an example of specifying custom data:

  > # Define the callback for returning custom data.
  > def getCustomData(node):
  >     # Add custom data only on Object nodes.
  >     if node.type().category().name() == "Object":
  >         return ["Fruits/Apples", "Fruits/Bananas", "Fruits/Oranges"]
  > 
  >     # Don\'t add custom data on all other nodes.
  >     return []
  > 
  > # Prompt the user to select node data.
  > selected_data = hou.ui.selectNodeData(custom_data_callback=getCustomData)
  > 
  > # Output the selected data.
  > print selected_data

    Here is an example of specifying a custom node filter:

  > # Define the callback for filtering nodes.
  > def hasNumberInName(node):
  >     # Only show nodes with numbers in the name.
  >     for letter in node.name():
  >         if letter in "1234567890":
  >             return True
  > 
  >     # Don\'t show nodes without a number in the name.
  >     return False
  > 
  > # Prompt the user to select node data.
  > selected_data = hou.ui.selectNodeData(custom_node_filter_callback=hasNumberInName)
  > 
  > # Output the selected data.
  > print selected_data
'''
def parameterPaneTabs(self: hou.ui, node: hou.Node | None, include_node_editors: bool = True) -> list[hou.ParameterEditor | hou.NetworkEditor]:
    """Return parameter editors displaying a given node including node editors
    with a displayed embedded parameter editor."""
def setParmFilterInEditors(self: hou.ui, node: hou.Node, parm_names: str) -> bool:
    """Iterate over parameter editors for a node and apply search filter."""
def scrollToParmsInEditors(self: hou.ui, parms: hou.Parm | hou.ParmTuple | list[hou.Parm] | list[hou.ParmTuple] | list[hou.Parm | hou.ParmTuple], pos: hou.EnumValue[hou.scrollPosition] = ...) -> bool:
    """Iterate over parameter editors for a node adjusting the scrollbar to
    center the parameters."""
def setMultiParmTabInEditors(self: hou.ui, parm: hou.Parm | hou.ParmTuple, index: int) -> bool:
    """Iterate over parameter editors for a node and set the index of a multi
    parm tab. Multi parm tabs aren't tied to real parameter."""
def switchTabsToParmInEditors(self: hou.ui, parm: hou.Parm | hou.ParmTuple) -> bool:
    """Switch the tabs containing a parameter to make the parameter visible.
    This also accounts for (non-nested) multi instance parameters."""
def sharedLayoutDataSource(self: hou.ui) -> hou.AssetGalleryDataSource: ...
def setSharedLayoutDataSource(self: hou.ui, data_source: hou.AssetGalleryDataSource) -> None: ...
def reloadSharedLayoutDataSource(self: hou.ui) -> None: ...
def isValidObject(self: hou.ui, hom_obj: object) -> bool:
    """
isValidObject(self, hom_obj) -> bool

    Returns True if the HOM object is still valid (i.e. not deleted),
    and False otherwise. Logs an error message to the log panel if the
    object has been deleted.

"""
