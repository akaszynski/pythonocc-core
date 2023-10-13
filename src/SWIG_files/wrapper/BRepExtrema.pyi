from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.Extrema import *
from OCC.Core.Message import *
from OCC.Core.gp import *
from OCC.Core.Bnd import *
from OCC.Core.BVH import *
from OCC.Core.Poly import *

# the following typedef cannot be wrapped as is
BRepExtrema_ShapeList = NewType("BRepExtrema_ShapeList", Any)

class BRepExtrema_SeqOfSolution:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepExtrema_SolutionElem: ...
    def Last(self) -> BRepExtrema_SolutionElem: ...
    def Length(self) -> int: ...
    def Append(self, theItem: BRepExtrema_SolutionElem) -> BRepExtrema_SolutionElem: ...
    def Prepend(self, theItem: BRepExtrema_SolutionElem) -> BRepExtrema_SolutionElem: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepExtrema_SolutionElem: ...
    def SetValue(self, theIndex: int, theValue: BRepExtrema_SolutionElem) -> None: ...

class BRepExtrema_SupportType(IntEnum):
    BRepExtrema_IsVertex: int = ...
    BRepExtrema_IsOnEdge: int = ...
    BRepExtrema_IsInFace: int = ...

BRepExtrema_IsVertex = BRepExtrema_SupportType.BRepExtrema_IsVertex
BRepExtrema_IsOnEdge = BRepExtrema_SupportType.BRepExtrema_IsOnEdge
BRepExtrema_IsInFace = BRepExtrema_SupportType.BRepExtrema_IsInFace

class BRepExtrema_DistShapeShape:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Shape1: TopoDS_Shape, Shape2: TopoDS_Shape, F: Optional[Extrema_ExtFlag] = Extrema_ExtFlag_MINMAX, A: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    @overload
    def __init__(self, Shape1: TopoDS_Shape, Shape2: TopoDS_Shape, theDeflection: float, F: Optional[Extrema_ExtFlag] = Extrema_ExtFlag_MINMAX, A: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
    def InnerSolution(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def IsMultiThread(self) -> bool: ...
    def LoadS1(self, Shape1: TopoDS_Shape) -> None: ...
    def LoadS2(self, Shape1: TopoDS_Shape) -> None: ...
    def NbSolution(self) -> int: ...
    def ParOnEdgeS1(self, N: int) -> float: ...
    def ParOnEdgeS2(self, N: int) -> float: ...
    def ParOnFaceS1(self, N: int) -> Tuple[float, float]: ...
    def ParOnFaceS2(self, N: int) -> Tuple[float, float]: ...
    def Perform(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> bool: ...
    def PointOnShape1(self, N: int) -> gp_Pnt: ...
    def PointOnShape2(self, N: int) -> gp_Pnt: ...
    def SetAlgo(self, A: Extrema_ExtAlgo) -> None: ...
    def SetDeflection(self, theDeflection: float) -> None: ...
    def SetFlag(self, F: Extrema_ExtFlag) -> None: ...
    def SetMultiThread(self, theIsMultiThread: bool) -> None: ...
    def SupportOnShape1(self, N: int) -> TopoDS_Shape: ...
    def SupportOnShape2(self, N: int) -> TopoDS_Shape: ...
    def SupportTypeShape1(self, N: int) -> BRepExtrema_SupportType: ...
    def SupportTypeShape2(self, N: int) -> BRepExtrema_SupportType: ...
    def Value(self) -> float: ...

class BRepExtrema_DistanceSS:
    def __init__(self, theS1: TopoDS_Shape, theS2: TopoDS_Shape, theBox1: Bnd_Box, theBox2: Bnd_Box, theDstRef: float, theDeflection: Optional[float] = Precision.Confusion(), theExtFlag: Optional[Extrema_ExtFlag] = Extrema_ExtFlag_MINMAX, theExtAlgo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad) -> None: ...
    def DistValue(self) -> float: ...
    def IsDone(self) -> bool: ...
    def Seq1Value(self) -> BRepExtrema_SeqOfSolution: ...
    def Seq2Value(self) -> BRepExtrema_SeqOfSolution: ...

class BRepExtrema_ElementFilter:
    pass

class BRepExtrema_ExtCC:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> None: ...
    def Initialize(self, E2: TopoDS_Edge) -> None: ...
    def IsDone(self) -> bool: ...
    def IsParallel(self) -> bool: ...
    def NbExt(self) -> int: ...
    def ParameterOnE1(self, N: int) -> float: ...
    def ParameterOnE2(self, N: int) -> float: ...
    def Perform(self, E1: TopoDS_Edge) -> None: ...
    def PointOnE1(self, N: int) -> gp_Pnt: ...
    def PointOnE2(self, N: int) -> gp_Pnt: ...
    def SquareDistance(self, N: int) -> float: ...
    def TrimmedSquareDistances(self, P11: gp_Pnt, P12: gp_Pnt, P21: gp_Pnt, P22: gp_Pnt) -> Tuple[float, float, float, float]: ...

class BRepExtrema_ExtCF:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    def Initialize(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    def IsDone(self) -> bool: ...
    def IsParallel(self) -> bool: ...
    def NbExt(self) -> int: ...
    def ParameterOnEdge(self, N: int) -> float: ...
    def ParameterOnFace(self, N: int) -> Tuple[float, float]: ...
    def Perform(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    def PointOnEdge(self, N: int) -> gp_Pnt: ...
    def PointOnFace(self, N: int) -> gp_Pnt: ...
    def SquareDistance(self, N: int) -> float: ...

class BRepExtrema_ExtFF:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
    def Initialize(self, F2: TopoDS_Face) -> None: ...
    def IsDone(self) -> bool: ...
    def IsParallel(self) -> bool: ...
    def NbExt(self) -> int: ...
    def ParameterOnFace1(self, N: int) -> Tuple[float, float]: ...
    def ParameterOnFace2(self, N: int) -> Tuple[float, float]: ...
    def Perform(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
    def PointOnFace1(self, N: int) -> gp_Pnt: ...
    def PointOnFace2(self, N: int) -> gp_Pnt: ...
    def SquareDistance(self, N: int) -> float: ...

class BRepExtrema_ExtPC:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> None: ...
    def Initialize(self, E: TopoDS_Edge) -> None: ...
    def IsDone(self) -> bool: ...
    def IsMin(self, N: int) -> bool: ...
    def NbExt(self) -> int: ...
    def Parameter(self, N: int) -> float: ...
    def Perform(self, V: TopoDS_Vertex) -> None: ...
    def Point(self, N: int) -> gp_Pnt: ...
    def SquareDistance(self, N: int) -> float: ...
    def TrimmedSquareDistances(self, pnt1: gp_Pnt, pnt2: gp_Pnt) -> Tuple[float, float]: ...

class BRepExtrema_ExtPF:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, TheVertex: TopoDS_Vertex, TheFace: TopoDS_Face, TheFlag: Optional[Extrema_ExtFlag] = Extrema_ExtFlag_MINMAX, TheAlgo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad) -> None: ...
    def Initialize(self, TheFace: TopoDS_Face, TheFlag: Optional[Extrema_ExtFlag] = Extrema_ExtFlag_MINMAX, TheAlgo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad) -> None: ...
    def IsDone(self) -> bool: ...
    def NbExt(self) -> int: ...
    def Parameter(self, N: int) -> Tuple[float, float]: ...
    def Perform(self, TheVertex: TopoDS_Vertex, TheFace: TopoDS_Face) -> None: ...
    def Point(self, N: int) -> gp_Pnt: ...
    def SetAlgo(self, A: Extrema_ExtAlgo) -> None: ...
    def SetFlag(self, F: Extrema_ExtFlag) -> None: ...
    def SquareDistance(self, N: int) -> float: ...

class BRepExtrema_Poly:
    @staticmethod
    def Distance(S1: TopoDS_Shape, S2: TopoDS_Shape, P1: gp_Pnt, P2: gp_Pnt) -> Tuple[bool, float]: ...

class BRepExtrema_ProximityDistTool():
    @overload
    def __init__(self) -> None: ...
    @staticmethod
    def IsEdgeOnBorder(theTrgIdx: int, theFirstEdgeNodeIdx: int, theSecondEdgeNodeIdx: int, theTr: Poly_Triangulation) -> bool: ...
    @staticmethod
    def IsNodeOnBorder(theNodeIdx: int, theTr: Poly_Triangulation) -> bool: ...
    def LoadShapeLists(self, theShapeList1: BRepExtrema_ShapeList, theShapeList2: BRepExtrema_ShapeList) -> None: ...
    def LoadTriangleSets(self, theSet1: BRepExtrema_TriangleSet, theSet2: BRepExtrema_TriangleSet) -> None: ...
    def Perform(self) -> None: ...
    def ProximityDistance(self) -> float: ...
    def ProximityPoints(self, thePoint1: BVH_Vec3d, thePoint2: BVH_Vec3d) -> None: ...
    def RejectNode(self, theCornerMin: BVH_Vec3d, theCornerMax: BVH_Vec3d) -> Tuple[bool, float]: ...

class BRepExtrema_ShapeProximity:
    @overload
    def __init__(self, theTolerance: Optional[float] = Precision.Infinite()) -> None: ...
    @overload
    def __init__(self, theShape1: TopoDS_Shape, theShape2: TopoDS_Shape, theTolerance: Optional[float] = Precision.Infinite()) -> None: ...
    def ElementSet1(self) -> BRepExtrema_TriangleSet: ...
    def ElementSet2(self) -> BRepExtrema_TriangleSet: ...
    def GetSubShape1(self, theID: int) -> TopoDS_Shape: ...
    def GetSubShape2(self, theID: int) -> TopoDS_Shape: ...
    def IsDone(self) -> bool: ...
    def LoadShape1(self, theShape1: TopoDS_Shape) -> bool: ...
    def LoadShape2(self, theShape2: TopoDS_Shape) -> bool: ...
    def OverlapSubShapes1(self) -> BRepExtrema_MapOfIntegerPackedMapOfInteger: ...
    def OverlapSubShapes2(self) -> BRepExtrema_MapOfIntegerPackedMapOfInteger: ...
    def Perform(self) -> None: ...
    def ProxPntStatus1(self) -> False: ...
    def ProxPntStatus2(self) -> False: ...
    def Proximity(self) -> float: ...
    def ProximityPoint1(self) -> gp_Pnt: ...
    def ProximityPoint2(self) -> gp_Pnt: ...
    def SetNbSamples1(self, theNbSamples: int) -> None: ...
    def SetNbSamples2(self, theNbSamples: int) -> None: ...
    def SetTolerance(self, theTolerance: float) -> None: ...
    def Tolerance(self) -> float: ...

class BRepExtrema_SolutionElem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theDist: float, thePoint: gp_Pnt, theSolType: BRepExtrema_SupportType, theVertex: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, theDist: float, thePoint: gp_Pnt, theSolType: BRepExtrema_SupportType, theEdge: TopoDS_Edge, theParam: float) -> None: ...
    @overload
    def __init__(self, theDist: float, thePoint: gp_Pnt, theSolType: BRepExtrema_SupportType, theFace: TopoDS_Face, theU: float, theV: float) -> None: ...
    def Dist(self) -> float: ...
    def Edge(self) -> TopoDS_Edge: ...
    def EdgeParameter(self) -> float: ...
    def Face(self) -> TopoDS_Face: ...
    def FaceParameter(self) -> Tuple[float, float]: ...
    def Point(self) -> gp_Pnt: ...
    def SupportKind(self) -> BRepExtrema_SupportType: ...
    def Vertex(self) -> TopoDS_Vertex: ...

class BRepExtrema_TriangleSet(BVH_PrimitiveSet3d):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theFaces: BRepExtrema_ShapeList) -> None: ...
    def Box(self, theIndex: int) -> False: ...
    def Center(self, theIndex: int, theAxis: int) -> float: ...
    def Clear(self) -> None: ...
    def GetFaceID(self, theIndex: int) -> int: ...
    def GetShapeIDOfVtx(self, theIndex: int) -> int: ...
    def GetTrgIdxInShape(self, theIndex: int) -> int: ...
    @overload
    def GetVertices(self) -> BVH_Array3d: ...
    @overload
    def GetVertices(self, theIndex: int, theVertex1: BVH_Vec3d, theVertex2: BVH_Vec3d, theVertex3: BVH_Vec3d) -> None: ...
    def GetVtxIdxInShape(self, theIndex: int) -> int: ...
    def Init(self, theShapes: BRepExtrema_ShapeList) -> bool: ...
    def Size(self) -> int: ...
    def Swap(self, theIndex1: int, theIndex2: int) -> None: ...

class BRepExtrema_SelfIntersection(BRepExtrema_ElementFilter):
    @overload
    def __init__(self, theTolerance: Optional[float] = 0.0) -> None: ...
    @overload
    def __init__(self, theShape: TopoDS_Shape, theTolerance: Optional[float] = 0.0) -> None: ...
    def ElementSet(self) -> BRepExtrema_TriangleSet: ...
    def GetSubShape(self, theID: int) -> TopoDS_Face: ...
    def IsDone(self) -> bool: ...
    def LoadShape(self, theShape: TopoDS_Shape) -> bool: ...
    def OverlapElements(self) -> BRepExtrema_MapOfIntegerPackedMapOfInteger: ...
    def Perform(self) -> None: ...
    def SetTolerance(self, theTolerance: float) -> None: ...
    def Tolerance(self) -> float: ...

#classnotwrapped
class BRepExtrema_OverlapTool: ...

# harray1 classes
# harray2 classes
# hsequence classes

