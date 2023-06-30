# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI_cmodule
import PyFnAttribute
import typing
from typing import Any, overload

@overload
def BuildAttrListFromDynamicParameterGroup(groupParam: NodegraphAPI_cmodule.Parameter, graphState: NodegraphAPI_cmodule.GraphState, applyLocalSettings: bool = ..., attrPath: str = ..., alwaysIncludeSet: list[str] = ..., multisampleDefault: bool = ...) -> list: ...
@overload
def BuildAttrListFromDynamicParameterGroup(groupParam: NodegraphAPI_cmodule.Parameter, frameTime: float, applyLocalSettings: bool = ..., attrPath: str = ..., alwaysIncludeSet: list[str] = ..., multisampleDefault: bool = ...) -> list: ...
def BuildGroupAttrFromParam(groupParam: NodegraphAPI_cmodule.Parameter, frameTime: float, inherit: bool = ..., returnRawAttrPaths: bool = ..., includeEmpty: bool = ...) -> Any: ...
def BuildHierarchyCreateOpArgs(frameTime: float, groupParameter: NodegraphAPI_cmodule.Parameter, rootAttrName: str = ...) -> PyFnAttribute.GroupAttribute: ...
def DefaultDAPCookOrder() -> PyFnAttribute.Attribute: ...
@overload
def EvaluateBoolExpresion(expression: str, tags: typing.Sequence) -> bool: ...
@overload
def EvaluateBoolExpresion(expression: str, tags: set) -> bool: ...
def GetLeafAttrPairs(groupAttribute: PyFnAttribute.GroupAttribute, prefix: str = ...) -> list: ...