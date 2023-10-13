from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TColStd import *
from OCC.Core.Aspect import *
from OCC.Core.TopoDS import *
from OCC.Core.Vrml import *
from OCC.Core.TopTools import *
from OCC.Core.HLRAlgo import *
from OCC.Core.Poly import *
from OCC.Core.TColgp import *
from OCC.Core.BRepAdaptor import *


class VrmlConverter_TypeOfCamera(IntEnum):
    VrmlConverter_NoCamera: int = ...
    VrmlConverter_PerspectiveCamera: int = ...
    VrmlConverter_OrthographicCamera: int = ...

VrmlConverter_NoCamera = VrmlConverter_TypeOfCamera.VrmlConverter_NoCamera
VrmlConverter_PerspectiveCamera = VrmlConverter_TypeOfCamera.VrmlConverter_PerspectiveCamera
VrmlConverter_OrthographicCamera = VrmlConverter_TypeOfCamera.VrmlConverter_OrthographicCamera

class VrmlConverter_TypeOfLight(IntEnum):
    VrmlConverter_NoLight: int = ...
    VrmlConverter_DirectionLight: int = ...
    VrmlConverter_PointLight: int = ...
    VrmlConverter_SpotLight: int = ...

VrmlConverter_NoLight = VrmlConverter_TypeOfLight.VrmlConverter_NoLight
VrmlConverter_DirectionLight = VrmlConverter_TypeOfLight.VrmlConverter_DirectionLight
VrmlConverter_PointLight = VrmlConverter_TypeOfLight.VrmlConverter_PointLight
VrmlConverter_SpotLight = VrmlConverter_TypeOfLight.VrmlConverter_SpotLight

class VrmlConverter_Curve:
    pass

class VrmlConverter_DeflectionCurve:
    pass

class VrmlConverter_Drawer(Standard_Transient):
    def __init__(self) -> None: ...
    def DeviationCoefficient(self) -> float: ...
    def DisableDrawHiddenLine(self) -> None: ...
    def Discretisation(self) -> int: ...
    def DrawHiddenLine(self) -> bool: ...
    def EnableDrawHiddenLine(self) -> None: ...
    def FreeBoundaryAspect(self) -> VrmlConverter_LineAspect: ...
    def FreeBoundaryDraw(self) -> bool: ...
    def HiddenLineAspect(self) -> VrmlConverter_LineAspect: ...
    def IsoOnPlane(self) -> bool: ...
    def LineAspect(self) -> VrmlConverter_LineAspect: ...
    def MaximalChordialDeviation(self) -> float: ...
    def MaximalParameterValue(self) -> float: ...
    def PointAspect(self) -> VrmlConverter_PointAspect: ...
    def SeenLineAspect(self) -> VrmlConverter_LineAspect: ...
    def SetDeviationCoefficient(self, aCoefficient: float) -> None: ...
    def SetDiscretisation(self, d: int) -> None: ...
    def SetFreeBoundaryAspect(self, anAspect: VrmlConverter_LineAspect) -> None: ...
    def SetFreeBoundaryDraw(self, OnOff: bool) -> None: ...
    def SetHiddenLineAspect(self, anAspect: VrmlConverter_LineAspect) -> None: ...
    def SetIsoOnPlane(self, OnOff: bool) -> None: ...
    def SetLineAspect(self, anAspect: VrmlConverter_LineAspect) -> None: ...
    def SetMaximalChordialDeviation(self, aChordialDeviation: float) -> None: ...
    def SetMaximalParameterValue(self, Value: float) -> None: ...
    def SetPointAspect(self, anAspect: VrmlConverter_PointAspect) -> None: ...
    def SetSeenLineAspect(self, anAspect: VrmlConverter_LineAspect) -> None: ...
    def SetShadingAspect(self, anAspect: VrmlConverter_ShadingAspect) -> None: ...
    def SetTypeOfDeflection(self, aTypeOfDeflection: Aspect_TypeOfDeflection) -> None: ...
    def SetUIsoAspect(self, anAspect: VrmlConverter_IsoAspect) -> None: ...
    def SetUnFreeBoundaryAspect(self, anAspect: VrmlConverter_LineAspect) -> None: ...
    def SetUnFreeBoundaryDraw(self, OnOff: bool) -> None: ...
    def SetVIsoAspect(self, anAspect: VrmlConverter_IsoAspect) -> None: ...
    def SetWireAspect(self, anAspect: VrmlConverter_LineAspect) -> None: ...
    def SetWireDraw(self, OnOff: bool) -> None: ...
    def ShadingAspect(self) -> VrmlConverter_ShadingAspect: ...
    def TypeOfDeflection(self) -> Aspect_TypeOfDeflection: ...
    def UIsoAspect(self) -> VrmlConverter_IsoAspect: ...
    def UnFreeBoundaryAspect(self) -> VrmlConverter_LineAspect: ...
    def UnFreeBoundaryDraw(self) -> bool: ...
    def VIsoAspect(self) -> VrmlConverter_IsoAspect: ...
    def WireAspect(self) -> VrmlConverter_LineAspect: ...
    def WireDraw(self) -> bool: ...

class VrmlConverter_HLRShape:
    pass

class VrmlConverter_LineAspect(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aMaterial: Vrml_Material, OnOff: bool) -> None: ...
    def HasMaterial(self) -> bool: ...
    def Material(self) -> Vrml_Material: ...
    def SetHasMaterial(self, OnOff: bool) -> None: ...
    def SetMaterial(self, aMaterial: Vrml_Material) -> None: ...

class VrmlConverter_PointAspect(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aMaterial: Vrml_Material, OnOff: bool) -> None: ...
    def HasMaterial(self) -> bool: ...
    def Material(self) -> Vrml_Material: ...
    def SetHasMaterial(self, OnOff: bool) -> None: ...
    def SetMaterial(self, aMaterial: Vrml_Material) -> None: ...

class VrmlConverter_Projector(Standard_Transient):
    def __init__(self, Shapes: TopTools_Array1OfShape, Focus: float, DX: float, DY: float, DZ: float, XUp: float, YUp: float, ZUp: float, Camera: Optional[VrmlConverter_TypeOfCamera] = VrmlConverter_NoCamera, Light: Optional[VrmlConverter_TypeOfLight] = VrmlConverter_NoLight) -> None: ...
    def Camera(self) -> VrmlConverter_TypeOfCamera: ...
    def Light(self) -> VrmlConverter_TypeOfLight: ...
    def Projector(self) -> HLRAlgo_Projector: ...
    def SetCamera(self, aCamera: VrmlConverter_TypeOfCamera) -> None: ...
    def SetLight(self, aLight: VrmlConverter_TypeOfLight) -> None: ...

class VrmlConverter_ShadedShape:
    @staticmethod
    def ComputeNormal(aFace: TopoDS_Face, pc: Poly_Connect, Nor: TColgp_Array1OfDir) -> None: ...

class VrmlConverter_ShadingAspect(Standard_Transient):
    def __init__(self) -> None: ...
    def FrontMaterial(self) -> Vrml_Material: ...
    def HasMaterial(self) -> bool: ...
    def HasNormals(self) -> bool: ...
    def SetFrontMaterial(self, aMaterial: Vrml_Material) -> None: ...
    def SetHasMaterial(self, OnOff: bool) -> None: ...
    def SetHasNormals(self, OnOff: bool) -> None: ...
    def SetShapeHints(self, aShapeHints: Vrml_ShapeHints) -> None: ...
    def ShapeHints(self) -> Vrml_ShapeHints: ...

class VrmlConverter_WFDeflectionRestrictedFace:
    pass

class VrmlConverter_WFDeflectionShape:
    pass

class VrmlConverter_WFRestrictedFace:
    pass

class VrmlConverter_WFShape:
    pass

class VrmlConverter_IsoAspect(VrmlConverter_LineAspect):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, aMaterial: Vrml_Material, OnOff: bool, aNumber: int) -> None: ...
    def Number(self) -> int: ...
    def SetNumber(self, aNumber: int) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes

