from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.gp import *


class XCAFView_ProjectionType(IntEnum):
    XCAFView_ProjectionType_NoCamera: int = ...
    XCAFView_ProjectionType_Parallel: int = ...
    XCAFView_ProjectionType_Central: int = ...

XCAFView_ProjectionType_NoCamera = XCAFView_ProjectionType.XCAFView_ProjectionType_NoCamera
XCAFView_ProjectionType_Parallel = XCAFView_ProjectionType.XCAFView_ProjectionType_Parallel
XCAFView_ProjectionType_Central = XCAFView_ProjectionType.XCAFView_ProjectionType_Central

class XCAFView_Object(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theObj: XCAFView_Object) -> None: ...
    def BackPlaneDistance(self) -> float: ...
    def ClippingExpression(self) -> TCollection_HAsciiString: ...
    def CreateGDTPoints(self, theLenght: int) -> None: ...
    def FrontPlaneDistance(self) -> float: ...
    def GDTPoint(self, theIndex: int) -> gp_Pnt: ...
    def HasBackPlaneClipping(self) -> bool: ...
    def HasFrontPlaneClipping(self) -> bool: ...
    def HasGDTPoints(self) -> bool: ...
    def HasViewVolumeSidesClipping(self) -> bool: ...
    def Name(self) -> TCollection_HAsciiString: ...
    def NbGDTPoints(self) -> int: ...
    def ProjectionPoint(self) -> gp_Pnt: ...
    def SetBackPlaneDistance(self, theDistance: float) -> None: ...
    def SetClippingExpression(self, theExpression: TCollection_HAsciiString) -> None: ...
    def SetFrontPlaneDistance(self, theDistance: float) -> None: ...
    def SetGDTPoint(self, theIndex: int, thePoint: gp_Pnt) -> None: ...
    def SetName(self, theName: TCollection_HAsciiString) -> None: ...
    def SetProjectionPoint(self, thePoint: gp_Pnt) -> None: ...
    def SetType(self, theType: XCAFView_ProjectionType) -> None: ...
    def SetUpDirection(self, theDirection: gp_Dir) -> None: ...
    def SetViewDirection(self, theDirection: gp_Dir) -> None: ...
    def SetViewVolumeSidesClipping(self, theViewVolumeSidesClipping: bool) -> None: ...
    def SetWindowHorizontalSize(self, theSize: float) -> None: ...
    def SetWindowVerticalSize(self, theSize: float) -> None: ...
    def SetZoomFactor(self, theZoomFactor: float) -> None: ...
    def Type(self) -> XCAFView_ProjectionType: ...
    def UnsetBackPlaneClipping(self) -> None: ...
    def UnsetFrontPlaneClipping(self) -> None: ...
    def UpDirection(self) -> gp_Dir: ...
    def ViewDirection(self) -> gp_Dir: ...
    def WindowHorizontalSize(self) -> float: ...
    def WindowVerticalSize(self) -> float: ...
    def ZoomFactor(self) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes

