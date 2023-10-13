from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.StepBasic import *
from OCC.Core.StepRepr import *
from OCC.Core.TCollection import *


class StepAP203_Array1OfApprovedItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_ApprovedItem: ...
    def __setitem__(self, index: int, value: StepAP203_ApprovedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_ApprovedItem]: ...
    def next(self) -> StepAP203_ApprovedItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_ApprovedItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_ApprovedItem: ...
    def Last(self) -> StepAP203_ApprovedItem: ...
    def Value(self, theIndex: int) -> StepAP203_ApprovedItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_ApprovedItem) -> None: ...

class StepAP203_Array1OfCertifiedItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_CertifiedItem: ...
    def __setitem__(self, index: int, value: StepAP203_CertifiedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_CertifiedItem]: ...
    def next(self) -> StepAP203_CertifiedItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_CertifiedItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_CertifiedItem: ...
    def Last(self) -> StepAP203_CertifiedItem: ...
    def Value(self, theIndex: int) -> StepAP203_CertifiedItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_CertifiedItem) -> None: ...

class StepAP203_Array1OfChangeRequestItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_ChangeRequestItem: ...
    def __setitem__(self, index: int, value: StepAP203_ChangeRequestItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_ChangeRequestItem]: ...
    def next(self) -> StepAP203_ChangeRequestItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_ChangeRequestItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_ChangeRequestItem: ...
    def Last(self) -> StepAP203_ChangeRequestItem: ...
    def Value(self, theIndex: int) -> StepAP203_ChangeRequestItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_ChangeRequestItem) -> None: ...

class StepAP203_Array1OfClassifiedItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_ClassifiedItem: ...
    def __setitem__(self, index: int, value: StepAP203_ClassifiedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_ClassifiedItem]: ...
    def next(self) -> StepAP203_ClassifiedItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_ClassifiedItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_ClassifiedItem: ...
    def Last(self) -> StepAP203_ClassifiedItem: ...
    def Value(self, theIndex: int) -> StepAP203_ClassifiedItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_ClassifiedItem) -> None: ...

class StepAP203_Array1OfContractedItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_ContractedItem: ...
    def __setitem__(self, index: int, value: StepAP203_ContractedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_ContractedItem]: ...
    def next(self) -> StepAP203_ContractedItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_ContractedItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_ContractedItem: ...
    def Last(self) -> StepAP203_ContractedItem: ...
    def Value(self, theIndex: int) -> StepAP203_ContractedItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_ContractedItem) -> None: ...

class StepAP203_Array1OfDateTimeItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_DateTimeItem: ...
    def __setitem__(self, index: int, value: StepAP203_DateTimeItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_DateTimeItem]: ...
    def next(self) -> StepAP203_DateTimeItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_DateTimeItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_DateTimeItem: ...
    def Last(self) -> StepAP203_DateTimeItem: ...
    def Value(self, theIndex: int) -> StepAP203_DateTimeItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_DateTimeItem) -> None: ...

class StepAP203_Array1OfPersonOrganizationItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_PersonOrganizationItem: ...
    def __setitem__(self, index: int, value: StepAP203_PersonOrganizationItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_PersonOrganizationItem]: ...
    def next(self) -> StepAP203_PersonOrganizationItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_PersonOrganizationItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_PersonOrganizationItem: ...
    def Last(self) -> StepAP203_PersonOrganizationItem: ...
    def Value(self, theIndex: int) -> StepAP203_PersonOrganizationItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_PersonOrganizationItem) -> None: ...

class StepAP203_Array1OfSpecifiedItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_SpecifiedItem: ...
    def __setitem__(self, index: int, value: StepAP203_SpecifiedItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_SpecifiedItem]: ...
    def next(self) -> StepAP203_SpecifiedItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_SpecifiedItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_SpecifiedItem: ...
    def Last(self) -> StepAP203_SpecifiedItem: ...
    def Value(self, theIndex: int) -> StepAP203_SpecifiedItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_SpecifiedItem) -> None: ...

class StepAP203_Array1OfStartRequestItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_StartRequestItem: ...
    def __setitem__(self, index: int, value: StepAP203_StartRequestItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_StartRequestItem]: ...
    def next(self) -> StepAP203_StartRequestItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_StartRequestItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_StartRequestItem: ...
    def Last(self) -> StepAP203_StartRequestItem: ...
    def Value(self, theIndex: int) -> StepAP203_StartRequestItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_StartRequestItem) -> None: ...

class StepAP203_Array1OfWorkItem:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepAP203_WorkItem: ...
    def __setitem__(self, index: int, value: StepAP203_WorkItem) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepAP203_WorkItem]: ...
    def next(self) -> StepAP203_WorkItem: ...
    __next__ = next
    def Init(self, theValue: StepAP203_WorkItem) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepAP203_WorkItem: ...
    def Last(self) -> StepAP203_WorkItem: ...
    def Value(self, theIndex: int) -> StepAP203_WorkItem: ...
    def SetValue(self, theIndex: int, theValue: StepAP203_WorkItem) -> None: ...

class StepAP203_ApprovedItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def Certification(self) -> StepBasic_Certification: ...
    def Change(self) -> StepAP203_Change: ...
    def ChangeRequest(self) -> StepAP203_ChangeRequest: ...
    def ConfigurationEffectivity(self) -> StepRepr_ConfigurationEffectivity: ...
    def ConfigurationItem(self) -> StepRepr_ConfigurationItem: ...
    def Contract(self) -> StepBasic_Contract: ...
    def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
    def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
    def StartRequest(self) -> StepAP203_StartRequest: ...
    def StartWork(self) -> StepAP203_StartWork: ...

class StepAP203_CcDesignApproval(StepBasic_ApprovalAssignment):
    def __init__(self) -> None: ...
    def Init(self, aApprovalAssignment_AssignedApproval: StepBasic_Approval, aItems: StepAP203_HArray1OfApprovedItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfApprovedItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfApprovedItem) -> None: ...

class StepAP203_CcDesignCertification(StepBasic_CertificationAssignment):
    def __init__(self) -> None: ...
    def Init(self, aCertificationAssignment_AssignedCertification: StepBasic_Certification, aItems: StepAP203_HArray1OfCertifiedItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfCertifiedItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfCertifiedItem) -> None: ...

class StepAP203_CcDesignContract(StepBasic_ContractAssignment):
    def __init__(self) -> None: ...
    def Init(self, aContractAssignment_AssignedContract: StepBasic_Contract, aItems: StepAP203_HArray1OfContractedItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfContractedItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfContractedItem) -> None: ...

class StepAP203_CcDesignDateAndTimeAssignment(StepBasic_DateAndTimeAssignment):
    def __init__(self) -> None: ...
    def Init(self, aDateAndTimeAssignment_AssignedDateAndTime: StepBasic_DateAndTime, aDateAndTimeAssignment_Role: StepBasic_DateTimeRole, aItems: StepAP203_HArray1OfDateTimeItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfDateTimeItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfDateTimeItem) -> None: ...

class StepAP203_CcDesignPersonAndOrganizationAssignment(StepBasic_PersonAndOrganizationAssignment):
    def __init__(self) -> None: ...
    def Init(self, aPersonAndOrganizationAssignment_AssignedPersonAndOrganization: StepBasic_PersonAndOrganization, aPersonAndOrganizationAssignment_Role: StepBasic_PersonAndOrganizationRole, aItems: StepAP203_HArray1OfPersonOrganizationItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfPersonOrganizationItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfPersonOrganizationItem) -> None: ...

class StepAP203_CcDesignSecurityClassification(StepBasic_SecurityClassificationAssignment):
    def __init__(self) -> None: ...
    def Init(self, aSecurityClassificationAssignment_AssignedSecurityClassification: StepBasic_SecurityClassification, aItems: StepAP203_HArray1OfClassifiedItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfClassifiedItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfClassifiedItem) -> None: ...

class StepAP203_CcDesignSpecificationReference(StepBasic_DocumentReference):
    def __init__(self) -> None: ...
    def Init(self, aDocumentReference_AssignedDocument: StepBasic_Document, aDocumentReference_Source: TCollection_HAsciiString, aItems: StepAP203_HArray1OfSpecifiedItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfSpecifiedItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfSpecifiedItem) -> None: ...

class StepAP203_CertifiedItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def SuppliedPartRelationship(self) -> StepRepr_SuppliedPartRelationship: ...

class StepAP203_Change(StepBasic_ActionAssignment):
    def __init__(self) -> None: ...
    def Init(self, aActionAssignment_AssignedAction: StepBasic_Action, aItems: StepAP203_HArray1OfWorkItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfWorkItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfWorkItem) -> None: ...

class StepAP203_ChangeRequest(StepBasic_ActionRequestAssignment):
    def __init__(self) -> None: ...
    def Init(self, aActionRequestAssignment_AssignedActionRequest: StepBasic_VersionedActionRequest, aItems: StepAP203_HArray1OfChangeRequestItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfChangeRequestItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfChangeRequestItem) -> None: ...

class StepAP203_ChangeRequestItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_ClassifiedItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def AssemblyComponentUsage(self) -> StepRepr_AssemblyComponentUsage: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_ContractedItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_DateTimeItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def ApprovalPersonOrganization(self) -> StepBasic_ApprovalPersonOrganization: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def Certification(self) -> StepBasic_Certification: ...
    def Change(self) -> StepAP203_Change: ...
    def ChangeRequest(self) -> StepAP203_ChangeRequest: ...
    def Contract(self) -> StepBasic_Contract: ...
    def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
    def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
    def StartRequest(self) -> StepAP203_StartRequest: ...
    def StartWork(self) -> StepAP203_StartWork: ...

class StepAP203_PersonOrganizationItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def Change(self) -> StepAP203_Change: ...
    def ChangeRequest(self) -> StepAP203_ChangeRequest: ...
    def ConfigurationItem(self) -> StepRepr_ConfigurationItem: ...
    def Contract(self) -> StepBasic_Contract: ...
    def Product(self) -> StepBasic_Product: ...
    def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...
    def SecurityClassification(self) -> StepBasic_SecurityClassification: ...
    def StartRequest(self) -> StepAP203_StartRequest: ...
    def StartWork(self) -> StepAP203_StartWork: ...

class StepAP203_SpecifiedItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def ProductDefinition(self) -> StepBasic_ProductDefinition: ...
    def ShapeAspect(self) -> StepRepr_ShapeAspect: ...

class StepAP203_StartRequest(StepBasic_ActionRequestAssignment):
    def __init__(self) -> None: ...
    def Init(self, aActionRequestAssignment_AssignedActionRequest: StepBasic_VersionedActionRequest, aItems: StepAP203_HArray1OfStartRequestItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfStartRequestItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfStartRequestItem) -> None: ...

class StepAP203_StartRequestItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

class StepAP203_StartWork(StepBasic_ActionAssignment):
    def __init__(self) -> None: ...
    def Init(self, aActionAssignment_AssignedAction: StepBasic_Action, aItems: StepAP203_HArray1OfWorkItem) -> None: ...
    def Items(self) -> StepAP203_HArray1OfWorkItem: ...
    def SetItems(self, Items: StepAP203_HArray1OfWorkItem) -> None: ...

class StepAP203_WorkItem(StepData_SelectType):
    def __init__(self) -> None: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def ProductDefinitionFormation(self) -> StepBasic_ProductDefinitionFormation: ...

# harray1 classes

class StepAP203_HArray1OfClassifiedItem(StepAP203_Array1OfClassifiedItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfClassifiedItem: ...


class StepAP203_HArray1OfWorkItem(StepAP203_Array1OfWorkItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfWorkItem: ...


class StepAP203_HArray1OfSpecifiedItem(StepAP203_Array1OfSpecifiedItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfSpecifiedItem: ...


class StepAP203_HArray1OfStartRequestItem(StepAP203_Array1OfStartRequestItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfStartRequestItem: ...


class StepAP203_HArray1OfChangeRequestItem(StepAP203_Array1OfChangeRequestItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfChangeRequestItem: ...


class StepAP203_HArray1OfPersonOrganizationItem(StepAP203_Array1OfPersonOrganizationItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfPersonOrganizationItem: ...


class StepAP203_HArray1OfDateTimeItem(StepAP203_Array1OfDateTimeItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfDateTimeItem: ...


class StepAP203_HArray1OfApprovedItem(StepAP203_Array1OfApprovedItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfApprovedItem: ...


class StepAP203_HArray1OfContractedItem(StepAP203_Array1OfContractedItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfContractedItem: ...


class StepAP203_HArray1OfCertifiedItem(StepAP203_Array1OfCertifiedItem, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepAP203_Array1OfCertifiedItem: ...

# harray2 classes
# hsequence classes

