# Auto generated from uco_master.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-06-25T09:25:23
# Schema: uco-master
#
# id: https://w3id.org/lmodel/uco-master
# description: Unified Cyber Ontology
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AFC = CurieNamespace('AFC', 'http://purl.allotrope.org/ontologies/common#AFC_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
EFO = CurieNamespace('EFO', 'http://identifiers.org/efo/')
ERO = CurieNamespace('ERO', 'http://purl.obolibrary.org/obo/ERO_')
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
INO = CurieNamespace('INO', 'http://purl.obolibrary.org/obo/INO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OM = CurieNamespace('OM', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
SAN = CurieNamespace('SAN', 'https://www.irit.fr/recherches/MELODI/ontologies/SAN.html#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
SWO = CurieNamespace('SWO', 'http://purl.obolibrary.org/obo/SWO_')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
ACTION = CurieNamespace('action', 'https://w3id.org/lmodel/uco-action/')
ANALYSIS = CurieNamespace('analysis', 'https://w3id.org/lmodel/uco-analysis/')
CO = CurieNamespace('co', 'http://purl.org/co/')
COLLECTIONS = CurieNamespace('collections', 'https://w3id.org/lmodel/collections/')
CONFIGURATION = CurieNamespace('configuration', 'https://w3id.org/lmodel/uco-configuration/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/uco-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DWC = CurieNamespace('dwc', 'https://dwc.tdwg.org/terms/#dc:')
EDAM_DATA = CurieNamespace('edam_data', 'http://edamontology.org/data_')
EDAM_FORMAT = CurieNamespace('edam_format', 'http://edamontology.org/format_')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
IDENTITY = CurieNamespace('identity', 'https://w3id.org/lmodel/uco-identity/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
LOCATION = CurieNamespace('location', 'https://w3id.org/lmodel/uco-location/')
MARKING = CurieNamespace('marking', 'https://w3id.org/lmodel/uco-marking/')
MASTER = CurieNamespace('master', 'https://w3id.org/lmodel/uco-master/')
METASAT = CurieNamespace('metasat', 'https://schema.space/metasat/')
OBSERVABLE = CurieNamespace('observable', 'https://w3id.org/lmodel/uco-observable/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PATTERN = CurieNamespace('pattern', 'https://w3id.org/lmodel/uco-pattern/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
ROLE = CurieNamespace('role', 'https://w3id.org/lmodel/uco-role/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_COLLECTIONS = CurieNamespace('schema_collections', 'https://w3id.org/lmodel/collections/schema/')
SCHEMA_UCO_ACTION = CurieNamespace('schema_uco_action', 'https://w3id.org/lmodel/uco-action/schema/')
SCHEMA_UCO_ANALYSIS = CurieNamespace('schema_uco_analysis', 'https://w3id.org/lmodel/uco-analysis/schema/')
SCHEMA_UCO_CONFIGURATION = CurieNamespace('schema_uco_configuration', 'https://w3id.org/lmodel/uco-configuration/schema/')
SCHEMA_UCO_CORE = CurieNamespace('schema_uco_core', 'https://w3id.org/lmodel/uco-core/schema/')
SCHEMA_UCO_IDENTITY = CurieNamespace('schema_uco_identity', 'https://w3id.org/lmodel/uco-identity/schema/')
SCHEMA_UCO_LOCATION = CurieNamespace('schema_uco_location', 'https://w3id.org/lmodel/uco-location/schema/')
SCHEMA_UCO_MARKING = CurieNamespace('schema_uco_marking', 'https://w3id.org/lmodel/uco-marking/schema/')
SCHEMA_UCO_OBSERVABLE = CurieNamespace('schema_uco_observable', 'https://w3id.org/lmodel/uco-observable/schema/')
SCHEMA_UCO_PATTERN = CurieNamespace('schema_uco_pattern', 'https://w3id.org/lmodel/uco-pattern/schema/')
SCHEMA_UCO_ROLE = CurieNamespace('schema_uco_role', 'https://w3id.org/lmodel/uco-role/schema/')
SCHEMA_UCO_TIME = CurieNamespace('schema_uco_time', 'https://w3id.org/lmodel/uco-time/schema/')
SCHEMA_UCO_TOOL = CurieNamespace('schema_uco_tool', 'https://w3id.org/lmodel/uco-tool/schema/')
SCHEMA_UCO_TYPES = CurieNamespace('schema_uco_types', 'https://w3id.org/lmodel/uco-types/schema/')
SCHEMA_UCO_VICTIM = CurieNamespace('schema_uco_victim', 'https://w3id.org/lmodel/uco-victim/schema/')
SCHEMA_UCO_VOCABULARY = CurieNamespace('schema_uco_vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
TIME = CurieNamespace('time', 'https://w3id.org/lmodel/uco-time/')
TOOL = CurieNamespace('tool', 'https://w3id.org/lmodel/uco-tool/')
TYPES = CurieNamespace('types', 'https://w3id.org/lmodel/uco-types/')
VICTIM = CurieNamespace('victim', 'https://w3id.org/lmodel/uco-victim/')
VOCABULARY = CurieNamespace('vocabulary', 'https://w3id.org/lmodel/uco-vocabulary/')
WIKIDATA = CurieNamespace('wIKIDATA', 'http://identifiers.org/wikidata/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
WIKIDATA_PROPERTY = CurieNamespace('wikidata_property', 'https://www.wikidata.org/wiki/Property:')
WIKIDATA_PROPERTY = CurieNamespace('wikidata_PROPERTY', 'https://www.wikidata.org/wiki/Property:')
WIKIDATA_PROPERTY = CurieNamespace('wikidata_property', 'https://www.wikidata.org/wiki/Property:')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MASTER


# Types
class StringType(String):
    """ A string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string type"
    type_model_uri = MASTER.StringType


class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates. """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = MASTER.LiteralType


class NonNegativeIntegerType(Integer):
    """ real number strictly greater than zero """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non negative integer type"
    type_model_uri = MASTER.NonNegativeIntegerType


class StatementType(StringType):
    """ "meaningful declarative sentence that is either true or false, or that which a true or false declarative sentence asserts" """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "statement type"
    type_model_uri = MASTER.StatementType


class IriType(Uriorcurie):
    """ A IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = MASTER.IriType


class BooleanType(Boolean):
    """ A boolean value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean type"
    type_model_uri = MASTER.BooleanType


class HexBinaryType(hex):
    """ "Represents arbitrary hex-encoded binary data" """
    type_class_uri = XSD.hexBinary
    type_class_curie = "xsd:hexBinary"
    type_name = "hex binary type"
    type_model_uri = MASTER.HexBinaryType


class DecimalType(Decimal):
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal type"
    type_model_uri = MASTER.DecimalType


class Base64BinaryType(String):
    type_class_uri = XSD.base64Binary
    type_class_curie = "xsd:base64Binary"
    type_name = "base64 binary type"
    type_model_uri = MASTER.Base64BinaryType


class ByteType(Integer):
    """ unit of digital information equal to 8 bits """
    type_class_uri = XSD.byte
    type_class_curie = "xsd:byte"
    type_name = "byte type"
    type_model_uri = MASTER.ByteType


class PositiveIntegerType(Integer):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD.positiveInteger
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer type"
    type_model_uri = MASTER.PositiveIntegerType


class UnsignedIntegerType(Integer):
    """ integer data type which represents non-negative numbers """
    type_class_uri = XSD.unsignedInt
    type_class_curie = "xsd:unsignedInt"
    type_name = "unsigned integer type"
    type_model_uri = MASTER.UnsignedIntegerType


class UnsignedShortType(Integer):
    """ data type for positive integers that can be represented with 16 bits """
    type_class_uri = XSD.unsignedShort
    type_class_curie = "xsd:unsignedShort"
    type_name = "unsigned short type"
    type_model_uri = MASTER.UnsignedShortType


class DurationType(Integer):
    type_class_uri = XSD.duration
    type_class_curie = "xsd:duration"
    type_name = "duration type"
    type_model_uri = MASTER.DurationType


class PositiveInteger(Integer):
    """ integer greater than zero; natural number explicitly excluding zero """
    type_class_uri = XSD.positiveInteger
    type_class_curie = "xsd:positiveInteger"
    type_name = "positive integer"
    type_model_uri = MASTER.PositiveInteger


# Class references



class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class within UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoThing
    class_class_curie: ClassVar[str] = "core:UcoThing"
    class_name: ClassVar[str] = "UcoThing"
    class_model_uri: ClassVar[URIRef] = MASTER.UcoThing


class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoInherentCharacterizationThing
    class_class_curie: ClassVar[str] = "core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "UcoInherentCharacterizationThing"
    class_model_uri: ClassVar[URIRef] = MASTER.UcoInherentCharacterizationThing


@dataclass
class ArrayOfAction(UcoInherentCharacterizationThing):
    """
    "An array of action is an ordered list of references to things that may be done or performed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ArrayOfAction
    class_class_curie: ClassVar[str] = "action:ArrayOfAction"
    class_name: ClassVar[str] = "ArrayOfAction"
    class_model_uri: ClassVar[URIRef] = MASTER.ArrayOfAction

    action: Optional[Union[dict, Action]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.action is not None and not isinstance(self.action, Action):
            self.action = Action(**as_dict(self.action))

        super().__post_init__(**kwargs)


@dataclass
class ArtifactClassification(UcoInherentCharacterizationThing):
    """
    "An artifact classification is a single specific assertion that a particular class of a classification taxonomy
    applies to something."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.ArtifactClassification
    class_class_curie: ClassVar[str] = "analysis:ArtifactClassification"
    class_name: ClassVar[str] = "ArtifactClassification"
    class_model_uri: ClassVar[URIRef] = MASTER.ArtifactClassification

    classificationConfidence: Optional[Union[Decimal, DecimalType]] = None
    class: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.classificationConfidence is not None and not isinstance(self.classificationConfidence, DecimalType):
            self.classificationConfidence = DecimalType(self.classificationConfidence)

        if self.class is not None and not isinstance(self.class, str):
            self.class = str(self.class)

        super().__post_init__(**kwargs)


@dataclass
class ConfigurationEntry(UcoInherentCharacterizationThing):
    """
    A configuration entry is a grouping of characteristics unique to a particular parameter or initial setting for the
    use of a tool, application, software, or other cyber object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIGURATION.ConfigurationEntry
    class_class_curie: ClassVar[str] = "configuration:ConfigurationEntry"
    class_name: ClassVar[str] = "ConfigurationEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.ConfigurationEntry

    itemObject: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    itemDescription: Optional[str] = None
    itemName: Optional[str] = None
    itemType: Optional[str] = None
    itemValue: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.itemObject, list):
            self.itemObject = [self.itemObject] if self.itemObject is not None else []
        self.itemObject = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.itemObject]

        if self.itemDescription is not None and not isinstance(self.itemDescription, str):
            self.itemDescription = str(self.itemDescription)

        if self.itemName is not None and not isinstance(self.itemName, str):
            self.itemName = str(self.itemName)

        if self.itemType is not None and not isinstance(self.itemType, str):
            self.itemType = str(self.itemType)

        if not isinstance(self.itemValue, list):
            self.itemValue = [self.itemValue] if self.itemValue is not None else []
        self.itemValue = [v if isinstance(v, str) else str(v) for v in self.itemValue]

        super().__post_init__(**kwargs)


@dataclass
class Dependency(UcoInherentCharacterizationThing):
    """
    A dependency is a grouping of characteristics unique to something that a tool or other software relies on to
    function as intended.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIGURATION.Dependency
    class_class_curie: ClassVar[str] = "configuration:Dependency"
    class_name: ClassVar[str] = "Dependency"
    class_model_uri: ClassVar[URIRef] = MASTER.Dependency

    dependencyDescription: Optional[str] = None
    dependencyType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dependencyDescription is not None and not isinstance(self.dependencyDescription, str):
            self.dependencyDescription = str(self.dependencyDescription)

        if self.dependencyType is not None and not isinstance(self.dependencyType, str):
            self.dependencyType = str(self.dependencyType)

        super().__post_init__(**kwargs)


@dataclass
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExternalReference
    class_class_curie: ClassVar[str] = "core:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = MASTER.ExternalReference

    referenceURL: Optional[Union[str, IriType]] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.referenceURL is not None and not isinstance(self.referenceURL, IriType):
            self.referenceURL = IriType(self.referenceURL)

        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        super().__post_init__(**kwargs)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Facet
    class_class_curie: ClassVar[str] = "core:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = MASTER.Facet


@dataclass
class ActionArgumentFacet(Facet):
    """
    "An action argument facet is a grouping of characteristics unique to a single parameter of an action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionArgumentFacet
    class_class_curie: ClassVar[str] = "action:ActionArgumentFacet"
    class_name: ClassVar[str] = "ActionArgumentFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ActionArgumentFacet

    argumentName: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.argumentName):
            self.MissingRequiredField("argumentName")
        if not isinstance(self.argumentName, str):
            self.argumentName = str(self.argumentName)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class ActionEstimationFacet(Facet):
    """
    "An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for
    an action that may potentially be performed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionEstimationFacet
    class_class_curie: ClassVar[str] = "action:ActionEstimationFacet"
    class_name: ClassVar[str] = "ActionEstimationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ActionEstimationFacet

    estimatedCost: Optional[str] = None
    estimatedEfficacy: Optional[str] = None
    estimatedImpact: Optional[str] = None
    objective: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.estimatedCost is not None and not isinstance(self.estimatedCost, str):
            self.estimatedCost = str(self.estimatedCost)

        if self.estimatedEfficacy is not None and not isinstance(self.estimatedEfficacy, str):
            self.estimatedEfficacy = str(self.estimatedEfficacy)

        if self.estimatedImpact is not None and not isinstance(self.estimatedImpact, str):
            self.estimatedImpact = str(self.estimatedImpact)

        if self.objective is not None and not isinstance(self.objective, str):
            self.objective = str(self.objective)

        super().__post_init__(**kwargs)


@dataclass
class ActionFrequencyFacet(Facet):
    """
    "An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionFrequencyFacet
    class_class_curie: ClassVar[str] = "action:ActionFrequencyFacet"
    class_name: ClassVar[str] = "ActionFrequencyFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ActionFrequencyFacet

    rate: Union[Decimal, DecimalType] = None
    scale: str = None
    units: str = None
    trend: Union[str, "TrendEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.rate):
            self.MissingRequiredField("rate")
        if not isinstance(self.rate, DecimalType):
            self.rate = DecimalType(self.rate)

        if self._is_empty(self.scale):
            self.MissingRequiredField("scale")
        if not isinstance(self.scale, str):
            self.scale = str(self.scale)

        if self._is_empty(self.units):
            self.MissingRequiredField("units")
        if not isinstance(self.units, str):
            self.units = str(self.units)

        if self._is_empty(self.trend):
            self.MissingRequiredField("trend")
        if not isinstance(self.trend, TrendEnum):
            self.trend = TrendEnum(self.trend)

        super().__post_init__(**kwargs)


class AnalyticResultFacet(Facet):
    """
    "An analytic result facet is a grouping of characteristics unique to the results of an analysis action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.AnalyticResultFacet
    class_class_curie: ClassVar[str] = "analysis:AnalyticResultFacet"
    class_name: ClassVar[str] = "AnalyticResultFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AnalyticResultFacet


@dataclass
class ArtifactClassificationResultFacet(AnalyticResultFacet):
    """
    "An artifact classification result facet is a grouping of characteristics unique to the results of an artifact
    classification analysis action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.ArtifactClassificationResultFacet
    class_class_curie: ClassVar[str] = "analysis:ArtifactClassificationResultFacet"
    class_name: ClassVar[str] = "ArtifactClassificationResultFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ArtifactClassificationResultFacet

    classification: Optional[Union[Union[dict, ArtifactClassification], List[Union[dict, ArtifactClassification]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.classification, list):
            self.classification = [self.classification] if self.classification is not None else []
        self.classification = [v if isinstance(v, ArtifactClassification) else ArtifactClassification(**as_dict(v)) for v in self.classification]

        super().__post_init__(**kwargs)


@dataclass
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ConfidenceFacet
    class_class_curie: ClassVar[str] = "core:ConfidenceFacet"
    class_name: ClassVar[str] = "ConfidenceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ConfidenceFacet

    confidence: Union[int, NonNegativeIntegerType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, NonNegativeIntegerType):
            self.confidence = NonNegativeIntegerType(self.confidence)

        super().__post_init__(**kwargs)


@dataclass
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoObject
    class_class_curie: ClassVar[str] = "core:UcoObject"
    class_name: ClassVar[str] = "UcoObject"
    class_model_uri: ClassVar[URIRef] = MASTER.UcoObject

    createdBy: Optional[str] = None
    description: Optional[Union[str, List[str]]] = empty_list()
    externalReference: Optional[Union[str, List[str]]] = empty_list()
    hasFacet: Optional[Union[str, List[str]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectMarking: Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]] = empty_list()
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.createdBy is not None and not isinstance(self.createdBy, str):
            self.createdBy = str(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, str) else str(v) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, str) else str(v) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstraction) else MarkingDefinitionAbstraction(**as_dict(v)) for v in self.objectMarking]

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Action(UcoObject):
    """
    "An action is something that may be done or performed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.Action
    class_class_curie: ClassVar[str] = "action:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = MASTER.Action

    subaction: Optional[Union[Union[dict, "Action"], List[Union[dict, "Action"]]]] = empty_list()
    environment: Optional[Union[dict, "UcoObject"]] = None
    performer: Optional[Union[dict, "UcoObject"]] = None
    error: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    instrument: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    participant: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    result: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()
    location: Optional[Union[Union[dict, "Location"], List[Union[dict, "Location"]]]] = empty_list()
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    actionCount: Optional[Union[int, NonNegativeIntegerType]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.subaction, list):
            self.subaction = [self.subaction] if self.subaction is not None else []
        self.subaction = [v if isinstance(v, Action) else Action(**as_dict(v)) for v in self.subaction]

        if self.environment is not None and not isinstance(self.environment, UcoObject):
            self.environment = UcoObject(**as_dict(self.environment))

        if self.performer is not None and not isinstance(self.performer, UcoObject):
            self.performer = UcoObject(**as_dict(self.performer))

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.error]

        if not isinstance(self.instrument, list):
            self.instrument = [self.instrument] if self.instrument is not None else []
        self.instrument = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.instrument]

        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        if not isinstance(self.participant, list):
            self.participant = [self.participant] if self.participant is not None else []
        self.participant = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.participant]

        if not isinstance(self.result, list):
            self.result = [self.result] if self.result is not None else []
        self.result = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.result]

        if not isinstance(self.location, list):
            self.location = [self.location] if self.location is not None else []
        self.location = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.location]

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.actionCount is not None and not isinstance(self.actionCount, NonNegativeIntegerType):
            self.actionCount = NonNegativeIntegerType(self.actionCount)

        if self.actionStatus is not None and not isinstance(self.actionStatus, ActionStatusTypeEnum):
            self.actionStatus = ActionStatusTypeEnum(self.actionStatus)

        super().__post_init__(**kwargs)


@dataclass
class ActionLifecycle(Action):
    """
    "An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action
    lifecycles."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionLifecycle
    class_class_curie: ClassVar[str] = "action:ActionLifecycle"
    class_name: ClassVar[str] = "ActionLifecycle"
    class_model_uri: ClassVar[URIRef] = MASTER.ActionLifecycle

    phase: Union[dict, "ArrayOfAction"] = None
    error: Optional[Union[dict, "UcoObject"]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    actionCount: Optional[Union[int, NonNegativeIntegerType]] = None
    actionStatus: Optional[Union[str, "ActionStatusTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.phase):
            self.MissingRequiredField("phase")
        if not isinstance(self.phase, ArrayOfAction):
            self.phase = ArrayOfAction(**as_dict(self.phase))

        if self.error is not None and not isinstance(self.error, UcoObject):
            self.error = UcoObject(**as_dict(self.error))

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.actionCount is not None and not isinstance(self.actionCount, NonNegativeIntegerType):
            self.actionCount = NonNegativeIntegerType(self.actionCount)

        if not isinstance(self.error, list):
            self.error = [self.error] if self.error is not None else []
        self.error = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.error]

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.actionStatus is not None and not isinstance(self.actionStatus, ActionStatusTypeEnum):
            self.actionStatus = ActionStatusTypeEnum(self.actionStatus)

        super().__post_init__(**kwargs)


class ActionPattern(Action):
    """
    "An action pattern is a grouping of characteristics unique to a combination of actions forming a consistent or
    characteristic arrangement."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ACTION.ActionPattern
    class_class_curie: ClassVar[str] = "action:ActionPattern"
    class_name: ClassVar[str] = "ActionPattern"
    class_model_uri: ClassVar[URIRef] = MASTER.ActionPattern


class Analysis(Action):
    """
    "An analysis is an action of detailed examination of something in order to understand its nature, context or
    essential features."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.Analysis
    class_class_curie: ClassVar[str] = "analysis:Analysis"
    class_name: ClassVar[str] = "Analysis"
    class_model_uri: ClassVar[URIRef] = MASTER.Analysis


@dataclass
class Configuration(UcoObject):
    """
    A configuration is a grouping of characteristics unique to a set of parameters or initial settings for the use of
    a tool, application, software, or other cyber object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONFIGURATION.Configuration
    class_class_curie: ClassVar[str] = "configuration:Configuration"
    class_name: ClassVar[str] = "Configuration"
    class_model_uri: ClassVar[URIRef] = MASTER.Configuration

    configurationEntry: Optional[Union[Union[dict, "ConfigurationEntry"], List[Union[dict, "ConfigurationEntry"]]]] = empty_list()
    dependencies: Optional[Union[Union[dict, "Dependency"], List[Union[dict, "Dependency"]]]] = empty_list()
    usageContextAssumptions: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.configurationEntry, list):
            self.configurationEntry = [self.configurationEntry] if self.configurationEntry is not None else []
        self.configurationEntry = [v if isinstance(v, ConfigurationEntry) else ConfigurationEntry(**as_dict(v)) for v in self.configurationEntry]

        if not isinstance(self.dependencies, list):
            self.dependencies = [self.dependencies] if self.dependencies is not None else []
        self.dependencies = [v if isinstance(v, Dependency) else Dependency(**as_dict(v)) for v in self.dependencies]

        if not isinstance(self.usageContextAssumptions, list):
            self.usageContextAssumptions = [self.usageContextAssumptions] if self.usageContextAssumptions is not None else []
        self.usageContextAssumptions = [v if isinstance(v, str) else str(v) for v in self.usageContextAssumptions]

        super().__post_init__(**kwargs)


@dataclass
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Assertion
    class_class_curie: ClassVar[str] = "core:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = MASTER.Assertion

    statement: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, str) else str(v) for v in self.statement]

        super().__post_init__(**kwargs)


@dataclass
class AnalyticResult(Assertion):
    """
    "An analytic result is a characterization of the understanding resulting from an analysis action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANALYSIS.AnalyticResult
    class_class_curie: ClassVar[str] = "analysis:AnalyticResult"
    class_name: ClassVar[str] = "AnalyticResult"
    class_model_uri: ClassVar[URIRef] = MASTER.AnalyticResult

    originatingAnalysis: Optional[Union[dict, Analysis]] = None
    resultContent: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.originatingAnalysis is not None and not isinstance(self.originatingAnalysis, Analysis):
            self.originatingAnalysis = Analysis(**as_dict(self.originatingAnalysis))

        if not isinstance(self.resultContent, list):
            self.resultContent = [self.resultContent] if self.resultContent is not None else []
        self.resultContent = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.resultContent]

        super().__post_init__(**kwargs)


@dataclass
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Annotation
    class_class_curie: ClassVar[str] = "core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = MASTER.Annotation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AttributedName
    class_class_curie: ClassVar[str] = "core:AttributedName"
    class_name: ClassVar[str] = "AttributedName"
    class_model_uri: ClassVar[URIRef] = MASTER.AttributedName

    namingAuthority: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.namingAuthority is not None and not isinstance(self.namingAuthority, str):
            self.namingAuthority = str(self.namingAuthority)

        super().__post_init__(**kwargs)


class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Compilation
    class_class_curie: ClassVar[str] = "core:Compilation"
    class_name: ClassVar[str] = "Compilation"
    class_model_uri: ClassVar[URIRef] = MASTER.Compilation


@dataclass
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ContextualCompilation
    class_class_curie: ClassVar[str] = "core:ContextualCompilation"
    class_name: ClassVar[str] = "ContextualCompilation"
    class_model_uri: ClassVar[URIRef] = MASTER.ContextualCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ControlledVocabulary
    class_class_curie: ClassVar[str] = "core:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = MASTER.ControlledVocabulary

    value: str = None
    constrainingVocabularyReference: Optional[Union[str, IriType]] = None
    constrainingVocabularyName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, IriType):
            self.constrainingVocabularyReference = IriType(self.constrainingVocabularyReference)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        super().__post_init__(**kwargs)


@dataclass
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.EnclosingCompilation
    class_class_curie: ClassVar[str] = "core:EnclosingCompilation"
    class_name: ClassVar[str] = "EnclosingCompilation"
    class_model_uri: ClassVar[URIRef] = MASTER.EnclosingCompilation

    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Bundle
    class_class_curie: ClassVar[str] = "core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = MASTER.Bundle


@dataclass
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Grouping
    class_class_curie: ClassVar[str] = "core:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = MASTER.Grouping

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    context: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)


class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.IdentityAbstraction
    class_class_curie: ClassVar[str] = "core:IdentityAbstraction"
    class_name: ClassVar[str] = "IdentityAbstraction"
    class_model_uri: ClassVar[URIRef] = MASTER.IdentityAbstraction


class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Item
    class_class_curie: ClassVar[str] = "core:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = MASTER.Item


class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking MarkingDefinition class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.MarkingDefinitionAbstraction
    class_class_curie: ClassVar[str] = "core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "MarkingDefinitionAbstraction"
    class_model_uri: ClassVar[URIRef] = MASTER.MarkingDefinitionAbstraction


class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ModusOperandi
    class_class_curie: ClassVar[str] = "core:ModusOperandi"
    class_name: ClassVar[str] = "ModusOperandi"
    class_model_uri: ClassVar[URIRef] = MASTER.ModusOperandi


@dataclass
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Relationship
    class_class_curie: ClassVar[str] = "core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = MASTER.Relationship

    isDirectional: Union[bool, BooleanType] = None
    source: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    target: Union[dict, "UcoObject"] = None
    endTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, BooleanType):
            self.isDirectional = BooleanType(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObject):
            self.target = UcoObject(**as_dict(self.target))

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)


class Identity(IdentityAbstraction):
    """
    An identity is a grouping of identifying characteristics unique to an individual or organization.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.Identity
    class_class_curie: ClassVar[str] = "identity:Identity"
    class_name: ClassVar[str] = "Identity"
    class_model_uri: ClassVar[URIRef] = MASTER.Identity


class IdentityFacet(Facet):
    """
    An IdentityFacet is a grouping of characteristics unique to a particular aspect of an identity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.IdentityFacet
    class_class_curie: ClassVar[str] = "identity:IdentityFacet"
    class_name: ClassVar[str] = "IdentityFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.IdentityFacet


@dataclass
class AddressFacet(IdentityFacet):
    """
    An Address Facet is a grouping of characteristics unique to an administrative identifier for a geolocation
    associated with a specific identity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.AddressFacet
    class_class_curie: ClassVar[str] = "identity:AddressFacet"
    class_name: ClassVar[str] = "AddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AddressFacet

    address: Optional[Union[dict, "Location"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.address is not None and not isinstance(self.address, Location):
            self.address = Location(**as_dict(self.address))

        super().__post_init__(**kwargs)


class AffiliationFacet(IdentityFacet):
    """
    An affiliation is a grouping of characteristics unique to the established affiliations of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.AffiliationFacet
    class_class_curie: ClassVar[str] = "identity:AffiliationFacet"
    class_name: ClassVar[str] = "AffiliationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AffiliationFacet


@dataclass
class BirthInformationFacet(IdentityFacet):
    """
    Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.BirthInformationFacet
    class_class_curie: ClassVar[str] = "identity:BirthInformationFacet"
    class_name: ClassVar[str] = "BirthInformationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.BirthInformationFacet

    birthdate: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.birthdate is not None and not isinstance(self.birthdate, XSDDateTime):
            self.birthdate = XSDDateTime(self.birthdate)

        super().__post_init__(**kwargs)


class CountryOfResidenceFacet(IdentityFacet):
    """
    Country of residence is a grouping of characteristics unique to information related to the country, or countries,
    where an entity resides.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.CountryOfResidenceFacet
    class_class_curie: ClassVar[str] = "identity:CountryOfResidenceFacet"
    class_name: ClassVar[str] = "CountryOfResidenceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CountryOfResidenceFacet


class EventsFacet(IdentityFacet):
    """
    Events is a grouping of characteristics unique to information related to specific relevant things that happen in
    the lifetime of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.EventsFacet
    class_class_curie: ClassVar[str] = "identity:EventsFacet"
    class_name: ClassVar[str] = "EventsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EventsFacet


class IdentifierFacet(IdentityFacet):
    """
    Identifier is a grouping of characteristics unique to information that uniquely and specifically identities an
    entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.IdentifierFacet
    class_class_curie: ClassVar[str] = "identity:IdentifierFacet"
    class_name: ClassVar[str] = "IdentifierFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.IdentifierFacet


class LanguagesFacet(IdentityFacet):
    """
    Languages is a grouping of characteristics unique to specific syntactically and grammatically standardized forms
    of communication (human or computer) in which an entity has proficiency (comprehends, speaks, reads, or writes).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.LanguagesFacet
    class_class_curie: ClassVar[str] = "identity:LanguagesFacet"
    class_name: ClassVar[str] = "LanguagesFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.LanguagesFacet


class NationalityFacet(IdentityFacet):
    """
    Nationality is a grouping of characteristics unique to the condition of an entity belonging to a particular nation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.NationalityFacet
    class_class_curie: ClassVar[str] = "identity:NationalityFacet"
    class_name: ClassVar[str] = "NationalityFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NationalityFacet


class OccupationFacet(IdentityFacet):
    """
    Occupation is a grouping of characteristics unique to the job or profession of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.OccupationFacet
    class_class_curie: ClassVar[str] = "identity:OccupationFacet"
    class_name: ClassVar[str] = "OccupationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.OccupationFacet


class Organization(Identity):
    """
    An organization is a grouping of identifying characteristics unique to a group of people who work together in an
    organized way for a shared purpose. [based on https://dictionary.cambridge.org/us/dictionary/english/organization]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.Organization
    class_class_curie: ClassVar[str] = "identity:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = MASTER.Organization


class OrganizationDetailsFacet(IdentityFacet):
    """
    Organization details is a grouping of characteristics unique to an identity representing an administrative and
    functional structure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.OrganizationDetailsFacet
    class_class_curie: ClassVar[str] = "identity:OrganizationDetailsFacet"
    class_name: ClassVar[str] = "OrganizationDetailsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.OrganizationDetailsFacet


class Person(Identity):
    """
    A person is a grouping of identifying characteristics unique to a human being regarded as an individual. [based on
    https://www.lexico.com/en/definition/person]
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.Person
    class_class_curie: ClassVar[str] = "identity:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MASTER.Person


class PersonalDetailsFacet(IdentityFacet):
    """
    Personal details is a grouping of characteristics unique to an identity representing an individual person.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.PersonalDetailsFacet
    class_class_curie: ClassVar[str] = "identity:PersonalDetailsFacet"
    class_name: ClassVar[str] = "PersonalDetailsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PersonalDetailsFacet


class PhysicalInfoFacet(IdentityFacet):
    """
    Physical info is a grouping of characteristics unique to the outwardly observable nature of an individual person.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.PhysicalInfoFacet
    class_class_curie: ClassVar[str] = "identity:PhysicalInfoFacet"
    class_name: ClassVar[str] = "PhysicalInfoFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PhysicalInfoFacet


class QualificationFacet(IdentityFacet):
    """
    Qualification is a grouping of characteristics unique to particular skills, capabilities or their related
    achievements (educational, professional, etc.) of an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.QualificationFacet
    class_class_curie: ClassVar[str] = "identity:QualificationFacet"
    class_name: ClassVar[str] = "QualificationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.QualificationFacet


class RelatedIdentityFacet(IdentityFacet):
    """
    <Needs fleshed out from CIQ>
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.RelatedIdentityFacet
    class_class_curie: ClassVar[str] = "identity:RelatedIdentityFacet"
    class_name: ClassVar[str] = "RelatedIdentityFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.RelatedIdentityFacet


@dataclass
class SimpleNameFacet(IdentityFacet):
    """
    A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held
    by an identity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.SimpleNameFacet
    class_class_curie: ClassVar[str] = "identity:SimpleNameFacet"
    class_name: ClassVar[str] = "SimpleNameFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SimpleNameFacet

    familyName: Optional[Union[str, List[str]]] = empty_list()
    givenName: Optional[Union[str, List[str]]] = empty_list()
    honorificPrefix: Optional[Union[str, List[str]]] = empty_list()
    honorificSuffix: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.familyName, list):
            self.familyName = [self.familyName] if self.familyName is not None else []
        self.familyName = [v if isinstance(v, str) else str(v) for v in self.familyName]

        if not isinstance(self.givenName, list):
            self.givenName = [self.givenName] if self.givenName is not None else []
        self.givenName = [v if isinstance(v, str) else str(v) for v in self.givenName]

        if not isinstance(self.honorificPrefix, list):
            self.honorificPrefix = [self.honorificPrefix] if self.honorificPrefix is not None else []
        self.honorificPrefix = [v if isinstance(v, str) else str(v) for v in self.honorificPrefix]

        if not isinstance(self.honorificSuffix, list):
            self.honorificSuffix = [self.honorificSuffix] if self.honorificSuffix is not None else []
        self.honorificSuffix = [v if isinstance(v, str) else str(v) for v in self.honorificSuffix]

        super().__post_init__(**kwargs)


class VisaFacet(IdentityFacet):
    """
    Visa is a grouping of characteristics unique to information related to a person's ability to enter, leave, or stay
    for a specified period of time in a country.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IDENTITY.VisaFacet
    class_class_curie: ClassVar[str] = "identity:VisaFacet"
    class_name: ClassVar[str] = "VisaFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.VisaFacet


@dataclass
class GPSCoordinatesFacet(Facet):
    """
    A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of
    precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such
    as the Global Positioning System (GPS).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.GPSCoordinatesFacet
    class_class_curie: ClassVar[str] = "location:GPSCoordinatesFacet"
    class_name: ClassVar[str] = "GPSCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.GPSCoordinatesFacet

    hdop: Optional[Union[Decimal, DecimalType]] = None
    pdop: Optional[Union[Decimal, DecimalType]] = None
    tdop: Optional[Union[Decimal, DecimalType]] = None
    vdop: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hdop is not None and not isinstance(self.hdop, DecimalType):
            self.hdop = DecimalType(self.hdop)

        if self.pdop is not None and not isinstance(self.pdop, DecimalType):
            self.pdop = DecimalType(self.pdop)

        if self.tdop is not None and not isinstance(self.tdop, DecimalType):
            self.tdop = DecimalType(self.tdop)

        if self.vdop is not None and not isinstance(self.vdop, DecimalType):
            self.vdop = DecimalType(self.vdop)

        super().__post_init__(**kwargs)


@dataclass
class LatLongCoordinatesFacet(Facet):
    """
    A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the
    intersection of specific latitude, longitude, and altitude values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.LatLongCoordinatesFacet
    class_class_curie: ClassVar[str] = "location:LatLongCoordinatesFacet"
    class_name: ClassVar[str] = "LatLongCoordinatesFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.LatLongCoordinatesFacet

    altitude: Optional[Union[Decimal, DecimalType]] = None
    latitude: Optional[Union[Decimal, DecimalType]] = None
    longitude: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.altitude is not None and not isinstance(self.altitude, DecimalType):
            self.altitude = DecimalType(self.altitude)

        if self.latitude is not None and not isinstance(self.latitude, DecimalType):
            self.latitude = DecimalType(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, DecimalType):
            self.longitude = DecimalType(self.longitude)

        super().__post_init__(**kwargs)


class Location(UcoObject):
    """
    A location is a geospatial place, site, or position.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.Location
    class_class_curie: ClassVar[str] = "location:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = MASTER.Location


@dataclass
class SimpleAddressFacet(Facet):
    """
    A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative
    address.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCATION.SimpleAddressFacet
    class_class_curie: ClassVar[str] = "location:SimpleAddressFacet"
    class_name: ClassVar[str] = "SimpleAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SimpleAddressFacet

    addressType: Optional[str] = None
    country: Optional[str] = None
    locality: Optional[str] = None
    postalCode: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.addressType is not None and not isinstance(self.addressType, str):
            self.addressType = str(self.addressType)

        if self.country is not None and not isinstance(self.country, str):
            self.country = str(self.country)

        if self.locality is not None and not isinstance(self.locality, str):
            self.locality = str(self.locality)

        if self.postalCode is not None and not isinstance(self.postalCode, str):
            self.postalCode = str(self.postalCode)

        if self.region is not None and not isinstance(self.region, str):
            self.region = str(self.region)

        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        super().__post_init__(**kwargs)


@dataclass
class GranularMarking(UcoInherentCharacterizationThing):
    """
    A granular marking is a grouping of characteristics unique to specification of MarkingDefinitions (restrictions,
    permissions, and other guidance for how data can be used and shared) that apply to particular portions of a
    particular UCO object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.GranularMarking
    class_class_curie: ClassVar[str] = "marking:GranularMarking"
    class_name: ClassVar[str] = "GranularMarking"
    class_model_uri: ClassVar[URIRef] = MASTER.GranularMarking

    marking: Optional[Union[str, List[str]]] = empty_list()
    contentSelectors: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.marking, list):
            self.marking = [self.marking] if self.marking is not None else []
        self.marking = [v if isinstance(v, str) else str(v) for v in self.marking]

        if not isinstance(self.contentSelectors, list):
            self.contentSelectors = [self.contentSelectors] if self.contentSelectors is not None else []
        self.contentSelectors = [v if isinstance(v, str) else str(v) for v in self.contentSelectors]

        super().__post_init__(**kwargs)


@dataclass
class MarkingDefinition(MarkingDefinitionAbstraction):
    """
    A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying
    restrictions, permissions, and other guidance for how marked data can be used and shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.MarkingDefinition
    class_class_curie: ClassVar[str] = "marking:MarkingDefinition"
    class_name: ClassVar[str] = "MarkingDefinition"
    class_model_uri: ClassVar[URIRef] = MASTER.MarkingDefinition

    definitionType: str = None
    definition: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.definitionType):
            self.MissingRequiredField("definitionType")
        if not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definition, list):
            self.definition = [self.definition] if self.definition is not None else []
        self.definition = [v if isinstance(v, str) else str(v) for v in self.definition]

        super().__post_init__(**kwargs)


class MarkingModel(UcoInherentCharacterizationThing):
    """
    A MarkingModel is a grouping of characteristics unique to the expression of a particular form of data
    MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.MarkingModel
    class_class_curie: ClassVar[str] = "marking:MarkingModel"
    class_name: ClassVar[str] = "MarkingModel"
    class_model_uri: ClassVar[URIRef] = MASTER.MarkingModel


@dataclass
class LicenseMarking(MarkingModel):
    """
    A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying
    restrictions, permissions, and other guidance for how marked data can be used and shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.LicenseMarking
    class_class_curie: ClassVar[str] = "marking:LicenseMarking"
    class_name: ClassVar[str] = "LicenseMarking"
    class_model_uri: ClassVar[URIRef] = MASTER.LicenseMarking

    license: str = None
    definitionType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, str):
            self.license = str(self.license)

        if self.definitionType is not None and not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class ReleaseToMarking(MarkingModel):
    """
    A release-to marking is a grouping of characteristics unique to the expression of data MarkingDefinitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of
    authorized persons and/or organizations to which to the associated content may be released. The existence of the
    Release-To marking restricts access to ONLY those identities explicitly listed, regardless of whether another data
    marking exists that allows sharing with other members of the community.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.ReleaseToMarking
    class_class_curie: ClassVar[str] = "marking:ReleaseToMarking"
    class_name: ClassVar[str] = "ReleaseToMarking"
    class_model_uri: ClassVar[URIRef] = MASTER.ReleaseToMarking

    authorizedIdentities: Union[str, List[str]] = None
    definitionType: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.authorizedIdentities):
            self.MissingRequiredField("authorizedIdentities")
        if not isinstance(self.authorizedIdentities, list):
            self.authorizedIdentities = [self.authorizedIdentities] if self.authorizedIdentities is not None else []
        self.authorizedIdentities = [v if isinstance(v, str) else str(v) for v in self.authorizedIdentities]

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class StatementMarking(MarkingModel):
    """
    A statement marking is a grouping of characteristics unique to the expression of data MarkingDefinitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual
    marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement
    markings are generally not machine-readable. An example of this would be a simple marking to apply copyright
    information, such as 'Copyright 2014 Acme Inc.'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.StatementMarking
    class_class_curie: ClassVar[str] = "marking:StatementMarking"
    class_name: ClassVar[str] = "StatementMarking"
    class_model_uri: ClassVar[URIRef] = MASTER.StatementMarking

    statement: str = None
    definitionType: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class TermsOfUseMarking(MarkingModel):
    """
    A terms of use marking is a grouping of characteristics unique to the expression of data MarkingDefinitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual
    statement specifying the Terms of Use (that is, the conditions under which the content may be shared, applied, or
    otherwise used) of the marked content. An example of this would be used to communicate a simple statement, such as
    'Acme Inc. is not responsible for the content of this file'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.TermsOfUseMarking
    class_class_curie: ClassVar[str] = "marking:TermsOfUseMarking"
    class_name: ClassVar[str] = "TermsOfUseMarking"
    class_model_uri: ClassVar[URIRef] = MASTER.TermsOfUseMarking

    termsOfUse: str = None
    definitionType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.termsOfUse):
            self.MissingRequiredField("termsOfUse")
        if not isinstance(self.termsOfUse, str):
            self.termsOfUse = str(self.termsOfUse)

        if self.definitionType is not None and not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class AccountAuthenticationFacet(Facet):
    """
    "An account authentication facet is a grouping of characteristics unique to the mechanism of accessing an account."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AccountAuthenticationFacet
    class_class_curie: ClassVar[str] = "observable:AccountAuthenticationFacet"
    class_name: ClassVar[str] = "AccountAuthenticationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AccountAuthenticationFacet

    passwordLastChanged: Optional[Union[str, XSDDateTime]] = None
    password: Optional[str] = None
    passwordType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.passwordLastChanged is not None and not isinstance(self.passwordLastChanged, XSDDateTime):
            self.passwordLastChanged = XSDDateTime(self.passwordLastChanged)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.passwordType is not None and not isinstance(self.passwordType, str):
            self.passwordType = str(self.passwordType)

        super().__post_init__(**kwargs)


@dataclass
class AccountFacet(Facet):
    """
    "An account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control
    the provision of some capability or service."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AccountFacet
    class_class_curie: ClassVar[str] = "observable:AccountFacet"
    class_name: ClassVar[str] = "AccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AccountFacet

    accountIssuer: Optional[Union[dict, UcoObject]] = None
    owner: Optional[Union[dict, UcoObject]] = None
    isActive: Optional[Union[bool, BooleanType]] = None
    expirationDate: Optional[Union[str, XSDDateTime]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    accountIdentifier: Optional[str] = None
    accountType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.accountIssuer is not None and not isinstance(self.accountIssuer, UcoObject):
            self.accountIssuer = UcoObject(**as_dict(self.accountIssuer))

        if self.owner is not None and not isinstance(self.owner, UcoObject):
            self.owner = UcoObject(**as_dict(self.owner))

        if self.isActive is not None and not isinstance(self.isActive, BooleanType):
            self.isActive = BooleanType(self.isActive)

        if self.expirationDate is not None and not isinstance(self.expirationDate, XSDDateTime):
            self.expirationDate = XSDDateTime(self.expirationDate)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.accountIdentifier is not None and not isinstance(self.accountIdentifier, str):
            self.accountIdentifier = str(self.accountIdentifier)

        if self.accountType is not None and not isinstance(self.accountType, str):
            self.accountType = str(self.accountType)

        super().__post_init__(**kwargs)


@dataclass
class AlternateDataStreamFacet(Facet):
    """
    "An alternate data stream facet is a grouping of characteristics unique to data content stored within an NTFS file
    that is independent of the standard content stream of the file and isHidden from access by default NTFS file
    viewing mechanisms."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AlternateDataStreamFacet
    class_class_curie: ClassVar[str] = "observable:AlternateDataStreamFacet"
    class_name: ClassVar[str] = "AlternateDataStreamFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AlternateDataStreamFacet

    hashes: Optional[Union[dict, "Hash"]] = None
    name: Optional[str] = None
    size: Optional[Union[int, PositiveInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hashes is not None and not isinstance(self.hashes, Hash):
            self.hashes = Hash(**as_dict(self.hashes))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.size is not None and not isinstance(self.size, PositiveInteger):
            self.size = PositiveInteger(self.size)

        super().__post_init__(**kwargs)


@dataclass
class AndroidDeviceFacet(Facet):
    """
    "An Android device facet is a grouping of characteristics unique to an Android device. [based on
    https://en.wikipedia.org/wiki/Android_(operating_system)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AndroidDeviceFacet
    class_class_curie: ClassVar[str] = "observable:AndroidDeviceFacet"
    class_name: ClassVar[str] = "AndroidDeviceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AndroidDeviceFacet

    androidFingerprint: Optional[str] = None
    androidVersion: Optional[str] = None
    androidID: Optional[hex] = None
    isADBRootEnabled: Optional[Union[bool, BooleanType]] = None
    isSURootEnabled: Optional[Union[bool, BooleanType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.androidFingerprint is not None and not isinstance(self.androidFingerprint, str):
            self.androidFingerprint = str(self.androidFingerprint)

        if self.androidVersion is not None and not isinstance(self.androidVersion, str):
            self.androidVersion = str(self.androidVersion)

        if self.androidID is not None and not isinstance(self.androidID, hex):
            self.androidID = hex(self.androidID)

        if self.isADBRootEnabled is not None and not isinstance(self.isADBRootEnabled, BooleanType):
            self.isADBRootEnabled = BooleanType(self.isADBRootEnabled)

        if self.isSURootEnabled is not None and not isinstance(self.isSURootEnabled, BooleanType):
            self.isSURootEnabled = BooleanType(self.isSURootEnabled)

        super().__post_init__(**kwargs)


@dataclass
class AntennaFacet(Facet):
    """
    "An antenna alignment facet contains the metadata surrounding the cell tower's antenna position."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AntennaFacet
    class_class_curie: ClassVar[str] = "observable:AntennaFacet"
    class_name: ClassVar[str] = "AntennaFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AntennaFacet

    antennaHeight: Optional[Union[Decimal, DecimalType]] = None
    azimuth: Optional[Union[Decimal, DecimalType]] = None
    elevation: Optional[Union[Decimal, DecimalType]] = None
    horizontalBeamWidth: Optional[Union[Decimal, DecimalType]] = None
    signalStrength: Optional[Union[Decimal, DecimalType]] = None
    skew: Optional[Union[Decimal, DecimalType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.antennaHeight is not None and not isinstance(self.antennaHeight, DecimalType):
            self.antennaHeight = DecimalType(self.antennaHeight)

        if self.azimuth is not None and not isinstance(self.azimuth, DecimalType):
            self.azimuth = DecimalType(self.azimuth)

        if self.elevation is not None and not isinstance(self.elevation, DecimalType):
            self.elevation = DecimalType(self.elevation)

        if self.horizontalBeamWidth is not None and not isinstance(self.horizontalBeamWidth, DecimalType):
            self.horizontalBeamWidth = DecimalType(self.horizontalBeamWidth)

        if self.signalStrength is not None and not isinstance(self.signalStrength, DecimalType):
            self.signalStrength = DecimalType(self.signalStrength)

        if self.skew is not None and not isinstance(self.skew, DecimalType):
            self.skew = DecimalType(self.skew)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationAccountFacet(Facet):
    """
    "An application account facet is a grouping of characteristics unique to an account within a particular software
    program designed for end users."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ApplicationAccountFacet
    class_class_curie: ClassVar[str] = "observable:ApplicationAccountFacet"
    class_name: ClassVar[str] = "ApplicationAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ApplicationAccountFacet

    application: Optional[Union[dict, "ObservableObject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        super().__post_init__(**kwargs)


@dataclass
class ApplicationFacet(Facet):
    """
    "An application facet is a grouping of characteristics unique to a particular software program designed for end
    users."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ApplicationFacet
    class_class_curie: ClassVar[str] = "observable:ApplicationFacet"
    class_name: ClassVar[str] = "ApplicationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ApplicationFacet

    numberOfLaunches: Optional[int] = None
    applicationIdentifier: Optional[str] = None
    installedVersionHistory: Optional[Union[Union[dict, "ApplicationVersion"], List[Union[dict, "ApplicationVersion"]]]] = empty_list()
    operatingSystem: Optional[Union[dict, "ObservableObject"]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.numberOfLaunches is not None and not isinstance(self.numberOfLaunches, int):
            self.numberOfLaunches = int(self.numberOfLaunches)

        if self.applicationIdentifier is not None and not isinstance(self.applicationIdentifier, str):
            self.applicationIdentifier = str(self.applicationIdentifier)

        if not isinstance(self.installedVersionHistory, list):
            self.installedVersionHistory = [self.installedVersionHistory] if self.installedVersionHistory is not None else []
        self.installedVersionHistory = [v if isinstance(v, ApplicationVersion) else ApplicationVersion(**as_dict(v)) for v in self.installedVersionHistory]

        if self.operatingSystem is not None and not isinstance(self.operatingSystem, ObservableObject):
            self.operatingSystem = ObservableObject(**as_dict(self.operatingSystem))

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class ApplicationVersion(UcoInherentCharacterizationThing):
    """
    "An application version is a grouping of characteristics unique to a particular software program version."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ApplicationVersion
    class_class_curie: ClassVar[str] = "observable:ApplicationVersion"
    class_name: ClassVar[str] = "ApplicationVersion"
    class_model_uri: ClassVar[URIRef] = MASTER.ApplicationVersion

    installDate: Optional[Union[str, XSDDateTime]] = None
    uninstallDate: Optional[Union[str, XSDDateTime]] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.installDate is not None and not isinstance(self.installDate, XSDDateTime):
            self.installDate = XSDDateTime(self.installDate)

        if self.uninstallDate is not None and not isinstance(self.uninstallDate, XSDDateTime):
            self.uninstallDate = XSDDateTime(self.uninstallDate)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class ArchiveFileFacet(Facet):
    """
    "An archive file facet is a grouping of characteristics unique to a file that is composed of one or more computer
    files along with metadata."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ArchiveFileFacet
    class_class_curie: ClassVar[str] = "observable:ArchiveFileFacet"
    class_name: ClassVar[str] = "ArchiveFileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ArchiveFileFacet

    archiveType: Optional[str] = None
    comment: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.archiveType is not None and not isinstance(self.archiveType, str):
            self.archiveType = str(self.archiveType)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class AudioFacet(Facet):
    """
    "An audio facet is a grouping of characteristics unique to a digital representation of sound."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AudioFacet
    class_class_curie: ClassVar[str] = "observable:AudioFacet"
    class_name: ClassVar[str] = "AudioFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AudioFacet

    bitRate: Optional[int] = None
    duration: Optional[int] = None
    audioType: Optional[str] = None
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.bitRate is not None and not isinstance(self.bitRate, int):
            self.bitRate = int(self.bitRate)

        if self.duration is not None and not isinstance(self.duration, int):
            self.duration = int(self.duration)

        if self.audioType is not None and not isinstance(self.audioType, str):
            self.audioType = str(self.audioType)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


@dataclass
class AutonomousSystemFacet(Facet):
    """
    "An autonomous system facet is a grouping of characteristics unique to a collection of connected Internet Protocol
    (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative
    entity or domain that presents a common, clearly defined routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AutonomousSystemFacet
    class_class_curie: ClassVar[str] = "observable:AutonomousSystemFacet"
    class_name: ClassVar[str] = "AutonomousSystemFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.AutonomousSystemFacet

    number: Optional[int] = None
    asHandle: Optional[str] = None
    regionalInternetRegistry: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.number is not None and not isinstance(self.number, int):
            self.number = int(self.number)

        if self.asHandle is not None and not isinstance(self.asHandle, str):
            self.asHandle = str(self.asHandle)

        if self.regionalInternetRegistry is not None and not isinstance(self.regionalInternetRegistry, str):
            self.regionalInternetRegistry = str(self.regionalInternetRegistry)

        super().__post_init__(**kwargs)


@dataclass
class BrowserBookmarkFacet(Facet):
    """
    "A browser bookmark facet is a grouping of characteristics unique to a saved shortcut that directs a WWW (World
    Wide Web) browser software program to a particular WWW accessible resource. [based on
    https://techterms.com/definition/bookmark]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BrowserBookmarkFacet
    class_class_curie: ClassVar[str] = "observable:BrowserBookmarkFacet"
    class_name: ClassVar[str] = "BrowserBookmarkFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.BrowserBookmarkFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    accessedTime: Optional[Union[str, XSDDateTime]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    urlTargeted: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    visitCount: Optional[int] = None
    bookmarkPath: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.accessedTime is not None and not isinstance(self.accessedTime, XSDDateTime):
            self.accessedTime = XSDDateTime(self.accessedTime)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if not isinstance(self.urlTargeted, list):
            self.urlTargeted = [self.urlTargeted] if self.urlTargeted is not None else []
        self.urlTargeted = [v if isinstance(v, IriType) else IriType(v) for v in self.urlTargeted]

        if self.visitCount is not None and not isinstance(self.visitCount, int):
            self.visitCount = int(self.visitCount)

        if self.bookmarkPath is not None and not isinstance(self.bookmarkPath, str):
            self.bookmarkPath = str(self.bookmarkPath)

        super().__post_init__(**kwargs)


@dataclass
class BrowserCookieFacet(Facet):
    """
    "A browser cookie facet is a grouping of characteristics unique to a piece of data sent from a website and stored
    on the user's computer by the user's web browser while the user is browsing. [based on
    https://en.wikipedia.org/wiki/HTTP_cookie]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BrowserCookieFacet
    class_class_curie: ClassVar[str] = "observable:BrowserCookieFacet"
    class_name: ClassVar[str] = "BrowserCookieFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.BrowserCookieFacet

    accessedTime: Optional[Union[str, XSDDateTime]] = None
    application: Optional[Union[dict, "ObservableObject"]] = None
    cookieDomain: Optional[Union[dict, "ObservableObject"]] = None
    cookieName: Optional[str] = None
    cookiePath: Optional[str] = None
    expirationTime: Optional[Union[str, XSDDateTime]] = None
    isSecure: Optional[Union[bool, BooleanType]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.accessedTime is not None and not isinstance(self.accessedTime, XSDDateTime):
            self.accessedTime = XSDDateTime(self.accessedTime)

        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.cookieDomain is not None and not isinstance(self.cookieDomain, ObservableObject):
            self.cookieDomain = ObservableObject(**as_dict(self.cookieDomain))

        if self.cookieName is not None and not isinstance(self.cookieName, str):
            self.cookieName = str(self.cookieName)

        if self.cookiePath is not None and not isinstance(self.cookiePath, str):
            self.cookiePath = str(self.cookiePath)

        if self.expirationTime is not None and not isinstance(self.expirationTime, XSDDateTime):
            self.expirationTime = XSDDateTime(self.expirationTime)

        if self.isSecure is not None and not isinstance(self.isSecure, BooleanType):
            self.isSecure = BooleanType(self.isSecure)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        super().__post_init__(**kwargs)


@dataclass
class CalendarEntryFacet(Facet):
    """
    "A calendar entry facet is a grouping of characteristics unique to an appointment, meeting, or event within a
    collection of appointments, meetings, and events."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CalendarEntryFacet
    class_class_curie: ClassVar[str] = "observable:CalendarEntryFacet"
    class_name: ClassVar[str] = "CalendarEntryFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CalendarEntryFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    attendant: Optional[Union[Union[dict, Identity], List[Union[dict, Identity]]]] = empty_list()
    isPrivate: Optional[Union[bool, BooleanType]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    location: Optional[Union[dict, Location]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    owner: Optional[Union[dict, UcoObject]] = None
    remindTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    duration: Optional[int] = None
    eventStatus: Optional[str] = None
    eventType: Optional[str] = None
    recurrence: Optional[str] = None
    subject: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if not isinstance(self.attendant, list):
            self.attendant = [self.attendant] if self.attendant is not None else []
        self.attendant = [v if isinstance(v, Identity) else Identity(**as_dict(v)) for v in self.attendant]

        if self.isPrivate is not None and not isinstance(self.isPrivate, BooleanType):
            self.isPrivate = BooleanType(self.isPrivate)

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.location is not None and not isinstance(self.location, Location):
            self.location = Location(**as_dict(self.location))

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.owner is not None and not isinstance(self.owner, UcoObject):
            self.owner = UcoObject(**as_dict(self.owner))

        if self.remindTime is not None and not isinstance(self.remindTime, XSDDateTime):
            self.remindTime = XSDDateTime(self.remindTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.duration is not None and not isinstance(self.duration, int):
            self.duration = int(self.duration)

        if self.eventStatus is not None and not isinstance(self.eventStatus, str):
            self.eventStatus = str(self.eventStatus)

        if self.eventType is not None and not isinstance(self.eventType, str):
            self.eventType = str(self.eventType)

        if self.recurrence is not None and not isinstance(self.recurrence, str):
            self.recurrence = str(self.recurrence)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class CalendarFacet(Facet):
    """
    "A calendar facet is a grouping of characteristics unique to a collection of appointments, meetings, and events."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CalendarFacet
    class_class_curie: ClassVar[str] = "observable:CalendarFacet"
    class_name: ClassVar[str] = "CalendarFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CalendarFacet

    owner: Optional[Union[dict, UcoObject]] = None
    application: Optional[Union[dict, "ObservableObject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owner is not None and not isinstance(self.owner, UcoObject):
            self.owner = UcoObject(**as_dict(self.owner))

        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        super().__post_init__(**kwargs)


@dataclass
class CallFacet(Facet):
    """
    "A call facet is a grouping of characteristics unique to a connection as part of a realtime cyber communication
    between one or more parties."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CallFacet
    class_class_curie: ClassVar[str] = "observable:CallFacet"
    class_name: ClassVar[str] = "CallFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CallFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    duration: Optional[int] = None
    participant: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    callType: Optional[str] = None
    from: Optional[Union[dict, "ObservableObject"]] = None
    to: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.duration is not None and not isinstance(self.duration, int):
            self.duration = int(self.duration)

        if not isinstance(self.participant, list):
            self.participant = [self.participant] if self.participant is not None else []
        self.participant = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.participant]

        if self.callType is not None and not isinstance(self.callType, str):
            self.callType = str(self.callType)

        if self.from is not None and not isinstance(self.from, ObservableObject):
            self.from = ObservableObject(**as_dict(self.from))

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.to]

        super().__post_init__(**kwargs)


@dataclass
class CapturedTelecommunicationsInformationFacet(Facet):
    """
    "A captured telecommunications information facet represents certain information within captured or intercepted
    telecommunications data."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CapturedTelecommunicationsInformationFacet
    class_class_curie: ClassVar[str] = "observable:CapturedTelecommunicationsInformationFacet"
    class_name: ClassVar[str] = "CapturedTelecommunicationsInformationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CapturedTelecommunicationsInformationFacet

    captureCellSite: Union[dict, "CellSite"] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    interceptedCallState: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.captureCellSite):
            self.MissingRequiredField("captureCellSite")
        if not isinstance(self.captureCellSite, CellSite):
            self.captureCellSite = CellSite(**as_dict(self.captureCellSite))

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.interceptedCallState is not None and not isinstance(self.interceptedCallState, str):
            self.interceptedCallState = str(self.interceptedCallState)

        super().__post_init__(**kwargs)


@dataclass
class CellSiteFacet(Facet):
    """
    "A cell site facet contains the metadata surrounding the cell site."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CellSiteFacet
    class_class_curie: ClassVar[str] = "observable:CellSiteFacet"
    class_name: ClassVar[str] = "CellSiteFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CellSiteFacet

    cellSiteCountryCode: Optional[str] = None
    cellSiteIdentifier: Optional[str] = None
    cellSiteLocationAreaCode: Optional[str] = None
    cellSiteNetworkCode: Optional[str] = None
    cellSiteType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cellSiteCountryCode is not None and not isinstance(self.cellSiteCountryCode, str):
            self.cellSiteCountryCode = str(self.cellSiteCountryCode)

        if self.cellSiteIdentifier is not None and not isinstance(self.cellSiteIdentifier, str):
            self.cellSiteIdentifier = str(self.cellSiteIdentifier)

        if self.cellSiteLocationAreaCode is not None and not isinstance(self.cellSiteLocationAreaCode, str):
            self.cellSiteLocationAreaCode = str(self.cellSiteLocationAreaCode)

        if self.cellSiteNetworkCode is not None and not isinstance(self.cellSiteNetworkCode, str):
            self.cellSiteNetworkCode = str(self.cellSiteNetworkCode)

        if self.cellSiteType is not None and not isinstance(self.cellSiteType, str):
            self.cellSiteType = str(self.cellSiteType)

        super().__post_init__(**kwargs)


@dataclass
class CompressedStreamFacet(Facet):
    """
    "A compressed stream facet is a grouping of characteristics unique to the application of a size-reduction process
    to a body of data content."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CompressedStreamFacet
    class_class_curie: ClassVar[str] = "observable:CompressedStreamFacet"
    class_name: ClassVar[str] = "CompressedStreamFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.CompressedStreamFacet

    compressionRatio: Optional[Union[Decimal, DecimalType]] = None
    compressionMethod: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.compressionRatio is not None and not isinstance(self.compressionRatio, DecimalType):
            self.compressionRatio = DecimalType(self.compressionRatio)

        if self.compressionMethod is not None and not isinstance(self.compressionMethod, str):
            self.compressionMethod = str(self.compressionMethod)

        super().__post_init__(**kwargs)


@dataclass
class ComputerSpecificationFacet(Facet):
    """
    "A computer specificaiton facet is a grouping of characteristics unique to the hardware and software of a
    programmable electronic device that can store, retrieve, and process data. [based on
    merriam-webster.com/dictionary/computer]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ComputerSpecificationFacet
    class_class_curie: ClassVar[str] = "observable:ComputerSpecificationFacet"
    class_name: ClassVar[str] = "ComputerSpecificationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ComputerSpecificationFacet

    biosDate: Optional[Union[str, XSDDateTime]] = None
    biosReleaseDate: Optional[Union[str, XSDDateTime]] = None
    currentSystemDate: Optional[Union[str, XSDDateTime]] = None
    localTime: Optional[Union[str, XSDDateTime]] = None
    systemTime: Optional[Union[str, XSDDateTime]] = None
    availableRam: Optional[int] = None
    totalRam: Optional[int] = None
    biosManufacturer: Optional[str] = None
    biosSerialNumber: Optional[str] = None
    biosVersion: Optional[str] = None
    cpu: Optional[str] = None
    cpuFamily: Optional[str] = None
    gpu: Optional[str] = None
    gpuFamily: Optional[str] = None
    hostname: Optional[str] = None
    networkInterface: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    processorArchitecture: Optional[str] = None
    timezoneDST: Optional[str] = None
    timezoneStandard: Optional[str] = None
    uptime: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.biosDate is not None and not isinstance(self.biosDate, XSDDateTime):
            self.biosDate = XSDDateTime(self.biosDate)

        if self.biosReleaseDate is not None and not isinstance(self.biosReleaseDate, XSDDateTime):
            self.biosReleaseDate = XSDDateTime(self.biosReleaseDate)

        if self.currentSystemDate is not None and not isinstance(self.currentSystemDate, XSDDateTime):
            self.currentSystemDate = XSDDateTime(self.currentSystemDate)

        if self.localTime is not None and not isinstance(self.localTime, XSDDateTime):
            self.localTime = XSDDateTime(self.localTime)

        if self.systemTime is not None and not isinstance(self.systemTime, XSDDateTime):
            self.systemTime = XSDDateTime(self.systemTime)

        if self.availableRam is not None and not isinstance(self.availableRam, int):
            self.availableRam = int(self.availableRam)

        if self.totalRam is not None and not isinstance(self.totalRam, int):
            self.totalRam = int(self.totalRam)

        if self.biosManufacturer is not None and not isinstance(self.biosManufacturer, str):
            self.biosManufacturer = str(self.biosManufacturer)

        if self.biosSerialNumber is not None and not isinstance(self.biosSerialNumber, str):
            self.biosSerialNumber = str(self.biosSerialNumber)

        if self.biosVersion is not None and not isinstance(self.biosVersion, str):
            self.biosVersion = str(self.biosVersion)

        if self.cpu is not None and not isinstance(self.cpu, str):
            self.cpu = str(self.cpu)

        if self.cpuFamily is not None and not isinstance(self.cpuFamily, str):
            self.cpuFamily = str(self.cpuFamily)

        if self.gpu is not None and not isinstance(self.gpu, str):
            self.gpu = str(self.gpu)

        if self.gpuFamily is not None and not isinstance(self.gpuFamily, str):
            self.gpuFamily = str(self.gpuFamily)

        if self.hostname is not None and not isinstance(self.hostname, str):
            self.hostname = str(self.hostname)

        if not isinstance(self.networkInterface, list):
            self.networkInterface = [self.networkInterface] if self.networkInterface is not None else []
        self.networkInterface = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.networkInterface]

        if self.processorArchitecture is not None and not isinstance(self.processorArchitecture, str):
            self.processorArchitecture = str(self.processorArchitecture)

        if self.timezoneDST is not None and not isinstance(self.timezoneDST, str):
            self.timezoneDST = str(self.timezoneDST)

        if self.timezoneStandard is not None and not isinstance(self.timezoneStandard, str):
            self.timezoneStandard = str(self.timezoneStandard)

        if self.uptime is not None and not isinstance(self.uptime, str):
            self.uptime = str(self.uptime)

        super().__post_init__(**kwargs)


@dataclass
class ContactAddress(UcoInherentCharacterizationThing):
    """
    "A contact address is a grouping of characteristics unique to a geolocation address of a contact entity."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactAddress
    class_class_curie: ClassVar[str] = "observable:ContactAddress"
    class_name: ClassVar[str] = "ContactAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactAddress

    geoLocationAddress: Optional[Union[dict, Location]] = None
    contactAddressScope: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.geoLocationAddress is not None and not isinstance(self.geoLocationAddress, Location):
            self.geoLocationAddress = Location(**as_dict(self.geoLocationAddress))

        if self.contactAddressScope is not None and not isinstance(self.contactAddressScope, str):
            self.contactAddressScope = str(self.contactAddressScope)

        super().__post_init__(**kwargs)


@dataclass
class ContactAffiliation(UcoInherentCharacterizationThing):
    """
    "A contact affiliation is a grouping of characteristics unique to details of an organizational affiliation for a
    single contact entity."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactAffiliation
    class_class_curie: ClassVar[str] = "observable:ContactAffiliation"
    class_name: ClassVar[str] = "ContactAffiliation"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactAffiliation

    contactOrganization: Optional[Union[dict, Organization]] = None
    organizationLocation: Optional[Union[dict, ContactAddress]] = None
    contactEmail: Optional[Union[dict, "ContactEmail"]] = None
    contactMessaging: Optional[Union[dict, "ContactMessaging"]] = None
    contactPhone: Optional[Union[dict, "ContactPhone"]] = None
    contactProfile: Optional[Union[dict, "ContactProfile"]] = None
    contactURL: Optional[Union[dict, "ContactURL"]] = None
    organizationDepartment: Optional[str] = None
    organizationPosition: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contactOrganization is not None and not isinstance(self.contactOrganization, Organization):
            self.contactOrganization = Organization(**as_dict(self.contactOrganization))

        if self.organizationLocation is not None and not isinstance(self.organizationLocation, ContactAddress):
            self.organizationLocation = ContactAddress(**as_dict(self.organizationLocation))

        if self.contactEmail is not None and not isinstance(self.contactEmail, ContactEmail):
            self.contactEmail = ContactEmail(**as_dict(self.contactEmail))

        if self.contactMessaging is not None and not isinstance(self.contactMessaging, ContactMessaging):
            self.contactMessaging = ContactMessaging(**as_dict(self.contactMessaging))

        if self.contactPhone is not None and not isinstance(self.contactPhone, ContactPhone):
            self.contactPhone = ContactPhone(**as_dict(self.contactPhone))

        if self.contactProfile is not None and not isinstance(self.contactProfile, ContactProfile):
            self.contactProfile = ContactProfile(**as_dict(self.contactProfile))

        if self.contactURL is not None and not isinstance(self.contactURL, ContactURL):
            self.contactURL = ContactURL(**as_dict(self.contactURL))

        if self.organizationDepartment is not None and not isinstance(self.organizationDepartment, str):
            self.organizationDepartment = str(self.organizationDepartment)

        if self.organizationPosition is not None and not isinstance(self.organizationPosition, str):
            self.organizationPosition = str(self.organizationPosition)

        super().__post_init__(**kwargs)


@dataclass
class ContactEmail(UcoInherentCharacterizationThing):
    """
    "A contact email is a grouping of characteristics unique to details for contacting a contact entity by email."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactEmail
    class_class_curie: ClassVar[str] = "observable:ContactEmail"
    class_name: ClassVar[str] = "ContactEmail"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactEmail

    emailAddress: Optional[Union[dict, "ObservableObject"]] = None
    contactEmailScope: Optional[Union[str, "ContactEmailScopeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.emailAddress is not None and not isinstance(self.emailAddress, ObservableObject):
            self.emailAddress = ObservableObject(**as_dict(self.emailAddress))

        if self.contactEmailScope is not None and not isinstance(self.contactEmailScope, ContactEmailScopeEnum):
            self.contactEmailScope = ContactEmailScopeEnum(self.contactEmailScope)

        super().__post_init__(**kwargs)


@dataclass
class ContactFacet(Facet):
    """
    "A contact facet is a grouping of characteristics unique to a set of identification and communication related
    details for a single entity."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactFacet
    class_class_curie: ClassVar[str] = "observable:ContactFacet"
    class_name: ClassVar[str] = "ContactFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactFacet

    contactAddress: Optional[Union[dict, ContactAddress]] = None
    contactAffiliation: Optional[Union[dict, ContactAffiliation]] = None
    contactEmail: Optional[Union[dict, ContactEmail]] = None
    contactMessaging: Optional[Union[dict, "ContactMessaging"]] = None
    contactPhone: Optional[Union[dict, "ContactPhone"]] = None
    contactProfile: Optional[Union[dict, "ContactProfile"]] = None
    contactSIP: Optional[Union[dict, "ContactSIP"]] = None
    contactURL: Optional[Union[dict, "ContactURL"]] = None
    sourceApplication: Optional[Union[dict, "ObservableObject"]] = None
    birthdate: Optional[Union[str, XSDDateTime]] = None
    lastTimeContacted: Optional[Union[str, XSDDateTime]] = None
    numberTimesContacted: Optional[int] = None
    contactID: Optional[str] = None
    displayName: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    namePhonetic: Optional[str] = None
    namePrefix: Optional[str] = None
    nameSuffix: Optional[str] = None
    contactGroup: Optional[str] = None
    contactNote: Optional[str] = None
    nickname: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contactAddress is not None and not isinstance(self.contactAddress, ContactAddress):
            self.contactAddress = ContactAddress(**as_dict(self.contactAddress))

        if self.contactAffiliation is not None and not isinstance(self.contactAffiliation, ContactAffiliation):
            self.contactAffiliation = ContactAffiliation(**as_dict(self.contactAffiliation))

        if self.contactEmail is not None and not isinstance(self.contactEmail, ContactEmail):
            self.contactEmail = ContactEmail(**as_dict(self.contactEmail))

        if self.contactMessaging is not None and not isinstance(self.contactMessaging, ContactMessaging):
            self.contactMessaging = ContactMessaging(**as_dict(self.contactMessaging))

        if self.contactPhone is not None and not isinstance(self.contactPhone, ContactPhone):
            self.contactPhone = ContactPhone(**as_dict(self.contactPhone))

        if self.contactProfile is not None and not isinstance(self.contactProfile, ContactProfile):
            self.contactProfile = ContactProfile(**as_dict(self.contactProfile))

        if self.contactSIP is not None and not isinstance(self.contactSIP, ContactSIP):
            self.contactSIP = ContactSIP(**as_dict(self.contactSIP))

        if self.contactURL is not None and not isinstance(self.contactURL, ContactURL):
            self.contactURL = ContactURL(**as_dict(self.contactURL))

        if self.sourceApplication is not None and not isinstance(self.sourceApplication, ObservableObject):
            self.sourceApplication = ObservableObject(**as_dict(self.sourceApplication))

        if self.birthdate is not None and not isinstance(self.birthdate, XSDDateTime):
            self.birthdate = XSDDateTime(self.birthdate)

        if self.lastTimeContacted is not None and not isinstance(self.lastTimeContacted, XSDDateTime):
            self.lastTimeContacted = XSDDateTime(self.lastTimeContacted)

        if self.numberTimesContacted is not None and not isinstance(self.numberTimesContacted, int):
            self.numberTimesContacted = int(self.numberTimesContacted)

        if self.contactID is not None and not isinstance(self.contactID, str):
            self.contactID = str(self.contactID)

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if self.firstName is not None and not isinstance(self.firstName, str):
            self.firstName = str(self.firstName)

        if self.lastName is not None and not isinstance(self.lastName, str):
            self.lastName = str(self.lastName)

        if self.middleName is not None and not isinstance(self.middleName, str):
            self.middleName = str(self.middleName)

        if self.namePhonetic is not None and not isinstance(self.namePhonetic, str):
            self.namePhonetic = str(self.namePhonetic)

        if self.namePrefix is not None and not isinstance(self.namePrefix, str):
            self.namePrefix = str(self.namePrefix)

        if self.nameSuffix is not None and not isinstance(self.nameSuffix, str):
            self.nameSuffix = str(self.nameSuffix)

        if self.contactGroup is not None and not isinstance(self.contactGroup, str):
            self.contactGroup = str(self.contactGroup)

        if self.contactNote is not None and not isinstance(self.contactNote, str):
            self.contactNote = str(self.contactNote)

        if self.nickname is not None and not isinstance(self.nickname, str):
            self.nickname = str(self.nickname)

        super().__post_init__(**kwargs)


@dataclass
class ContactListFacet(Facet):
    """
    "A contact list facet is a grouping of characteristics unique to a set of multiple individual contacts such as
    that found in a digital address book."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactListFacet
    class_class_curie: ClassVar[str] = "observable:ContactListFacet"
    class_name: ClassVar[str] = "ContactListFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactListFacet

    sourceApplication: Optional[Union[dict, "ObservableObject"]] = None
    contact: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sourceApplication is not None and not isinstance(self.sourceApplication, ObservableObject):
            self.sourceApplication = ObservableObject(**as_dict(self.sourceApplication))

        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.contact]

        super().__post_init__(**kwargs)


@dataclass
class ContactMessaging(UcoInherentCharacterizationThing):
    """
    "A contactMessaging is a grouping of characteristics unique to details for contacting a contact entity by digital
    messaging."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactMessaging
    class_class_curie: ClassVar[str] = "observable:ContactMessaging"
    class_name: ClassVar[str] = "ContactMessaging"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactMessaging

    contactMessagingPlatform: Optional[Union[dict, "ObservableObject"]] = None
    messagingAddress: Optional[Union[dict, "ObservableObject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contactMessagingPlatform is not None and not isinstance(self.contactMessagingPlatform, ObservableObject):
            self.contactMessagingPlatform = ObservableObject(**as_dict(self.contactMessagingPlatform))

        if self.messagingAddress is not None and not isinstance(self.messagingAddress, ObservableObject):
            self.messagingAddress = ObservableObject(**as_dict(self.messagingAddress))

        super().__post_init__(**kwargs)


@dataclass
class ContactPhone(UcoInherentCharacterizationThing):
    """
    "A contactPhone is a grouping of characteristics unique to details for contacting a contact entity by telephone."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactPhone
    class_class_curie: ClassVar[str] = "observable:ContactPhone"
    class_name: ClassVar[str] = "ContactPhone"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactPhone

    contactPhoneNumber: Optional[Union[dict, "ObservableObject"]] = None
    contactPhoneScope: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contactPhoneNumber is not None and not isinstance(self.contactPhoneNumber, ObservableObject):
            self.contactPhoneNumber = ObservableObject(**as_dict(self.contactPhoneNumber))

        if self.contactPhoneScope is not None and not isinstance(self.contactPhoneScope, str):
            self.contactPhoneScope = str(self.contactPhoneScope)

        super().__post_init__(**kwargs)


@dataclass
class ContactProfile(UcoInherentCharacterizationThing):
    """
    "A contactProfile is a grouping of characteristics unique to details for contacting a contact entity by online
    service."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactProfile
    class_class_curie: ClassVar[str] = "observable:ContactProfile"
    class_name: ClassVar[str] = "ContactProfile"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactProfile

    contactProfilePlatform: Optional[Union[dict, "ObservableObject"]] = None
    profile: Optional[Union[dict, "ObservableObject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contactProfilePlatform is not None and not isinstance(self.contactProfilePlatform, ObservableObject):
            self.contactProfilePlatform = ObservableObject(**as_dict(self.contactProfilePlatform))

        if self.profile is not None and not isinstance(self.profile, ObservableObject):
            self.profile = ObservableObject(**as_dict(self.profile))

        super().__post_init__(**kwargs)


@dataclass
class ContactSIP(UcoInherentCharacterizationThing):
    """
    "A contactSIP is a grouping of characteristics unique to details for contacting a contact entity by Session
    Initiation Protocol (SIP)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactSIP
    class_class_curie: ClassVar[str] = "observable:ContactSIP"
    class_name: ClassVar[str] = "ContactSIP"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactSIP

    sipAddress: Optional[Union[dict, "ObservableObject"]] = None
    contactSIPScope: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sipAddress is not None and not isinstance(self.sipAddress, ObservableObject):
            self.sipAddress = ObservableObject(**as_dict(self.sipAddress))

        if self.contactSIPScope is not None and not isinstance(self.contactSIPScope, str):
            self.contactSIPScope = str(self.contactSIPScope)

        super().__post_init__(**kwargs)


@dataclass
class ContactURL(UcoInherentCharacterizationThing):
    """
    "A contactURL is a grouping of characteristics unique to details for contacting a contact entity by Uniform
    Resource Locator (URL)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactURL
    class_class_curie: ClassVar[str] = "observable:ContactURL"
    class_name: ClassVar[str] = "ContactURL"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactURL

    contactURLScope: Optional[str] = None
    url: Optional[Union[dict, "ObservableObject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contactURLScope is not None and not isinstance(self.contactURLScope, str):
            self.contactURLScope = str(self.contactURLScope)

        if self.url is not None and not isinstance(self.url, ObservableObject):
            self.url = ObservableObject(**as_dict(self.url))

        super().__post_init__(**kwargs)


@dataclass
class ContentDataFacet(Facet):
    """
    "A content data facet is a grouping of characteristics unique to a block of digital data."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContentDataFacet
    class_class_curie: ClassVar[str] = "observable:ContentDataFacet"
    class_name: ClassVar[str] = "ContentDataFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ContentDataFacet

    dataPayloadReferenceURL: Optional[Union[dict, "ObservableObject"]] = None
    hash: Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]] = empty_list()
    isEncrypted: Optional[Union[bool, BooleanType]] = None
    entropy: Optional[Union[Decimal, DecimalType]] = None
    sizeInBytes: Optional[int] = None
    dataPayload: Optional[str] = None
    magicNumber: Optional[str] = None
    mimeClass: Optional[str] = None
    mimeType: Optional[Union[str, List[str]]] = empty_list()
    byteOrder: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dataPayloadReferenceURL is not None and not isinstance(self.dataPayloadReferenceURL, ObservableObject):
            self.dataPayloadReferenceURL = ObservableObject(**as_dict(self.dataPayloadReferenceURL))

        self._normalize_inlined_as_dict(slot_name="hash", slot_type=Hash, key_name="hashValue", keyed=False)

        if self.isEncrypted is not None and not isinstance(self.isEncrypted, BooleanType):
            self.isEncrypted = BooleanType(self.isEncrypted)

        if self.entropy is not None and not isinstance(self.entropy, DecimalType):
            self.entropy = DecimalType(self.entropy)

        if self.sizeInBytes is not None and not isinstance(self.sizeInBytes, int):
            self.sizeInBytes = int(self.sizeInBytes)

        if self.dataPayload is not None and not isinstance(self.dataPayload, str):
            self.dataPayload = str(self.dataPayload)

        if self.magicNumber is not None and not isinstance(self.magicNumber, str):
            self.magicNumber = str(self.magicNumber)

        if self.mimeClass is not None and not isinstance(self.mimeClass, str):
            self.mimeClass = str(self.mimeClass)

        if not isinstance(self.mimeType, list):
            self.mimeType = [self.mimeType] if self.mimeType is not None else []
        self.mimeType = [v if isinstance(v, str) else str(v) for v in self.mimeType]

        if self.byteOrder is not None and not isinstance(self.byteOrder, str):
            self.byteOrder = str(self.byteOrder)

        super().__post_init__(**kwargs)


@dataclass
class DataRangeFacet(Facet):
    """
    "A data range facet is a grouping of characteristics unique to a particular contiguous scope within a block of
    digital data."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DataRangeFacet
    class_class_curie: ClassVar[str] = "observable:DataRangeFacet"
    class_name: ClassVar[str] = "DataRangeFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DataRangeFacet

    rangeOffset: Optional[int] = None
    rangeSize: Optional[int] = None
    rangeOffsetType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.rangeOffset is not None and not isinstance(self.rangeOffset, int):
            self.rangeOffset = int(self.rangeOffset)

        if self.rangeSize is not None and not isinstance(self.rangeSize, int):
            self.rangeSize = int(self.rangeSize)

        if self.rangeOffsetType is not None and not isinstance(self.rangeOffsetType, str):
            self.rangeOffsetType = str(self.rangeOffsetType)

        super().__post_init__(**kwargs)


class DefinedEffectFacet(Facet):
    """
    "A defined effect facet is a grouping of characteristics unique to the effect of an observable action in relation
    to one or more observable objects."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DefinedEffectFacet
    class_class_curie: ClassVar[str] = "observable:DefinedEffectFacet"
    class_name: ClassVar[str] = "DefinedEffectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DefinedEffectFacet


@dataclass
class DeviceFacet(Facet):
    """
    "A device facet is a grouping of characteristics unique to a piece of equipment or a mechanism designed to serve a
    special purpose or perform a special function. [based on https://www.merriam-webster.com/dictionary/device]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DeviceFacet
    class_class_curie: ClassVar[str] = "observable:DeviceFacet"
    class_name: ClassVar[str] = "DeviceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DeviceFacet

    manufacturer: Optional[Union[dict, Identity]] = None
    deviceType: Optional[str] = None
    model: Optional[str] = None
    serialNumber: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.manufacturer is not None and not isinstance(self.manufacturer, Identity):
            self.manufacturer = Identity(**as_dict(self.manufacturer))

        if self.deviceType is not None and not isinstance(self.deviceType, str):
            self.deviceType = str(self.deviceType)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.serialNumber is not None and not isinstance(self.serialNumber, str):
            self.serialNumber = str(self.serialNumber)

        super().__post_init__(**kwargs)


@dataclass
class DigitalAccountFacet(Facet):
    """
    "A digital account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of some capability or service within the digital domain."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalAccountFacet
    class_class_curie: ClassVar[str] = "observable:DigitalAccountFacet"
    class_name: ClassVar[str] = "DigitalAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalAccountFacet

    isDisabled: Optional[Union[bool, BooleanType]] = None
    firstLoginTime: Optional[Union[str, XSDDateTime]] = None
    lastLoginTime: Optional[Union[str, XSDDateTime]] = None
    displayName: Optional[str] = None
    accountLogin: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isDisabled is not None and not isinstance(self.isDisabled, BooleanType):
            self.isDisabled = BooleanType(self.isDisabled)

        if self.firstLoginTime is not None and not isinstance(self.firstLoginTime, XSDDateTime):
            self.firstLoginTime = XSDDateTime(self.firstLoginTime)

        if self.lastLoginTime is not None and not isinstance(self.lastLoginTime, XSDDateTime):
            self.lastLoginTime = XSDDateTime(self.lastLoginTime)

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if not isinstance(self.accountLogin, list):
            self.accountLogin = [self.accountLogin] if self.accountLogin is not None else []
        self.accountLogin = [v if isinstance(v, str) else str(v) for v in self.accountLogin]

        super().__post_init__(**kwargs)


@dataclass
class DigitalAddressFacet(Facet):
    """
    "A digital address facet is a grouping of characteristics unique to an identifier assigned to enable routing and
    management of digital communication."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalAddressFacet
    class_class_curie: ClassVar[str] = "observable:DigitalAddressFacet"
    class_name: ClassVar[str] = "DigitalAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalAddressFacet

    addressValue: Optional[str] = None
    displayName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.addressValue is not None and not isinstance(self.addressValue, str):
            self.addressValue = str(self.addressValue)

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        super().__post_init__(**kwargs)


@dataclass
class DigitalSignatureInfoFacet(Facet):
    """
    "A digital signature info facet is a grouping of characteristics unique to a value calculated via a mathematical
    scheme for demonstrating the authenticity of an electronic message or document."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalSignatureInfoFacet
    class_class_curie: ClassVar[str] = "observable:DigitalSignatureInfoFacet"
    class_name: ClassVar[str] = "DigitalSignatureInfoFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalSignatureInfoFacet

    certificateSubject: Optional[Union[dict, UcoObject]] = None
    certificateIssuer: Optional[Union[dict, Identity]] = None
    signatureExists: Optional[Union[bool, BooleanType]] = None
    signatureVerified: Optional[Union[bool, BooleanType]] = None
    signatureDescription: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.certificateSubject is not None and not isinstance(self.certificateSubject, UcoObject):
            self.certificateSubject = UcoObject(**as_dict(self.certificateSubject))

        if self.certificateIssuer is not None and not isinstance(self.certificateIssuer, Identity):
            self.certificateIssuer = Identity(**as_dict(self.certificateIssuer))

        if self.signatureExists is not None and not isinstance(self.signatureExists, BooleanType):
            self.signatureExists = BooleanType(self.signatureExists)

        if self.signatureVerified is not None and not isinstance(self.signatureVerified, BooleanType):
            self.signatureVerified = BooleanType(self.signatureVerified)

        if self.signatureDescription is not None and not isinstance(self.signatureDescription, str):
            self.signatureDescription = str(self.signatureDescription)

        super().__post_init__(**kwargs)


@dataclass
class DiskFacet(Facet):
    """
    "A disk facet is a grouping of characteristics unique to a storage mechanism where data is recorded by various
    electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DiskFacet
    class_class_curie: ClassVar[str] = "observable:DiskFacet"
    class_name: ClassVar[str] = "DiskFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DiskFacet

    partition: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    diskSize: Optional[int] = None
    freeSpace: Optional[int] = None
    diskType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.partition, list):
            self.partition = [self.partition] if self.partition is not None else []
        self.partition = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.partition]

        if self.diskSize is not None and not isinstance(self.diskSize, int):
            self.diskSize = int(self.diskSize)

        if self.freeSpace is not None and not isinstance(self.freeSpace, int):
            self.freeSpace = int(self.freeSpace)

        if self.diskType is not None and not isinstance(self.diskType, str):
            self.diskType = str(self.diskType)

        super().__post_init__(**kwargs)


@dataclass
class DiskPartitionFacet(Facet):
    """
    "A disk partition facet is a grouping of characteristics unique to a particular managed region on a storage
    mechanism."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DiskPartitionFacet
    class_class_curie: ClassVar[str] = "observable:DiskPartitionFacet"
    class_name: ClassVar[str] = "DiskPartitionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DiskPartitionFacet

    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    partitionLength: Optional[int] = None
    partitionOffset: Optional[int] = None
    spaceLeft: Optional[int] = None
    spaceUsed: Optional[int] = None
    totalSpace: Optional[int] = None
    diskPartitionType: Optional[str] = None
    mountPoint: Optional[str] = None
    partitionID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.partitionLength is not None and not isinstance(self.partitionLength, int):
            self.partitionLength = int(self.partitionLength)

        if self.partitionOffset is not None and not isinstance(self.partitionOffset, int):
            self.partitionOffset = int(self.partitionOffset)

        if self.spaceLeft is not None and not isinstance(self.spaceLeft, int):
            self.spaceLeft = int(self.spaceLeft)

        if self.spaceUsed is not None and not isinstance(self.spaceUsed, int):
            self.spaceUsed = int(self.spaceUsed)

        if self.totalSpace is not None and not isinstance(self.totalSpace, int):
            self.totalSpace = int(self.totalSpace)

        if self.diskPartitionType is not None and not isinstance(self.diskPartitionType, str):
            self.diskPartitionType = str(self.diskPartitionType)

        if self.mountPoint is not None and not isinstance(self.mountPoint, str):
            self.mountPoint = str(self.mountPoint)

        if self.partitionID is not None and not isinstance(self.partitionID, str):
            self.partitionID = str(self.partitionID)

        super().__post_init__(**kwargs)


@dataclass
class DomainNameFacet(Facet):
    """
    "A domainName facet is a grouping of characteristics unique to an identification string that defines a realm of
    administrative autonomy, authority or control within the Internet. [based on
    https://en.wikipedia.org/wiki/Domain_name]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DomainNameFacet
    class_class_curie: ClassVar[str] = "observable:DomainNameFacet"
    class_name: ClassVar[str] = "DomainNameFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.DomainNameFacet

    isTLD: Optional[Union[bool, BooleanType]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isTLD is not None and not isinstance(self.isTLD, BooleanType):
            self.isTLD = BooleanType(self.isTLD)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class EXIFFacet(Facet):
    """
    "An EXIF (exchangeable image file format) facet is a grouping of characteristics unique to the formats for images,
    sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling
    image and sound files recorded by digital cameras conformant to JEIDA/JEITA/CIPA specifications. [based on
    https://en.wikipedia.org/wiki/Exif]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EXIFFacet
    class_class_curie: ClassVar[str] = "observable:EXIFFacet"
    class_name: ClassVar[str] = "EXIFFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EXIFFacet

    exifData: Optional[Union[Union[dict, "ControlledDictionary"], List[Union[dict, "ControlledDictionary"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.exifData, list):
            self.exifData = [self.exifData] if self.exifData is not None else []
        self.exifData = [v if isinstance(v, ControlledDictionary) else ControlledDictionary(**as_dict(v)) for v in self.exifData]

        super().__post_init__(**kwargs)


@dataclass
class EmailAccountFacet(Facet):
    """
    "An email account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of electronic mail (email) capabilities or services."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmailAccountFacet
    class_class_curie: ClassVar[str] = "observable:EmailAccountFacet"
    class_name: ClassVar[str] = "EmailAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EmailAccountFacet

    emailAddress: Optional[Union[dict, "ObservableObject"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.emailAddress is not None and not isinstance(self.emailAddress, ObservableObject):
            self.emailAddress = ObservableObject(**as_dict(self.emailAddress))

        super().__post_init__(**kwargs)


class EmailAddressFacet(DigitalAddressFacet):
    """
    "An emailAddress facet is a grouping of characteristics unique to an identifier for an electronic mailbox to which
    electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmailAddressFacet
    class_class_curie: ClassVar[str] = "observable:EmailAddressFacet"
    class_name: ClassVar[str] = "EmailAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EmailAddressFacet


@dataclass
class EmailMessageFacet(Facet):
    """
    "An email message facet is a grouping of characteristics unique to a message that is an instance of an electronic
    mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmailMessageFacet
    class_class_curie: ClassVar[str] = "observable:EmailMessageFacet"
    class_name: ClassVar[str] = "EmailMessageFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EmailMessageFacet

    bodyMultipart: Optional[Union[Union[dict, "MimePartType"], List[Union[dict, "MimePartType"]]]] = empty_list()
    application: Optional[Union[dict, "ObservableObject"]] = None
    bodyRaw: Optional[Union[dict, "ObservableObject"]] = None
    from: Optional[Union[dict, "ObservableObject"]] = None
    headerRaw: Optional[Union[dict, "ObservableObject"]] = None
    sender: Optional[Union[dict, "ObservableObject"]] = None
    xOriginatingIP: Optional[Union[dict, "ObservableObject"]] = None
    bcc: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    cc: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    references: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    to: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    otherHeaders: Optional[Union[dict, "Dictionary"]] = None
    isMimeEncoded: Optional[Union[bool, BooleanType]] = None
    isMultipart: Optional[Union[bool, BooleanType]] = None
    isRead: Optional[Union[bool, BooleanType]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    receivedTime: Optional[Union[str, XSDDateTime]] = None
    sentTime: Optional[Union[str, XSDDateTime]] = None
    body: Optional[str] = None
    contentDisposition: Optional[str] = None
    contentType: Optional[str] = None
    inReplyTo: Optional[str] = None
    messageID: Optional[str] = None
    priority: Optional[str] = None
    subject: Optional[str] = None
    xMailer: Optional[str] = None
    categories: Optional[Union[str, List[str]]] = empty_list()
    labels: Optional[Union[str, List[str]]] = empty_list()
    receivedLines: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.bodyMultipart, list):
            self.bodyMultipart = [self.bodyMultipart] if self.bodyMultipart is not None else []
        self.bodyMultipart = [v if isinstance(v, MimePartType) else MimePartType(**as_dict(v)) for v in self.bodyMultipart]

        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.bodyRaw is not None and not isinstance(self.bodyRaw, ObservableObject):
            self.bodyRaw = ObservableObject(**as_dict(self.bodyRaw))

        if self.from is not None and not isinstance(self.from, ObservableObject):
            self.from = ObservableObject(**as_dict(self.from))

        if self.headerRaw is not None and not isinstance(self.headerRaw, ObservableObject):
            self.headerRaw = ObservableObject(**as_dict(self.headerRaw))

        if self.sender is not None and not isinstance(self.sender, ObservableObject):
            self.sender = ObservableObject(**as_dict(self.sender))

        if self.xOriginatingIP is not None and not isinstance(self.xOriginatingIP, ObservableObject):
            self.xOriginatingIP = ObservableObject(**as_dict(self.xOriginatingIP))

        if not isinstance(self.bcc, list):
            self.bcc = [self.bcc] if self.bcc is not None else []
        self.bcc = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.bcc]

        if not isinstance(self.cc, list):
            self.cc = [self.cc] if self.cc is not None else []
        self.cc = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.cc]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.references]

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.to]

        if self.otherHeaders is not None and not isinstance(self.otherHeaders, Dictionary):
            self.otherHeaders = Dictionary(**as_dict(self.otherHeaders))

        if self.isMimeEncoded is not None and not isinstance(self.isMimeEncoded, BooleanType):
            self.isMimeEncoded = BooleanType(self.isMimeEncoded)

        if self.isMultipart is not None and not isinstance(self.isMultipart, BooleanType):
            self.isMultipart = BooleanType(self.isMultipart)

        if self.isRead is not None and not isinstance(self.isRead, BooleanType):
            self.isRead = BooleanType(self.isRead)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.receivedTime is not None and not isinstance(self.receivedTime, XSDDateTime):
            self.receivedTime = XSDDateTime(self.receivedTime)

        if self.sentTime is not None and not isinstance(self.sentTime, XSDDateTime):
            self.sentTime = XSDDateTime(self.sentTime)

        if self.body is not None and not isinstance(self.body, str):
            self.body = str(self.body)

        if self.contentDisposition is not None and not isinstance(self.contentDisposition, str):
            self.contentDisposition = str(self.contentDisposition)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        if self.inReplyTo is not None and not isinstance(self.inReplyTo, str):
            self.inReplyTo = str(self.inReplyTo)

        if self.messageID is not None and not isinstance(self.messageID, str):
            self.messageID = str(self.messageID)

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.xMailer is not None and not isinstance(self.xMailer, str):
            self.xMailer = str(self.xMailer)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if not isinstance(self.labels, list):
            self.labels = [self.labels] if self.labels is not None else []
        self.labels = [v if isinstance(v, str) else str(v) for v in self.labels]

        if not isinstance(self.receivedLines, list):
            self.receivedLines = [self.receivedLines] if self.receivedLines is not None else []
        self.receivedLines = [v if isinstance(v, str) else str(v) for v in self.receivedLines]

        super().__post_init__(**kwargs)


@dataclass
class EncodedStreamFacet(Facet):
    """
    "An encoded stream facet is a grouping of characteristics unique to the conversion of a body of data content from
    one form to another form."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EncodedStreamFacet
    class_class_curie: ClassVar[str] = "observable:EncodedStreamFacet"
    class_name: ClassVar[str] = "EncodedStreamFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EncodedStreamFacet

    encodingMethod: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.encodingMethod is not None and not isinstance(self.encodingMethod, str):
            self.encodingMethod = str(self.encodingMethod)

        super().__post_init__(**kwargs)


@dataclass
class EncryptedStreamFacet(Facet):
    """
    "An encrypted stream facet is a grouping of characteristics unique to the conversion of a body of data content
    from one form to another obfuscated form in such a way that reversing the conversion to obtain the original data
    form can only be accomplished through possession and use of a specific key."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EncryptedStreamFacet
    class_class_curie: ClassVar[str] = "observable:EncryptedStreamFacet"
    class_name: ClassVar[str] = "EncryptedStreamFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EncryptedStreamFacet

    encryptionMethod: Optional[str] = None
    encryptionMode: Optional[str] = None
    encryptionIV: Optional[Union[str, List[str]]] = empty_list()
    encryptionKey: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.encryptionMethod is not None and not isinstance(self.encryptionMethod, str):
            self.encryptionMethod = str(self.encryptionMethod)

        if self.encryptionMode is not None and not isinstance(self.encryptionMode, str):
            self.encryptionMode = str(self.encryptionMode)

        if not isinstance(self.encryptionIV, list):
            self.encryptionIV = [self.encryptionIV] if self.encryptionIV is not None else []
        self.encryptionIV = [v if isinstance(v, str) else str(v) for v in self.encryptionIV]

        if not isinstance(self.encryptionKey, list):
            self.encryptionKey = [self.encryptionKey] if self.encryptionKey is not None else []
        self.encryptionKey = [v if isinstance(v, str) else str(v) for v in self.encryptionKey]

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentVariable(UcoInherentCharacterizationThing):
    """
    "An environment variable is a grouping of characteristics unique to a dynamic-named value that can affect the way
    running processes will behave on a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EnvironmentVariable
    class_class_curie: ClassVar[str] = "observable:EnvironmentVariable"
    class_name: ClassVar[str] = "EnvironmentVariable"
    class_model_uri: ClassVar[URIRef] = MASTER.EnvironmentVariable

    name: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class EventRecordFacet(Facet):
    """
    "An event record facet is a grouping of characteristics unique to something that happens in a digital context
    (e.g., operating system events)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EventRecordFacet
    class_class_curie: ClassVar[str] = "observable:EventRecordFacet"
    class_name: ClassVar[str] = "EventRecordFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.EventRecordFacet

    cyberAction: Optional[Union[dict, "ObservableAction"]] = None
    account: Optional[Union[dict, "ObservableObject"]] = None
    application: Optional[Union[dict, "ObservableObject"]] = None
    eventRecordDevice: Optional[Union[dict, "ObservableObject"]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    eventID: Optional[str] = None
    eventRecordID: Optional[str] = None
    eventRecordRaw: Optional[str] = None
    eventRecordServiceName: Optional[str] = None
    eventRecordText: Optional[str] = None
    eventType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cyberAction is not None and not isinstance(self.cyberAction, ObservableAction):
            self.cyberAction = ObservableAction(**as_dict(self.cyberAction))

        if self.account is not None and not isinstance(self.account, ObservableObject):
            self.account = ObservableObject(**as_dict(self.account))

        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.eventRecordDevice is not None and not isinstance(self.eventRecordDevice, ObservableObject):
            self.eventRecordDevice = ObservableObject(**as_dict(self.eventRecordDevice))

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.eventID is not None and not isinstance(self.eventID, str):
            self.eventID = str(self.eventID)

        if self.eventRecordID is not None and not isinstance(self.eventRecordID, str):
            self.eventRecordID = str(self.eventRecordID)

        if self.eventRecordRaw is not None and not isinstance(self.eventRecordRaw, str):
            self.eventRecordRaw = str(self.eventRecordRaw)

        if self.eventRecordServiceName is not None and not isinstance(self.eventRecordServiceName, str):
            self.eventRecordServiceName = str(self.eventRecordServiceName)

        if self.eventRecordText is not None and not isinstance(self.eventRecordText, str):
            self.eventRecordText = str(self.eventRecordText)

        if self.eventType is not None and not isinstance(self.eventType, str):
            self.eventType = str(self.eventType)

        super().__post_init__(**kwargs)


@dataclass
class ExtInodeFacet(Facet):
    """
    "An extInode facet is a grouping of characteristics unique to a file system object (file, directory, etc.)
    conformant to the extended file system (EXT or related derivations) specification."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ExtInodeFacet
    class_class_curie: ClassVar[str] = "observable:ExtInodeFacet"
    class_name: ClassVar[str] = "ExtInodeFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ExtInodeFacet

    extDeletionTime: Optional[Union[str, XSDDateTime]] = None
    extInodeChangeTime: Optional[Union[str, XSDDateTime]] = None
    extFileType: Optional[int] = None
    extFlags: Optional[int] = None
    extHardLinkCount: Optional[int] = None
    extInodeID: Optional[int] = None
    extPermissions: Optional[int] = None
    extSGID: Optional[int] = None
    extSUID: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.extDeletionTime is not None and not isinstance(self.extDeletionTime, XSDDateTime):
            self.extDeletionTime = XSDDateTime(self.extDeletionTime)

        if self.extInodeChangeTime is not None and not isinstance(self.extInodeChangeTime, XSDDateTime):
            self.extInodeChangeTime = XSDDateTime(self.extInodeChangeTime)

        if self.extFileType is not None and not isinstance(self.extFileType, int):
            self.extFileType = int(self.extFileType)

        if self.extFlags is not None and not isinstance(self.extFlags, int):
            self.extFlags = int(self.extFlags)

        if self.extHardLinkCount is not None and not isinstance(self.extHardLinkCount, int):
            self.extHardLinkCount = int(self.extHardLinkCount)

        if self.extInodeID is not None and not isinstance(self.extInodeID, int):
            self.extInodeID = int(self.extInodeID)

        if self.extPermissions is not None and not isinstance(self.extPermissions, int):
            self.extPermissions = int(self.extPermissions)

        if self.extSGID is not None and not isinstance(self.extSGID, int):
            self.extSGID = int(self.extSGID)

        if self.extSUID is not None and not isinstance(self.extSUID, int):
            self.extSUID = int(self.extSUID)

        super().__post_init__(**kwargs)


@dataclass
class ExtractedString(UcoInherentCharacterizationThing):
    """
    "An extracted string is a grouping of characteristics unique to a series of characters pulled from an observable
    object."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ExtractedString
    class_class_curie: ClassVar[str] = "observable:ExtractedString"
    class_name: ClassVar[str] = "ExtractedString"
    class_model_uri: ClassVar[URIRef] = MASTER.ExtractedString

    length: Optional[int] = None
    byteStringValue: Optional[Union[str, Base64BinaryType]] = None
    encoding: Optional[str] = None
    englishTranslation: Optional[str] = None
    language: Optional[str] = None
    stringValue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.byteStringValue is not None and not isinstance(self.byteStringValue, Base64BinaryType):
            self.byteStringValue = Base64BinaryType(self.byteStringValue)

        if self.encoding is not None and not isinstance(self.encoding, str):
            self.encoding = str(self.encoding)

        if self.englishTranslation is not None and not isinstance(self.englishTranslation, str):
            self.englishTranslation = str(self.englishTranslation)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.stringValue is not None and not isinstance(self.stringValue, str):
            self.stringValue = str(self.stringValue)

        super().__post_init__(**kwargs)


@dataclass
class ExtractedStringsFacet(Facet):
    """
    "An extracted strings facet is a grouping of characteristics unique to one or more sequences of characters pulled
    from an observable object."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ExtractedStringsFacet
    class_class_curie: ClassVar[str] = "observable:ExtractedStringsFacet"
    class_name: ClassVar[str] = "ExtractedStringsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ExtractedStringsFacet

    strings: Optional[Union[Union[dict, ExtractedString], List[Union[dict, ExtractedString]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.strings, list):
            self.strings = [self.strings] if self.strings is not None else []
        self.strings = [v if isinstance(v, ExtractedString) else ExtractedString(**as_dict(v)) for v in self.strings]

        super().__post_init__(**kwargs)


@dataclass
class FileFacet(Facet):
    """
    "A file facet is a grouping of characteristics unique to the storage of a file (computer resource for recording
    data discretely in a computer storage device) on a file system (process that manages how and where data on a
    storage device is stored, accessed and managed). [based on https://en.wikipedia.org/computer_file and
    https://www.techopedia.com/definition/5510/file-system]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.FileFacet
    class_class_curie: ClassVar[str] = "observable:FileFacet"
    class_name: ClassVar[str] = "FileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.FileFacet

    isDirectory: Optional[Union[Union[bool, BooleanType], List[Union[bool, BooleanType]]]] = empty_list()
    accessedTime: Optional[Union[str, XSDDateTime]] = None
    metadataChangeTime: Optional[Union[str, XSDDateTime]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    sizeInBytes: Optional[int] = None
    allocationStatus: Optional[str] = None
    extension: Optional[str] = None
    fileName: Optional[Union[str, List[str]]] = empty_list()
    filePath: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.isDirectory, list):
            self.isDirectory = [self.isDirectory] if self.isDirectory is not None else []
        self.isDirectory = [v if isinstance(v, BooleanType) else BooleanType(v) for v in self.isDirectory]

        if self.accessedTime is not None and not isinstance(self.accessedTime, XSDDateTime):
            self.accessedTime = XSDDateTime(self.accessedTime)

        if self.metadataChangeTime is not None and not isinstance(self.metadataChangeTime, XSDDateTime):
            self.metadataChangeTime = XSDDateTime(self.metadataChangeTime)

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.sizeInBytes is not None and not isinstance(self.sizeInBytes, int):
            self.sizeInBytes = int(self.sizeInBytes)

        if self.allocationStatus is not None and not isinstance(self.allocationStatus, str):
            self.allocationStatus = str(self.allocationStatus)

        if self.extension is not None and not isinstance(self.extension, str):
            self.extension = str(self.extension)

        if not isinstance(self.fileName, list):
            self.fileName = [self.fileName] if self.fileName is not None else []
        self.fileName = [v if isinstance(v, str) else str(v) for v in self.fileName]

        if not isinstance(self.filePath, list):
            self.filePath = [self.filePath] if self.filePath is not None else []
        self.filePath = [v if isinstance(v, str) else str(v) for v in self.filePath]

        super().__post_init__(**kwargs)


@dataclass
class FilePermissionsFacet(Facet):
    """
    "A file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change,
    navigate, execute) of a file on a file system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.FilePermissionsFacet
    class_class_curie: ClassVar[str] = "observable:FilePermissionsFacet"
    class_name: ClassVar[str] = "FilePermissionsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.FilePermissionsFacet

    owner: Optional[Union[dict, UcoObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.owner is not None and not isinstance(self.owner, UcoObject):
            self.owner = UcoObject(**as_dict(self.owner))

        super().__post_init__(**kwargs)


@dataclass
class FileSystemFacet(Facet):
    """
    "A file system facet is a grouping of characteristics unique to the process that manages how and where data on a
    storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.FileSystemFacet
    class_class_curie: ClassVar[str] = "observable:FileSystemFacet"
    class_name: ClassVar[str] = "FileSystemFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.FileSystemFacet

    clusterSize: Optional[int] = None
    fileSystemType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.clusterSize is not None and not isinstance(self.clusterSize, int):
            self.clusterSize = int(self.clusterSize)

        if self.fileSystemType is not None and not isinstance(self.fileSystemType, str):
            self.fileSystemType = str(self.fileSystemType)

        super().__post_init__(**kwargs)


@dataclass
class FragmentFacet(Facet):
    """
    "A fragment facet is a grouping of characteristics unique to an individual piece of the content of a file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.FragmentFacet
    class_class_curie: ClassVar[str] = "observable:FragmentFacet"
    class_name: ClassVar[str] = "FragmentFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.FragmentFacet

    fragmentIndex: Optional[Union[int, List[int]]] = empty_list()
    totalFragments: Optional[Union[int, List[int]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.fragmentIndex, list):
            self.fragmentIndex = [self.fragmentIndex] if self.fragmentIndex is not None else []
        self.fragmentIndex = [v if isinstance(v, int) else int(v) for v in self.fragmentIndex]

        if not isinstance(self.totalFragments, list):
            self.totalFragments = [self.totalFragments] if self.totalFragments is not None else []
        self.totalFragments = [v if isinstance(v, int) else int(v) for v in self.totalFragments]

        super().__post_init__(**kwargs)


@dataclass
class GeoLocationEntryFacet(Facet):
    """
    "A geolocation entry facet is a grouping of characteristics unique to a single application-specific geolocation
    entry."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GeoLocationEntryFacet
    class_class_curie: ClassVar[str] = "observable:GeoLocationEntryFacet"
    class_name: ClassVar[str] = "GeoLocationEntryFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.GeoLocationEntryFacet

    location: Optional[Union[dict, Location]] = None
    application: Optional[Union[dict, "ObservableObject"]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.location is not None and not isinstance(self.location, Location):
            self.location = Location(**as_dict(self.location))

        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        super().__post_init__(**kwargs)


@dataclass
class GeoLocationLogFacet(Facet):
    """
    "A geolocation log facet is a grouping of characteristics unique to a record containing geolocation tracks and/or
    geolocation entries."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GeoLocationLogFacet
    class_class_curie: ClassVar[str] = "observable:GeoLocationLogFacet"
    class_name: ClassVar[str] = "GeoLocationLogFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.GeoLocationLogFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        super().__post_init__(**kwargs)


@dataclass
class GeoLocationTrackFacet(Facet):
    """
    "A geolocation track facet is a grouping of characteristics unique to a set of contiguous geolocation entries
    representing a path/track taken."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GeoLocationTrackFacet
    class_class_curie: ClassVar[str] = "observable:GeoLocationTrackFacet"
    class_name: ClassVar[str] = "GeoLocationTrackFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.GeoLocationTrackFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    geoLocationEntry: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if not isinstance(self.geoLocationEntry, list):
            self.geoLocationEntry = [self.geoLocationEntry] if self.geoLocationEntry is not None else []
        self.geoLocationEntry = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.geoLocationEntry]

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        super().__post_init__(**kwargs)


@dataclass
class GlobalFlagType(UcoInherentCharacterizationThing):
    """
    'A globalFlagType is a grouping of characteristics unique to the Windows systemwide global variable named
    NtGlobalFlag that enables various internal debugging, tracing, and validation support in the operating system.
    [based on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals by Solomon, Russinovich, and
    Ionescu]'
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GlobalFlagType
    class_class_curie: ClassVar[str] = "observable:GlobalFlagType"
    class_name: ClassVar[str] = "GlobalFlagType"
    class_model_uri: ClassVar[URIRef] = MASTER.GlobalFlagType

    hexadecimalValue: Optional[Union[hex, List[hex]]] = empty_list()
    abbreviation: Optional[str] = None
    destination: Optional[str] = None
    symbolicName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.hexadecimalValue, list):
            self.hexadecimalValue = [self.hexadecimalValue] if self.hexadecimalValue is not None else []
        self.hexadecimalValue = [v if isinstance(v, hex) else hex(v) for v in self.hexadecimalValue]

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if self.destination is not None and not isinstance(self.destination, str):
            self.destination = str(self.destination)

        if self.symbolicName is not None and not isinstance(self.symbolicName, str):
            self.symbolicName = str(self.symbolicName)

        super().__post_init__(**kwargs)


@dataclass
class HTTPConnectionFacet(Facet):
    """
    "An HTTP connection facet is a grouping of characteristics unique to portions of a network connection that are
    conformant to the Hypertext Transfer Protocol (HTTP) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.HTTPConnectionFacet
    class_class_curie: ClassVar[str] = "observable:HTTPConnectionFacet"
    class_name: ClassVar[str] = "HTTPConnectionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.HTTPConnectionFacet

    httpMessageBodyData: Optional[Union[dict, "ObservableObject"]] = None
    httpMessageBodyLength: Optional[int] = None
    httpRequestHeader: Optional[Union[dict, "Dictionary"]] = None
    requestMethod: Optional[str] = None
    requestValue: Optional[str] = None
    requestVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.httpMessageBodyData is not None and not isinstance(self.httpMessageBodyData, ObservableObject):
            self.httpMessageBodyData = ObservableObject(**as_dict(self.httpMessageBodyData))

        if self.httpMessageBodyLength is not None and not isinstance(self.httpMessageBodyLength, int):
            self.httpMessageBodyLength = int(self.httpMessageBodyLength)

        if self.httpRequestHeader is not None and not isinstance(self.httpRequestHeader, Dictionary):
            self.httpRequestHeader = Dictionary(**as_dict(self.httpRequestHeader))

        if self.requestMethod is not None and not isinstance(self.requestMethod, str):
            self.requestMethod = str(self.requestMethod)

        if self.requestValue is not None and not isinstance(self.requestValue, str):
            self.requestValue = str(self.requestValue)

        if self.requestVersion is not None and not isinstance(self.requestVersion, str):
            self.requestVersion = str(self.requestVersion)

        super().__post_init__(**kwargs)


@dataclass
class ICMPConnectionFacet(Facet):
    """
    "An ICMP connection facet is a grouping of characteristics unique to portions of a network connection that are
    conformant to the Internet Control message Protocol (ICMP) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ICMPConnectionFacet
    class_class_curie: ClassVar[str] = "observable:ICMPConnectionFacet"
    class_name: ClassVar[str] = "ICMPConnectionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ICMPConnectionFacet

    icmpCode: Optional[Union[hex, List[hex]]] = empty_list()
    icmpType: Optional[Union[hex, List[hex]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.icmpCode, list):
            self.icmpCode = [self.icmpCode] if self.icmpCode is not None else []
        self.icmpCode = [v if isinstance(v, hex) else hex(v) for v in self.icmpCode]

        if not isinstance(self.icmpType, list):
            self.icmpType = [self.icmpType] if self.icmpType is not None else []
        self.icmpType = [v if isinstance(v, hex) else hex(v) for v in self.icmpType]

        super().__post_init__(**kwargs)


@dataclass
class IComHandlerActionType(UcoInherentCharacterizationThing):
    """
    "An IComHandler action type is a grouping of characteristics unique to a Windows Task-related action that fires a
    Windows COM handler (smart code in the client address space that can optimize calls between a client and server).
    [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IComHandlerActionType
    class_class_curie: ClassVar[str] = "observable:IComHandlerActionType"
    class_name: ClassVar[str] = "IComHandlerActionType"
    class_model_uri: ClassVar[URIRef] = MASTER.IComHandlerActionType

    comClassID: Optional[str] = None
    comData: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.comClassID is not None and not isinstance(self.comClassID, str):
            self.comClassID = str(self.comClassID)

        if self.comData is not None and not isinstance(self.comData, str):
            self.comData = str(self.comData)

        super().__post_init__(**kwargs)


@dataclass
class IExecActionType(UcoInherentCharacterizationThing):
    """
    "An IExec action type is a grouping of characteristics unique to an action that executes a command-line operation
    on a Windows operating system. [based on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IExecActionType
    class_class_curie: ClassVar[str] = "observable:IExecActionType"
    class_name: ClassVar[str] = "IExecActionType"
    class_model_uri: ClassVar[URIRef] = MASTER.IExecActionType

    execProgramHashes: Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]] = empty_list()
    execArguments: Optional[str] = None
    execProgramPath: Optional[str] = None
    execWorkingDirectory: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="execProgramHashes", slot_type=Hash, key_name="hashValue", keyed=False)

        if self.execArguments is not None and not isinstance(self.execArguments, str):
            self.execArguments = str(self.execArguments)

        if self.execProgramPath is not None and not isinstance(self.execProgramPath, str):
            self.execProgramPath = str(self.execProgramPath)

        if self.execWorkingDirectory is not None and not isinstance(self.execWorkingDirectory, str):
            self.execWorkingDirectory = str(self.execWorkingDirectory)

        super().__post_init__(**kwargs)


class IPAddressFacet(DigitalAddressFacet):
    """
    "An IP address facet is a grouping of characteristics unique to an Internet Protocol (IP) standards conformant
    identifier assigned to a device to enable routing and management of IP standards conformant communication to or
    from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPAddressFacet
    class_class_curie: ClassVar[str] = "observable:IPAddressFacet"
    class_name: ClassVar[str] = "IPAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.IPAddressFacet


class IPv4AddressFacet(IPAddressFacet):
    """
    "An IPv4 (Internet Protocol version 4) address facet is a grouping of characteristics unique to an IPv4 standards
    conformant identifier assigned to a device to enable routing and management of IPv4 standards conformant
    communication to or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPv4AddressFacet
    class_class_curie: ClassVar[str] = "observable:IPv4AddressFacet"
    class_name: ClassVar[str] = "IPv4AddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.IPv4AddressFacet


class IPv6AddressFacet(IPAddressFacet):
    """
    "An IPv6 (Internet Protocol version 6) address facet is a grouping of characteristics unique to an IPv6 standards
    conformant identifier assigned to a device to enable routing and management of IPv6 standards conformant
    communication to or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPv6AddressFacet
    class_class_curie: ClassVar[str] = "observable:IPv6AddressFacet"
    class_name: ClassVar[str] = "IPv6AddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.IPv6AddressFacet


@dataclass
class IShowMessageActionType(UcoInherentCharacterizationThing):
    """
    "An IShow message action type is a grouping of characteristics unique to an action that shows a message box when a
    task is activate. [based on
    https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IShowMessageActionType
    class_class_curie: ClassVar[str] = "observable:IShowMessageActionType"
    class_name: ClassVar[str] = "IShowMessageActionType"
    class_model_uri: ClassVar[URIRef] = MASTER.IShowMessageActionType

    showMessageBody: Optional[str] = None
    showMessageTitle: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.showMessageBody is not None and not isinstance(self.showMessageBody, str):
            self.showMessageBody = str(self.showMessageBody)

        if self.showMessageTitle is not None and not isinstance(self.showMessageTitle, str):
            self.showMessageTitle = str(self.showMessageTitle)

        super().__post_init__(**kwargs)


@dataclass
class ImageFacet(Facet):
    """
    "An image facet is a grouping of characteristics unique to a complete copy of a hard disk, memory, or other
    digital media."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ImageFacet
    class_class_curie: ClassVar[str] = "observable:ImageFacet"
    class_name: ClassVar[str] = "ImageFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ImageFacet

    imageType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.imageType is not None and not isinstance(self.imageType, str):
            self.imageType = str(self.imageType)

        super().__post_init__(**kwargs)


class InstantMessagingAddressFacet(DigitalAddressFacet):
    """
    "An instant messagingAddress facet is a grouping of characteristics unique to an identifier assigned to enable
    routing and management of instant messaging digital communication."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.InstantMessagingAddressFacet
    class_class_curie: ClassVar[str] = "observable:InstantMessagingAddressFacet"
    class_name: ClassVar[str] = "InstantMessagingAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.InstantMessagingAddressFacet


@dataclass
class LibraryFacet(Facet):
    """
    "A library facet is a grouping of characteristics unique to a suite of data and programming code that is used to
    develop software programs and applications. [based on
    https://www.techopedia.com/definition/3828/software-library]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.LibraryFacet
    class_class_curie: ClassVar[str] = "observable:LibraryFacet"
    class_name: ClassVar[str] = "LibraryFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.LibraryFacet

    libraryType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.libraryType is not None and not isinstance(self.libraryType, str):
            self.libraryType = str(self.libraryType)

        super().__post_init__(**kwargs)


class MACAddressFacet(DigitalAddressFacet):
    """
    "A MAC address facet is a grouping of characteristics unique to a media access control standards conformant
    identifier assigned to a networkInterface to enable routing and management of communications at the data link
    layer of a network segment."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MACAddressFacet
    class_class_curie: ClassVar[str] = "observable:MACAddressFacet"
    class_name: ClassVar[str] = "MACAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MACAddressFacet


class BluetoothAddressFacet(MACAddressFacet):
    """
    "A Bluetooth address facet is a grouping of characteristics unique to a Bluetooth standard conformant identifier
    assigned to a Bluetooth device to enable routing and management of Bluetooth standards conformant communication to
    or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BluetoothAddressFacet
    class_class_curie: ClassVar[str] = "observable:BluetoothAddressFacet"
    class_name: ClassVar[str] = "BluetoothAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.BluetoothAddressFacet


@dataclass
class MemoryFacet(Facet):
    """
    "A memory facet is a grouping of characteristics unique to a particular region of temporary information storage
    (e.g., RAM (random access memory), ROM (read only memory)) on a digital device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MemoryFacet
    class_class_curie: ClassVar[str] = "observable:MemoryFacet"
    class_name: ClassVar[str] = "MemoryFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MemoryFacet

    isInjected: Optional[Union[bool, BooleanType]] = None
    isMapped: Optional[Union[bool, BooleanType]] = None
    isProtected: Optional[Union[bool, BooleanType]] = None
    isVolatile: Optional[Union[bool, BooleanType]] = None
    regionEndAddress: Optional[Union[hex, List[hex]]] = empty_list()
    regionStartAddress: Optional[Union[hex, List[hex]]] = empty_list()
    regionSize: Optional[int] = None
    blockType: Optional[Union[str, "MemoryBlockTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isInjected is not None and not isinstance(self.isInjected, BooleanType):
            self.isInjected = BooleanType(self.isInjected)

        if self.isMapped is not None and not isinstance(self.isMapped, BooleanType):
            self.isMapped = BooleanType(self.isMapped)

        if self.isProtected is not None and not isinstance(self.isProtected, BooleanType):
            self.isProtected = BooleanType(self.isProtected)

        if self.isVolatile is not None and not isinstance(self.isVolatile, BooleanType):
            self.isVolatile = BooleanType(self.isVolatile)

        if not isinstance(self.regionEndAddress, list):
            self.regionEndAddress = [self.regionEndAddress] if self.regionEndAddress is not None else []
        self.regionEndAddress = [v if isinstance(v, hex) else hex(v) for v in self.regionEndAddress]

        if not isinstance(self.regionStartAddress, list):
            self.regionStartAddress = [self.regionStartAddress] if self.regionStartAddress is not None else []
        self.regionStartAddress = [v if isinstance(v, hex) else hex(v) for v in self.regionStartAddress]

        if self.regionSize is not None and not isinstance(self.regionSize, int):
            self.regionSize = int(self.regionSize)

        if self.blockType is not None and not isinstance(self.blockType, MemoryBlockTypeEnum):
            self.blockType = MemoryBlockTypeEnum(self.blockType)

        super().__post_init__(**kwargs)


@dataclass
class MessageFacet(Facet):
    """
    "A message facet is a grouping of characteristics unique to a discrete unit of electronic communication intended
    by the source for consumption by some recipient or group of recipients. [based on
    https://en.wikipedia.org/wiki/message]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MessageFacet
    class_class_curie: ClassVar[str] = "observable:MessageFacet"
    class_name: ClassVar[str] = "MessageFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MessageFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    from: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    to: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    sentTime: Optional[Union[str, XSDDateTime]] = None
    messageID: Optional[str] = None
    messageText: Optional[str] = None
    messageType: Optional[str] = None
    sessionID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if not isinstance(self.from, list):
            self.from = [self.from] if self.from is not None else []
        self.from = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.from]

        if not isinstance(self.to, list):
            self.to = [self.to] if self.to is not None else []
        self.to = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.to]

        if self.sentTime is not None and not isinstance(self.sentTime, XSDDateTime):
            self.sentTime = XSDDateTime(self.sentTime)

        if self.messageID is not None and not isinstance(self.messageID, str):
            self.messageID = str(self.messageID)

        if self.messageText is not None and not isinstance(self.messageText, str):
            self.messageText = str(self.messageText)

        if self.messageType is not None and not isinstance(self.messageType, str):
            self.messageType = str(self.messageType)

        if self.sessionID is not None and not isinstance(self.sessionID, str):
            self.sessionID = str(self.sessionID)

        super().__post_init__(**kwargs)


@dataclass
class MessageThreadFacet(Facet):
    """
    "A messageThread facet is a grouping of characteristics unique to a running commentary of electronic messages
    pertaining to one topic or question."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MessageThreadFacet
    class_class_curie: ClassVar[str] = "observable:MessageThreadFacet"
    class_name: ClassVar[str] = "MessageThreadFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MessageThreadFacet

    messageThreadOrderedItems: Optional[Union[dict, "Thread"]] = None
    messageThreadOriginItems: Optional[Union[dict, "Thread"]] = None
    messageThreadTerminalItems: Optional[Union[dict, "Thread"]] = None
    messageThreadUnorderedItems: Optional[Union[dict, "Thread"]] = None
    participant: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    messageThread: Optional[Union[dict, "Thread"]] = None
    visibility: Optional[Union[bool, BooleanType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.messageThreadOrderedItems is not None and not isinstance(self.messageThreadOrderedItems, Thread):
            self.messageThreadOrderedItems = Thread(**as_dict(self.messageThreadOrderedItems))

        if self.messageThreadOriginItems is not None and not isinstance(self.messageThreadOriginItems, Thread):
            self.messageThreadOriginItems = Thread(**as_dict(self.messageThreadOriginItems))

        if self.messageThreadTerminalItems is not None and not isinstance(self.messageThreadTerminalItems, Thread):
            self.messageThreadTerminalItems = Thread(**as_dict(self.messageThreadTerminalItems))

        if self.messageThreadUnorderedItems is not None and not isinstance(self.messageThreadUnorderedItems, Thread):
            self.messageThreadUnorderedItems = Thread(**as_dict(self.messageThreadUnorderedItems))

        if not isinstance(self.participant, list):
            self.participant = [self.participant] if self.participant is not None else []
        self.participant = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.participant]

        if self.messageThread is not None and not isinstance(self.messageThread, Thread):
            self.messageThread = Thread(**as_dict(self.messageThread))

        if self.visibility is not None and not isinstance(self.visibility, BooleanType):
            self.visibility = BooleanType(self.visibility)

        super().__post_init__(**kwargs)


@dataclass
class MftRecordFacet(Facet):
    """
    "An MFT record facet is a grouping of characteristics unique to the details of a single file as managed in an NTFS
    (new technology filesystem) master file table (which is a collection of information about all files on an NTFS
    filesystem). [based on https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MftRecordFacet
    class_class_curie: ClassVar[str] = "observable:MftRecordFacet"
    class_name: ClassVar[str] = "MftRecordFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MftRecordFacet

    mftFileNameAccessedTime: Optional[Union[str, XSDDateTime]] = None
    mftFileNameCreatedTime: Optional[Union[str, XSDDateTime]] = None
    mftFileNameModifiedTime: Optional[Union[str, XSDDateTime]] = None
    mftFileNameRecordChangeTme: Optional[Union[str, XSDDateTime]] = None
    mftRecordChangeTime: Optional[Union[str, XSDDateTime]] = None
    mftFileID: Optional[int] = None
    mftFileNameLength: Optional[int] = None
    mftFlags: Optional[int] = None
    mftParentID: Optional[int] = None
    ntfsHardLinkCount: Optional[int] = None
    ntfsOwnerID: Optional[str] = None
    ntfsOwnerSID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mftFileNameAccessedTime is not None and not isinstance(self.mftFileNameAccessedTime, XSDDateTime):
            self.mftFileNameAccessedTime = XSDDateTime(self.mftFileNameAccessedTime)

        if self.mftFileNameCreatedTime is not None and not isinstance(self.mftFileNameCreatedTime, XSDDateTime):
            self.mftFileNameCreatedTime = XSDDateTime(self.mftFileNameCreatedTime)

        if self.mftFileNameModifiedTime is not None and not isinstance(self.mftFileNameModifiedTime, XSDDateTime):
            self.mftFileNameModifiedTime = XSDDateTime(self.mftFileNameModifiedTime)

        if self.mftFileNameRecordChangeTme is not None and not isinstance(self.mftFileNameRecordChangeTme, XSDDateTime):
            self.mftFileNameRecordChangeTme = XSDDateTime(self.mftFileNameRecordChangeTme)

        if self.mftRecordChangeTime is not None and not isinstance(self.mftRecordChangeTime, XSDDateTime):
            self.mftRecordChangeTime = XSDDateTime(self.mftRecordChangeTime)

        if self.mftFileID is not None and not isinstance(self.mftFileID, int):
            self.mftFileID = int(self.mftFileID)

        if self.mftFileNameLength is not None and not isinstance(self.mftFileNameLength, int):
            self.mftFileNameLength = int(self.mftFileNameLength)

        if self.mftFlags is not None and not isinstance(self.mftFlags, int):
            self.mftFlags = int(self.mftFlags)

        if self.mftParentID is not None and not isinstance(self.mftParentID, int):
            self.mftParentID = int(self.mftParentID)

        if self.ntfsHardLinkCount is not None and not isinstance(self.ntfsHardLinkCount, int):
            self.ntfsHardLinkCount = int(self.ntfsHardLinkCount)

        if self.ntfsOwnerID is not None and not isinstance(self.ntfsOwnerID, str):
            self.ntfsOwnerID = str(self.ntfsOwnerID)

        if self.ntfsOwnerSID is not None and not isinstance(self.ntfsOwnerSID, str):
            self.ntfsOwnerSID = str(self.ntfsOwnerSID)

        super().__post_init__(**kwargs)


@dataclass
class MimePartType(UcoInherentCharacterizationThing):
    """
    "A mime part type is a grouping of characteristics unique to a component of a multi-part email body."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MimePartType
    class_class_curie: ClassVar[str] = "observable:MimePartType"
    class_name: ClassVar[str] = "MimePartType"
    class_model_uri: ClassVar[URIRef] = MASTER.MimePartType

    bodyRaw: Optional[Union[dict, "ObservableObject"]] = None
    body: Optional[str] = None
    contentDisposition: Optional[str] = None
    contentType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.bodyRaw is not None and not isinstance(self.bodyRaw, ObservableObject):
            self.bodyRaw = ObservableObject(**as_dict(self.bodyRaw))

        if self.body is not None and not isinstance(self.body, str):
            self.body = str(self.body)

        if self.contentDisposition is not None and not isinstance(self.contentDisposition, str):
            self.contentDisposition = str(self.contentDisposition)

        if self.contentType is not None and not isinstance(self.contentType, str):
            self.contentType = str(self.contentType)

        super().__post_init__(**kwargs)


@dataclass
class MobileAccountFacet(Facet):
    """
    "A mobile account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of some capability or service on a portable computing device. [based on
    https://www.lexico.com/definition/mobile_device]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MobileAccountFacet
    class_class_curie: ClassVar[str] = "observable:MobileAccountFacet"
    class_name: ClassVar[str] = "MobileAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MobileAccountFacet

    IMSI: Optional[str] = None
    MSISDN: Optional[str] = None
    MSISDNType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.IMSI is not None and not isinstance(self.IMSI, str):
            self.IMSI = str(self.IMSI)

        if self.MSISDN is not None and not isinstance(self.MSISDN, str):
            self.MSISDN = str(self.MSISDN)

        if self.MSISDNType is not None and not isinstance(self.MSISDNType, str):
            self.MSISDNType = str(self.MSISDNType)

        super().__post_init__(**kwargs)


@dataclass
class MobileDeviceFacet(Facet):
    """
    "A mobile device facet is a grouping of characteristics unique to a portable computing device. [based on
    https://www.lexico.com/definition/mobile_device]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MobileDeviceFacet
    class_class_curie: ClassVar[str] = "observable:MobileDeviceFacet"
    class_name: ClassVar[str] = "MobileDeviceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MobileDeviceFacet

    mockLocationsAllowed: Optional[Union[bool, BooleanType]] = None
    clockSetting: Optional[Union[str, XSDDateTime]] = None
    phoneActivationTime: Optional[Union[str, XSDDateTime]] = None
    storageCapacityInBytes: Optional[int] = None
    ESN: Optional[str] = None
    IMEI: Optional[str] = None
    bluetoothDeviceName: Optional[str] = None
    keypadUnlockCode: Optional[str] = None
    network: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mockLocationsAllowed is not None and not isinstance(self.mockLocationsAllowed, BooleanType):
            self.mockLocationsAllowed = BooleanType(self.mockLocationsAllowed)

        if self.clockSetting is not None and not isinstance(self.clockSetting, XSDDateTime):
            self.clockSetting = XSDDateTime(self.clockSetting)

        if self.phoneActivationTime is not None and not isinstance(self.phoneActivationTime, XSDDateTime):
            self.phoneActivationTime = XSDDateTime(self.phoneActivationTime)

        if self.storageCapacityInBytes is not None and not isinstance(self.storageCapacityInBytes, int):
            self.storageCapacityInBytes = int(self.storageCapacityInBytes)

        if self.ESN is not None and not isinstance(self.ESN, str):
            self.ESN = str(self.ESN)

        if self.IMEI is not None and not isinstance(self.IMEI, str):
            self.IMEI = str(self.IMEI)

        if self.bluetoothDeviceName is not None and not isinstance(self.bluetoothDeviceName, str):
            self.bluetoothDeviceName = str(self.bluetoothDeviceName)

        if self.keypadUnlockCode is not None and not isinstance(self.keypadUnlockCode, str):
            self.keypadUnlockCode = str(self.keypadUnlockCode)

        if self.network is not None and not isinstance(self.network, str):
            self.network = str(self.network)

        super().__post_init__(**kwargs)


@dataclass
class MutexFacet(Facet):
    """
    "A mutex facet is a grouping of characteristics unique to a mechanism that enforces limits on access to a resource
    when there are many threads of execution. A mutex is designed to enforce a mutual exclusion concurrency control
    policy, and with a variety of possible methods there exists multiple unique implementations for different
    applications. [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MutexFacet
    class_class_curie: ClassVar[str] = "observable:MutexFacet"
    class_name: ClassVar[str] = "MutexFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.MutexFacet

    isNamed: Optional[Union[bool, BooleanType]] = None
    mutexName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isNamed is not None and not isinstance(self.isNamed, BooleanType):
            self.isNamed = BooleanType(self.isNamed)

        if self.mutexName is not None and not isinstance(self.mutexName, str):
            self.mutexName = str(self.mutexName)

        super().__post_init__(**kwargs)


@dataclass
class NTFSFileFacet(Facet):
    """
    "An NTFS file facet is a grouping of characteristics unique to a file on an NTFS (new technology filesystem) file
    system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NTFSFileFacet
    class_class_curie: ClassVar[str] = "observable:NTFSFileFacet"
    class_name: ClassVar[str] = "NTFSFileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NTFSFileFacet

    alternateDataStreams: Optional[Union[Union[dict, AlternateDataStream], List[Union[dict, AlternateDataStream]]]] = empty_list()
    entryID: Optional[int] = None
    sid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.alternateDataStreams, list):
            self.alternateDataStreams = [self.alternateDataStreams] if self.alternateDataStreams is not None else []
        self.alternateDataStreams = [v if isinstance(v, AlternateDataStream) else AlternateDataStream(**as_dict(v)) for v in self.alternateDataStreams]

        if self.entryID is not None and not isinstance(self.entryID, int):
            self.entryID = int(self.entryID)

        if self.sid is not None and not isinstance(self.sid, str):
            self.sid = str(self.sid)

        super().__post_init__(**kwargs)


class NTFSFilePermissionsFacet(Facet):
    """
    "An NTFS file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change,
    navigate, execute) of a file on an NTFS (new technology filesystem) file system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NTFSFilePermissionsFacet
    class_class_curie: ClassVar[str] = "observable:NTFSFilePermissionsFacet"
    class_name: ClassVar[str] = "NTFSFilePermissionsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NTFSFilePermissionsFacet


@dataclass
class NetworkConnectionFacet(Facet):
    """
    "A network connection facet is a grouping of characteristics unique to a connection (complete or attempted)
    accross a digital network (a group of two or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkConnectionFacet
    class_class_curie: ClassVar[str] = "observable:NetworkConnectionFacet"
    class_name: ClassVar[str] = "NetworkConnectionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkConnectionFacet

    src: Optional[Union[Union[dict, UcoObject], List[Union[dict, UcoObject]]]] = empty_list()
    dst: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    protocols: Optional[Union[dict, "ControlledDictionary"]] = None
    isActive: Optional[Union[bool, BooleanType]] = None
    endTime: Optional[Union[str, XSDDateTime]] = None
    startTime: Optional[Union[str, XSDDateTime]] = None
    destinationPort: Optional[int] = None
    sourcePort: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.src, list):
            self.src = [self.src] if self.src is not None else []
        self.src = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.src]

        if not isinstance(self.dst, list):
            self.dst = [self.dst] if self.dst is not None else []
        self.dst = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.dst]

        if self.protocols is not None and not isinstance(self.protocols, ControlledDictionary):
            self.protocols = ControlledDictionary(**as_dict(self.protocols))

        if self.isActive is not None and not isinstance(self.isActive, BooleanType):
            self.isActive = BooleanType(self.isActive)

        if self.endTime is not None and not isinstance(self.endTime, XSDDateTime):
            self.endTime = XSDDateTime(self.endTime)

        if self.startTime is not None and not isinstance(self.startTime, XSDDateTime):
            self.startTime = XSDDateTime(self.startTime)

        if self.destinationPort is not None and not isinstance(self.destinationPort, int):
            self.destinationPort = int(self.destinationPort)

        if self.sourcePort is not None and not isinstance(self.sourcePort, int):
            self.sourcePort = int(self.sourcePort)

        super().__post_init__(**kwargs)


@dataclass
class NetworkFlowFacet(Facet):
    """
    "A network flow facet is a grouping of characteristics unique to a sequence of data transiting one or more digital
    network (a group of two or more computer systems linked together) connections. [based on
    https://www.webopedia.com/TERM/N/network.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkFlowFacet
    class_class_curie: ClassVar[str] = "observable:NetworkFlowFacet"
    class_name: ClassVar[str] = "NetworkFlowFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkFlowFacet

    dstPayload: Optional[Union[dict, "ObservableObject"]] = None
    srcPayload: Optional[Union[dict, "ObservableObject"]] = None
    ipfix: Optional[Union[dict, "Dictionary"]] = None
    dstBytes: Optional[int] = None
    dstPackets: Optional[int] = None
    srcBytes: Optional[int] = None
    srcPackets: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dstPayload is not None and not isinstance(self.dstPayload, ObservableObject):
            self.dstPayload = ObservableObject(**as_dict(self.dstPayload))

        if self.srcPayload is not None and not isinstance(self.srcPayload, ObservableObject):
            self.srcPayload = ObservableObject(**as_dict(self.srcPayload))

        if self.ipfix is not None and not isinstance(self.ipfix, Dictionary):
            self.ipfix = Dictionary(**as_dict(self.ipfix))

        if self.dstBytes is not None and not isinstance(self.dstBytes, int):
            self.dstBytes = int(self.dstBytes)

        if self.dstPackets is not None and not isinstance(self.dstPackets, int):
            self.dstPackets = int(self.dstPackets)

        if self.srcBytes is not None and not isinstance(self.srcBytes, int):
            self.srcBytes = int(self.srcBytes)

        if self.srcPackets is not None and not isinstance(self.srcPackets, int):
            self.srcPackets = int(self.srcPackets)

        super().__post_init__(**kwargs)


@dataclass
class NetworkInterfaceFacet(Facet):
    """
    "A networkInterface facet is a grouping of characteristics unique to a software or hardware interface between two
    pieces of equipment or protocol layers in a computer network."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkInterfaceFacet
    class_class_curie: ClassVar[str] = "observable:NetworkInterfaceFacet"
    class_name: ClassVar[str] = "NetworkInterfaceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkInterfaceFacet

    macAddress: Optional[Union[dict, "ObservableObject"]] = None
    dhcpServer: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    ip: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    ipGateway: Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]] = empty_list()
    dhcpLeaseExpires: Optional[Union[str, XSDDateTime]] = None
    dhcpLeaseObtained: Optional[Union[str, XSDDateTime]] = None
    adapterName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.macAddress is not None and not isinstance(self.macAddress, ObservableObject):
            self.macAddress = ObservableObject(**as_dict(self.macAddress))

        if not isinstance(self.dhcpServer, list):
            self.dhcpServer = [self.dhcpServer] if self.dhcpServer is not None else []
        self.dhcpServer = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.dhcpServer]

        if not isinstance(self.ip, list):
            self.ip = [self.ip] if self.ip is not None else []
        self.ip = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.ip]

        if not isinstance(self.ipGateway, list):
            self.ipGateway = [self.ipGateway] if self.ipGateway is not None else []
        self.ipGateway = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.ipGateway]

        if self.dhcpLeaseExpires is not None and not isinstance(self.dhcpLeaseExpires, XSDDateTime):
            self.dhcpLeaseExpires = XSDDateTime(self.dhcpLeaseExpires)

        if self.dhcpLeaseObtained is not None and not isinstance(self.dhcpLeaseObtained, XSDDateTime):
            self.dhcpLeaseObtained = XSDDateTime(self.dhcpLeaseObtained)

        if self.adapterName is not None and not isinstance(self.adapterName, str):
            self.adapterName = str(self.adapterName)

        super().__post_init__(**kwargs)


class NetworkSocketAddressFamily(YAMLRoot):
    """
    "The address family parameter on a socket() API determines the format of the address structure to be used on
    socket APIs."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkSocketAddressFamily
    class_class_curie: ClassVar[str] = "observable:NetworkSocketAddressFamily"
    class_name: ClassVar[str] = "NetworkSocketAddressFamily"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkSocketAddressFamily


class NetworkSocketProtocolFamily(YAMLRoot):
    """
    "The protocol family specifies the protocol scheme that is used by the Socket class to resolve an address."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkSocketProtocolFamily
    class_class_curie: ClassVar[str] = "observable:NetworkSocketProtocolFamily"
    class_name: ClassVar[str] = "NetworkSocketProtocolFamily"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkSocketProtocolFamily


class NetworkSocketType(YAMLRoot):
    """
    "Depending on the type and importance of data exchanged between the applications via sockets, different types of
    network sockets are implemented."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkSocketType
    class_class_curie: ClassVar[str] = "observable:NetworkSocketType"
    class_name: ClassVar[str] = "NetworkSocketType"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkSocketType


@dataclass
class NoteFacet(Facet):
    """
    "A note facet is a grouping of characteristics unique to a brief textual record."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NoteFacet
    class_class_curie: ClassVar[str] = "observable:NoteFacet"
    class_name: ClassVar[str] = "NoteFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.NoteFacet

    application: Optional[Union[dict, "ObservableObject"]] = None
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


class Observable(UcoObject):
    """
    "An observable is a characterizable item or action within the digital domain."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Observable
    class_class_curie: ClassVar[str] = "observable:Observable"
    class_name: ClassVar[str] = "Observable"
    class_model_uri: ClassVar[URIRef] = MASTER.Observable


class ObservableAction(Action):
    """
    "An observable action is a grouping of characteristics unique to something that may be done or performed within
    the digital domain."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ObservableAction
    class_class_curie: ClassVar[str] = "observable:ObservableAction"
    class_name: ClassVar[str] = "ObservableAction"
    class_model_uri: ClassVar[URIRef] = MASTER.ObservableAction


class ObservablePattern(Observable):
    """
    "An observable pattern is a grouping of characteristics unique to a logical pattern composed of observable object
    and observable action properties."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ObservablePattern
    class_class_curie: ClassVar[str] = "observable:ObservablePattern"
    class_name: ClassVar[str] = "ObservablePattern"
    class_model_uri: ClassVar[URIRef] = MASTER.ObservablePattern


@dataclass
class ObservableRelationship(Relationship):
    """
    "An observable relationship is a grouping of characteristics unique to an assertion of an association between two
    observable objects."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ObservableRelationship
    class_class_curie: ClassVar[str] = "observable:ObservableRelationship"
    class_name: ClassVar[str] = "ObservableRelationship"
    class_model_uri: ClassVar[URIRef] = MASTER.ObservableRelationship

    isDirectional: Union[bool, BooleanType] = None
    source: Union[Union[dict, UcoObject], List[Union[dict, UcoObject]]] = None
    target: Union[dict, UcoObject] = None

@dataclass
class Observation(Action):
    """
    "An observation is a temporal perception of an observable."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Observation
    class_class_curie: ClassVar[str] = "observable:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = MASTER.Observation

    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class OnlineServiceFacet(Facet):
    """
    "An online service facet is a grouping of characteristics unique to a particular provision mechanism of
    information access, distribution or manipulation over the Internet"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.OnlineServiceFacet
    class_class_curie: ClassVar[str] = "observable:OnlineServiceFacet"
    class_name: ClassVar[str] = "OnlineServiceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.OnlineServiceFacet

    location: Optional[Union[dict, Location]] = None
    inetLocation: Optional[Union[dict, ObservableObject]] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.location is not None and not isinstance(self.location, Location):
            self.location = Location(**as_dict(self.location))

        if self.inetLocation is not None and not isinstance(self.inetLocation, ObservableObject):
            self.inetLocation = ObservableObject(**as_dict(self.inetLocation))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class OperatingSystemFacet(Facet):
    """
    "An operating system facet is a grouping of characteristics unique to the software that manages computer hardware,
    software resources, and provides common services for computer programs. [based on
    https://en.wikipedia.org/wiki/Operating_system]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.OperatingSystemFacet
    class_class_curie: ClassVar[str] = "observable:OperatingSystemFacet"
    class_name: ClassVar[str] = "OperatingSystemFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.OperatingSystemFacet

    manufacturer: Optional[Union[dict, Identity]] = None
    environmentVariables: Optional[Union[dict, "Dictionary"]] = None
    isLimitAdTrackingEnabled: Optional[Union[bool, BooleanType]] = None
    installDate: Optional[Union[str, XSDDateTime]] = None
    bitness: Optional[str] = None
    version: Optional[str] = None
    advertisingID: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.manufacturer is not None and not isinstance(self.manufacturer, Identity):
            self.manufacturer = Identity(**as_dict(self.manufacturer))

        if self.environmentVariables is not None and not isinstance(self.environmentVariables, Dictionary):
            self.environmentVariables = Dictionary(**as_dict(self.environmentVariables))

        if self.isLimitAdTrackingEnabled is not None and not isinstance(self.isLimitAdTrackingEnabled, BooleanType):
            self.isLimitAdTrackingEnabled = BooleanType(self.isLimitAdTrackingEnabled)

        if self.installDate is not None and not isinstance(self.installDate, XSDDateTime):
            self.installDate = XSDDateTime(self.installDate)

        if self.bitness is not None and not isinstance(self.bitness, str):
            self.bitness = str(self.bitness)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.advertisingID, list):
            self.advertisingID = [self.advertisingID] if self.advertisingID is not None else []
        self.advertisingID = [v if isinstance(v, str) else str(v) for v in self.advertisingID]

        super().__post_init__(**kwargs)


@dataclass
class PDFFileFacet(Facet):
    """
    "A PDF file facet is a grouping of characteristics unique to a PDF (Portable Document Format) file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PDFFileFacet
    class_class_curie: ClassVar[str] = "observable:PDFFileFacet"
    class_name: ClassVar[str] = "PDFFileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PDFFileFacet

    documentInformationDictionary: Optional[Union[dict, "ControlledDictionary"]] = None
    isOptimized: Optional[Union[bool, BooleanType]] = None
    pdfCreationDate: Optional[Union[str, XSDDateTime]] = None
    pdfModDate: Optional[Union[str, XSDDateTime]] = None
    pdfId1: Optional[str] = None
    version: Optional[str] = None
    pdfId0: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.documentInformationDictionary is not None and not isinstance(self.documentInformationDictionary, ControlledDictionary):
            self.documentInformationDictionary = ControlledDictionary(**as_dict(self.documentInformationDictionary))

        if self.isOptimized is not None and not isinstance(self.isOptimized, BooleanType):
            self.isOptimized = BooleanType(self.isOptimized)

        if self.pdfCreationDate is not None and not isinstance(self.pdfCreationDate, XSDDateTime):
            self.pdfCreationDate = XSDDateTime(self.pdfCreationDate)

        if self.pdfModDate is not None and not isinstance(self.pdfModDate, XSDDateTime):
            self.pdfModDate = XSDDateTime(self.pdfModDate)

        if self.pdfId1 is not None and not isinstance(self.pdfId1, str):
            self.pdfId1 = str(self.pdfId1)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.pdfId0, list):
            self.pdfId0 = [self.pdfId0] if self.pdfId0 is not None else []
        self.pdfId0 = [v if isinstance(v, str) else str(v) for v in self.pdfId0]

        super().__post_init__(**kwargs)


@dataclass
class PathRelationFacet(Facet):
    """
    "A path relation facet is a grouping of characteristics unique to the location of one object within another
    containing object."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PathRelationFacet
    class_class_curie: ClassVar[str] = "observable:PathRelationFacet"
    class_name: ClassVar[str] = "PathRelationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PathRelationFacet

    path: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.path, list):
            self.path = [self.path] if self.path is not None else []
        self.path = [v if isinstance(v, str) else str(v) for v in self.path]

        super().__post_init__(**kwargs)


@dataclass
class PhoneAccountFacet(Facet):
    """
    "A phone account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
    control the provision of a telephony capability or service."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PhoneAccountFacet
    class_class_curie: ClassVar[str] = "observable:PhoneAccountFacet"
    class_name: ClassVar[str] = "PhoneAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PhoneAccountFacet

    phoneNumber: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.phoneNumber is not None and not isinstance(self.phoneNumber, str):
            self.phoneNumber = str(self.phoneNumber)

        super().__post_init__(**kwargs)


@dataclass
class ProcessFacet(Facet):
    """
    "A process facet is a grouping of characteristics unique to an instance of a computer program executed on an
    operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ProcessFacet
    class_class_curie: ClassVar[str] = "observable:ProcessFacet"
    class_name: ClassVar[str] = "ProcessFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ProcessFacet

    binary: Optional[Union[dict, ObservableObject]] = None
    creatorUser: Optional[Union[dict, ObservableObject]] = None
    parent: Optional[Union[dict, ObservableObject]] = None
    environmentVariables: Optional[Union[dict, "Dictionary"]] = None
    isHidden: Optional[Union[bool, BooleanType]] = None
    exitTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    exitStatus: Optional[int] = None
    pid: Optional[int] = None
    currentWorkingDirectory: Optional[str] = None
    status: Optional[str] = None
    arguments: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.binary is not None and not isinstance(self.binary, ObservableObject):
            self.binary = ObservableObject(**as_dict(self.binary))

        if self.creatorUser is not None and not isinstance(self.creatorUser, ObservableObject):
            self.creatorUser = ObservableObject(**as_dict(self.creatorUser))

        if self.parent is not None and not isinstance(self.parent, ObservableObject):
            self.parent = ObservableObject(**as_dict(self.parent))

        if self.environmentVariables is not None and not isinstance(self.environmentVariables, Dictionary):
            self.environmentVariables = Dictionary(**as_dict(self.environmentVariables))

        if self.isHidden is not None and not isinstance(self.isHidden, BooleanType):
            self.isHidden = BooleanType(self.isHidden)

        if self.exitTime is not None and not isinstance(self.exitTime, XSDDateTime):
            self.exitTime = XSDDateTime(self.exitTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.exitStatus is not None and not isinstance(self.exitStatus, int):
            self.exitStatus = int(self.exitStatus)

        if self.pid is not None and not isinstance(self.pid, int):
            self.pid = int(self.pid)

        if self.currentWorkingDirectory is not None and not isinstance(self.currentWorkingDirectory, str):
            self.currentWorkingDirectory = str(self.currentWorkingDirectory)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if not isinstance(self.arguments, list):
            self.arguments = [self.arguments] if self.arguments is not None else []
        self.arguments = [v if isinstance(v, str) else str(v) for v in self.arguments]

        super().__post_init__(**kwargs)


@dataclass
class ProfileFacet(Facet):
    """
    "A profile facet is a grouping of characteristics unique to an explicit digital representation of identity and
    characteristics of the owner of a single user account associated with an online service or application. [based on
    https://en.wikipedia.org/wiki/User_profile]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ProfileFacet
    class_class_curie: ClassVar[str] = "observable:ProfileFacet"
    class_name: ClassVar[str] = "ProfileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ProfileFacet

    profileIdentity: Optional[Union[dict, Identity]] = None
    contactAddress: Optional[Union[dict, ContactAddress]] = None
    contactEmail: Optional[Union[dict, ContactEmail]] = None
    contactMessaging: Optional[Union[dict, ContactMessaging]] = None
    contactPhone: Optional[Union[dict, ContactPhone]] = None
    contactURL: Optional[Union[dict, ContactURL]] = None
    profileAccount: Optional[Union[dict, ObservableObject]] = None
    profileService: Optional[Union[dict, ObservableObject]] = None
    profileWebsite: Optional[Union[dict, ObservableObject]] = None
    profileCreated: Optional[Union[str, XSDDateTime]] = None
    name: Optional[str] = None
    displayName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.profileIdentity is not None and not isinstance(self.profileIdentity, Identity):
            self.profileIdentity = Identity(**as_dict(self.profileIdentity))

        if self.contactAddress is not None and not isinstance(self.contactAddress, ContactAddress):
            self.contactAddress = ContactAddress(**as_dict(self.contactAddress))

        if self.contactEmail is not None and not isinstance(self.contactEmail, ContactEmail):
            self.contactEmail = ContactEmail(**as_dict(self.contactEmail))

        if self.contactMessaging is not None and not isinstance(self.contactMessaging, ContactMessaging):
            self.contactMessaging = ContactMessaging(**as_dict(self.contactMessaging))

        if self.contactPhone is not None and not isinstance(self.contactPhone, ContactPhone):
            self.contactPhone = ContactPhone(**as_dict(self.contactPhone))

        if self.contactURL is not None and not isinstance(self.contactURL, ContactURL):
            self.contactURL = ContactURL(**as_dict(self.contactURL))

        if self.profileAccount is not None and not isinstance(self.profileAccount, ObservableObject):
            self.profileAccount = ObservableObject(**as_dict(self.profileAccount))

        if self.profileService is not None and not isinstance(self.profileService, ObservableObject):
            self.profileService = ObservableObject(**as_dict(self.profileService))

        if self.profileWebsite is not None and not isinstance(self.profileWebsite, ObservableObject):
            self.profileWebsite = ObservableObject(**as_dict(self.profileWebsite))

        if self.profileCreated is not None and not isinstance(self.profileCreated, XSDDateTime):
            self.profileCreated = XSDDateTime(self.profileCreated)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        super().__post_init__(**kwargs)


@dataclass
class PropertiesEnumeratedEffectFacet(DefinedEffectFacet):
    """
    "A properties enumerated effect facet is a grouping of characteristics unique to the effects of actions upon
    observable objects where a characteristic of the observable object is enumerated. An example of this would be
    startup parameters for a process."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PropertiesEnumeratedEffectFacet
    class_class_curie: ClassVar[str] = "observable:PropertiesEnumeratedEffectFacet"
    class_name: ClassVar[str] = "PropertiesEnumeratedEffectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PropertiesEnumeratedEffectFacet

    properties: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.properties is not None and not isinstance(self.properties, str):
            self.properties = str(self.properties)

        super().__post_init__(**kwargs)


@dataclass
class PropertyReadEffectFacet(DefinedEffectFacet):
    """
    "A properties read effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a characteristic isRead from an observable object. An example of this would be the current running
    state of a process."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PropertyReadEffectFacet
    class_class_curie: ClassVar[str] = "observable:PropertyReadEffectFacet"
    class_name: ClassVar[str] = "PropertyReadEffectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.PropertyReadEffectFacet

    propertyName: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.propertyName is not None and not isinstance(self.propertyName, str):
            self.propertyName = str(self.propertyName)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class RasterPictureFacet(Facet):
    """
    "A raster picture facet is a grouping of characteristics unique to a raster (or bitmap) image."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.RasterPictureFacet
    class_class_curie: ClassVar[str] = "observable:RasterPictureFacet"
    class_name: ClassVar[str] = "RasterPictureFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.RasterPictureFacet

    camera: Optional[Union[dict, ObservableObject]] = None
    bitsPerPixel: Optional[int] = None
    pictureHeight: Optional[int] = None
    pictureWidth: Optional[int] = None
    imageCompressionMethod: Optional[str] = None
    pictureType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.camera is not None and not isinstance(self.camera, ObservableObject):
            self.camera = ObservableObject(**as_dict(self.camera))

        if self.bitsPerPixel is not None and not isinstance(self.bitsPerPixel, int):
            self.bitsPerPixel = int(self.bitsPerPixel)

        if self.pictureHeight is not None and not isinstance(self.pictureHeight, int):
            self.pictureHeight = int(self.pictureHeight)

        if self.pictureWidth is not None and not isinstance(self.pictureWidth, int):
            self.pictureWidth = int(self.pictureWidth)

        if self.imageCompressionMethod is not None and not isinstance(self.imageCompressionMethod, str):
            self.imageCompressionMethod = str(self.imageCompressionMethod)

        if self.pictureType is not None and not isinstance(self.pictureType, str):
            self.pictureType = str(self.pictureType)

        super().__post_init__(**kwargs)


@dataclass
class RecoveredObjectFacet(Facet):
    """
    "Recoverability status of name, metadata, and content."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.RecoveredObjectFacet
    class_class_curie: ClassVar[str] = "observable:RecoveredObjectFacet"
    class_name: ClassVar[str] = "RecoveredObjectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.RecoveredObjectFacet

    contentRecoveredStatus: Optional[Union[str, "RecoveredObjectStatusEnum"]] = None
    metadataRecoveredStatus: Optional[Union[str, "RecoveredObjectStatusEnum"]] = None
    nameRecoveredStatus: Optional[Union[str, "RecoveredObjectStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.contentRecoveredStatus is not None and not isinstance(self.contentRecoveredStatus, RecoveredObjectStatusEnum):
            self.contentRecoveredStatus = RecoveredObjectStatusEnum(self.contentRecoveredStatus)

        if self.metadataRecoveredStatus is not None and not isinstance(self.metadataRecoveredStatus, RecoveredObjectStatusEnum):
            self.metadataRecoveredStatus = RecoveredObjectStatusEnum(self.metadataRecoveredStatus)

        if self.nameRecoveredStatus is not None and not isinstance(self.nameRecoveredStatus, RecoveredObjectStatusEnum):
            self.nameRecoveredStatus = RecoveredObjectStatusEnum(self.nameRecoveredStatus)

        super().__post_init__(**kwargs)


class RegistryDatatype(YAMLRoot):
    """
    "Data types used in Windows operating systems Registry, and the earlier IBM/Microsoft OS/2 operating system"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.RegistryDatatype
    class_class_curie: ClassVar[str] = "observable:RegistryDatatype"
    class_name: ClassVar[str] = "RegistryDatatype"
    class_model_uri: ClassVar[URIRef] = MASTER.RegistryDatatype


@dataclass
class SIMCardFacet(Facet):
    """
    "A SIM card facet is a grouping of characteristics unique to a subscriber identification module card intended to
    securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to
    identify and authenticate subscribers on mobile telephony devices (such as mobile phones and computers). [based on
    https://en.wikipedia.org/wiki/SIM_card]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SIMCardFacet
    class_class_curie: ClassVar[str] = "observable:SIMCardFacet"
    class_name: ClassVar[str] = "SIMCardFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SIMCardFacet

    carrier: Optional[Union[dict, Identity]] = None
    storageCapacityInBytes: Optional[int] = None
    ICCID: Optional[str] = None
    IMSI: Optional[str] = None
    PIN: Optional[str] = None
    PUK: Optional[str] = None
    SIMForm: Optional[str] = None
    SIMType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.carrier is not None and not isinstance(self.carrier, Identity):
            self.carrier = Identity(**as_dict(self.carrier))

        if self.storageCapacityInBytes is not None and not isinstance(self.storageCapacityInBytes, int):
            self.storageCapacityInBytes = int(self.storageCapacityInBytes)

        if self.ICCID is not None and not isinstance(self.ICCID, str):
            self.ICCID = str(self.ICCID)

        if self.IMSI is not None and not isinstance(self.IMSI, str):
            self.IMSI = str(self.IMSI)

        if self.PIN is not None and not isinstance(self.PIN, str):
            self.PIN = str(self.PIN)

        if self.PUK is not None and not isinstance(self.PUK, str):
            self.PUK = str(self.PUK)

        if self.SIMForm is not None and not isinstance(self.SIMForm, str):
            self.SIMForm = str(self.SIMForm)

        if self.SIMType is not None and not isinstance(self.SIMType, str):
            self.SIMType = str(self.SIMType)

        super().__post_init__(**kwargs)


class SIPAddressFacet(DigitalAddressFacet):
    """
    "A SIP address facet is a grouping of characteristics unique to a Session Initiation Protocol (SIP) standards
    conformant identifier assigned to a user to enable routing and management of SIP standards conformant
    communication to or from that user loosely coupled from any particular devices."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SIPAddressFacet
    class_class_curie: ClassVar[str] = "observable:SIPAddressFacet"
    class_name: ClassVar[str] = "SIPAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SIPAddressFacet


@dataclass
class SMSMessageFacet(Facet):
    """
    "A SMS message facet is a grouping of characteristics unique to a message conformant to the short message service
    (SMS) communication protocol standards."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SMSMessageFacet
    class_class_curie: ClassVar[str] = "observable:SMSMessageFacet"
    class_name: ClassVar[str] = "SMSMessageFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SMSMessageFacet

    isRead: Optional[Union[bool, BooleanType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isRead is not None and not isinstance(self.isRead, BooleanType):
            self.isRead = BooleanType(self.isRead)

        super().__post_init__(**kwargs)


@dataclass
class SQLiteBlobFacet(Facet):
    """
    "An SQLite blob facet is a grouping of characteristics unique to a blob (binary large object) of data within an
    SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SQLiteBlobFacet
    class_class_curie: ClassVar[str] = "observable:SQLiteBlobFacet"
    class_name: ClassVar[str] = "SQLiteBlobFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SQLiteBlobFacet

    rowIndex: Optional[Union[Union[int, PositiveIntegerType], List[Union[int, PositiveIntegerType]]]] = empty_list()
    columnName: Optional[str] = None
    rowCondition: Optional[str] = None
    tableName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.rowIndex, list):
            self.rowIndex = [self.rowIndex] if self.rowIndex is not None else []
        self.rowIndex = [v if isinstance(v, PositiveIntegerType) else PositiveIntegerType(v) for v in self.rowIndex]

        if self.columnName is not None and not isinstance(self.columnName, str):
            self.columnName = str(self.columnName)

        if self.rowCondition is not None and not isinstance(self.rowCondition, str):
            self.rowCondition = str(self.rowCondition)

        if self.tableName is not None and not isinstance(self.tableName, str):
            self.tableName = str(self.tableName)

        super().__post_init__(**kwargs)


@dataclass
class SendControlCodeEffectFacet(DefinedEffectFacet):
    """
    "A send controlCode effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a controlCode, or other control-oriented communication signal, is sent to the observable object. An
    example of this would be an action sending a controlCode changing the running state of a process."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SendControlCodeEffectFacet
    class_class_curie: ClassVar[str] = "observable:SendControlCodeEffectFacet"
    class_name: ClassVar[str] = "SendControlCodeEffectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SendControlCodeEffectFacet

    controlCode: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.controlCode is not None and not isinstance(self.controlCode, str):
            self.controlCode = str(self.controlCode)

        super().__post_init__(**kwargs)


@dataclass
class SoftwareFacet(Facet):
    """
    "A software facet is a grouping of characteristics unique to a software program (a definitively scoped instance of
    a collection of data or computer instructions that tell the computer how to work). [based on
    https://en.wikipedia.org/wiki/Software]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SoftwareFacet
    class_class_curie: ClassVar[str] = "observable:SoftwareFacet"
    class_name: ClassVar[str] = "SoftwareFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SoftwareFacet

    manufacturer: Optional[Union[dict, Identity]] = None
    cpeid: Optional[str] = None
    language: Optional[str] = None
    swid: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.manufacturer is not None and not isinstance(self.manufacturer, Identity):
            self.manufacturer = Identity(**as_dict(self.manufacturer))

        if self.cpeid is not None and not isinstance(self.cpeid, str):
            self.cpeid = str(self.cpeid)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        if self.swid is not None and not isinstance(self.swid, str):
            self.swid = str(self.swid)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class StateChangeEffectFacet(DefinedEffectFacet):
    """
    "A state change effect facet is a grouping of characteristics unique to the effects of actions upon observable
    objects where a state of the observable object is changed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.StateChangeEffectFacet
    class_class_curie: ClassVar[str] = "observable:StateChangeEffectFacet"
    class_name: ClassVar[str] = "StateChangeEffectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.StateChangeEffectFacet

    newObject: Optional[Union[dict, ObservableObject]] = None
    oldObject: Optional[Union[dict, ObservableObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.newObject is not None and not isinstance(self.newObject, ObservableObject):
            self.newObject = ObservableObject(**as_dict(self.newObject))

        if self.oldObject is not None and not isinstance(self.oldObject, ObservableObject):
            self.oldObject = ObservableObject(**as_dict(self.oldObject))

        super().__post_init__(**kwargs)


@dataclass
class SymbolicLinkFacet(Facet):
    """
    "A symbolic link facet is a grouping of characteristics unique to a file that contains a reference to another file
    or directory in the form of an absolute or relative path and that affects pathname resolution. [based on
    https://en.wikipedia.org/wiki/Symbolic_link]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SymbolicLinkFacet
    class_class_curie: ClassVar[str] = "observable:SymbolicLinkFacet"
    class_name: ClassVar[str] = "SymbolicLinkFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.SymbolicLinkFacet

    targetFile: Optional[Union[dict, ObservableObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.targetFile is not None and not isinstance(self.targetFile, ObservableObject):
            self.targetFile = ObservableObject(**as_dict(self.targetFile))

        super().__post_init__(**kwargs)


@dataclass
class TCPConnectionFacet(Facet):
    """
    "A TCP connection facet is a grouping of characteristics unique to portions of a network connection that are
    conformant to the Transmission Control Protocl (TCP) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TCPConnectionFacet
    class_class_curie: ClassVar[str] = "observable:TCPConnectionFacet"
    class_name: ClassVar[str] = "TCPConnectionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.TCPConnectionFacet

    sourceFlags: Optional[Union[hex, List[hex]]] = empty_list()
    destinationFlags: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.sourceFlags, list):
            self.sourceFlags = [self.sourceFlags] if self.sourceFlags is not None else []
        self.sourceFlags = [v if isinstance(v, hex) else hex(v) for v in self.sourceFlags]

        if not isinstance(self.destinationFlags, list):
            self.destinationFlags = [self.destinationFlags] if self.destinationFlags is not None else []
        self.destinationFlags = [v if isinstance(v, str) else str(v) for v in self.destinationFlags]

        super().__post_init__(**kwargs)


@dataclass
class TableFieldFacet(Facet):
    """
    "A database record facet contains properties associated with a specific table record value from a database."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TableFieldFacet
    class_class_curie: ClassVar[str] = "observable:TableFieldFacet"
    class_name: ClassVar[str] = "TableFieldFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.TableFieldFacet

    recordFieldIsNull: Optional[Union[bool, BooleanType]] = None
    recordFieldName: Optional[str] = None
    tableName: Optional[str] = None
    tableSchema: Optional[str] = None
    recordFieldValue: Optional[str] = None
    recordRowID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.recordFieldIsNull is not None and not isinstance(self.recordFieldIsNull, BooleanType):
            self.recordFieldIsNull = BooleanType(self.recordFieldIsNull)

        if self.recordFieldName is not None and not isinstance(self.recordFieldName, str):
            self.recordFieldName = str(self.recordFieldName)

        if self.tableName is not None and not isinstance(self.tableName, str):
            self.tableName = str(self.tableName)

        if self.tableSchema is not None and not isinstance(self.tableSchema, str):
            self.tableSchema = str(self.tableSchema)

        if self.recordFieldValue is not None and not isinstance(self.recordFieldValue, str):
            self.recordFieldValue = str(self.recordFieldValue)

        if self.recordRowID is not None and not isinstance(self.recordRowID, str):
            self.recordRowID = str(self.recordRowID)

        super().__post_init__(**kwargs)


@dataclass
class TaskActionType(UcoInherentCharacterizationThing):
    """
    "A task action type is a grouping of characteristics for a scheduled action to be completed."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TaskActionType
    class_class_curie: ClassVar[str] = "observable:TaskActionType"
    class_name: ClassVar[str] = "TaskActionType"
    class_model_uri: ClassVar[URIRef] = MASTER.TaskActionType

    iComHandlerAction: Optional[Union[dict, IComHandlerActionType]] = None
    iExecAction: Optional[Union[dict, IExecActionType]] = None
    iShowMessageAction: Optional[Union[dict, IShowMessageActionType]] = None
    iEmailAction: Optional[Union[dict, ObservableObject]] = None
    actionID: Optional[str] = None
    actionType: Optional[Union[str, "TaskActionTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.iComHandlerAction is not None and not isinstance(self.iComHandlerAction, IComHandlerActionType):
            self.iComHandlerAction = IComHandlerActionType(**as_dict(self.iComHandlerAction))

        if self.iExecAction is not None and not isinstance(self.iExecAction, IExecActionType):
            self.iExecAction = IExecActionType(**as_dict(self.iExecAction))

        if self.iShowMessageAction is not None and not isinstance(self.iShowMessageAction, IShowMessageActionType):
            self.iShowMessageAction = IShowMessageActionType(**as_dict(self.iShowMessageAction))

        if self.iEmailAction is not None and not isinstance(self.iEmailAction, ObservableObject):
            self.iEmailAction = ObservableObject(**as_dict(self.iEmailAction))

        if self.actionID is not None and not isinstance(self.actionID, str):
            self.actionID = str(self.actionID)

        if self.actionType is not None and not isinstance(self.actionType, TaskActionTypeEnum):
            self.actionType = TaskActionTypeEnum(self.actionType)

        super().__post_init__(**kwargs)


@dataclass
class TriggerType(UcoInherentCharacterizationThing):
    """
    "A triggerType is a grouping of characterizes unique to a set of criteria that, when met, starts the execution of
    a task within a Windows operating system. [based on
    https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TriggerType
    class_class_curie: ClassVar[str] = "observable:TriggerType"
    class_name: ClassVar[str] = "TriggerType"
    class_model_uri: ClassVar[URIRef] = MASTER.TriggerType

    isEnabled: Optional[Union[bool, BooleanType]] = None
    triggerBeginTime: Optional[Union[str, XSDDateTime]] = None
    triggerEndTime: Optional[Union[str, XSDDateTime]] = None
    triggerDelay: Optional[str] = None
    triggerMaxRunTime: Optional[str] = None
    triggerSessionChangeType: Optional[str] = None
    triggerFrequency: Optional[Union[str, "TriggerFrequencyEnum"]] = None
    triggerType: Optional[Union[str, "TriggerTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.isEnabled is not None and not isinstance(self.isEnabled, BooleanType):
            self.isEnabled = BooleanType(self.isEnabled)

        if self.triggerBeginTime is not None and not isinstance(self.triggerBeginTime, XSDDateTime):
            self.triggerBeginTime = XSDDateTime(self.triggerBeginTime)

        if self.triggerEndTime is not None and not isinstance(self.triggerEndTime, XSDDateTime):
            self.triggerEndTime = XSDDateTime(self.triggerEndTime)

        if self.triggerDelay is not None and not isinstance(self.triggerDelay, str):
            self.triggerDelay = str(self.triggerDelay)

        if self.triggerMaxRunTime is not None and not isinstance(self.triggerMaxRunTime, str):
            self.triggerMaxRunTime = str(self.triggerMaxRunTime)

        if self.triggerSessionChangeType is not None and not isinstance(self.triggerSessionChangeType, str):
            self.triggerSessionChangeType = str(self.triggerSessionChangeType)

        if self.triggerFrequency is not None and not isinstance(self.triggerFrequency, TriggerFrequencyEnum):
            self.triggerFrequency = TriggerFrequencyEnum(self.triggerFrequency)

        if self.triggerType is not None and not isinstance(self.triggerType, TriggerTypeEnum):
            self.triggerType = TriggerTypeEnum(self.triggerType)

        super().__post_init__(**kwargs)


@dataclass
class TwitterProfileFacet(Facet):
    """
    "A twitter profile facet is a grouping of characteristics unique to an explicit digital representation of identity
    and characteristics of the owner of a single Twitter user account. [based on
    https://en.wikipedia.org/wiki/User_profile]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TwitterProfileFacet
    class_class_curie: ClassVar[str] = "observable:TwitterProfileFacet"
    class_name: ClassVar[str] = "TwitterProfileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.TwitterProfileFacet

    profileBackgroundLocation: Optional[Union[dict, ObservableObject]] = None
    profileBannerLocation: Optional[Union[dict, ObservableObject]] = None
    profileImageLocation: Optional[Union[dict, ObservableObject]] = None
    profileBackgroundHash: Optional[Union[dict, "Hash"]] = None
    profileBannerHash: Optional[Union[dict, "Hash"]] = None
    profileImageHash: Optional[Union[dict, "Hash"]] = None
    profileIsProtected: Optional[Union[bool, BooleanType]] = None
    profileIsVerified: Optional[Union[bool, BooleanType]] = None
    listedCount: Optional[int] = None
    favoritesCount: Optional[Union[int, NonNegativeIntegerType]] = None
    followersCount: Optional[Union[int, NonNegativeIntegerType]] = None
    friendsCount: Optional[Union[int, NonNegativeIntegerType]] = None
    statusesCount: Optional[Union[int, NonNegativeIntegerType]] = None
    twitterHandle: Optional[str] = None
    twitterId: Optional[str] = None
    userLocationString: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.profileBackgroundLocation is not None and not isinstance(self.profileBackgroundLocation, ObservableObject):
            self.profileBackgroundLocation = ObservableObject(**as_dict(self.profileBackgroundLocation))

        if self.profileBannerLocation is not None and not isinstance(self.profileBannerLocation, ObservableObject):
            self.profileBannerLocation = ObservableObject(**as_dict(self.profileBannerLocation))

        if self.profileImageLocation is not None and not isinstance(self.profileImageLocation, ObservableObject):
            self.profileImageLocation = ObservableObject(**as_dict(self.profileImageLocation))

        if self.profileBackgroundHash is not None and not isinstance(self.profileBackgroundHash, Hash):
            self.profileBackgroundHash = Hash(**as_dict(self.profileBackgroundHash))

        if self.profileBannerHash is not None and not isinstance(self.profileBannerHash, Hash):
            self.profileBannerHash = Hash(**as_dict(self.profileBannerHash))

        if self.profileImageHash is not None and not isinstance(self.profileImageHash, Hash):
            self.profileImageHash = Hash(**as_dict(self.profileImageHash))

        if self.profileIsProtected is not None and not isinstance(self.profileIsProtected, BooleanType):
            self.profileIsProtected = BooleanType(self.profileIsProtected)

        if self.profileIsVerified is not None and not isinstance(self.profileIsVerified, BooleanType):
            self.profileIsVerified = BooleanType(self.profileIsVerified)

        if self.listedCount is not None and not isinstance(self.listedCount, int):
            self.listedCount = int(self.listedCount)

        if self.favoritesCount is not None and not isinstance(self.favoritesCount, NonNegativeIntegerType):
            self.favoritesCount = NonNegativeIntegerType(self.favoritesCount)

        if self.followersCount is not None and not isinstance(self.followersCount, NonNegativeIntegerType):
            self.followersCount = NonNegativeIntegerType(self.followersCount)

        if self.friendsCount is not None and not isinstance(self.friendsCount, NonNegativeIntegerType):
            self.friendsCount = NonNegativeIntegerType(self.friendsCount)

        if self.statusesCount is not None and not isinstance(self.statusesCount, NonNegativeIntegerType):
            self.statusesCount = NonNegativeIntegerType(self.statusesCount)

        if self.twitterHandle is not None and not isinstance(self.twitterHandle, str):
            self.twitterHandle = str(self.twitterHandle)

        if self.twitterId is not None and not isinstance(self.twitterId, str):
            self.twitterId = str(self.twitterId)

        if self.userLocationString is not None and not isinstance(self.userLocationString, str):
            self.userLocationString = str(self.userLocationString)

        super().__post_init__(**kwargs)


@dataclass
class UNIXAccountFacet(Facet):
    """
    "A UNIX account facet is a grouping of characteristics unique to an account on a UNIX operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXAccountFacet
    class_class_curie: ClassVar[str] = "observable:UNIXAccountFacet"
    class_name: ClassVar[str] = "UNIXAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXAccountFacet

    gid: Optional[int] = None
    shell: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gid is not None and not isinstance(self.gid, int):
            self.gid = int(self.gid)

        if self.shell is not None and not isinstance(self.shell, str):
            self.shell = str(self.shell)

        super().__post_init__(**kwargs)


class UNIXFilePermissionsFacet(Facet):
    """
    "A UNIX file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change,
    navigate, execute) of a file on a UNIX file system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXFilePermissionsFacet
    class_class_curie: ClassVar[str] = "observable:UNIXFilePermissionsFacet"
    class_name: ClassVar[str] = "UNIXFilePermissionsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXFilePermissionsFacet


@dataclass
class UNIXProcessFacet(Facet):
    """
    "A UNIX process facet is a grouping of characteristics unique to an instance of a computer program executed on a
    UNIX operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXProcessFacet
    class_class_curie: ClassVar[str] = "observable:UNIXProcessFacet"
    class_name: ClassVar[str] = "UNIXProcessFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXProcessFacet

    openFileDescriptor: Optional[Union[int, List[int]]] = empty_list()
    ruid: Optional[Union[Union[int, NonNegativeIntegerType], List[Union[int, NonNegativeIntegerType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.openFileDescriptor, list):
            self.openFileDescriptor = [self.openFileDescriptor] if self.openFileDescriptor is not None else []
        self.openFileDescriptor = [v if isinstance(v, int) else int(v) for v in self.openFileDescriptor]

        if not isinstance(self.ruid, list):
            self.ruid = [self.ruid] if self.ruid is not None else []
        self.ruid = [v if isinstance(v, NonNegativeIntegerType) else NonNegativeIntegerType(v) for v in self.ruid]

        super().__post_init__(**kwargs)


@dataclass
class UNIXVolumeFacet(Facet):
    """
    "A UNIX volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a
    single UNIX file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXVolumeFacet
    class_class_curie: ClassVar[str] = "observable:UNIXVolumeFacet"
    class_name: ClassVar[str] = "UNIXVolumeFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXVolumeFacet

    mountPoint: Optional[str] = None
    options: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.mountPoint is not None and not isinstance(self.mountPoint, str):
            self.mountPoint = str(self.mountPoint)

        if self.options is not None and not isinstance(self.options, str):
            self.options = str(self.options)

        super().__post_init__(**kwargs)


@dataclass
class URLFacet(Facet):
    """
    "A URL facet is a grouping of characteristics unique to a uniform resource locator (URL) acting as a resolvable
    address to a particular WWW (World Wide Web) accessible resource."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URLFacet
    class_class_curie: ClassVar[str] = "observable:URLFacet"
    class_name: ClassVar[str] = "URLFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.URLFacet

    host: Optional[Union[dict, ObservableObject]] = None
    port: Optional[int] = None
    fragment: Optional[str] = None
    fullValue: Optional[str] = None
    password: Optional[str] = None
    path: Optional[str] = None
    query: Optional[str] = None
    scheme: Optional[str] = None
    userName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.host is not None and not isinstance(self.host, ObservableObject):
            self.host = ObservableObject(**as_dict(self.host))

        if self.port is not None and not isinstance(self.port, int):
            self.port = int(self.port)

        if self.fragment is not None and not isinstance(self.fragment, str):
            self.fragment = str(self.fragment)

        if self.fullValue is not None and not isinstance(self.fullValue, str):
            self.fullValue = str(self.fullValue)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.path is not None and not isinstance(self.path, str):
            self.path = str(self.path)

        if self.query is not None and not isinstance(self.query, str):
            self.query = str(self.query)

        if self.scheme is not None and not isinstance(self.scheme, str):
            self.scheme = str(self.scheme)

        if self.userName is not None and not isinstance(self.userName, str):
            self.userName = str(self.userName)

        super().__post_init__(**kwargs)


@dataclass
class URLHistoryEntry(UcoInherentCharacterizationThing):
    """
    "A URL history entry is a grouping of characteristics unique to the properties of a single URL history entry for a
    particular browser"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URLHistoryEntry
    class_class_curie: ClassVar[str] = "observable:URLHistoryEntry"
    class_name: ClassVar[str] = "URLHistoryEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.URLHistoryEntry

    url: Optional[Union[dict, ObservableObject]] = None
    referrerURL: Optional[Union[dict, ObservableObject]] = None
    expirationTime: Optional[Union[str, XSDDateTime]] = None
    firstVisit: Optional[Union[str, XSDDateTime]] = None
    lastVisit: Optional[Union[str, XSDDateTime]] = None
    visitCount: Optional[int] = None
    manuallyEnteredCount: Optional[Union[int, NonNegativeIntegerType]] = None
    browserUserProfile: Optional[str] = None
    hostname: Optional[str] = None
    pageTitle: Optional[str] = None
    keywordSearchTerm: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, ObservableObject):
            self.url = ObservableObject(**as_dict(self.url))

        if self.referrerURL is not None and not isinstance(self.referrerURL, ObservableObject):
            self.referrerURL = ObservableObject(**as_dict(self.referrerURL))

        if self.expirationTime is not None and not isinstance(self.expirationTime, XSDDateTime):
            self.expirationTime = XSDDateTime(self.expirationTime)

        if self.firstVisit is not None and not isinstance(self.firstVisit, XSDDateTime):
            self.firstVisit = XSDDateTime(self.firstVisit)

        if self.lastVisit is not None and not isinstance(self.lastVisit, XSDDateTime):
            self.lastVisit = XSDDateTime(self.lastVisit)

        if self.visitCount is not None and not isinstance(self.visitCount, int):
            self.visitCount = int(self.visitCount)

        if self.manuallyEnteredCount is not None and not isinstance(self.manuallyEnteredCount, NonNegativeIntegerType):
            self.manuallyEnteredCount = NonNegativeIntegerType(self.manuallyEnteredCount)

        if self.browserUserProfile is not None and not isinstance(self.browserUserProfile, str):
            self.browserUserProfile = str(self.browserUserProfile)

        if self.hostname is not None and not isinstance(self.hostname, str):
            self.hostname = str(self.hostname)

        if self.pageTitle is not None and not isinstance(self.pageTitle, str):
            self.pageTitle = str(self.pageTitle)

        if self.keywordSearchTerm is not None and not isinstance(self.keywordSearchTerm, str):
            self.keywordSearchTerm = str(self.keywordSearchTerm)

        super().__post_init__(**kwargs)


@dataclass
class URLHistoryFacet(Facet):
    """
    "A URL history facet is a grouping of characteristics unique to the stored URL history for a particular web
    browser"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URLHistoryFacet
    class_class_curie: ClassVar[str] = "observable:URLHistoryFacet"
    class_name: ClassVar[str] = "URLHistoryFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.URLHistoryFacet

    browserInformation: Optional[Union[dict, ObservableObject]] = None
    urlHistoryEntry: Optional[Union[Union[dict, URLHistoryEntry], List[Union[dict, URLHistoryEntry]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.browserInformation is not None and not isinstance(self.browserInformation, ObservableObject):
            self.browserInformation = ObservableObject(**as_dict(self.browserInformation))

        if not isinstance(self.urlHistoryEntry, list):
            self.urlHistoryEntry = [self.urlHistoryEntry] if self.urlHistoryEntry is not None else []
        self.urlHistoryEntry = [v if isinstance(v, URLHistoryEntry) else URLHistoryEntry(**as_dict(v)) for v in self.urlHistoryEntry]

        super().__post_init__(**kwargs)


@dataclass
class URLVisitFacet(Facet):
    """
    "A URL visit facet is a grouping of characteristics unique to the properties of a visit of a URL within a
    particular browser."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URLVisitFacet
    class_class_curie: ClassVar[str] = "observable:URLVisitFacet"
    class_name: ClassVar[str] = "URLVisitFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.URLVisitFacet

    browserInformation: Optional[Union[dict, ObservableObject]] = None
    fromURLVisit: Optional[Union[dict, ObservableObject]] = None
    url: Optional[Union[dict, ObservableObject]] = None
    visitTime: Optional[Union[str, XSDDateTime]] = None
    visitDuration: Optional[Union[int, DurationType]] = None
    urlTransitionType: Optional[Union[str, "URLTransitionTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.browserInformation is not None and not isinstance(self.browserInformation, ObservableObject):
            self.browserInformation = ObservableObject(**as_dict(self.browserInformation))

        if self.fromURLVisit is not None and not isinstance(self.fromURLVisit, ObservableObject):
            self.fromURLVisit = ObservableObject(**as_dict(self.fromURLVisit))

        if self.url is not None and not isinstance(self.url, ObservableObject):
            self.url = ObservableObject(**as_dict(self.url))

        if self.visitTime is not None and not isinstance(self.visitTime, XSDDateTime):
            self.visitTime = XSDDateTime(self.visitTime)

        if self.visitDuration is not None and not isinstance(self.visitDuration, DurationType):
            self.visitDuration = DurationType(self.visitDuration)

        if self.urlTransitionType is not None and not isinstance(self.urlTransitionType, URLTransitionTypeEnum):
            self.urlTransitionType = URLTransitionTypeEnum(self.urlTransitionType)

        super().__post_init__(**kwargs)


@dataclass
class UserAccountFacet(Facet):
    """
    "A user account facet is a grouping of characteristics unique to an account controlling a user's access to a
    network, system, or platform."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UserAccountFacet
    class_class_curie: ClassVar[str] = "observable:UserAccountFacet"
    class_name: ClassVar[str] = "UserAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.UserAccountFacet

    canEscalatePrivs: Optional[Union[bool, BooleanType]] = None
    isPrivileged: Optional[Union[bool, BooleanType]] = None
    isServiceAccount: Optional[Union[bool, BooleanType]] = None
    homeDirectory: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.canEscalatePrivs is not None and not isinstance(self.canEscalatePrivs, BooleanType):
            self.canEscalatePrivs = BooleanType(self.canEscalatePrivs)

        if self.isPrivileged is not None and not isinstance(self.isPrivileged, BooleanType):
            self.isPrivileged = BooleanType(self.isPrivileged)

        if self.isServiceAccount is not None and not isinstance(self.isServiceAccount, BooleanType):
            self.isServiceAccount = BooleanType(self.isServiceAccount)

        if self.homeDirectory is not None and not isinstance(self.homeDirectory, str):
            self.homeDirectory = str(self.homeDirectory)

        super().__post_init__(**kwargs)


@dataclass
class UserSessionFacet(Facet):
    """
    "A user session facet is a grouping of characteristics unique to a temporary and interactive information
    interchange between two or more communicating devices within the managed scope of a single user. [based on
    https://en.wikipedia.org/wiki/Session_(computer_science)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UserSessionFacet
    class_class_curie: ClassVar[str] = "observable:UserSessionFacet"
    class_name: ClassVar[str] = "UserSessionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.UserSessionFacet

    effectiveUser: Optional[Union[dict, ObservableObject]] = None
    loginTime: Optional[Union[str, XSDDateTime]] = None
    logoutTime: Optional[Union[str, XSDDateTime]] = None
    effectiveGroup: Optional[str] = None
    effectiveGroupID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.effectiveUser is not None and not isinstance(self.effectiveUser, ObservableObject):
            self.effectiveUser = ObservableObject(**as_dict(self.effectiveUser))

        if self.loginTime is not None and not isinstance(self.loginTime, XSDDateTime):
            self.loginTime = XSDDateTime(self.loginTime)

        if self.logoutTime is not None and not isinstance(self.logoutTime, XSDDateTime):
            self.logoutTime = XSDDateTime(self.logoutTime)

        if self.effectiveGroup is not None and not isinstance(self.effectiveGroup, str):
            self.effectiveGroup = str(self.effectiveGroup)

        if self.effectiveGroupID is not None and not isinstance(self.effectiveGroupID, str):
            self.effectiveGroupID = str(self.effectiveGroupID)

        super().__post_init__(**kwargs)


@dataclass
class ValuesEnumeratedEffectFacet(DefinedEffectFacet):
    """
    "A values enumerated effect facet is a grouping of characteristics unique to the effects of actions upon
    observable objects where a value of the observable object is enumerated. An example of this would be the values of
    a registry key."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ValuesEnumeratedEffectFacet
    class_class_curie: ClassVar[str] = "observable:ValuesEnumeratedEffectFacet"
    class_name: ClassVar[str] = "ValuesEnumeratedEffectFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.ValuesEnumeratedEffectFacet

    values: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.values is not None and not isinstance(self.values, str):
            self.values = str(self.values)

        super().__post_init__(**kwargs)


@dataclass
class VolumeFacet(Facet):
    """
    "A volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single
    file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.VolumeFacet
    class_class_curie: ClassVar[str] = "observable:VolumeFacet"
    class_name: ClassVar[str] = "VolumeFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.VolumeFacet

    sectorSize: Optional[int] = None
    volumeID: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sectorSize is not None and not isinstance(self.sectorSize, int):
            self.sectorSize = int(self.sectorSize)

        if self.volumeID is not None and not isinstance(self.volumeID, str):
            self.volumeID = str(self.volumeID)

        super().__post_init__(**kwargs)


@dataclass
class WhoisFacet(Facet):
    """
    "A Whois facet is a grouping of characteristics unique to a response record conformant to the WHOIS protocol
    standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WhoisFacet
    class_class_curie: ClassVar[str] = "observable:WhoisFacet"
    class_name: ClassVar[str] = "WhoisFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WhoisFacet

    domainName: Optional[Union[dict, ObservableObject]] = None
    ipAddress: Optional[Union[dict, ObservableObject]] = None
    registrantContactInfo: Optional[Union[dict, ObservableObject]] = None
    serverName: Optional[Union[dict, ObservableObject]] = None
    nameServer: Optional[Union[Union[dict, ObservableObject], List[Union[dict, ObservableObject]]]] = empty_list()
    registrarInfo: Optional[Union[dict, "WhoisRegistrarInfoType"]] = None
    creationDate: Optional[Union[str, XSDDateTime]] = None
    expirationDate: Optional[Union[str, XSDDateTime]] = None
    lookupDate: Optional[Union[str, XSDDateTime]] = None
    updatedDate: Optional[Union[str, XSDDateTime]] = None
    domainID: Optional[str] = None
    remarks: Optional[str] = None
    sponsoringRegistrar: Optional[str] = None
    registrantIDs: Optional[Union[str, List[str]]] = empty_list()
    dnssec: Optional[str] = None
    status: Optional[Union[str, "WhoisStatusTypeEnum"]] = None
    regionalInternetRegistry: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.domainName is not None and not isinstance(self.domainName, ObservableObject):
            self.domainName = ObservableObject(**as_dict(self.domainName))

        if self.ipAddress is not None and not isinstance(self.ipAddress, ObservableObject):
            self.ipAddress = ObservableObject(**as_dict(self.ipAddress))

        if self.registrantContactInfo is not None and not isinstance(self.registrantContactInfo, ObservableObject):
            self.registrantContactInfo = ObservableObject(**as_dict(self.registrantContactInfo))

        if self.serverName is not None and not isinstance(self.serverName, ObservableObject):
            self.serverName = ObservableObject(**as_dict(self.serverName))

        if not isinstance(self.nameServer, list):
            self.nameServer = [self.nameServer] if self.nameServer is not None else []
        self.nameServer = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.nameServer]

        if self.registrarInfo is not None and not isinstance(self.registrarInfo, WhoisRegistrarInfoType):
            self.registrarInfo = WhoisRegistrarInfoType(**as_dict(self.registrarInfo))

        if self.creationDate is not None and not isinstance(self.creationDate, XSDDateTime):
            self.creationDate = XSDDateTime(self.creationDate)

        if self.expirationDate is not None and not isinstance(self.expirationDate, XSDDateTime):
            self.expirationDate = XSDDateTime(self.expirationDate)

        if self.lookupDate is not None and not isinstance(self.lookupDate, XSDDateTime):
            self.lookupDate = XSDDateTime(self.lookupDate)

        if self.updatedDate is not None and not isinstance(self.updatedDate, XSDDateTime):
            self.updatedDate = XSDDateTime(self.updatedDate)

        if self.domainID is not None and not isinstance(self.domainID, str):
            self.domainID = str(self.domainID)

        if self.remarks is not None and not isinstance(self.remarks, str):
            self.remarks = str(self.remarks)

        if self.sponsoringRegistrar is not None and not isinstance(self.sponsoringRegistrar, str):
            self.sponsoringRegistrar = str(self.sponsoringRegistrar)

        if not isinstance(self.registrantIDs, list):
            self.registrantIDs = [self.registrantIDs] if self.registrantIDs is not None else []
        self.registrantIDs = [v if isinstance(v, str) else str(v) for v in self.registrantIDs]

        if self.dnssec is not None and not isinstance(self.dnssec, str):
            self.dnssec = str(self.dnssec)

        if self.status is not None and not isinstance(self.status, WhoisStatusTypeEnum):
            self.status = WhoisStatusTypeEnum(self.status)

        if self.regionalInternetRegistry is not None and not isinstance(self.regionalInternetRegistry, str):
            self.regionalInternetRegistry = str(self.regionalInternetRegistry)

        super().__post_init__(**kwargs)


@dataclass
class WhoisContactFacet(ContactFacet):
    """
    "A Whois contact type is a grouping of characteristics unique to contact-related information present in a response
    record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WhoisContactFacet
    class_class_curie: ClassVar[str] = "observable:WhoisContactFacet"
    class_name: ClassVar[str] = "WhoisContactFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WhoisContactFacet

    whoisContactType: Optional[Union[str, "WhoisContactTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.whoisContactType is not None and not isinstance(self.whoisContactType, WhoisContactTypeEnum):
            self.whoisContactType = WhoisContactTypeEnum(self.whoisContactType)

        super().__post_init__(**kwargs)


@dataclass
class WhoisRegistrarInfoType(UcoInherentCharacterizationThing):
    """
    "A Whois registrarInfo type is a grouping of characteristics unique to registrar-related information present in a
    response record conformant to the WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WhoisRegistrarInfoType
    class_class_curie: ClassVar[str] = "observable:WhoisRegistrarInfoType"
    class_name: ClassVar[str] = "WhoisRegistrarInfoType"
    class_model_uri: ClassVar[URIRef] = MASTER.WhoisRegistrarInfoType

    geoLocationAddress: Optional[Union[dict, Location]] = None
    contactPhoneNumber: Optional[Union[dict, ObservableObject]] = None
    emailAddress: Optional[Union[dict, ObservableObject]] = None
    referralURL: Optional[Union[dict, ObservableObject]] = None
    whoisServer: Optional[Union[dict, ObservableObject]] = None
    registrarGUID: Optional[str] = None
    registrarID: Optional[str] = None
    registrarName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.geoLocationAddress is not None and not isinstance(self.geoLocationAddress, Location):
            self.geoLocationAddress = Location(**as_dict(self.geoLocationAddress))

        if self.contactPhoneNumber is not None and not isinstance(self.contactPhoneNumber, ObservableObject):
            self.contactPhoneNumber = ObservableObject(**as_dict(self.contactPhoneNumber))

        if self.emailAddress is not None and not isinstance(self.emailAddress, ObservableObject):
            self.emailAddress = ObservableObject(**as_dict(self.emailAddress))

        if self.referralURL is not None and not isinstance(self.referralURL, ObservableObject):
            self.referralURL = ObservableObject(**as_dict(self.referralURL))

        if self.whoisServer is not None and not isinstance(self.whoisServer, ObservableObject):
            self.whoisServer = ObservableObject(**as_dict(self.whoisServer))

        if self.registrarGUID is not None and not isinstance(self.registrarGUID, str):
            self.registrarGUID = str(self.registrarGUID)

        if self.registrarID is not None and not isinstance(self.registrarID, str):
            self.registrarID = str(self.registrarID)

        if self.registrarName is not None and not isinstance(self.registrarName, str):
            self.registrarName = str(self.registrarName)

        super().__post_init__(**kwargs)


class WifiAddressFacet(MACAddressFacet):
    """
    "A Wi-Fi address facet is a grouping of characteristics unique to a media access control (MAC) standards
    conformant identifier assigned to a device networkInterface to enable routing and management of IEEE 802.11
    standards-conformant communications to and from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WifiAddressFacet
    class_class_curie: ClassVar[str] = "observable:WifiAddressFacet"
    class_name: ClassVar[str] = "WifiAddressFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WifiAddressFacet


@dataclass
class WindowsAccountFacet(Facet):
    """
    "A Windows account facet is a grouping of characteristics unique to a user account on a Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsAccountFacet
    class_class_curie: ClassVar[str] = "observable:WindowsAccountFacet"
    class_name: ClassVar[str] = "WindowsAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsAccountFacet

    groups: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.groups, list):
            self.groups = [self.groups] if self.groups is not None else []
        self.groups = [v if isinstance(v, str) else str(v) for v in self.groups]

        super().__post_init__(**kwargs)


@dataclass
class WindowsActiveDirectoryAccountFacet(Facet):
    """
    "A Windows Active Directory account facet is a grouping of characteristics unique to an account managed by
    directory-based identity-related services of a Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsActiveDirectoryAccountFacet
    class_class_curie: ClassVar[str] = "observable:WindowsActiveDirectoryAccountFacet"
    class_name: ClassVar[str] = "WindowsActiveDirectoryAccountFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsActiveDirectoryAccountFacet

    objectGUID: Optional[str] = None
    activeDirectoryGroups: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.objectGUID is not None and not isinstance(self.objectGUID, str):
            self.objectGUID = str(self.objectGUID)

        if not isinstance(self.activeDirectoryGroups, list):
            self.activeDirectoryGroups = [self.activeDirectoryGroups] if self.activeDirectoryGroups is not None else []
        self.activeDirectoryGroups = [v if isinstance(v, str) else str(v) for v in self.activeDirectoryGroups]

        super().__post_init__(**kwargs)


@dataclass
class WindowsComputerSpecificationFacet(Facet):
    """
    "A Windows computer specification facet is a grouping of characteristics unique to the hardware and software of a
    programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating
    system. [based on merriam-webster.com/dictionary/computer]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsComputerSpecificationFacet
    class_class_curie: ClassVar[str] = "observable:WindowsComputerSpecificationFacet"
    class_name: ClassVar[str] = "WindowsComputerSpecificationFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsComputerSpecificationFacet

    registeredOrganization: Optional[Union[dict, Identity]] = None
    registeredOwner: Optional[Union[dict, Identity]] = None
    globalFlagList: Optional[Union[Union[dict, GlobalFlagType], List[Union[dict, GlobalFlagType]]]] = empty_list()
    windowsDirectory: Optional[Union[dict, ObservableObject]] = None
    windowsSystemDirectory: Optional[Union[dict, ObservableObject]] = None
    windowsTempDirectory: Optional[Union[dict, ObservableObject]] = None
    lastShutdownDate: Optional[Union[str, XSDDateTime]] = None
    osInstallDate: Optional[Union[str, XSDDateTime]] = None
    osLastUpgradeDate: Optional[Union[str, XSDDateTime]] = None
    msProductID: Optional[str] = None
    msProductName: Optional[str] = None
    netBIOSName: Optional[str] = None
    domain: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.registeredOrganization is not None and not isinstance(self.registeredOrganization, Identity):
            self.registeredOrganization = Identity(**as_dict(self.registeredOrganization))

        if self.registeredOwner is not None and not isinstance(self.registeredOwner, Identity):
            self.registeredOwner = Identity(**as_dict(self.registeredOwner))

        if not isinstance(self.globalFlagList, list):
            self.globalFlagList = [self.globalFlagList] if self.globalFlagList is not None else []
        self.globalFlagList = [v if isinstance(v, GlobalFlagType) else GlobalFlagType(**as_dict(v)) for v in self.globalFlagList]

        if self.windowsDirectory is not None and not isinstance(self.windowsDirectory, ObservableObject):
            self.windowsDirectory = ObservableObject(**as_dict(self.windowsDirectory))

        if self.windowsSystemDirectory is not None and not isinstance(self.windowsSystemDirectory, ObservableObject):
            self.windowsSystemDirectory = ObservableObject(**as_dict(self.windowsSystemDirectory))

        if self.windowsTempDirectory is not None and not isinstance(self.windowsTempDirectory, ObservableObject):
            self.windowsTempDirectory = ObservableObject(**as_dict(self.windowsTempDirectory))

        if self.lastShutdownDate is not None and not isinstance(self.lastShutdownDate, XSDDateTime):
            self.lastShutdownDate = XSDDateTime(self.lastShutdownDate)

        if self.osInstallDate is not None and not isinstance(self.osInstallDate, XSDDateTime):
            self.osInstallDate = XSDDateTime(self.osInstallDate)

        if self.osLastUpgradeDate is not None and not isinstance(self.osLastUpgradeDate, XSDDateTime):
            self.osLastUpgradeDate = XSDDateTime(self.osLastUpgradeDate)

        if self.msProductID is not None and not isinstance(self.msProductID, str):
            self.msProductID = str(self.msProductID)

        if self.msProductName is not None and not isinstance(self.msProductName, str):
            self.msProductName = str(self.msProductName)

        if self.netBIOSName is not None and not isinstance(self.netBIOSName, str):
            self.netBIOSName = str(self.netBIOSName)

        if not isinstance(self.domain, list):
            self.domain = [self.domain] if self.domain is not None else []
        self.domain = [v if isinstance(v, str) else str(v) for v in self.domain]

        super().__post_init__(**kwargs)


@dataclass
class WindowsPEBinaryFileFacet(Facet):
    """
    "A Windows PE binary file facet is a grouping of characteristics unique to a Windows portable executable (PE)
    file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPEBinaryFileFacet
    class_class_curie: ClassVar[str] = "observable:WindowsPEBinaryFileFacet"
    class_name: ClassVar[str] = "WindowsPEBinaryFileFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPEBinaryFileFacet

    optionalHeader: Optional[Union[dict, "WindowsPEOptionalHeader"]] = None
    sections: Optional[Union[Union[dict, "WindowsPESection"], List[Union[dict, "WindowsPESection"]]]] = empty_list()
    fileHeaderHashes: Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]] = empty_list()
    timeDateStamp: Optional[Union[str, XSDDateTime]] = None
    pointerToSymbolTable: Optional[Union[hex, List[hex]]] = empty_list()
    numberOfSections: Optional[int] = None
    numberOfSymbols: Optional[int] = None
    sizeOfOptionalHeader: Optional[int] = None
    impHash: Optional[str] = None
    peType: Optional[str] = None
    machine: Optional[Union[str, List[str]]] = empty_list()
    characteristics: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.optionalHeader is not None and not isinstance(self.optionalHeader, WindowsPEOptionalHeader):
            self.optionalHeader = WindowsPEOptionalHeader(**as_dict(self.optionalHeader))

        if not isinstance(self.sections, list):
            self.sections = [self.sections] if self.sections is not None else []
        self.sections = [v if isinstance(v, WindowsPESection) else WindowsPESection(**as_dict(v)) for v in self.sections]

        self._normalize_inlined_as_dict(slot_name="fileHeaderHashes", slot_type=Hash, key_name="hashValue", keyed=False)

        if self.timeDateStamp is not None and not isinstance(self.timeDateStamp, XSDDateTime):
            self.timeDateStamp = XSDDateTime(self.timeDateStamp)

        if not isinstance(self.pointerToSymbolTable, list):
            self.pointerToSymbolTable = [self.pointerToSymbolTable] if self.pointerToSymbolTable is not None else []
        self.pointerToSymbolTable = [v if isinstance(v, hex) else hex(v) for v in self.pointerToSymbolTable]

        if self.numberOfSections is not None and not isinstance(self.numberOfSections, int):
            self.numberOfSections = int(self.numberOfSections)

        if self.numberOfSymbols is not None and not isinstance(self.numberOfSymbols, int):
            self.numberOfSymbols = int(self.numberOfSymbols)

        if self.sizeOfOptionalHeader is not None and not isinstance(self.sizeOfOptionalHeader, int):
            self.sizeOfOptionalHeader = int(self.sizeOfOptionalHeader)

        if self.impHash is not None and not isinstance(self.impHash, str):
            self.impHash = str(self.impHash)

        if self.peType is not None and not isinstance(self.peType, str):
            self.peType = str(self.peType)

        if not isinstance(self.machine, list):
            self.machine = [self.machine] if self.machine is not None else []
        self.machine = [v if isinstance(v, str) else str(v) for v in self.machine]

        if not isinstance(self.characteristics, list):
            self.characteristics = [self.characteristics] if self.characteristics is not None else []
        self.characteristics = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.characteristics]

        super().__post_init__(**kwargs)


class WindowsPEBinaryType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPEBinaryType
    class_class_curie: ClassVar[str] = "observable:WindowsPEBinaryType"
    class_name: ClassVar[str] = "WindowsPEBinaryType"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPEBinaryType


@dataclass
class WindowsPEFileHheader(UcoInherentCharacterizationThing):
    """
    "A Windows PE file header is a grouping of characteristics unique to the 'header' of a Windows PE (Portable
    Executable) file, consisting of a collection of metadata about the overall nature and structure of the file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPEFileHheader
    class_class_curie: ClassVar[str] = "observable:WindowsPEFileHheader"
    class_name: ClassVar[str] = "WindowsPEFileHheader"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPEFileHheader

    timeDateStamp: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.timeDateStamp is not None and not isinstance(self.timeDateStamp, XSDDateTime):
            self.timeDateStamp = XSDDateTime(self.timeDateStamp)

        super().__post_init__(**kwargs)


@dataclass
class WindowsPEOptionalHeader(UcoInherentCharacterizationThing):
    """
    "A Windows PE optional header is a grouping of characteristics unique to the 'optionalHeader' of a Windows PE
    (Portable Executable) file, consisting of a collection of metadata about the executable code structure of the
    file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPEOptionalHeader
    class_class_curie: ClassVar[str] = "observable:WindowsPEOptionalHeader"
    class_name: ClassVar[str] = "WindowsPEOptionalHeader"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPEOptionalHeader

    majorLinkerVersion: Optional[Union[Union[int, ByteType], List[Union[int, ByteType]]]] = empty_list()
    minorLinkerVersion: Optional[Union[Union[int, ByteType], List[Union[int, ByteType]]]] = empty_list()
    addressOfEntryPoint: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    baseOfCode: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    checksum: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    fileAlignment: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    imageBase: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    loaderFlags: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    numberOfRVAAndSizes: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sectionAlignment: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfCode: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfHeaders: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfHeapCommit: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfHeapReserve: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfImage: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfInitializedData: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfStackCommit: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfStackReserve: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    sizeOfUninitializedData: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    win32VersionValue: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()
    dllCharacteristics: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    magic: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    majorImageVersion: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    majorOSVersion: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    majorSubsystemVersion: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    minorImageVersion: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    minorOSVersion: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    minorSubsystemVersion: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()
    subsystem: Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.majorLinkerVersion, list):
            self.majorLinkerVersion = [self.majorLinkerVersion] if self.majorLinkerVersion is not None else []
        self.majorLinkerVersion = [v if isinstance(v, ByteType) else ByteType(v) for v in self.majorLinkerVersion]

        if not isinstance(self.minorLinkerVersion, list):
            self.minorLinkerVersion = [self.minorLinkerVersion] if self.minorLinkerVersion is not None else []
        self.minorLinkerVersion = [v if isinstance(v, ByteType) else ByteType(v) for v in self.minorLinkerVersion]

        if not isinstance(self.addressOfEntryPoint, list):
            self.addressOfEntryPoint = [self.addressOfEntryPoint] if self.addressOfEntryPoint is not None else []
        self.addressOfEntryPoint = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.addressOfEntryPoint]

        if not isinstance(self.baseOfCode, list):
            self.baseOfCode = [self.baseOfCode] if self.baseOfCode is not None else []
        self.baseOfCode = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.baseOfCode]

        if not isinstance(self.checksum, list):
            self.checksum = [self.checksum] if self.checksum is not None else []
        self.checksum = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.checksum]

        if not isinstance(self.fileAlignment, list):
            self.fileAlignment = [self.fileAlignment] if self.fileAlignment is not None else []
        self.fileAlignment = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.fileAlignment]

        if not isinstance(self.imageBase, list):
            self.imageBase = [self.imageBase] if self.imageBase is not None else []
        self.imageBase = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.imageBase]

        if not isinstance(self.loaderFlags, list):
            self.loaderFlags = [self.loaderFlags] if self.loaderFlags is not None else []
        self.loaderFlags = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.loaderFlags]

        if not isinstance(self.numberOfRVAAndSizes, list):
            self.numberOfRVAAndSizes = [self.numberOfRVAAndSizes] if self.numberOfRVAAndSizes is not None else []
        self.numberOfRVAAndSizes = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.numberOfRVAAndSizes]

        if not isinstance(self.sectionAlignment, list):
            self.sectionAlignment = [self.sectionAlignment] if self.sectionAlignment is not None else []
        self.sectionAlignment = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sectionAlignment]

        if not isinstance(self.sizeOfCode, list):
            self.sizeOfCode = [self.sizeOfCode] if self.sizeOfCode is not None else []
        self.sizeOfCode = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfCode]

        if not isinstance(self.sizeOfHeaders, list):
            self.sizeOfHeaders = [self.sizeOfHeaders] if self.sizeOfHeaders is not None else []
        self.sizeOfHeaders = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfHeaders]

        if not isinstance(self.sizeOfHeapCommit, list):
            self.sizeOfHeapCommit = [self.sizeOfHeapCommit] if self.sizeOfHeapCommit is not None else []
        self.sizeOfHeapCommit = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfHeapCommit]

        if not isinstance(self.sizeOfHeapReserve, list):
            self.sizeOfHeapReserve = [self.sizeOfHeapReserve] if self.sizeOfHeapReserve is not None else []
        self.sizeOfHeapReserve = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfHeapReserve]

        if not isinstance(self.sizeOfImage, list):
            self.sizeOfImage = [self.sizeOfImage] if self.sizeOfImage is not None else []
        self.sizeOfImage = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfImage]

        if not isinstance(self.sizeOfInitializedData, list):
            self.sizeOfInitializedData = [self.sizeOfInitializedData] if self.sizeOfInitializedData is not None else []
        self.sizeOfInitializedData = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfInitializedData]

        if not isinstance(self.sizeOfStackCommit, list):
            self.sizeOfStackCommit = [self.sizeOfStackCommit] if self.sizeOfStackCommit is not None else []
        self.sizeOfStackCommit = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfStackCommit]

        if not isinstance(self.sizeOfStackReserve, list):
            self.sizeOfStackReserve = [self.sizeOfStackReserve] if self.sizeOfStackReserve is not None else []
        self.sizeOfStackReserve = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfStackReserve]

        if not isinstance(self.sizeOfUninitializedData, list):
            self.sizeOfUninitializedData = [self.sizeOfUninitializedData] if self.sizeOfUninitializedData is not None else []
        self.sizeOfUninitializedData = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.sizeOfUninitializedData]

        if not isinstance(self.win32VersionValue, list):
            self.win32VersionValue = [self.win32VersionValue] if self.win32VersionValue is not None else []
        self.win32VersionValue = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.win32VersionValue]

        if not isinstance(self.dllCharacteristics, list):
            self.dllCharacteristics = [self.dllCharacteristics] if self.dllCharacteristics is not None else []
        self.dllCharacteristics = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.dllCharacteristics]

        if not isinstance(self.magic, list):
            self.magic = [self.magic] if self.magic is not None else []
        self.magic = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.magic]

        if not isinstance(self.majorImageVersion, list):
            self.majorImageVersion = [self.majorImageVersion] if self.majorImageVersion is not None else []
        self.majorImageVersion = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.majorImageVersion]

        if not isinstance(self.majorOSVersion, list):
            self.majorOSVersion = [self.majorOSVersion] if self.majorOSVersion is not None else []
        self.majorOSVersion = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.majorOSVersion]

        if not isinstance(self.majorSubsystemVersion, list):
            self.majorSubsystemVersion = [self.majorSubsystemVersion] if self.majorSubsystemVersion is not None else []
        self.majorSubsystemVersion = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.majorSubsystemVersion]

        if not isinstance(self.minorImageVersion, list):
            self.minorImageVersion = [self.minorImageVersion] if self.minorImageVersion is not None else []
        self.minorImageVersion = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.minorImageVersion]

        if not isinstance(self.minorOSVersion, list):
            self.minorOSVersion = [self.minorOSVersion] if self.minorOSVersion is not None else []
        self.minorOSVersion = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.minorOSVersion]

        if not isinstance(self.minorSubsystemVersion, list):
            self.minorSubsystemVersion = [self.minorSubsystemVersion] if self.minorSubsystemVersion is not None else []
        self.minorSubsystemVersion = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.minorSubsystemVersion]

        if not isinstance(self.subsystem, list):
            self.subsystem = [self.subsystem] if self.subsystem is not None else []
        self.subsystem = [v if isinstance(v, UnsignedShortType) else UnsignedShortType(v) for v in self.subsystem]

        super().__post_init__(**kwargs)


@dataclass
class WindowsPESection(UcoInherentCharacterizationThing):
    """
    "A Windows PE section is a grouping of characteristics unique to a specific default or custom-defined region of a
    Windows PE (Portable Executable) file, consisting of an individual portion of the actual executable content of the
    file delineated according to unique purpose and memory protection requirements."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPESection
    class_class_curie: ClassVar[str] = "observable:WindowsPESection"
    class_name: ClassVar[str] = "WindowsPESection"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPESection

    hashes: Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]] = empty_list()
    entropy: Optional[Union[Decimal, DecimalType]] = None
    size: Optional[Union[int, PositiveInteger]] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="hashes", slot_type=Hash, key_name="hashValue", keyed=False)

        if self.entropy is not None and not isinstance(self.entropy, DecimalType):
            self.entropy = DecimalType(self.entropy)

        if self.size is not None and not isinstance(self.size, PositiveInteger):
            self.size = PositiveInteger(self.size)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class WindowsPrefetchFacet(Facet):
    """
    "A Windows prefetch facet is a grouping of characteristics unique to entries in the Windows prefetch file (used to
    speed up application startup starting with Windows XP)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPrefetchFacet
    class_class_curie: ClassVar[str] = "observable:WindowsPrefetchFacet"
    class_name: ClassVar[str] = "WindowsPrefetchFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPrefetchFacet

    volume: Optional[Union[dict, ObservableObject]] = None
    accessedDirectory: Optional[Union[Union[dict, ObservableObject], List[Union[dict, ObservableObject]]]] = empty_list()
    accessedFile: Optional[Union[Union[dict, ObservableObject], List[Union[dict, ObservableObject]]]] = empty_list()
    firstRun: Optional[Union[str, XSDDateTime]] = None
    lastRun: Optional[Union[str, XSDDateTime]] = None
    timesExecuted: Optional[int] = None
    applicationFileName: Optional[str] = None
    prefetchHash: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.volume is not None and not isinstance(self.volume, ObservableObject):
            self.volume = ObservableObject(**as_dict(self.volume))

        if not isinstance(self.accessedDirectory, list):
            self.accessedDirectory = [self.accessedDirectory] if self.accessedDirectory is not None else []
        self.accessedDirectory = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.accessedDirectory]

        if not isinstance(self.accessedFile, list):
            self.accessedFile = [self.accessedFile] if self.accessedFile is not None else []
        self.accessedFile = [v if isinstance(v, ObservableObject) else ObservableObject(**as_dict(v)) for v in self.accessedFile]

        if self.firstRun is not None and not isinstance(self.firstRun, XSDDateTime):
            self.firstRun = XSDDateTime(self.firstRun)

        if self.lastRun is not None and not isinstance(self.lastRun, XSDDateTime):
            self.lastRun = XSDDateTime(self.lastRun)

        if self.timesExecuted is not None and not isinstance(self.timesExecuted, int):
            self.timesExecuted = int(self.timesExecuted)

        if self.applicationFileName is not None and not isinstance(self.applicationFileName, str):
            self.applicationFileName = str(self.applicationFileName)

        if self.prefetchHash is not None and not isinstance(self.prefetchHash, str):
            self.prefetchHash = str(self.prefetchHash)

        super().__post_init__(**kwargs)


@dataclass
class WindowsProcessFacet(Facet):
    """
    "A Windows process facet is a grouping of characteristics unique to a program running on a Windows operating
    system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsProcessFacet
    class_class_curie: ClassVar[str] = "observable:WindowsProcessFacet"
    class_name: ClassVar[str] = "WindowsProcessFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsProcessFacet

    startupInfo: Optional[Union[dict, "Dictionary"]] = None
    aslrEnabled: Optional[Union[bool, BooleanType]] = None
    depEnabled: Optional[Union[bool, BooleanType]] = None
    ownerSID: Optional[str] = None
    priority: Optional[str] = None
    windowTitle: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.startupInfo is not None and not isinstance(self.startupInfo, Dictionary):
            self.startupInfo = Dictionary(**as_dict(self.startupInfo))

        if self.aslrEnabled is not None and not isinstance(self.aslrEnabled, BooleanType):
            self.aslrEnabled = BooleanType(self.aslrEnabled)

        if self.depEnabled is not None and not isinstance(self.depEnabled, BooleanType):
            self.depEnabled = BooleanType(self.depEnabled)

        if self.ownerSID is not None and not isinstance(self.ownerSID, str):
            self.ownerSID = str(self.ownerSID)

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if self.windowTitle is not None and not isinstance(self.windowTitle, str):
            self.windowTitle = str(self.windowTitle)

        super().__post_init__(**kwargs)


@dataclass
class WindowsRegistryHiveFacet(Facet):
    """
    "A Windows registry hive facet is a grouping of characteristics unique to a particular logical group of keys,
    subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the
    Microsoft Windows operating sytem and for applications that opt to use the registry). [based on
    https://en.wikipedia.org/wiki/Windows_Registry]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsRegistryHiveFacet
    class_class_curie: ClassVar[str] = "observable:WindowsRegistryHiveFacet"
    class_name: ClassVar[str] = "WindowsRegistryHiveFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsRegistryHiveFacet

    hiveType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hiveType is not None and not isinstance(self.hiveType, str):
            self.hiveType = str(self.hiveType)

        super().__post_init__(**kwargs)


@dataclass
class WindowsRegistrykeyFacet(Facet):
    """
    "A Windows registry key facet is a grouping of characteristics unique to a particular key within a Windows
    registry (A hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for
    applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsRegistrykeyFacet
    class_class_curie: ClassVar[str] = "observable:WindowsRegistrykeyFacet"
    class_name: ClassVar[str] = "WindowsRegistrykeyFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsRegistrykeyFacet

    creator: Optional[Union[dict, ObservableObject]] = None
    registryValues: Optional[Union[Union[dict, "WindowsRegistryValue"], List[Union[dict, "WindowsRegistryValue"]]]] = empty_list()
    modifiedTime: Optional[Union[str, XSDDateTime]] = None
    numberOfSubkeys: Optional[int] = None
    key: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.creator is not None and not isinstance(self.creator, ObservableObject):
            self.creator = ObservableObject(**as_dict(self.creator))

        if not isinstance(self.registryValues, list):
            self.registryValues = [self.registryValues] if self.registryValues is not None else []
        self.registryValues = [v if isinstance(v, WindowsRegistryValue) else WindowsRegistryValue(**as_dict(v)) for v in self.registryValues]

        if self.modifiedTime is not None and not isinstance(self.modifiedTime, XSDDateTime):
            self.modifiedTime = XSDDateTime(self.modifiedTime)

        if self.numberOfSubkeys is not None and not isinstance(self.numberOfSubkeys, int):
            self.numberOfSubkeys = int(self.numberOfSubkeys)

        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        super().__post_init__(**kwargs)


@dataclass
class WindowsRegistryValue(UcoInherentCharacterizationThing):
    """
    "A Windows registry value is a grouping of characteristics unique to a particular value within a Windows registry
    (a hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for
    applications that opt to use the registry. [based on https://en.wikipedia.org/wiki/Windows_Registry]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsRegistryValue
    class_class_curie: ClassVar[str] = "observable:WindowsRegistryValue"
    class_name: ClassVar[str] = "WindowsRegistryValue"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsRegistryValue

    name: Optional[str] = None
    data: Optional[str] = None
    dataType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.data is not None and not isinstance(self.data, str):
            self.data = str(self.data)

        if self.dataType is not None and not isinstance(self.dataType, str):
            self.dataType = str(self.dataType)

        super().__post_init__(**kwargs)


@dataclass
class WindowsServiceFacet(Facet):
    """
    "A Windows service facet is a grouping of characteristics unique to a specific Windows service (a computer program
    that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX ).
    [based on https://en.wikipedia.org/wiki/Windows_service]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsServiceFacet
    class_class_curie: ClassVar[str] = "observable:WindowsServiceFacet"
    class_name: ClassVar[str] = "WindowsServiceFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsServiceFacet

    displayName: Optional[str] = None
    groupName: Optional[str] = None
    serviceName: Optional[str] = None
    servicStatus: Optional[str] = None
    serviceType: Optional[str] = None
    startCommandLine: Optional[str] = None
    startType: Optional[str] = None
    descriptions: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.displayName is not None and not isinstance(self.displayName, str):
            self.displayName = str(self.displayName)

        if self.groupName is not None and not isinstance(self.groupName, str):
            self.groupName = str(self.groupName)

        if self.serviceName is not None and not isinstance(self.serviceName, str):
            self.serviceName = str(self.serviceName)

        if self.servicStatus is not None and not isinstance(self.servicStatus, str):
            self.servicStatus = str(self.servicStatus)

        if self.serviceType is not None and not isinstance(self.serviceType, str):
            self.serviceType = str(self.serviceType)

        if self.startCommandLine is not None and not isinstance(self.startCommandLine, str):
            self.startCommandLine = str(self.startCommandLine)

        if self.startType is not None and not isinstance(self.startType, str):
            self.startType = str(self.startType)

        if not isinstance(self.descriptions, list):
            self.descriptions = [self.descriptions] if self.descriptions is not None else []
        self.descriptions = [v if isinstance(v, str) else str(v) for v in self.descriptions]

        super().__post_init__(**kwargs)


class WindowsServiceStartType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsServiceStartType
    class_class_curie: ClassVar[str] = "observable:WindowsServiceStartType"
    class_name: ClassVar[str] = "WindowsServiceStartType"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsServiceStartType


class WindowsServiceStatus(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsServiceStatus
    class_class_curie: ClassVar[str] = "observable:WindowsServiceStatus"
    class_name: ClassVar[str] = "WindowsServiceStatus"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsServiceStatus


class WindowsServiceType(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsServiceType
    class_class_curie: ClassVar[str] = "observable:WindowsServiceType"
    class_name: ClassVar[str] = "WindowsServiceType"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsServiceType


@dataclass
class WindowsTaskFacet(Facet):
    """
    "A Windows Task facet is a grouping of characteristics unique to a Windows Task (a process that is scheduled to
    execute on a Windows operating system by the Windows Task Scheduler). [based on
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsTaskFacet
    class_class_curie: ClassVar[str] = "observable:WindowsTaskFacet"
    class_name: ClassVar[str] = "WindowsTaskFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsTaskFacet

    account: Optional[Union[dict, ObservableObject]] = None
    application: Optional[Union[dict, ObservableObject]] = None
    workItemData: Optional[Union[dict, ObservableObject]] = None
    workingDirectory: Optional[Union[dict, ObservableObject]] = None
    actionList: Optional[Union[Union[dict, TaskActionType], List[Union[dict, TaskActionType]]]] = empty_list()
    triggerList: Optional[Union[str, List[str]]] = empty_list()
    mostRecentRunTime: Optional[Union[str, XSDDateTime]] = None
    nextRunTime: Optional[Union[str, XSDDateTime]] = None
    observableCreatedTime: Optional[Union[str, XSDDateTime]] = None
    exitCode: Optional[int] = None
    maxRunTime: Optional[int] = None
    accountLogonType: Optional[str] = None
    accountRunLevel: Optional[str] = None
    imageName: Optional[str] = None
    parameters: Optional[str] = None
    taskComment: Optional[str] = None
    taskCreator: Optional[str] = None
    flags: Optional[Union[str, "TaskFlagEnum"]] = None
    priority: Optional[Union[str, "TaskPriorityEnum"]] = None
    status: Optional[Union[str, "TaskStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.account is not None and not isinstance(self.account, ObservableObject):
            self.account = ObservableObject(**as_dict(self.account))

        if self.application is not None and not isinstance(self.application, ObservableObject):
            self.application = ObservableObject(**as_dict(self.application))

        if self.workItemData is not None and not isinstance(self.workItemData, ObservableObject):
            self.workItemData = ObservableObject(**as_dict(self.workItemData))

        if self.workingDirectory is not None and not isinstance(self.workingDirectory, ObservableObject):
            self.workingDirectory = ObservableObject(**as_dict(self.workingDirectory))

        if not isinstance(self.actionList, list):
            self.actionList = [self.actionList] if self.actionList is not None else []
        self.actionList = [v if isinstance(v, TaskActionType) else TaskActionType(**as_dict(v)) for v in self.actionList]

        if not isinstance(self.triggerList, list):
            self.triggerList = [self.triggerList] if self.triggerList is not None else []
        self.triggerList = [v if isinstance(v, str) else str(v) for v in self.triggerList]

        if self.mostRecentRunTime is not None and not isinstance(self.mostRecentRunTime, XSDDateTime):
            self.mostRecentRunTime = XSDDateTime(self.mostRecentRunTime)

        if self.nextRunTime is not None and not isinstance(self.nextRunTime, XSDDateTime):
            self.nextRunTime = XSDDateTime(self.nextRunTime)

        if self.observableCreatedTime is not None and not isinstance(self.observableCreatedTime, XSDDateTime):
            self.observableCreatedTime = XSDDateTime(self.observableCreatedTime)

        if self.exitCode is not None and not isinstance(self.exitCode, int):
            self.exitCode = int(self.exitCode)

        if self.maxRunTime is not None and not isinstance(self.maxRunTime, int):
            self.maxRunTime = int(self.maxRunTime)

        if self.accountLogonType is not None and not isinstance(self.accountLogonType, str):
            self.accountLogonType = str(self.accountLogonType)

        if self.accountRunLevel is not None and not isinstance(self.accountRunLevel, str):
            self.accountRunLevel = str(self.accountRunLevel)

        if self.imageName is not None and not isinstance(self.imageName, str):
            self.imageName = str(self.imageName)

        if self.parameters is not None and not isinstance(self.parameters, str):
            self.parameters = str(self.parameters)

        if self.taskComment is not None and not isinstance(self.taskComment, str):
            self.taskComment = str(self.taskComment)

        if self.taskCreator is not None and not isinstance(self.taskCreator, str):
            self.taskCreator = str(self.taskCreator)

        if self.flags is not None and not isinstance(self.flags, TaskFlagEnum):
            self.flags = TaskFlagEnum(self.flags)

        if self.priority is not None and not isinstance(self.priority, TaskPriorityEnum):
            self.priority = TaskPriorityEnum(self.priority)

        if self.status is not None and not isinstance(self.status, TaskStatusEnum):
            self.status = TaskStatusEnum(self.status)

        super().__post_init__(**kwargs)


@dataclass
class WindowsThreadFacet(Facet):
    """
    "A Windows thread facet is a grouping os characteristics unique to a single thread of execution within a Windows
    process."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsThreadFacet
    class_class_curie: ClassVar[str] = "observable:WindowsThreadFacet"
    class_name: ClassVar[str] = "WindowsThreadFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsThreadFacet

    creationTime: Optional[Union[str, XSDDateTime]] = None
    parameterAddress: Optional[Union[hex, List[hex]]] = empty_list()
    startAddress: Optional[Union[hex, List[hex]]] = empty_list()
    priority: Optional[str] = None
    stackSize: Optional[Union[Union[int, NonNegativeIntegerType], List[Union[int, NonNegativeIntegerType]]]] = empty_list()
    threadID: Optional[Union[Union[int, NonNegativeIntegerType], List[Union[int, NonNegativeIntegerType]]]] = empty_list()
    context: Optional[str] = None
    runningStatus: Optional[str] = None
    securityAttributes: Optional[str] = None
    creationFlags: Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.creationTime is not None and not isinstance(self.creationTime, XSDDateTime):
            self.creationTime = XSDDateTime(self.creationTime)

        if not isinstance(self.parameterAddress, list):
            self.parameterAddress = [self.parameterAddress] if self.parameterAddress is not None else []
        self.parameterAddress = [v if isinstance(v, hex) else hex(v) for v in self.parameterAddress]

        if not isinstance(self.startAddress, list):
            self.startAddress = [self.startAddress] if self.startAddress is not None else []
        self.startAddress = [v if isinstance(v, hex) else hex(v) for v in self.startAddress]

        if self.priority is not None and not isinstance(self.priority, str):
            self.priority = str(self.priority)

        if not isinstance(self.stackSize, list):
            self.stackSize = [self.stackSize] if self.stackSize is not None else []
        self.stackSize = [v if isinstance(v, NonNegativeIntegerType) else NonNegativeIntegerType(v) for v in self.stackSize]

        if not isinstance(self.threadID, list):
            self.threadID = [self.threadID] if self.threadID is not None else []
        self.threadID = [v if isinstance(v, NonNegativeIntegerType) else NonNegativeIntegerType(v) for v in self.threadID]

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.runningStatus is not None and not isinstance(self.runningStatus, str):
            self.runningStatus = str(self.runningStatus)

        if self.securityAttributes is not None and not isinstance(self.securityAttributes, str):
            self.securityAttributes = str(self.securityAttributes)

        if not isinstance(self.creationFlags, list):
            self.creationFlags = [self.creationFlags] if self.creationFlags is not None else []
        self.creationFlags = [v if isinstance(v, UnsignedIntegerType) else UnsignedIntegerType(v) for v in self.creationFlags]

        super().__post_init__(**kwargs)


@dataclass
class WindowsVolumeFacet(Facet):
    """
    "A Windows volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with
    a single windows file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsVolumeFacet
    class_class_curie: ClassVar[str] = "observable:WindowsVolumeFacet"
    class_name: ClassVar[str] = "WindowsVolumeFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsVolumeFacet

    driveLetter: Optional[str] = None
    driveType: Optional[Union[str, "WindowsDriveTypeEnum"]] = None
    windowsVolumeAttributes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.driveLetter is not None and not isinstance(self.driveLetter, str):
            self.driveLetter = str(self.driveLetter)

        if self.driveType is not None and not isinstance(self.driveType, WindowsDriveTypeEnum):
            self.driveType = WindowsDriveTypeEnum(self.driveType)

        if self.windowsVolumeAttributes is not None and not isinstance(self.windowsVolumeAttributes, str):
            self.windowsVolumeAttributes = str(self.windowsVolumeAttributes)

        super().__post_init__(**kwargs)


@dataclass
class WirelessNetworkConnectionFacet(Facet):
    """
    "A wireless network connection facet is a grouping of characteristics unique to a connection (completed or
    attempted) across an IEEE 802.11 standards-conformant digital network (a group of two or more computer systems
    linked together). [based on https://www.webopedia.com/TERM/N/network.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WirelessNetworkConnectionFacet
    class_class_curie: ClassVar[str] = "observable:WirelessNetworkConnectionFacet"
    class_name: ClassVar[str] = "WirelessNetworkConnectionFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.WirelessNetworkConnectionFacet

    baseStation: Optional[str] = None
    password: Optional[str] = None
    ssid: Optional[str] = None
    wirelessNetworkSecurityMode: Optional[Union[str, "WirelessNetworkSecurityModeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.baseStation is not None and not isinstance(self.baseStation, str):
            self.baseStation = str(self.baseStation)

        if self.password is not None and not isinstance(self.password, str):
            self.password = str(self.password)

        if self.ssid is not None and not isinstance(self.ssid, str):
            self.ssid = str(self.ssid)

        if self.wirelessNetworkSecurityMode is not None and not isinstance(self.wirelessNetworkSecurityMode, WirelessNetworkSecurityModeEnum):
            self.wirelessNetworkSecurityMode = WirelessNetworkSecurityModeEnum(self.wirelessNetworkSecurityMode)

        super().__post_init__(**kwargs)


@dataclass
class X509CertificateFacet(Facet):
    """
    "A X.509 certificate facet is a grouping of characteristics unique to a public key digital identity certificate
    conformant to the X.509 PKI (Public Key Infrastructure) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.X509CertificateFacet
    class_class_curie: ClassVar[str] = "observable:X509CertificateFacet"
    class_name: ClassVar[str] = "X509CertificateFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.X509CertificateFacet

    x509v3extensions: Optional[Union[dict, "X509V3ExtensionsFacet"]] = None
    issuerHash: Optional[Union[dict, "Hash"]] = None
    subjectHash: Optional[Union[dict, "Hash"]] = None
    thumbprintHash: Optional[Union[dict, "Hash"]] = None
    isSelfSigned: Optional[Union[bool, BooleanType]] = None
    validityNotAfter: Optional[Union[str, XSDDateTime]] = None
    validityNotBefore: Optional[Union[str, XSDDateTime]] = None
    subjectPublicKeyExponent: Optional[int] = None
    issuer: Optional[str] = None
    serialNumber: Optional[str] = None
    signature: Optional[str] = None
    signatureAlgorithm: Optional[str] = None
    subject: Optional[str] = None
    subjectPublicKeyAlgorithm: Optional[str] = None
    subjectPublicKeyModulus: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.x509v3extensions is not None and not isinstance(self.x509v3extensions, X509V3ExtensionsFacet):
            self.x509v3extensions = X509V3ExtensionsFacet(**as_dict(self.x509v3extensions))

        if self.issuerHash is not None and not isinstance(self.issuerHash, Hash):
            self.issuerHash = Hash(**as_dict(self.issuerHash))

        if self.subjectHash is not None and not isinstance(self.subjectHash, Hash):
            self.subjectHash = Hash(**as_dict(self.subjectHash))

        if self.thumbprintHash is not None and not isinstance(self.thumbprintHash, Hash):
            self.thumbprintHash = Hash(**as_dict(self.thumbprintHash))

        if self.isSelfSigned is not None and not isinstance(self.isSelfSigned, BooleanType):
            self.isSelfSigned = BooleanType(self.isSelfSigned)

        if self.validityNotAfter is not None and not isinstance(self.validityNotAfter, XSDDateTime):
            self.validityNotAfter = XSDDateTime(self.validityNotAfter)

        if self.validityNotBefore is not None and not isinstance(self.validityNotBefore, XSDDateTime):
            self.validityNotBefore = XSDDateTime(self.validityNotBefore)

        if self.subjectPublicKeyExponent is not None and not isinstance(self.subjectPublicKeyExponent, int):
            self.subjectPublicKeyExponent = int(self.subjectPublicKeyExponent)

        if self.issuer is not None and not isinstance(self.issuer, str):
            self.issuer = str(self.issuer)

        if self.serialNumber is not None and not isinstance(self.serialNumber, str):
            self.serialNumber = str(self.serialNumber)

        if self.signature is not None and not isinstance(self.signature, str):
            self.signature = str(self.signature)

        if self.signatureAlgorithm is not None and not isinstance(self.signatureAlgorithm, str):
            self.signatureAlgorithm = str(self.signatureAlgorithm)

        if self.subject is not None and not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self.subjectPublicKeyAlgorithm is not None and not isinstance(self.subjectPublicKeyAlgorithm, str):
            self.subjectPublicKeyAlgorithm = str(self.subjectPublicKeyAlgorithm)

        if self.subjectPublicKeyModulus is not None and not isinstance(self.subjectPublicKeyModulus, str):
            self.subjectPublicKeyModulus = str(self.subjectPublicKeyModulus)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class X509V3ExtensionsFacet(Facet):
    """
    "An X.509 v3 certificate extensions facet is a grouping of characteristics unique to a public key digital identity
    certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.X509V3ExtensionsFacet
    class_class_curie: ClassVar[str] = "observable:X509V3ExtensionsFacet"
    class_name: ClassVar[str] = "X509V3ExtensionsFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.X509V3ExtensionsFacet

    privateKeyUsagePeriodNotAfter: Optional[Union[str, XSDDateTime]] = None
    privateKeyUsagePeriodNotBefore: Optional[Union[str, XSDDateTime]] = None
    authorityKeyIdentifier: Optional[str] = None
    basicConstraints: Optional[str] = None
    certificatePolicies: Optional[str] = None
    crlDistributionPoints: Optional[str] = None
    extendedKeyUsage: Optional[str] = None
    inhibitAnyPolicy: Optional[str] = None
    issuerAlternativeName: Optional[str] = None
    keyUsage: Optional[str] = None
    nameConstraints: Optional[str] = None
    policyConstraints: Optional[str] = None
    policyMappings: Optional[str] = None
    subjectAlternativeName: Optional[str] = None
    subjectDirectoryAttributes: Optional[str] = None
    subjectKeyIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.privateKeyUsagePeriodNotAfter is not None and not isinstance(self.privateKeyUsagePeriodNotAfter, XSDDateTime):
            self.privateKeyUsagePeriodNotAfter = XSDDateTime(self.privateKeyUsagePeriodNotAfter)

        if self.privateKeyUsagePeriodNotBefore is not None and not isinstance(self.privateKeyUsagePeriodNotBefore, XSDDateTime):
            self.privateKeyUsagePeriodNotBefore = XSDDateTime(self.privateKeyUsagePeriodNotBefore)

        if self.authorityKeyIdentifier is not None and not isinstance(self.authorityKeyIdentifier, str):
            self.authorityKeyIdentifier = str(self.authorityKeyIdentifier)

        if self.basicConstraints is not None and not isinstance(self.basicConstraints, str):
            self.basicConstraints = str(self.basicConstraints)

        if self.certificatePolicies is not None and not isinstance(self.certificatePolicies, str):
            self.certificatePolicies = str(self.certificatePolicies)

        if self.crlDistributionPoints is not None and not isinstance(self.crlDistributionPoints, str):
            self.crlDistributionPoints = str(self.crlDistributionPoints)

        if self.extendedKeyUsage is not None and not isinstance(self.extendedKeyUsage, str):
            self.extendedKeyUsage = str(self.extendedKeyUsage)

        if self.inhibitAnyPolicy is not None and not isinstance(self.inhibitAnyPolicy, str):
            self.inhibitAnyPolicy = str(self.inhibitAnyPolicy)

        if self.issuerAlternativeName is not None and not isinstance(self.issuerAlternativeName, str):
            self.issuerAlternativeName = str(self.issuerAlternativeName)

        if self.keyUsage is not None and not isinstance(self.keyUsage, str):
            self.keyUsage = str(self.keyUsage)

        if self.nameConstraints is not None and not isinstance(self.nameConstraints, str):
            self.nameConstraints = str(self.nameConstraints)

        if self.policyConstraints is not None and not isinstance(self.policyConstraints, str):
            self.policyConstraints = str(self.policyConstraints)

        if self.policyMappings is not None and not isinstance(self.policyMappings, str):
            self.policyMappings = str(self.policyMappings)

        if self.subjectAlternativeName is not None and not isinstance(self.subjectAlternativeName, str):
            self.subjectAlternativeName = str(self.subjectAlternativeName)

        if self.subjectDirectoryAttributes is not None and not isinstance(self.subjectDirectoryAttributes, str):
            self.subjectDirectoryAttributes = str(self.subjectDirectoryAttributes)

        if self.subjectKeyIdentifier is not None and not isinstance(self.subjectKeyIdentifier, str):
            self.subjectKeyIdentifier = str(self.subjectKeyIdentifier)

        super().__post_init__(**kwargs)


class Pattern(UcoObject):
    """
    A pattern is a combination of properties, acts, tendencies, etc., forming a consistent or characteristic
    arrangement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN.Pattern
    class_class_curie: ClassVar[str] = "pattern:Pattern"
    class_name: ClassVar[str] = "Pattern"
    class_model_uri: ClassVar[URIRef] = MASTER.Pattern


@dataclass
class LogicalPattern(Pattern):
    """
    A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured
    pattern expression following the rules of logic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN.LogicalPattern
    class_class_curie: ClassVar[str] = "pattern:LogicalPattern"
    class_name: ClassVar[str] = "LogicalPattern"
    class_model_uri: ClassVar[URIRef] = MASTER.LogicalPattern

    patternExpression: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.patternExpression is not None and not isinstance(self.patternExpression, str):
            self.patternExpression = str(self.patternExpression)

        super().__post_init__(**kwargs)


class PatternExpression(UcoInherentCharacterizationThing):
    """
    A pattern expression is a grouping of characteristics unique to an explicit logical expression defining a pattern
    (e.g., regular expression, SQL Select expression, etc.).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PATTERN.PatternExpression
    class_class_curie: ClassVar[str] = "pattern:PatternExpression"
    class_name: ClassVar[str] = "PatternExpression"
    class_model_uri: ClassVar[URIRef] = MASTER.PatternExpression


class Role(UcoObject):
    """
    A role is a usual or customary function based on contextual perspective.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ROLE.Role
    class_class_curie: ClassVar[str] = "role:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = MASTER.Role


class BenevolentRole(Role):
    """
    A benevolent role is a role with positive and/or beneficial intent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ROLE.BenevolentRole
    class_class_curie: ClassVar[str] = "role:BenevolentRole"
    class_name: ClassVar[str] = "BenevolentRole"
    class_model_uri: ClassVar[URIRef] = MASTER.BenevolentRole


class MaliciousRole(Role):
    """
    A malicious role is a role with malevolent intent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ROLE.MaliciousRole
    class_class_curie: ClassVar[str] = "role:MaliciousRole"
    class_name: ClassVar[str] = "MaliciousRole"
    class_model_uri: ClassVar[URIRef] = MASTER.MaliciousRole


class NeutralRole(Role):
    """
    A neutral role is a role with impartial intent.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ROLE.NeutralRole
    class_class_curie: ClassVar[str] = "role:NeutralRole"
    class_name: ClassVar[str] = "NeutralRole"
    class_model_uri: ClassVar[URIRef] = MASTER.NeutralRole


class Time(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME.Time
    class_class_curie: ClassVar[str] = "time:Time"
    class_name: ClassVar[str] = "Time"
    class_model_uri: ClassVar[URIRef] = MASTER.Time


class TimeRange(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME.TimeRange
    class_class_curie: ClassVar[str] = "time:TimeRange"
    class_name: ClassVar[str] = "TimeRange"
    class_model_uri: ClassVar[URIRef] = MASTER.TimeRange


class TimeStamp(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME.TimeStamp
    class_class_curie: ClassVar[str] = "time:TimeStamp"
    class_name: ClassVar[str] = "TimeStamp"
    class_model_uri: ClassVar[URIRef] = MASTER.TimeStamp


@dataclass
class BuildFacet(Facet):
    """
    "A build facet is a grouping of characteristics unique to a particular version of a software."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.BuildFacet
    class_class_curie: ClassVar[str] = "tool:BuildFacet"
    class_name: ClassVar[str] = "BuildFacet"
    class_model_uri: ClassVar[URIRef] = MASTER.BuildFacet

    buildInformation: Optional[Union[dict, "BuildInformationType"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.buildInformation is not None and not isinstance(self.buildInformation, BuildInformationType):
            self.buildInformation = BuildInformationType(**as_dict(self.buildInformation))

        super().__post_init__(**kwargs)


@dataclass
class BuildInformationType(UcoInherentCharacterizationThing):
    """
    "A build information type is a grouping of characteristics that describe how a particular version of software was
    converted from source code to executable code."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.BuildInformationType
    class_class_curie: ClassVar[str] = "tool:BuildInformationType"
    class_name: ClassVar[str] = "BuildInformationType"
    class_model_uri: ClassVar[URIRef] = MASTER.BuildInformationType

    buildConfiguration: Optional[Union[dict, Configuration]] = None
    buildUtility: Optional[Union[dict, "BuildUtilityType"]] = None
    compilers: Optional[Union[Union[dict, "CompilerType"], List[Union[dict, "CompilerType"]]]] = empty_list()
    libraries: Optional[Union[Union[dict, "LibraryType"], List[Union[dict, "LibraryType"]]]] = empty_list()
    compilationDate: Optional[Union[str, XSDDateTime]] = None
    buildID: Optional[str] = None
    buildLabel: Optional[str] = None
    buildOutputLog: Optional[str] = None
    buildProject: Optional[str] = None
    buildScript: Optional[str] = None
    buildVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.buildConfiguration is not None and not isinstance(self.buildConfiguration, Configuration):
            self.buildConfiguration = Configuration(**as_dict(self.buildConfiguration))

        if self.buildUtility is not None and not isinstance(self.buildUtility, BuildUtilityType):
            self.buildUtility = BuildUtilityType(**as_dict(self.buildUtility))

        if not isinstance(self.compilers, list):
            self.compilers = [self.compilers] if self.compilers is not None else []
        self.compilers = [v if isinstance(v, CompilerType) else CompilerType(**as_dict(v)) for v in self.compilers]

        if not isinstance(self.libraries, list):
            self.libraries = [self.libraries] if self.libraries is not None else []
        self.libraries = [v if isinstance(v, LibraryType) else LibraryType(**as_dict(v)) for v in self.libraries]

        if self.compilationDate is not None and not isinstance(self.compilationDate, XSDDateTime):
            self.compilationDate = XSDDateTime(self.compilationDate)

        if self.buildID is not None and not isinstance(self.buildID, str):
            self.buildID = str(self.buildID)

        if self.buildLabel is not None and not isinstance(self.buildLabel, str):
            self.buildLabel = str(self.buildLabel)

        if self.buildOutputLog is not None and not isinstance(self.buildOutputLog, str):
            self.buildOutputLog = str(self.buildOutputLog)

        if self.buildProject is not None and not isinstance(self.buildProject, str):
            self.buildProject = str(self.buildProject)

        if self.buildScript is not None and not isinstance(self.buildScript, str):
            self.buildScript = str(self.buildScript)

        if self.buildVersion is not None and not isinstance(self.buildVersion, str):
            self.buildVersion = str(self.buildVersion)

        super().__post_init__(**kwargs)


@dataclass
class BuildUtilityType(UcoInherentCharacterizationThing):
    """
    "A build utility type characterizes the tool used to convert from source code to executable code for a particular
    version of software."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.BuildUtilityType
    class_class_curie: ClassVar[str] = "tool:BuildUtilityType"
    class_name: ClassVar[str] = "BuildUtilityType"
    class_model_uri: ClassVar[URIRef] = MASTER.BuildUtilityType

    buildUtilityName: Optional[str] = None
    _cpeid: Optional[str] = None
    _swid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.buildUtilityName is not None and not isinstance(self.buildUtilityName, str):
            self.buildUtilityName = str(self.buildUtilityName)

        if self._cpeid is not None and not isinstance(self._cpeid, str):
            self._cpeid = str(self._cpeid)

        if self._swid is not None and not isinstance(self._swid, str):
            self._swid = str(self._swid)

        super().__post_init__(**kwargs)


@dataclass
class CompilerType(UcoInherentCharacterizationThing):
    """
    "A compiler type is a grouping of characteristics unique to a specific program that translates computer code
    written in one programming language (the source language) into another language (the target language). Typically a
    program that translates source code from a high-level programming language to a lower-level language (e.g.,
    assembly language, object code, or machine code) to create an executable program. [based on
    https://en.wikipedia.org/wiki/Compiler]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.CompilerType
    class_class_curie: ClassVar[str] = "tool:CompilerType"
    class_name: ClassVar[str] = "CompilerType"
    class_model_uri: ClassVar[URIRef] = MASTER.CompilerType

    compilerInformalDescription: Optional[str] = None
    _cpeid: Optional[str] = None
    _swid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.compilerInformalDescription is not None and not isinstance(self.compilerInformalDescription, str):
            self.compilerInformalDescription = str(self.compilerInformalDescription)

        if self._cpeid is not None and not isinstance(self._cpeid, str):
            self._cpeid = str(self._cpeid)

        if self._swid is not None and not isinstance(self._swid, str):
            self._swid = str(self._swid)

        super().__post_init__(**kwargs)


@dataclass
class LibraryType(UcoInherentCharacterizationThing):
    """
    "A library type is a grouping of characteristics unique to a collection of resources incorporated into the build
    of a software."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.LibraryType
    class_class_curie: ClassVar[str] = "tool:LibraryType"
    class_name: ClassVar[str] = "LibraryType"
    class_model_uri: ClassVar[URIRef] = MASTER.LibraryType

    libraryName: Optional[str] = None
    libraryVersion: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.libraryName is not None and not isinstance(self.libraryName, str):
            self.libraryName = str(self.libraryName)

        if self.libraryVersion is not None and not isinstance(self.libraryVersion, str):
            self.libraryVersion = str(self.libraryVersion)

        super().__post_init__(**kwargs)


@dataclass
class Tool(UcoObject):
    """
    "A tool is an element of hardware and/or software utilized to carry out a particular function."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.Tool
    class_class_curie: ClassVar[str] = "tool:Tool"
    class_name: ClassVar[str] = "Tool"
    class_model_uri: ClassVar[URIRef] = MASTER.Tool

    _creator: Optional[Union[dict, Identity]] = None
    _references: Optional[Union[Union[str, IriType], List[Union[str, IriType]]]] = empty_list()
    servicePack: Optional[str] = None
    toolType: Optional[str] = None
    _version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._creator is not None and not isinstance(self._creator, Identity):
            self._creator = Identity(**as_dict(self._creator))

        if not isinstance(self._references, list):
            self._references = [self._references] if self._references is not None else []
        self._references = [v if isinstance(v, IriType) else IriType(v) for v in self._references]

        if self.servicePack is not None and not isinstance(self.servicePack, str):
            self.servicePack = str(self.servicePack)

        if self.toolType is not None and not isinstance(self.toolType, str):
            self.toolType = str(self.toolType)

        if self._version is not None and not isinstance(self._version, str):
            self._version = str(self._version)

        super().__post_init__(**kwargs)


class AnalyticTool(Tool):
    """
    "An analytic tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of
    explanation, interpretation or logical reasoning."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.AnalyticTool
    class_class_curie: ClassVar[str] = "tool:AnalyticTool"
    class_name: ClassVar[str] = "AnalyticTool"
    class_model_uri: ClassVar[URIRef] = MASTER.AnalyticTool


@dataclass
class ConfiguredTool(Tool):
    """
    "A ConfiguredTool is a Tool that is known to be configured to run in a more specified manner than some
    unconfigured or less-configured Tool."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.ConfiguredTool
    class_class_curie: ClassVar[str] = "tool:ConfiguredTool"
    class_name: ClassVar[str] = "ConfiguredTool"
    class_model_uri: ClassVar[URIRef] = MASTER.ConfiguredTool

    usesConfiguration: Optional[Union[dict, Configuration]] = None
    isConfigurationOf: Optional[Union[dict, UcoObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.usesConfiguration is not None and not isinstance(self.usesConfiguration, Configuration):
            self.usesConfiguration = Configuration(**as_dict(self.usesConfiguration))

        if self.isConfigurationOf is not None and not isinstance(self.isConfigurationOf, UcoObject):
            self.isConfigurationOf = UcoObject(**as_dict(self.isConfigurationOf))

        super().__post_init__(**kwargs)


class DefensiveTool(Tool):
    """
    "A defensive tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of guarding."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.DefensiveTool
    class_class_curie: ClassVar[str] = "tool:DefensiveTool"
    class_name: ClassVar[str] = "DefensiveTool"
    class_model_uri: ClassVar[URIRef] = MASTER.DefensiveTool


class MaliciousTool(Tool):
    """
    "A malicious tool is an artifact of hardware and/or software utilized to accomplish a malevolent task or purpose."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TOOL.MaliciousTool
    class_class_curie: ClassVar[str] = "tool:MaliciousTool"
    class_name: ClassVar[str] = "MaliciousTool"
    class_model_uri: ClassVar[URIRef] = MASTER.MaliciousTool


@dataclass
class Dictionary(UcoInherentCharacterizationThing):
    """
    "A dictionary is list of (term/key, value) pairs with each term/key existing no more than once."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Dictionary
    class_class_curie: ClassVar[str] = "types:Dictionary"
    class_name: ClassVar[str] = "Dictionary"
    class_model_uri: ClassVar[URIRef] = MASTER.Dictionary

    entry: Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.entry):
            self.MissingRequiredField("entry")
        self._normalize_inlined_as_dict(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class ControlledDictionary(Dictionary):
    """
    "A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is
    constrained to an explicitly defined set of values."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.ControlledDictionary
    class_class_curie: ClassVar[str] = "types:ControlledDictionary"
    class_name: ClassVar[str] = "ControlledDictionary"
    class_model_uri: ClassVar[URIRef] = MASTER.ControlledDictionary

    entry: Optional[Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entry", slot_type=DictionaryEntry, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class DictionaryEntry(UcoInherentCharacterizationThing):
    """
    "A dictionary entry is a single (term/key, value) pair."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.DictionaryEntry
    class_class_curie: ClassVar[str] = "types:DictionaryEntry"
    class_name: ClassVar[str] = "DictionaryEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.DictionaryEntry

    key: str = None
    value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class ControlledDictionaryEntry(DictionaryEntry):
    """
    "A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an
    explicitly defined set of values."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.ControlledDictionaryEntry
    class_class_curie: ClassVar[str] = "types:ControlledDictionaryEntry"
    class_name: ClassVar[str] = "ControlledDictionaryEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.ControlledDictionaryEntry

    key: str = None
    value: str = None

@dataclass
class Hash(UcoInherentCharacterizationThing):
    """
    "A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data
    of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically
    infeasible to invert. This is commonly used for integrity checking of data. [based on
    https://en.wikipedia.org/wiki/Cryptographic_hash_function]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Hash
    class_class_curie: ClassVar[str] = "types:Hash"
    class_name: ClassVar[str] = "Hash"
    class_model_uri: ClassVar[URIRef] = MASTER.Hash

    hashValue: hex = None
    hashMethod: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.hashValue):
            self.MissingRequiredField("hashValue")
        if not isinstance(self.hashValue, hex):
            self.hashValue = hex(self.hashValue)

        if self._is_empty(self.hashMethod):
            self.MissingRequiredField("hashMethod")
        if not isinstance(self.hashMethod, str):
            self.hashMethod = str(self.hashMethod)

        super().__post_init__(**kwargs)


@dataclass
class ThreadItem(YAMLRoot):
    """
    "A ThreadItem is a member of a thread."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "ThreadItem"
    class_model_uri: ClassVar[URIRef] = MASTER.ThreadItem

    itemContent: Optional[Union[Union[dict, "CoItem"], List[Union[dict, "CoItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.itemContent, list):
            self.itemContent = [self.itemContent] if self.itemContent is not None else []
        self.itemContent = [v if isinstance(v, CoItem) else CoItem(**as_dict(v)) for v in self.itemContent]

        super().__post_init__(**kwargs)


class Victim(NeutralRole):
    """
    "A victim is a role played by a person or organization that is/was the target of some malicious action."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VICTIM.Victim
    class_class_curie: ClassVar[str] = "victim:Victim"
    class_name: ClassVar[str] = "Victim"
    class_model_uri: ClassVar[URIRef] = MASTER.Victim


class VictimTargeting(Victim):
    """
    "A victim targeting is a grouping of characteristics unique to people or organizations that are the target of some
    malicious activity."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = VICTIM.VictimTargeting
    class_class_curie: ClassVar[str] = "victim:VictimTargeting"
    class_name: ClassVar[str] = "VictimTargeting"
    class_model_uri: ClassVar[URIRef] = MASTER.VictimTargeting


class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Thing
    class_class_curie: ClassVar[str] = "collections:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = MASTER.Thing


@dataclass
class Collection(Thing):
    """
    A group of objects that can be considered as a whole.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Collection
    class_class_curie: ClassVar[str] = "collections:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = MASTER.Collection

    element: Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]] = empty_list()
    size: Optional[Union[int, PositiveInteger]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.element, list):
            self.element = [self.element] if self.element is not None else []
        self.element = [v if isinstance(v, Thing) else Thing(**as_dict(v)) for v in self.element]

        if self.size is not None and not isinstance(self.size, PositiveInteger):
            self.size = PositiveInteger(self.size)

        super().__post_init__(**kwargs)


class Bag(Collection):
    """
    Collection that can have a number of copies of each object
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Bag
    class_class_curie: ClassVar[str] = "collections:Bag"
    class_name: ClassVar[str] = "Bag"
    class_model_uri: ClassVar[URIRef] = MASTER.Bag


@dataclass
class Thread(Bag):
    """
    "A semi-ordered array of items, that can be present in multiple copies. Implemetation of a UCO Thread is similar
    to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or
    more direct successors, and two or more direct predecessors."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TYPES.Thread
    class_class_curie: ClassVar[str] = "types:Thread"
    class_name: ClassVar[str] = "Thread"
    class_model_uri: ClassVar[URIRef] = MASTER.Thread

    item: Optional[Union[Union[dict, "ThreadItem"], List[Union[dict, "ThreadItem"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.item, list):
            self.item = [self.item] if self.item is not None else []
        self.item = [v if isinstance(v, ThreadItem) else ThreadItem(**as_dict(v)) for v in self.item]

        super().__post_init__(**kwargs)


@dataclass
class CoItem(Thing):
    """
    Element belonging to a bag
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.CoItem
    class_class_curie: ClassVar[str] = "collections:CoItem"
    class_name: ClassVar[str] = "CoItem"
    class_model_uri: ClassVar[URIRef] = MASTER.CoItem

    itemOf: Optional[Union[dict, Bag]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.itemOf is not None and not isinstance(self.itemOf, Bag):
            self.itemOf = Bag(**as_dict(self.itemOf))

        super().__post_init__(**kwargs)


@dataclass
class ObservableObject(CoItem):
    """
    "An observable object is a grouping of characteristics unique to a distinct article or unit within the digital
    domain."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ObservableObject
    class_class_curie: ClassVar[str] = "observable:ObservableObject"
    class_name: ClassVar[str] = "ObservableObject"
    class_model_uri: ClassVar[URIRef] = MASTER.ObservableObject

    hasChanged: Optional[Union[bool, BooleanType]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hasChanged is not None and not isinstance(self.hasChanged, BooleanType):
            self.hasChanged = BooleanType(self.hasChanged)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


class API(ObservableObject):
    """
    "An API (application programming interface) is a computing interface that defines interactions between multiple
    software or mixed hardware-software intermediaries. It defines the kinds of calls or requests that can be made,
    how to make them, the data formats that should be used, the conventions to follow, etc. [based on
    https://en.wikipedia.org/wiki/API]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.API
    class_class_curie: ClassVar[str] = "observable:API"
    class_name: ClassVar[str] = "API"
    class_model_uri: ClassVar[URIRef] = MASTER.API


class ARPCache(ObservableObject):
    """
    "An ARP cache is a collection of Address Resolution Protocol (ARP) entries (mostly dynamic) that are created when
    an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address).
    [based on https://en.wikipedia.org/wiki/ARP_cache]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ARPCache
    class_class_curie: ClassVar[str] = "observable:ARPCache"
    class_name: ClassVar[str] = "ARPCache"
    class_model_uri: ClassVar[URIRef] = MASTER.ARPCache


class ARPCacheEntry(ObservableObject):
    """
    "An ARP cache entry is a single Address Resolution Protocol (ARP) response record that is created when an IP
    address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on
    https://en.wikipedia.org/wiki/ARP_cache]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ARPCacheEntry
    class_class_curie: ClassVar[str] = "observable:ARPCacheEntry"
    class_name: ClassVar[str] = "ARPCacheEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.ARPCacheEntry


class Account(ObservableObject):
    """
    "An account is an arrangement with an entity to enable and control the provision of some capability or service."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Account
    class_class_curie: ClassVar[str] = "observable:Account"
    class_name: ClassVar[str] = "Account"
    class_model_uri: ClassVar[URIRef] = MASTER.Account


class Address(ObservableObject):
    """
    "An address is an identifier assigned to enable routing and management of information."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Address
    class_class_curie: ClassVar[str] = "observable:Address"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = MASTER.Address


class AlternateDataStream(ObservableObject):
    """
    "An alternate data stream is data content stored within an NTFS file that is independent of the standard content
    stream of the file and isHidden from access by default NTFS file viewing mechanisms."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AlternateDataStream
    class_class_curie: ClassVar[str] = "observable:AlternateDataStream"
    class_name: ClassVar[str] = "AlternateDataStream"
    class_model_uri: ClassVar[URIRef] = MASTER.AlternateDataStream


class Application(ObservableObject):
    """
    "An application is a particular software program designed for end users."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Application
    class_class_curie: ClassVar[str] = "observable:Application"
    class_name: ClassVar[str] = "Application"
    class_model_uri: ClassVar[URIRef] = MASTER.Application


class Audio(ObservableObject):
    """
    "audio is a digital representation of sound."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Audio
    class_class_curie: ClassVar[str] = "observable:Audio"
    class_name: ClassVar[str] = "Audio"
    class_model_uri: ClassVar[URIRef] = MASTER.Audio


class AutonomousSystem(ObservableObject):
    """
    "An autonomous system is a collection of connected Internet Protocol (IP) routing prefixes under the control of
    one or more network operators on behalf of a single administrative entity or domain that presents a common,
    clearly defined routing policy to the Internet. [based on
    https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AutonomousSystem
    class_class_curie: ClassVar[str] = "observable:AutonomousSystem"
    class_name: ClassVar[str] = "AutonomousSystem"
    class_model_uri: ClassVar[URIRef] = MASTER.AutonomousSystem


class BotConfiguration(ObservableObject):
    """
    "A bot configuration is a set of contextual settings for a software application that runs automated tasks
    (scripts) over the Internet at a much higher rate than would be possible for a human alone."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BotConfiguration
    class_class_curie: ClassVar[str] = "observable:BotConfiguration"
    class_name: ClassVar[str] = "BotConfiguration"
    class_model_uri: ClassVar[URIRef] = MASTER.BotConfiguration


class BrowserBookmark(ObservableObject):
    """
    "A browser bookmark is a saved shortcut that directs a WWW (World Wide Web) browser software program to a
    particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BrowserBookmark
    class_class_curie: ClassVar[str] = "observable:BrowserBookmark"
    class_name: ClassVar[str] = "BrowserBookmark"
    class_model_uri: ClassVar[URIRef] = MASTER.BrowserBookmark


class BrowserCookie(ObservableObject):
    """
    "A browser cookie is a piece of of data sent from a website and stored on the user's computer by the user's web
    browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BrowserCookie
    class_class_curie: ClassVar[str] = "observable:BrowserCookie"
    class_name: ClassVar[str] = "BrowserCookie"
    class_model_uri: ClassVar[URIRef] = MASTER.BrowserCookie


class Calendar(ObservableObject):
    """
    "A calendar is a collection of appointments, meetings, and events."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Calendar
    class_class_curie: ClassVar[str] = "observable:Calendar"
    class_name: ClassVar[str] = "Calendar"
    class_model_uri: ClassVar[URIRef] = MASTER.Calendar


class CalendarEntry(ObservableObject):
    """
    "A calendar entry is an appointment, meeting or event within a collection of appointments, meetings and events."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CalendarEntry
    class_class_curie: ClassVar[str] = "observable:CalendarEntry"
    class_name: ClassVar[str] = "CalendarEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.CalendarEntry


class Call(ObservableObject):
    """
    "A call is a connection as part of a realtime cyber communication between one or more parties."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Call
    class_class_curie: ClassVar[str] = "observable:Call"
    class_name: ClassVar[str] = "Call"
    class_model_uri: ClassVar[URIRef] = MASTER.Call


class CapturedTelecommunicationsInformation(ObservableObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CapturedTelecommunicationsInformation
    class_class_curie: ClassVar[str] = "observable:CapturedTelecommunicationsInformation"
    class_name: ClassVar[str] = "CapturedTelecommunicationsInformation"
    class_model_uri: ClassVar[URIRef] = MASTER.CapturedTelecommunicationsInformation


class CellSite(ObservableObject):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CellSite
    class_class_curie: ClassVar[str] = "observable:CellSite"
    class_name: ClassVar[str] = "CellSite"
    class_model_uri: ClassVar[URIRef] = MASTER.CellSite


class Code(ObservableObject):
    """
    "Code is a direct representation (source, byte or binary) of a collection of computer instructions that form
    software which tell a computer how to work. [based on https://en.wikipedia.org/wiki/Software]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Code
    class_class_curie: ClassVar[str] = "observable:Code"
    class_name: ClassVar[str] = "Code"
    class_model_uri: ClassVar[URIRef] = MASTER.Code


class ComputerSpecification(ObservableObject):
    """
    "A computer specification is the hardware and software of a programmable electronic device that can store,
    retrieve, and process data. {based on merriam-webster.com/dictionary/computer]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ComputerSpecification
    class_class_curie: ClassVar[str] = "observable:ComputerSpecification"
    class_name: ClassVar[str] = "ComputerSpecification"
    class_model_uri: ClassVar[URIRef] = MASTER.ComputerSpecification


class Contact(ObservableObject):
    """
    "A contact is a set of identification and communication related details for a single entity."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Contact
    class_class_curie: ClassVar[str] = "observable:Contact"
    class_name: ClassVar[str] = "Contact"
    class_model_uri: ClassVar[URIRef] = MASTER.Contact


class ContactList(ObservableObject):
    """
    "A contact list is a set of multiple individual contacts such as that found in a digital address book."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContactList
    class_class_curie: ClassVar[str] = "observable:ContactList"
    class_name: ClassVar[str] = "ContactList"
    class_model_uri: ClassVar[URIRef] = MASTER.ContactList


class ContentData(ObservableObject):
    """
    "Content data is a block of digital data."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ContentData
    class_class_curie: ClassVar[str] = "observable:ContentData"
    class_name: ClassVar[str] = "ContentData"
    class_model_uri: ClassVar[URIRef] = MASTER.ContentData


class CookieHistory(ObservableObject):
    """
    "A cookie history is the stored web cookie history for a particular web browser."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CookieHistory
    class_class_curie: ClassVar[str] = "observable:CookieHistory"
    class_name: ClassVar[str] = "CookieHistory"
    class_model_uri: ClassVar[URIRef] = MASTER.CookieHistory


class Credential(ObservableObject):
    """
    "A credential is a single specific login and password combination for authorization of access to a digital account
    or system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Credential
    class_class_curie: ClassVar[str] = "observable:Credential"
    class_name: ClassVar[str] = "Credential"
    class_model_uri: ClassVar[URIRef] = MASTER.Credential


class CredentialDump(ObservableObject):
    """
    "A credential dump is a collection (typically forcibly extracted from a system) of specific login and password
    combinations for authorization of access to a digital account or system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CredentialDump
    class_class_curie: ClassVar[str] = "observable:CredentialDump"
    class_name: ClassVar[str] = "CredentialDump"
    class_model_uri: ClassVar[URIRef] = MASTER.CredentialDump


class DNSCache(ObservableObject):
    """
    "An DNS cache is a temporary locally stored collection of previous Domain Name System (DNS) query results (created
    when an domainName is resolved to a IP address) for a particular computer."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DNSCache
    class_class_curie: ClassVar[str] = "observable:DNSCache"
    class_name: ClassVar[str] = "DNSCache"
    class_model_uri: ClassVar[URIRef] = MASTER.DNSCache


class DNSRecord(ObservableObject):
    """
    "A DNS record is a single Domain Name System (DNS) artifact specifying information of a particular type (routing,
    authority, responsibility, security, etc.) for a specific Internet domainName."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DNSRecord
    class_class_curie: ClassVar[str] = "observable:DNSRecord"
    class_name: ClassVar[str] = "DNSRecord"
    class_model_uri: ClassVar[URIRef] = MASTER.DNSRecord


class Device(ObservableObject):
    """
    "A device is a piece of equipment or a mechanism designed to serve a special purpose or perform a special
    function. [based on https://www.merriam-webster.com/dictionary/device]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Device
    class_class_curie: ClassVar[str] = "observable:Device"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = MASTER.Device


class Adaptor(Device):
    """
    "An adaptor is a device that physically converts the pin outputs but does not alter the underlying protocol (e.g.
    uSD to SD, CF to ATA, etc.)"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Adaptor
    class_class_curie: ClassVar[str] = "observable:Adaptor"
    class_name: ClassVar[str] = "Adaptor"
    class_model_uri: ClassVar[URIRef] = MASTER.Adaptor


class AndroidDevice(Device):
    """
    "An Android device is a device running the Android operating system. [based on
    https://en.wikipedia.org/wiki/Android_(operating_system)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AndroidDevice
    class_class_curie: ClassVar[str] = "observable:AndroidDevice"
    class_name: ClassVar[str] = "AndroidDevice"
    class_model_uri: ClassVar[URIRef] = MASTER.AndroidDevice


class AndroidPhone(AndroidDevice):
    """
    An android phone is a smart phone that applies the Android mobile operating system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AndroidPhone
    class_class_curie: ClassVar[str] = "observable:AndroidPhone"
    class_name: ClassVar[str] = "AndroidPhone"
    class_model_uri: ClassVar[URIRef] = MASTER.AndroidPhone


class AppleDevice(Device):
    """
    "An apple device is a smart device that applies either the MacOS or iOS operating system"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.AppleDevice
    class_class_curie: ClassVar[str] = "observable:AppleDevice"
    class_name: ClassVar[str] = "AppleDevice"
    class_model_uri: ClassVar[URIRef] = MASTER.AppleDevice


class Appliance(Device):
    """
    "An appliance is a purpose-built computer with software or firmware that is designed to provide a specific
    computing capability or resource. [based on https://en.wikipedia.org/wiki/computer_appliance]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Appliance
    class_class_curie: ClassVar[str] = "observable:Appliance"
    class_name: ClassVar[str] = "Appliance"
    class_model_uri: ClassVar[URIRef] = MASTER.Appliance


class Computer(Device):
    """
    "A computer is an electronic device for storing and processing data, typically in binary, according to
    instructions given to it in a variable program. [based on 'computer.' Oxford English Dictionary, Oxford University
    Press, 2022.]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Computer
    class_class_curie: ClassVar[str] = "observable:Computer"
    class_name: ClassVar[str] = "Computer"
    class_model_uri: ClassVar[URIRef] = MASTER.Computer


class DigitalAccount(Account):
    """
    "A digital account is an arrangement with an entity to enable and control the provision of some capability or
    service within the digital domain."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalAccount
    class_class_curie: ClassVar[str] = "observable:DigitalAccount"
    class_name: ClassVar[str] = "DigitalAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalAccount


class ApplicationAccount(DigitalAccount):
    """
    "An application account is an account within a particular software program designed for end users."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ApplicationAccount
    class_class_curie: ClassVar[str] = "observable:ApplicationAccount"
    class_name: ClassVar[str] = "ApplicationAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.ApplicationAccount


class DigitalAddress(Address):
    """
    "A digital address is an identifier assigned to enable routing and management of digital communication."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalAddress
    class_class_curie: ClassVar[str] = "observable:DigitalAddress"
    class_name: ClassVar[str] = "DigitalAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalAddress


class DigitalCamera(Device):
    """
    "A digital camera is a camera that captures photographs in digital memory as opposed to capturing images on
    photographic film"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalCamera
    class_class_curie: ClassVar[str] = "observable:DigitalCamera"
    class_name: ClassVar[str] = "DigitalCamera"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalCamera


class DigitalSignatureInfo(ObservableObject):
    """
    "A digital signature info is a value calculated via a mathematical scheme for demonstrating the authenticity of an
    electronic message or document."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DigitalSignatureInfo
    class_class_curie: ClassVar[str] = "observable:DigitalSignatureInfo"
    class_name: ClassVar[str] = "DigitalSignatureInfo"
    class_model_uri: ClassVar[URIRef] = MASTER.DigitalSignatureInfo


class Disk(ObservableObject):
    """
    "A disk is a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical
    changes to a surface layer of one or more rotating disks."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Disk
    class_class_curie: ClassVar[str] = "observable:Disk"
    class_name: ClassVar[str] = "Disk"
    class_model_uri: ClassVar[URIRef] = MASTER.Disk


class DiskPartition(ObservableObject):
    """
    "A disk partition is a particular managed region on a storage mechanism where data is recorded by various
    electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks. [based on
    https://en.wikipedia.org/wiki/disk_storage]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DiskPartition
    class_class_curie: ClassVar[str] = "observable:DiskPartition"
    class_name: ClassVar[str] = "DiskPartition"
    class_model_uri: ClassVar[URIRef] = MASTER.DiskPartition


class DomainName(ObservableObject):
    """
    "A domainName is an identification string that defines a realm of administrative autonomy, authority or control
    within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.DomainName
    class_class_curie: ClassVar[str] = "observable:DomainName"
    class_name: ClassVar[str] = "DomainName"
    class_model_uri: ClassVar[URIRef] = MASTER.DomainName


class EmailAccount(DigitalAccount):
    """
    "An email account is an arrangement with an entity to enable and control the provision of electronic mail (email)
    capabilities or services."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmailAccount
    class_class_curie: ClassVar[str] = "observable:EmailAccount"
    class_name: ClassVar[str] = "EmailAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.EmailAccount


class EmailAddress(DigitalAddress):
    """
    "An emailAddress is an identifier for an electronic mailbox to which electronic mail messages (conformant to the
    Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmailAddress
    class_class_curie: ClassVar[str] = "observable:EmailAddress"
    class_name: ClassVar[str] = "EmailAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.EmailAddress


class EmbeddedDevice(Device):
    """
    "An embedded device is a highly specialized microprocessor device meant for one or very few specific purposes and
    is usually embedded or included within another object or as part of a larger system. Examples include answer
    machine, door access logger, card scanner, etc"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmbeddedDevice
    class_class_curie: ClassVar[str] = "observable:EmbeddedDevice"
    class_name: ClassVar[str] = "EmbeddedDevice"
    class_model_uri: ClassVar[URIRef] = MASTER.EmbeddedDevice


class EventLog(ObservableObject):
    """
    "An event log is a collection of event records."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EventLog
    class_class_curie: ClassVar[str] = "observable:EventLog"
    class_name: ClassVar[str] = "EventLog"
    class_model_uri: ClassVar[URIRef] = MASTER.EventLog


class EventRecord(ObservableObject):
    """
    "An event record is something that happens in a digital context (e.g., operating system events)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EventRecord
    class_class_curie: ClassVar[str] = "observable:EventRecord"
    class_name: ClassVar[str] = "EventRecord"
    class_model_uri: ClassVar[URIRef] = MASTER.EventRecord


class FileSystem(ObservableObject):
    """
    "A file system is the process that manages how and where data on a storage medium is stored, accessed and managed.
    [based on https://www.techopedia.com/definition/5510/file-system]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.FileSystem
    class_class_curie: ClassVar[str] = "observable:FileSystem"
    class_name: ClassVar[str] = "FileSystem"
    class_model_uri: ClassVar[URIRef] = MASTER.FileSystem


class FileSystemObject(ObservableObject):
    """
    "A file system object is an informational object represented and managed within a file system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.FileSystemObject
    class_class_curie: ClassVar[str] = "observable:FileSystemObject"
    class_name: ClassVar[str] = "FileSystemObject"
    class_model_uri: ClassVar[URIRef] = MASTER.FileSystemObject


class BlockDeviceNode(FileSystemObject):
    """
    "A block device node is a UNIX filesystem special file that serves as a conduit to communicate with devices,
    providing buffered randomly accesible input and output. Block device nodes are used to apply access rights to the
    devices and to direct operations on the files to the appropriate device drivers. [based on
    https://en.wikipedia.org/wiki/Unix_file_types]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BlockDeviceNode
    class_class_curie: ClassVar[str] = "observable:BlockDeviceNode"
    class_name: ClassVar[str] = "BlockDeviceNode"
    class_model_uri: ClassVar[URIRef] = MASTER.BlockDeviceNode


class CharacterDeviceNode(FileSystemObject):
    """
    "A character device node is a UNIX filesystem special file that serves as a conduit to communicate with devices,
    providing only a serial stream of input or accepting a serial stream of output. Character device nodes are used to
    apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based
    on https://en.wikipedia.org/wiki/Unix_file_types]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.CharacterDeviceNode
    class_class_curie: ClassVar[str] = "observable:CharacterDeviceNode"
    class_name: ClassVar[str] = "CharacterDeviceNode"
    class_model_uri: ClassVar[URIRef] = MASTER.CharacterDeviceNode


class Directory(FileSystemObject):
    """
    "A directory is a file system cataloging structure which contains references to other computer files, and possibly
    other directories. On many computers, directories are known as folders, or drawers, analogous to a workbench or
    the traditional office filing cabinet. In UNIX a directory is implemented as a special file. [based on
    https://en.wikipedia.org/wiki/Directory_(computing)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Directory
    class_class_curie: ClassVar[str] = "observable:Directory"
    class_name: ClassVar[str] = "Directory"
    class_model_uri: ClassVar[URIRef] = MASTER.Directory


class File(FileSystemObject):
    """
    "A file is a computer resource for recording data discretely on a computer storage device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.File
    class_class_curie: ClassVar[str] = "observable:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = MASTER.File


class ArchiveFile(File):
    """
    "An archive file is a file that is composed of one or more computer files along with metadata."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ArchiveFile
    class_class_curie: ClassVar[str] = "observable:ArchiveFile"
    class_name: ClassVar[str] = "ArchiveFile"
    class_model_uri: ClassVar[URIRef] = MASTER.ArchiveFile


class GUI(ObservableObject):
    """
    "A GUI is a graphical user interface that allows users to interact with electronic devices through graphical icons
    and audio indicators such as primary notation, instead of text-based user interfaces, typed command labels or text
    navigation. [based on https://en.wikipedia.org/wiki/Graphical_user_interface]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GUI
    class_class_curie: ClassVar[str] = "observable:GUI"
    class_name: ClassVar[str] = "GUI"
    class_model_uri: ClassVar[URIRef] = MASTER.GUI


class GamingConsole(Device):
    """
    "A gaming console (video game console or game console) is an electronic system that connects to a display,
    typically a TV or computer monitor, for the primary purpose of playing video games"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GamingConsole
    class_class_curie: ClassVar[str] = "observable:GamingConsole"
    class_name: ClassVar[str] = "GamingConsole"
    class_model_uri: ClassVar[URIRef] = MASTER.GamingConsole


class GenericObservableObject(ObservableObject):
    """
    "A generic observable object is an article or unit within the digital domain."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GenericObservableObject
    class_class_curie: ClassVar[str] = "observable:GenericObservableObject"
    class_name: ClassVar[str] = "GenericObservableObject"
    class_model_uri: ClassVar[URIRef] = MASTER.GenericObservableObject


class GeoLocationEntry(ObservableObject):
    """
    "A geolocation entry is a single application-specific geolocation entry."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GeoLocationEntry
    class_class_curie: ClassVar[str] = "observable:GeoLocationEntry"
    class_name: ClassVar[str] = "GeoLocationEntry"
    class_model_uri: ClassVar[URIRef] = MASTER.GeoLocationEntry


class GeoLocationLog(ObservableObject):
    """
    "A geolocation log is a record containing geolocation tracks and/or geolocation entries."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GeoLocationLog
    class_class_curie: ClassVar[str] = "observable:GeoLocationLog"
    class_name: ClassVar[str] = "GeoLocationLog"
    class_model_uri: ClassVar[URIRef] = MASTER.GeoLocationLog


class GeoLocationTrack(ObservableObject):
    """
    "A geolocation track is a set of contiguous geolocation entries representing a path/track taken."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.GeoLocationTrack
    class_class_curie: ClassVar[str] = "observable:GeoLocationTrack"
    class_name: ClassVar[str] = "GeoLocationTrack"
    class_model_uri: ClassVar[URIRef] = MASTER.GeoLocationTrack


class Hostname(ObservableObject):
    """
    "A hostname is a label that is assigned to a device connected to a computer network and that is used to identify
    the device in various forms of electronic communication, such as the World Wide Web. A hostname may be a
    domainName, if it is properly organized into the domainName system. A domainName may be a hostname if it has been
    assigned to an Internet host and associated with the host's IP address. [based on
    https://en.wikipedia.org/wiki/hostname]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Hostname
    class_class_curie: ClassVar[str] = "observable:Hostname"
    class_name: ClassVar[str] = "Hostname"
    class_model_uri: ClassVar[URIRef] = MASTER.Hostname


class IPAddress(DigitalAddress):
    """
    "An IP address is an Internet Protocol (IP) standards conformant identifier assigned to a device to enable routing
    and management of IP standards conformant communication to or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPAddress
    class_class_curie: ClassVar[str] = "observable:IPAddress"
    class_name: ClassVar[str] = "IPAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.IPAddress


class IPNetmask(ObservableObject):
    """
    "An IP netmask is a 32-bit 'mask' used to divide an IP address into subnets and specify the network's available
    hosts."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPNetmask
    class_class_curie: ClassVar[str] = "observable:IPNetmask"
    class_name: ClassVar[str] = "IPNetmask"
    class_model_uri: ClassVar[URIRef] = MASTER.IPNetmask


class IPhone(AppleDevice):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPhone
    class_class_curie: ClassVar[str] = "observable:IPhone"
    class_name: ClassVar[str] = "IPhone"
    class_model_uri: ClassVar[URIRef] = MASTER.IPhone


class IPv4Address(IPAddress):
    """
    "An IPv4 (Internet Protocol version 4) address is an IPv4 standards conformant identifier assigned to a device to
    enable routing and management of IPv4 standards conformant communication to or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPv4Address
    class_class_curie: ClassVar[str] = "observable:IPv4Address"
    class_name: ClassVar[str] = "IPv4Address"
    class_model_uri: ClassVar[URIRef] = MASTER.IPv4Address


class IPv6Address(IPAddress):
    """
    "An IPv6 (Internet Protocol version 6) address is an IPv6 standards conformant identifier assigned to a device to
    enable routing and management of IPv6 standards conformant communication to or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.IPv6Address
    class_class_curie: ClassVar[str] = "observable:IPv6Address"
    class_name: ClassVar[str] = "IPv6Address"
    class_model_uri: ClassVar[URIRef] = MASTER.IPv6Address


class Image(ObservableObject):
    """
    "An image is a complete copy of a hard disk, memory, or other digital media."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Image
    class_class_curie: ClassVar[str] = "observable:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = MASTER.Image


class InstantMessagingAddress(DigitalAddress):
    """
    ""
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.InstantMessagingAddress
    class_class_curie: ClassVar[str] = "observable:InstantMessagingAddress"
    class_name: ClassVar[str] = "InstantMessagingAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.InstantMessagingAddress


class Junction(FileSystemObject):
    """
    "A junction is a specific NTFS (New Technology file System) reparse point to redirect a directory access to
    another directory which can be on the same volume or another volume. A junction is similar to a directory symbolic
    link but may differ on whether they are processed on the local system or on the remote file server. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Junction
    class_class_curie: ClassVar[str] = "observable:Junction"
    class_name: ClassVar[str] = "Junction"
    class_model_uri: ClassVar[URIRef] = MASTER.Junction


class Laptop(Computer):
    """
    "A laptop, laptop computer, or notebook computer is a small, portable personal computer with a screen and
    alphanumeric keyboard. These typically have a clam shell form factor with the screen mounted on the inside of the
    upper lid and the keyboard on the inside of the lower lid, although 2-in-1 PCs with a detachable keyboard are
    often marketed as laptops or as having a laptop mode. (Devices categorized by their manufacturer as a laptop)"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Laptop
    class_class_curie: ClassVar[str] = "observable:Laptop"
    class_name: ClassVar[str] = "Laptop"
    class_model_uri: ClassVar[URIRef] = MASTER.Laptop


class Library(ObservableObject):
    """
    "A library is a suite of data and programming code that is used to develop software programs and applications.
    [based on https://www.techopedia.com/definition/3828/software-library]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Library
    class_class_curie: ClassVar[str] = "observable:Library"
    class_name: ClassVar[str] = "Library"
    class_model_uri: ClassVar[URIRef] = MASTER.Library


class MACAddress(DigitalAddress):
    """
    "A MAC address is a media access control standards conformant identifier assigned to a networkInterface to enable
    routing and management of communications at the data link layer of a network segment."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MACAddress
    class_class_curie: ClassVar[str] = "observable:MACAddress"
    class_name: ClassVar[str] = "MACAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.MACAddress


class BluetoothAddress(MACAddress):
    """
    "A Bluetooth address is a Bluetooth standard conformant identifier assigned to a Bluetooth device to enable
    routing and management of Bluetooth standards conformant communication to or from that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BluetoothAddress
    class_class_curie: ClassVar[str] = "observable:BluetoothAddress"
    class_name: ClassVar[str] = "BluetoothAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.BluetoothAddress


class Memory(ObservableObject):
    """
    "memory is a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only
    memory)) on a digital device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Memory
    class_class_curie: ClassVar[str] = "observable:Memory"
    class_name: ClassVar[str] = "Memory"
    class_model_uri: ClassVar[URIRef] = MASTER.Memory


class Message(ObservableObject):
    """
    "A message is a discrete unit of electronic communication intended by the source for consumption by some recipient
    or group of recipients. [based on https://en.wikipedia.org/wiki/message]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Message
    class_class_curie: ClassVar[str] = "observable:Message"
    class_name: ClassVar[str] = "Message"
    class_model_uri: ClassVar[URIRef] = MASTER.Message


class EmailMessage(Message):
    """
    "An email message is a message that is an instance of an electronic mail correspondence conformant to the internet
    message format described in RFC 5322 and related RFCs."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.EmailMessage
    class_class_curie: ClassVar[str] = "observable:EmailMessage"
    class_name: ClassVar[str] = "EmailMessage"
    class_model_uri: ClassVar[URIRef] = MASTER.EmailMessage


class ForumPost(Message):
    """
    "A forum post is message submitted by a user account to an online forum where the message content (and typically
    metadata including who posted it and when) is viewable by any party with viewing permissions on the forum."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ForumPost
    class_class_curie: ClassVar[str] = "observable:ForumPost"
    class_name: ClassVar[str] = "ForumPost"
    class_model_uri: ClassVar[URIRef] = MASTER.ForumPost


class ForumPrivateMessage(Message):
    """
    "A forum private message (aka PM or DM (direct message)) is a one-to-one message from one specific user account to
    another specific user account on an online form where transmission is managed by the online forum platform and the
    message is only viewable by the parties directly involved."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ForumPrivateMessage
    class_class_curie: ClassVar[str] = "observable:ForumPrivateMessage"
    class_name: ClassVar[str] = "ForumPrivateMessage"
    class_model_uri: ClassVar[URIRef] = MASTER.ForumPrivateMessage


class MobileAccount(DigitalAccount):
    """
    "A mobile account is an arrangement with an entity to enable and control the provision of some capability or
    service on a portable computing device. [based on https://www.lexico.com/definition/mobile_device]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MobileAccount
    class_class_curie: ClassVar[str] = "observable:MobileAccount"
    class_name: ClassVar[str] = "MobileAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.MobileAccount


class MobileDevice(Device):
    """
    "A mobile device is a portable computing device. [based on https://www.lexico.com.definition/mobile_device]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MobileDevice
    class_class_curie: ClassVar[str] = "observable:MobileDevice"
    class_name: ClassVar[str] = "MobileDevice"
    class_model_uri: ClassVar[URIRef] = MASTER.MobileDevice


class Drone(MobileDevice):
    """
    "A drone, unmanned aerial vehicle (UAV), is an aircraft without a human pilot, crew, or passengers that typically
    involve a ground-based controller and a system for communications with the UAV"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Drone
    class_class_curie: ClassVar[str] = "observable:Drone"
    class_name: ClassVar[str] = "Drone"
    class_model_uri: ClassVar[URIRef] = MASTER.Drone


class MobilePhone(MobileDevice):
    """
    "A mobile phone is a portable telephone that at least can make and receive calls over a radio frequency link while
    the user is moving within a telephone service area. This category encompasses all types of mobiles, simple and
    smart and satellite ones all together"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.MobilePhone
    class_class_curie: ClassVar[str] = "observable:MobilePhone"
    class_name: ClassVar[str] = "MobilePhone"
    class_model_uri: ClassVar[URIRef] = MASTER.MobilePhone


class Mutex(ObservableObject):
    """
    "A mutex is a mechanism that enforces limits on access to a resource when there are many threads of execution. A
    mutex is designed to enforce a mutual exclusion concurrency control policy, and with a variety of possible methods
    there exists multiple unique implementations for different applications. [based on
    https://en.wikipedia.org/wiki/Lock_(computer_science)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Mutex
    class_class_curie: ClassVar[str] = "observable:Mutex"
    class_name: ClassVar[str] = "Mutex"
    class_model_uri: ClassVar[URIRef] = MASTER.Mutex


class NTFSFile(File):
    """
    "An NTFS file is a New Technology file System (NTFS) file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NTFSFile
    class_class_curie: ClassVar[str] = "observable:NTFSFile"
    class_name: ClassVar[str] = "NTFSFile"
    class_model_uri: ClassVar[URIRef] = MASTER.NTFSFile


class NamedPipe(FileSystemObject):
    """
    "A named pipe is a mechanism for FIFO (first-in-first-out) inter-process communication. It is persisted as a
    filesystem object (that can be deleted like any other file), can be written to or read from by any process and
    exists beyond the lifespan of any process interacting with it (unlike simple anonymous pipes). [based on
    https://en.wikipedia.org/wiki/Named_pipe]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NamedPipe
    class_class_curie: ClassVar[str] = "observable:NamedPipe"
    class_name: ClassVar[str] = "NamedPipe"
    class_model_uri: ClassVar[URIRef] = MASTER.NamedPipe


class NetworkAppliance(Appliance):
    """
    "A network appliance is a purpose-built computer with software or firmware that is designed to provide a specific
    network management function."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkAppliance
    class_class_curie: ClassVar[str] = "observable:NetworkAppliance"
    class_name: ClassVar[str] = "NetworkAppliance"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkAppliance


class NetworkConnection(ObservableObject):
    """
    "A network connection is a connection (completed or attempted) across a digital network (a group of two or more
    computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkConnection
    class_class_curie: ClassVar[str] = "observable:NetworkConnection"
    class_name: ClassVar[str] = "NetworkConnection"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkConnection


class HTTPConnection(NetworkConnection):
    """
    "An HTTP connection is network connection that is conformant to the Hypertext Transfer Protocol (HTTP) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.HTTPConnection
    class_class_curie: ClassVar[str] = "observable:HTTPConnection"
    class_name: ClassVar[str] = "HTTPConnection"
    class_model_uri: ClassVar[URIRef] = MASTER.HTTPConnection


class ICMPConnection(NetworkConnection):
    """
    "An ICMP connection is a network connection that is conformant to the Internet Control message Protocol (ICMP)
    standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ICMPConnection
    class_class_curie: ClassVar[str] = "observable:ICMPConnection"
    class_name: ClassVar[str] = "ICMPConnection"
    class_model_uri: ClassVar[URIRef] = MASTER.ICMPConnection


class NetworkFlow(ObservableObject):
    """
    "A network flow is a sequence of data transiting one or more digital network (a group or two or more computer
    systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkFlow
    class_class_curie: ClassVar[str] = "observable:NetworkFlow"
    class_name: ClassVar[str] = "NetworkFlow"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkFlow


class NetworkInterface(ObservableObject):
    """
    "A networkInterface is a software or hardware interface between two pieces of equipment or protocol layers in a
    computer network."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkInterface
    class_class_curie: ClassVar[str] = "observable:NetworkInterface"
    class_name: ClassVar[str] = "NetworkInterface"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkInterface


class NetworkProtocol(ObservableObject):
    """
    "A network protocol is an established set of structured rules that determine how data is transmitted between
    different devices in the same network. Essentially, it allows connected devices to communicate with each other,
    regardless of any differences in their internal processes, structure or design. [based on
    https://www.comptia.org/content/guides/what-is-a-network-protocol]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkProtocol
    class_class_curie: ClassVar[str] = "observable:NetworkProtocol"
    class_name: ClassVar[str] = "NetworkProtocol"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkProtocol


class NetworkRoute(ObservableObject):
    """
    "A network route is a specific path (of specific network nodes, connections and protocols) for traffic in a
    network or between or across multiple networks."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkRoute
    class_class_curie: ClassVar[str] = "observable:NetworkRoute"
    class_name: ClassVar[str] = "NetworkRoute"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkRoute


class NetworkSubnet(ObservableObject):
    """
    "A network subnet is a logical subdivision of an IP network. [based on https://en.wikipedia.org/wiki/Subnetwork]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.NetworkSubnet
    class_class_curie: ClassVar[str] = "observable:NetworkSubnet"
    class_name: ClassVar[str] = "NetworkSubnet"
    class_model_uri: ClassVar[URIRef] = MASTER.NetworkSubnet


class Note(ObservableObject):
    """
    "A note is a brief textual record."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Note
    class_class_curie: ClassVar[str] = "observable:Note"
    class_name: ClassVar[str] = "Note"
    class_model_uri: ClassVar[URIRef] = MASTER.Note


class OnlineService(ObservableObject):
    """
    "An online service is a particular provision mechanism of information access, distribution or manipulation over
    the Internet."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.OnlineService
    class_class_curie: ClassVar[str] = "observable:OnlineService"
    class_name: ClassVar[str] = "OnlineService"
    class_model_uri: ClassVar[URIRef] = MASTER.OnlineService


class OperatingSystem(ObservableObject):
    """
    "An operating system is the software that manages computer hardware, software resources, and provides common
    services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.OperatingSystem
    class_class_curie: ClassVar[str] = "observable:OperatingSystem"
    class_name: ClassVar[str] = "OperatingSystem"
    class_model_uri: ClassVar[URIRef] = MASTER.OperatingSystem


class PDFFile(File):
    """
    "A PDF file is a Portable Document Format (PDF) file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PDFFile
    class_class_curie: ClassVar[str] = "observable:PDFFile"
    class_name: ClassVar[str] = "PDFFile"
    class_model_uri: ClassVar[URIRef] = MASTER.PDFFile


class PaymentCard(ObservableObject):
    """
    "A payment card is a physical token that is part of a payment system issued by financial institutions, such as a
    bank, to a customer that enables its owner (the cardholder) to access the funds in the customer's designated bank
    accounts, or through a credit account and make payments by electronic funds transfer and access automated teller
    machines (ATMs). [based on https://en.wikipedia.org/wiki/Payment_card]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PaymentCard
    class_class_curie: ClassVar[str] = "observable:PaymentCard"
    class_name: ClassVar[str] = "PaymentCard"
    class_model_uri: ClassVar[URIRef] = MASTER.PaymentCard


class PhoneAccount(DigitalAccount):
    """
    "A phone account is an arrangement with an entity to enable and control the provision of a telephony capability or
    service."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.PhoneAccount
    class_class_curie: ClassVar[str] = "observable:PhoneAccount"
    class_name: ClassVar[str] = "PhoneAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.PhoneAccount


class Pipe(ObservableObject):
    """
    "A pipe is a mechanism for one-way inter-process communication using message passing where data written by one
    process is buffered by the operating system until it isRead by the next process, and this uni-directional channel
    disappears when the processes are completed. [based on https://en.wikipedia.org/wiki/Pipeline_(Unix) ;
    https://en.wikipedia.org/wiki/Anonymous_pipe]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Pipe
    class_class_curie: ClassVar[str] = "observable:Pipe"
    class_name: ClassVar[str] = "Pipe"
    class_model_uri: ClassVar[URIRef] = MASTER.Pipe


class Post(Message):
    """
    "A post is message submitted to an online discussion/publishing site (forum, blog, etc.)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Post
    class_class_curie: ClassVar[str] = "observable:Post"
    class_name: ClassVar[str] = "Post"
    class_model_uri: ClassVar[URIRef] = MASTER.Post


class Process(ObservableObject):
    """
    "A process is an instance of a computer program executed on an operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Process
    class_class_curie: ClassVar[str] = "observable:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = MASTER.Process


class ProcessThread(ObservableObject):
    """
    "A process thread is the smallest sequence of programmed instructions that can be managed independently by a
    scheduler on a computer, which is typically a part of the operating system. It is a component of a process.
    Multiple threads can exist within one process, executing concurrently and sharing resources such as memory, while
    different processes do not share these resources. In particular, the threads of a process share its executable
    code and the values of its dynamically allocated variables and non-thread-local global variables at any given
    time. [based on https://en.wikipedia.org/wiki/Thread_(computing)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ProcessThread
    class_class_curie: ClassVar[str] = "observable:ProcessThread"
    class_name: ClassVar[str] = "ProcessThread"
    class_model_uri: ClassVar[URIRef] = MASTER.ProcessThread


class Profile(ObservableObject):
    """
    "A profile is an explicit digital representation of identity and characteristics of the owner of a single user
    account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Profile
    class_class_curie: ClassVar[str] = "observable:Profile"
    class_name: ClassVar[str] = "Profile"
    class_model_uri: ClassVar[URIRef] = MASTER.Profile


class ProtocolConverter(Device):
    """
    "A protocol converter is a device that converts from one protocol to another (e.g. SD to USB, SATA to USB, etc"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ProtocolConverter
    class_class_curie: ClassVar[str] = "observable:ProtocolConverter"
    class_name: ClassVar[str] = "ProtocolConverter"
    class_model_uri: ClassVar[URIRef] = MASTER.ProtocolConverter


class RasterPicture(File):
    """
    "A raster picture is a raster (or bitmap) image."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.RasterPicture
    class_class_curie: ClassVar[str] = "observable:RasterPicture"
    class_name: ClassVar[str] = "RasterPicture"
    class_model_uri: ClassVar[URIRef] = MASTER.RasterPicture


class RecoveredObject(ObservableObject):
    """
    "An observable object that was the result of a recovery operation."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.RecoveredObject
    class_class_curie: ClassVar[str] = "observable:RecoveredObject"
    class_name: ClassVar[str] = "RecoveredObject"
    class_model_uri: ClassVar[URIRef] = MASTER.RecoveredObject


class ReparsePoint(FileSystemObject):
    """
    "A reparse point is a type of NTFS (New Technology file System) object which is an optional attribute of files and
    directories meant to define some sort of preprocessing before accessing the said file or directory. For instance
    reparse points can be used to redirect access to files which have been moved to long term storage so that some
    application would retrieve them and make them directly accessible. A reparse point contains a reparse tag and data
    that are interpreted by a filesystem filter identified by the tag. [based on
    https://jp-andre.pagesperso-orange.fr/junctions.html ; https://en.wikipedia.org/wiki/NTFS_reparse_point]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ReparsePoint
    class_class_curie: ClassVar[str] = "observable:ReparsePoint"
    class_name: ClassVar[str] = "ReparsePoint"
    class_model_uri: ClassVar[URIRef] = MASTER.ReparsePoint


class SIMCard(Device):
    """
    "A SIM card is a subscriber identification module card intended to securely store the international mobile
    subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on
    mobile telephony. [based on https://en.wikipedia.org/wiki/SIM_card]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SIMCard
    class_class_curie: ClassVar[str] = "observable:SIMCard"
    class_name: ClassVar[str] = "SIMCard"
    class_model_uri: ClassVar[URIRef] = MASTER.SIMCard


class SIPAaddress(DigitalAddress):
    """
    "A SIP address is an identifier for Session Initiation Protocol (SIP) communication."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SIPAaddress
    class_class_curie: ClassVar[str] = "observable:SIPAaddress"
    class_name: ClassVar[str] = "SIPAaddress"
    class_model_uri: ClassVar[URIRef] = MASTER.SIPAaddress


class SMSMessage(Message):
    """
    "An SMS message is a message conformant to the short message service (SMS) communication protocol standards."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SMSMessage
    class_class_curie: ClassVar[str] = "observable:SMSMessage"
    class_name: ClassVar[str] = "SMSMessage"
    class_model_uri: ClassVar[URIRef] = MASTER.SMSMessage


class SQLiteBlob(ObservableObject):
    """
    "An SQLite blob is a blob (binary large object) of data within an SQLite database. [based on
    https://en.wikipedia.org/wiki/SQLite]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SQLiteBlob
    class_class_curie: ClassVar[str] = "observable:SQLiteBlob"
    class_name: ClassVar[str] = "SQLiteBlob"
    class_model_uri: ClassVar[URIRef] = MASTER.SQLiteBlob


class SecurityAppliance(Appliance):
    """
    "A security appliance is a purpose-built computer with software or firmware that is designed to provide a specific
    security function to protect computer networks."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SecurityAppliance
    class_class_curie: ClassVar[str] = "observable:SecurityAppliance"
    class_name: ClassVar[str] = "SecurityAppliance"
    class_model_uri: ClassVar[URIRef] = MASTER.SecurityAppliance


class Semaphore(ObservableObject):
    """
    "A semaphore is a variable or abstract dataType used to control access to a common resource by multiple processes
    and avoid critical section problems in a concurrent system such as a multitasking operating system. [based on
    https://en.wikipedia.org/wiki/semaphore_(programming)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Semaphore
    class_class_curie: ClassVar[str] = "observable:Semaphore"
    class_name: ClassVar[str] = "Semaphore"
    class_model_uri: ClassVar[URIRef] = MASTER.Semaphore


class Server(Computer):
    """
    "A server is a server rack-mount based computer, minicomputer, supercomputer, etc"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Server
    class_class_curie: ClassVar[str] = "observable:Server"
    class_name: ClassVar[str] = "Server"
    class_model_uri: ClassVar[URIRef] = MASTER.Server


class ShopListing(ObservableObject):
    """
    "A shop listing is a listing of offered products on an online marketplace/shop."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ShopListing
    class_class_curie: ClassVar[str] = "observable:ShopListing"
    class_name: ClassVar[str] = "ShopListing"
    class_model_uri: ClassVar[URIRef] = MASTER.ShopListing


class SmartDevice(Device):
    """
    "A smart device is a microprocessor IoT device that is expected to be connected directly to cloud-based networks
    or via smartphone"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SmartDevice
    class_class_curie: ClassVar[str] = "observable:SmartDevice"
    class_name: ClassVar[str] = "SmartDevice"
    class_model_uri: ClassVar[URIRef] = MASTER.SmartDevice


class SmartPhone(SmartDevice):
    """
    "A smartphone is a portable device that combines mobile telephone and computing functions into one unit. Examples
    include iPhone, Samsung Galaxy, Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SmartPhone
    class_class_curie: ClassVar[str] = "observable:SmartPhone"
    class_name: ClassVar[str] = "SmartPhone"
    class_model_uri: ClassVar[URIRef] = MASTER.SmartPhone


class BlackBerryPhone(SmartPhone):
    """
    "A blackberry phone is a smart phone that applies the Blackberry OS mobile operating system. (Blackberry 10
    re-introduces Blackberry OS, prior to that the OS was Android.)"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.BlackBerryPhone
    class_class_curie: ClassVar[str] = "observable:BlackBerryPhone"
    class_name: ClassVar[str] = "BlackBerryPhone"
    class_model_uri: ClassVar[URIRef] = MASTER.BlackBerryPhone


class Snapshot(FileSystemObject):
    """
    "A snapshot is a file system object representing a snapshot of the contents of a part of a file system at a point
    in time."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Snapshot
    class_class_curie: ClassVar[str] = "observable:Snapshot"
    class_name: ClassVar[str] = "Snapshot"
    class_model_uri: ClassVar[URIRef] = MASTER.Snapshot


class Socket(FileSystemObject):
    """
    "A socket is a special file used for inter-process communication, which enables communication between two
    processes. In addition to sending data, processes can send file descriptors across a Unix domain socket connection
    using the sendmsg() and recvmsg() system calls. Unlike named pipes which allow only unidirectional data flow,
    sockets are fully duplex-capable. [based on https://en.wikipedia.org/wiki/Unix_file_types]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Socket
    class_class_curie: ClassVar[str] = "observable:Socket"
    class_name: ClassVar[str] = "Socket"
    class_model_uri: ClassVar[URIRef] = MASTER.Socket


class SocketAddress(Address):
    """
    "A socket address (combining and IP address and a port number) is a composite identifier for a network socket
    endpoint supporting internet protocol communications."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SocketAddress
    class_class_curie: ClassVar[str] = "observable:SocketAddress"
    class_name: ClassVar[str] = "SocketAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.SocketAddress


class Software(ObservableObject):
    """
    "Software is a definitely scoped instance of a collection of data or computer instructions that tell the computer
    how to work. [based on https://en.wikipedia.org/wiki/Software]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Software
    class_class_curie: ClassVar[str] = "observable:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = MASTER.Software


@dataclass
class ConfiguredSoftware(Software):
    """
    "A configured software is a Software that is known to be configured to run in a more specified manner than some
    unconfigured or less-configured Software."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.ConfiguredSoftware
    class_class_curie: ClassVar[str] = "observable:ConfiguredSoftware"
    class_name: ClassVar[str] = "ConfiguredSoftware"
    class_model_uri: ClassVar[URIRef] = MASTER.ConfiguredSoftware

    usesConfiguration: Optional[Union[dict, Configuration]] = None
    isConfigurationOf: Optional[Union[dict, UcoObject]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.usesConfiguration is not None and not isinstance(self.usesConfiguration, Configuration):
            self.usesConfiguration = Configuration(**as_dict(self.usesConfiguration))

        if self.isConfigurationOf is not None and not isinstance(self.isConfigurationOf, UcoObject):
            self.isConfigurationOf = UcoObject(**as_dict(self.isConfigurationOf))

        super().__post_init__(**kwargs)


class StorageMedium(Device):
    """
    "A storage medium is any digital storage device that applies electromagnetic or optical surfaces, or depends
    solely on electronic circuits as solid state storage, for storing digital data. Examples include HDD (PATA), SATA,
    SSD, Optical, memory_Card, Tape, etc"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.StorageMedium
    class_class_curie: ClassVar[str] = "observable:StorageMedium"
    class_name: ClassVar[str] = "StorageMedium"
    class_model_uri: ClassVar[URIRef] = MASTER.StorageMedium


class SymbolicLink(FileSystemObject):
    """
    "A symbolic link is a file that contains a reference to another file or directory in the form of an absolute or
    relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.SymbolicLink
    class_class_curie: ClassVar[str] = "observable:SymbolicLink"
    class_name: ClassVar[str] = "SymbolicLink"
    class_model_uri: ClassVar[URIRef] = MASTER.SymbolicLink


class TCPConnection(NetworkConnection):
    """
    "A TCP connection is a network connection that is conformant to the Transfer"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TCPConnection
    class_class_curie: ClassVar[str] = "observable:TCPConnection"
    class_name: ClassVar[str] = "TCPConnection"
    class_model_uri: ClassVar[URIRef] = MASTER.TCPConnection


class TableField(ObservableObject):
    """
    "A database table field and its associated value contained within a relational database."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.TableField
    class_class_curie: ClassVar[str] = "observable:TableField"
    class_name: ClassVar[str] = "TableField"
    class_model_uri: ClassVar[URIRef] = MASTER.TableField


class Tablet(Computer):
    """
    "A tablet is a mobile computer that is primarily operated by touching the screen. (Devices categorized by their
    manufacturer as a Tablet"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Tablet
    class_class_curie: ClassVar[str] = "observable:Tablet"
    class_name: ClassVar[str] = "Tablet"
    class_model_uri: ClassVar[URIRef] = MASTER.Tablet


class Tweet(Message):
    """
    "A tweet is message submitted by a Twitter user account to the Twitter microblogging platform."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Tweet
    class_class_curie: ClassVar[str] = "observable:Tweet"
    class_name: ClassVar[str] = "Tweet"
    class_model_uri: ClassVar[URIRef] = MASTER.Tweet


class UNIXAccount(DigitalAccount):
    """
    "A UNIX account is an account on a UNIX operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXAccount
    class_class_curie: ClassVar[str] = "observable:UNIXAccount"
    class_name: ClassVar[str] = "UNIXAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXAccount


class UNIXFile(File):
    """
    "A UNIX file is a file pertaining to the UNIX operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXFile
    class_class_curie: ClassVar[str] = "observable:UNIXFile"
    class_name: ClassVar[str] = "UNIXFile"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXFile


class UNIXProcess(Process):
    """
    "A UNIX process is an instance of a computer program executed on a UNIX operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UNIXProcess
    class_class_curie: ClassVar[str] = "observable:UNIXProcess"
    class_name: ClassVar[str] = "UNIXProcess"
    class_model_uri: ClassVar[URIRef] = MASTER.UNIXProcess


class URL(ObservableObject):
    """
    "A URL is a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web)
    accessible resource."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URL
    class_class_curie: ClassVar[str] = "observable:URL"
    class_name: ClassVar[str] = "URL"
    class_model_uri: ClassVar[URIRef] = MASTER.URL


class URLHistory(ObservableObject):
    """
    "A URL history characterizes the stored URL history for a particular web browser"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URLHistory
    class_class_curie: ClassVar[str] = "observable:URLHistory"
    class_name: ClassVar[str] = "URLHistory"
    class_model_uri: ClassVar[URIRef] = MASTER.URLHistory


class URLVisit(ObservableObject):
    """
    "A URL visit characterizes the properties of a visit of a URL within a particular browser."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.URLVisit
    class_class_curie: ClassVar[str] = "observable:URLVisit"
    class_name: ClassVar[str] = "URLVisit"
    class_model_uri: ClassVar[URIRef] = MASTER.URLVisit


class UserAccount(DigitalAccount):
    """
    "A user account is an account controlling a user's access to a network, system or platform."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UserAccount
    class_class_curie: ClassVar[str] = "observable:UserAccount"
    class_name: ClassVar[str] = "UserAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.UserAccount


class UserSession(ObservableObject):
    """
    "A user session is a temporary and interactive information interchange between two or more communicating devices
    within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.UserSession
    class_class_curie: ClassVar[str] = "observable:UserSession"
    class_name: ClassVar[str] = "UserSession"
    class_model_uri: ClassVar[URIRef] = MASTER.UserSession


class Volume(ObservableObject):
    """
    "A volume is a single accessible storage area (volume) with a single file system. [based on
    https://en.wikipedia.org/wiki/volume_(computing)]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Volume
    class_class_curie: ClassVar[str] = "observable:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = MASTER.Volume


class WearableDevice(SmartDevice):
    """
    "A wearable device is an electronic device that is designed to be worn on a person's body"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WearableDevice
    class_class_curie: ClassVar[str] = "observable:WearableDevice"
    class_name: ClassVar[str] = "WearableDevice"
    class_model_uri: ClassVar[URIRef] = MASTER.WearableDevice


class WebPage(ObservableObject):
    """
    "A web page is a specific collection of information provided by a website and displayed to a user in a web
    browser. A website typically consists of many web pages linked together in a coherent fashion. [based on
    https://en.wikipedia.org/wiki/Web_page]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WebPage
    class_class_curie: ClassVar[str] = "observable:WebPage"
    class_name: ClassVar[str] = "WebPage"
    class_model_uri: ClassVar[URIRef] = MASTER.WebPage


class Whois(ObservableObject):
    """
    "Whois is a response record conformant to the WHOIS protocol standard (RFC 3912). [based on
    https://en.wikipedia.org/wiki/WHOIS]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Whois
    class_class_curie: ClassVar[str] = "observable:Whois"
    class_name: ClassVar[str] = "Whois"
    class_model_uri: ClassVar[URIRef] = MASTER.Whois


class WifiAddress(MACAddress):
    """
    "A Wi-Fi address is a media access control (MAC) standards-conformant identifier assigned to a device
    networkInterface to enable routing and management of IEEE 802.11 standards-conformant communications to and from
    that device."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WifiAddress
    class_class_curie: ClassVar[str] = "observable:WifiAddress"
    class_name: ClassVar[str] = "WifiAddress"
    class_model_uri: ClassVar[URIRef] = MASTER.WifiAddress


class Wiki(ObservableObject):
    """
    "A wiki is an online hypertext publication collaboratively edited and managed by its own audience directly using a
    web browser. A typical wiki contains multiple pages/articles for the subjects or scope of the project and could be
    either open to the public or limited to use within an organization for maintaining its internal knowledge base.
    [based on https://en.wikipedia.org/wiki/Wiki]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.Wiki
    class_class_curie: ClassVar[str] = "observable:Wiki"
    class_name: ClassVar[str] = "Wiki"
    class_model_uri: ClassVar[URIRef] = MASTER.Wiki


class WikiArticle(ObservableObject):
    """
    "A wiki article is one or more pages in a wiki focused on characterizing a particular topic."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WikiArticle
    class_class_curie: ClassVar[str] = "observable:WikiArticle"
    class_name: ClassVar[str] = "WikiArticle"
    class_model_uri: ClassVar[URIRef] = MASTER.WikiArticle


class WindowsAccount(DigitalAccount):
    """
    "A Windows account is a user account on a Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsAccount
    class_class_curie: ClassVar[str] = "observable:WindowsAccount"
    class_name: ClassVar[str] = "WindowsAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsAccount


class WindowsActiveDirectoryAccount(DigitalAccount):
    """
    "A Windows Active Directory account is an account managed by directory-based identity-related services of a
    Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsActiveDirectoryAccount
    class_class_curie: ClassVar[str] = "observable:WindowsActiveDirectoryAccount"
    class_name: ClassVar[str] = "WindowsActiveDirectoryAccount"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsActiveDirectoryAccount


class WindowsComputerSpecification(ObservableObject):
    """
    "A Windows computer specification is the hardware ans software of a programmable electronic device that can store,
    retrieve, and process data running a Microsoft Windows operating system. [based on
    merriam-webster.com/dictionary/computer]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsComputerSpecification
    class_class_curie: ClassVar[str] = "observable:WindowsComputerSpecification"
    class_name: ClassVar[str] = "WindowsComputerSpecification"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsComputerSpecification


class WindowsCriticalSection(ObservableObject):
    """
    "A Windows critical section is a Windows object that provides synchronization similar to that provided by a mutex
    object, except that a critical section can be used only by the threads of a single process. Critical section
    objects cannot be shared across processes. Event, mutex, and semaphore objects can also be used in a
    single-process application, but critical section objects provide a slightly faster, more efficient mechanism for
    mutual-exclusion synchronization (a processor-specific test and set instruction). Like a mutex object, a critical
    section object can be owned by only one thread at a time, which makes it useful for protecting a shared resource
    from simultaneous access. Unlike a mutex object, there is no way to tell whether a critical section has been
    abandoned. [based on https://docs.microsoft.com/en-us/windows/win32/sync/critical-section-objects]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsCriticalSection
    class_class_curie: ClassVar[str] = "observable:WindowsCriticalSection"
    class_name: ClassVar[str] = "WindowsCriticalSection"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsCriticalSection


class WindowsEvent(ObservableObject):
    """
    "A Windows event is a notification record of an occurance of interest (system, security, application, etc.) on a
    Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsEvent
    class_class_curie: ClassVar[str] = "observable:WindowsEvent"
    class_name: ClassVar[str] = "WindowsEvent"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsEvent


class WindowsFileMapping(ObservableObject):
    """
    "A windows file mapping is the association of a file's contents with a portion of the virtual address space of a
    process within a Windows operating system. The system creates a file mapping object (also known as a section
    object) to maintain this association. A file view is the portion of virtual address space that a process uses to
    access the file's contents. file mapping allows the process to use both random input and output (I/O) and
    sequential I/O. It also allows the process to work efficiently with a large data file, such as a database, without
    having to map the whole file into memory. Multiple processes can also use memory-mapped files to share data.
    processes read from and write to the file view using pointers, just as they would with dynamically allocated
    memory. The use of file mapping improves efficiency because the file resides on disk, but the file view resides in
    memory.[based on https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsFileMapping
    class_class_curie: ClassVar[str] = "observable:WindowsFileMapping"
    class_name: ClassVar[str] = "WindowsFileMapping"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsFileMapping


class WindowsHandle(ObservableObject):
    """
    "A Windows handle is an abstract reference to a resource within the Windows operating system, such as a window,
    memory, an open file or a pipe. It is the mechanism by which applications interact with such resources in the
    Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsHandle
    class_class_curie: ClassVar[str] = "observable:WindowsHandle"
    class_name: ClassVar[str] = "WindowsHandle"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsHandle


class WindowsHook(ObservableObject):
    """
    "A Windows hook is a mechanism by which an application can intercept events, such as messages, mouse actions, and
    keystrokes within the Windows operating system. A function that intercepts a particular type of event is known as
    a hook procedure. A hook procedure can act on each event it receives, and then modify or discard the event. [based
    on https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsHook
    class_class_curie: ClassVar[str] = "observable:WindowsHook"
    class_name: ClassVar[str] = "WindowsHook"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsHook


class WindowsMailSlot(ObservableObject):
    """
    "A Windows mailslot is is a pseudofile that resides in memory, and may be accessed using standard file functions.
    The data in a mailslot message can be in any form, but cannot be larger than 424 bytes when sent between
    computers. Unlike disk files, mailslots are temporary. When all handles to a mailslot are closed, the mailslot and
    all the data it contains are deleted. [based on
    https://docs.microsoft.com/en-us/windows/win32/ipc/about-mailslots]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsMailSlot
    class_class_curie: ClassVar[str] = "observable:WindowsMailSlot"
    class_name: ClassVar[str] = "WindowsMailSlot"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsMailSlot


class WindowsNetworkShare(ObservableObject):
    """
    "A Windows network share is a Windows computer resource made available from one host to other hosts on a computer
    network. It is a device or piece of information on a computer that can be remotely accessed from another computer
    transparently as if it were a resource in the local machine. network sharing is made possible by inter-process
    communication over the network. [based on https://en.wikipedia.org/wiki/Shared_resource]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsNetworkShare
    class_class_curie: ClassVar[str] = "observable:WindowsNetworkShare"
    class_name: ClassVar[str] = "WindowsNetworkShare"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsNetworkShare


class WindowsPEBinaryFile(File):
    """
    "A Windows PE binary file is a Windows portable executable (PE) file."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPEBinaryFile
    class_class_curie: ClassVar[str] = "observable:WindowsPEBinaryFile"
    class_name: ClassVar[str] = "WindowsPEBinaryFile"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPEBinaryFile


class WindowsPrefetch(ObservableObject):
    """
    "The Windows prefetch contains entries in a Windows prefetch file (used to speed up application startup starting
    with Windows XP)."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsPrefetch
    class_class_curie: ClassVar[str] = "observable:WindowsPrefetch"
    class_name: ClassVar[str] = "WindowsPrefetch"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsPrefetch


class WindowsProcess(Process):
    """
    "A Windows process is a program running on a Windows operating system."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsProcess
    class_class_curie: ClassVar[str] = "observable:WindowsProcess"
    class_name: ClassVar[str] = "WindowsProcess"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsProcess


class WindowsRegistryHive(ObservableObject):
    """
    "The Windows registry hive is a particular logical group of keys, subkeys, and values in a Windows registry (a
    hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for
    applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsRegistryHive
    class_class_curie: ClassVar[str] = "observable:WindowsRegistryHive"
    class_name: ClassVar[str] = "WindowsRegistryHive"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsRegistryHive


class WindowsRegistryKey(ObservableObject):
    """
    "A Windows registry key is a particular key within a Windows registry (a hierarchical database that stores
    low-level settings for the Microsoft Windows operating sytem and for applications that opt to use the registry).
    [based on https://en.wikipedia.org/wiki/Windows_Registry]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsRegistryKey
    class_class_curie: ClassVar[str] = "observable:WindowsRegistryKey"
    class_name: ClassVar[str] = "WindowsRegistryKey"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsRegistryKey


class WindowsService(ObservableObject):
    """
    "A Windows service is a specific Windows service (a computer program that operates in the background of a Windows
    operating system, similar to the way a UNIX daemon runs on UNIX ). [based on
    https://en.wikipedia.org/wiki/Windows_service]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsService
    class_class_curie: ClassVar[str] = "observable:WindowsService"
    class_name: ClassVar[str] = "WindowsService"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsService


class WindowsSystemRestore(ObservableObject):
    """
    "A Windows system restore is a capture of a Windows computer's state (including system files, installed
    applications, Windows Registry, and system settings) at a particular point in time such that the computer can be
    reverted to that state in the event of system malfunctions or other problems. [based on
    https://en.wikipedia.org/wiki/System_Restore]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsSystemRestore
    class_class_curie: ClassVar[str] = "observable:WindowsSystemRestore"
    class_name: ClassVar[str] = "WindowsSystemRestore"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsSystemRestore


class WindowsTask(ObservableObject):
    """
    "A Windows task is a process that is scheduled to execute on a Windows operating system by the Windows Task
    Scheduler. [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsTask
    class_class_curie: ClassVar[str] = "observable:WindowsTask"
    class_name: ClassVar[str] = "WindowsTask"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsTask


class WindowsThread(ProcessThread):
    """
    "A Windows thread is a single thread of execution within a Windows process."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsThread
    class_class_curie: ClassVar[str] = "observable:WindowsThread"
    class_name: ClassVar[str] = "WindowsThread"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsThread


class WindowsWaitableTime(ObservableObject):
    """
    "A Windows waitable timer is a synchronization object within the Windows operating system whose state is set to
    signaled when a specified due time arrives. There are two types of waitable timers that can be created:
    manual-reset and synchronization. A timer of either type can also be a periodic timer. [based on
    https://docs.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WindowsWaitableTime
    class_class_curie: ClassVar[str] = "observable:WindowsWaitableTime"
    class_name: ClassVar[str] = "WindowsWaitableTime"
    class_model_uri: ClassVar[URIRef] = MASTER.WindowsWaitableTime


class WirelessNetworkConnection(NetworkConnection):
    """
    "A wireless network connection is a connection (completed or attempted) across an IEEE 802.11 standards-confromant
    digital network (a group of two or more computer systems linked together). [based on
    https://www.webopedia.com/TERM/N/network.html]"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WirelessNetworkConnection
    class_class_curie: ClassVar[str] = "observable:WirelessNetworkConnection"
    class_name: ClassVar[str] = "wirelessNetworkConnection"
    class_model_uri: ClassVar[URIRef] = MASTER.WirelessNetworkConnection


class WriteBlocker(Device):
    """
    "A write blocker is a device that allows read-only access to storage mediums in order to preserve the integrity of
    the data being analyzed. Examples include Tableau, Cellibrite, Talon, etc"
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.WriteBlocker
    class_class_curie: ClassVar[str] = "observable:WriteBlocker"
    class_name: ClassVar[str] = "WriteBlocker"
    class_model_uri: ClassVar[URIRef] = MASTER.WriteBlocker


class X509Certificate(ObservableObject):
    """
    "A X.509 certificate is a public key digital identity certificate conformant to the X.509 PKI (Public Key
    Infrastructure) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.X509Certificate
    class_class_curie: ClassVar[str] = "observable:X509Certificate"
    class_name: ClassVar[str] = "X509Certificate"
    class_model_uri: ClassVar[URIRef] = MASTER.X509Certificate


class X509V3Certificate(ObservableObject):
    """
    "An X.509 v3 certificate is a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key
    Infrastructure) standard."
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBSERVABLE.X509V3Certificate
    class_class_curie: ClassVar[str] = "observable:X509V3Certificate"
    class_name: ClassVar[str] = "X509V3Certificate"
    class_model_uri: ClassVar[URIRef] = MASTER.X509V3Certificate


@dataclass
class List(Bag):
    """
    An ordered array of items, that can be present in multiple copies
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.List
    class_class_curie: ClassVar[str] = "collections:List"
    class_name: ClassVar[str] = "List"
    class_model_uri: ClassVar[URIRef] = MASTER.List

    item: Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]] = empty_list()
    lastItem: Optional[Union[dict, "ListItem"]] = None
    firstItem: Optional[Union[dict, "ListItem"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="item", slot_type=ListItem, key_name="_index", keyed=False)

        if self.lastItem is not None and not isinstance(self.lastItem, ListItem):
            self.lastItem = ListItem(**as_dict(self.lastItem))

        if self.firstItem is not None and not isinstance(self.firstItem, ListItem):
            self.firstItem = ListItem(**as_dict(self.firstItem))

        super().__post_init__(**kwargs)


@dataclass
class ListItem(CoItem):
    """
    element belonging to a list
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.ListItem
    class_class_curie: ClassVar[str] = "collections:ListItem"
    class_name: ClassVar[str] = "ListItem"
    class_model_uri: ClassVar[URIRef] = MASTER.ListItem

    _index: Union[int, PositiveInteger] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self._index):
            self.MissingRequiredField("_index")
        if not isinstance(self._index, PositiveInteger):
            self._index = PositiveInteger(self._index)

        super().__post_init__(**kwargs)


class Set(Collection):
    """
    A collection that cannot contain duplicate elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COLLECTIONS.Set
    class_class_curie: ClassVar[str] = "collections:Set"
    class_name: ClassVar[str] = "Set"
    class_model_uri: ClassVar[URIRef] = MASTER.Set


# Enumerations
class ContactPhoneScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    mobile = PermissibleValue(text="mobile")
    main = PermissibleValue(text="main")
    pager = PermissibleValue(text="pager")

    _defn = EnumDefinition(
        name="ContactPhoneScopeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "home fax",
                PermissibleValue(text="home fax") )
        setattr(cls, "work fax",
                PermissibleValue(text="work fax") )

class NetworkSocketAddressFamilyEnum(EnumDefinitionImpl):
    """
    From https://www.freepascal.org/daily/doc/rtl/sockets/index-2.html
    """
    af_appletalk = PermissibleValue(text="af_appletalk",
                                               description=""Address family Appletalk DDP"")
    af_bth = PermissibleValue(text="af_bth",
                                   description=""Address family: Bluetooth sockets"")
    af_inet = PermissibleValue(text="af_inet",
                                     description=""Address family Internet IP Protocol"")
    af_inet6 = PermissibleValue(text="af_inet6",
                                       description=""Address family IP version 6"")
    af_ipx = PermissibleValue(text="af_ipx",
                                   description=""Address family Novell IPX"")
    af_irda = PermissibleValue(text="af_irda",
                                     description=""Address family: IRDA sockets"")
    af_netbios = PermissibleValue(text="af_netbios",
                                           description=""Address family: NetBIOS"")
    af_unspec = PermissibleValue(text="af_unspec",
                                         description=""Address family Not specified"")

    _defn = EnumDefinition(
        name="NetworkSocketAddressFamilyEnum",
        description="From https://www.freepascal.org/daily/doc/rtl/sockets/index-2.html",
    )

class NetworkSocketProtocolFamilyEnum(EnumDefinitionImpl):
    """
    From https://www.freepascal.org/daily/doc/rtl/sockets/index-2.html
    """
    pf_appletalk = PermissibleValue(text="pf_appletalk",
                                               description=""Protocol family: Appletalk DDP"")
    pf_ash = PermissibleValue(text="pf_ash",
                                   description=""Protocol family: Ash"")
    pf_atmpvc = PermissibleValue(text="pf_atmpvc",
                                         description=""Protocol family: ATM PVCs"")
    pf_atmsvc = PermissibleValue(text="pf_atmsvc",
                                         description=""Protocol family: ATM SVCs"")
    pf_ax25 = PermissibleValue(text="pf_ax25",
                                     description=""Protocol family: Amateur Radio AX.25"")
    pf_bluetooth = PermissibleValue(text="pf_bluetooth",
                                               description=""Protocol family: BlueTooth sockets"")
    pf_bridge = PermissibleValue(text="pf_bridge",
                                         description=""Protocol family: Multiprotocol bridge"")
    pf_decnet = PermissibleValue(text="pf_decnet",
                                         description=""Protocol family: DECNET project"")
    pf_econet = PermissibleValue(text="pf_econet",
                                         description=""Protocol family: Acorn Econet"")
    pf_inet = PermissibleValue(text="pf_inet",
                                     description=""Protocol family: Internet IP Protocol"")
    pf_inet6 = PermissibleValue(text="pf_inet6",
                                       description=""Protocol family: IP version 6"")
    pf_ipx = PermissibleValue(text="pf_ipx",
                                   description=""Protocol family: Novell IPX"")
    pf_irda = PermissibleValue(text="pf_irda",
                                     description=""Protocol family: IRDA sockets"")
    pf_key = PermissibleValue(text="pf_key",
                                   description=""Protocol family: Key management API"")
    pf_netbeui = PermissibleValue(text="pf_netbeui",
                                           description=""Protocol family: Reserved for 802.2LLC project"")
    pf_netlink = PermissibleValue(text="pf_netlink",
                                           description=""Protocol family: Netlink?"")
    pf_netrom = PermissibleValue(text="pf_netrom",
                                         description=""Protocol family: Amateur radio NetROM"")
    pf_packet = PermissibleValue(text="pf_packet",
                                         description=""Protocol family: Packet family"")
    pf_pppox = PermissibleValue(text="pf_pppox",
                                       description=""Protocol family: PPPoX sockets"")
    pf_rose = PermissibleValue(text="pf_rose",
                                     description=""Protocol family: Amateur Radio X.25 PLP"")
    pf_route = PermissibleValue(text="pf_route",
                                       description=""Protocol family: Route?"")
    pf_security = PermissibleValue(text="pf_security",
                                             description=""Protocol family: Security callback pseudo PF"")
    pf_sna = PermissibleValue(text="pf_sna",
                                   description=""Protocol family: Linux SNA project"")
    pf_wanpipe = PermissibleValue(text="pf_wanpipe",
                                           description=""Protocol family: Wanpipe API Sockets"")
    pf_x25 = PermissibleValue(text="pf_x25",
                                   description=""Protocol family: Reserved for X.25 project"")

    _defn = EnumDefinition(
        name="NetworkSocketProtocolFamilyEnum",
        description="From https://www.freepascal.org/daily/doc/rtl/sockets/index-2.html",
    )

class NetworkSocketTypeEnum(EnumDefinitionImpl):
    """
    From https://www.freepascal.org/daily/doc/rtl/sockets/index-2.html
    """
    sock_dgram = PermissibleValue(text="sock_dgram",
                                           description=""Type of socket: datagram (conn.less) socket (UDP)"")
    sock_raw = PermissibleValue(text="sock_raw",
                                       description=""Type of socket: raw socket"")
    sock_rdm = PermissibleValue(text="sock_rdm",
                                       description=""Type of socket: reliably-delivered message"")
    sock_seqpacket = PermissibleValue(text="sock_seqpacket",
                                                   description=""Type of socket: sequential packet socket"")
    sock_stream = PermissibleValue(text="sock_stream",
                                             description=""Type of socket: stream (connection) type socket (TCP)"")

    _defn = EnumDefinition(
        name="NetworkSocketTypeEnum",
        description="From https://www.freepascal.org/daily/doc/rtl/sockets/index-2.html",
    )

class TriggerFrequencyEunum(EnumDefinitionImpl):

    TASK_EVENT_TRIGGER_AT_LOGON = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_LOGON")
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_SYSTEMSTART")
    TASK_EVENT_TRIGGER_ON_IDLE = PermissibleValue(text="TASK_EVENT_TRIGGER_ON_IDLE")
    TASK_TIME_TRIGGER_DAILY = PermissibleValue(text="TASK_TIME_TRIGGER_DAILY")
    TASK_TIME_TRIGGER_MONTHLYDATE = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDATE")
    TASK_TIME_TRIGGER_MONTHLYDOW = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDOW")
    TASK_TIME_TRIGGER_ONCE = PermissibleValue(text="TASK_TIME_TRIGGER_ONCE")
    TASK_TIME_TRIGGER_WEEKLY = PermissibleValue(text="TASK_TIME_TRIGGER_WEEKLY")

    _defn = EnumDefinition(
        name="TriggerFrequencyEunum",
    )

class WindowsPEBinaryTypeEnum(EnumDefinitionImpl):

    dll = PermissibleValue(text="dll")
    exe = PermissibleValue(text="exe")
    sys = PermissibleValue(text="sys")

    _defn = EnumDefinition(
        name="WindowsPEBinaryTypeEnum",
    )

class WindowsServiceStartTypeEnum(EnumDefinitionImpl):

    service_auto_start = PermissibleValue(text="service_auto_start")
    service_boot_start = PermissibleValue(text="service_boot_start")
    service_demand_start = PermissibleValue(text="service_demand_start")
    service_disabled = PermissibleValue(text="service_disabled")
    service_system_alert = PermissibleValue(text="service_system_alert")

    _defn = EnumDefinition(
        name="WindowsServiceStartTypeEnum",
    )

class WindowsServiceStatusEnum(EnumDefinitionImpl):

    service_continue_pending = PermissibleValue(text="service_continue_pending")
    service_pause_pending = PermissibleValue(text="service_pause_pending")
    service_paused = PermissibleValue(text="service_paused")
    service_running = PermissibleValue(text="service_running")
    service_start_pending = PermissibleValue(text="service_start_pending")
    service_stop_pending = PermissibleValue(text="service_stop_pending")
    service_stopped = PermissibleValue(text="service_stopped")

    _defn = EnumDefinition(
        name="WindowsServiceStatusEnum",
    )

class WindowsServiceTypeEnum(EnumDefinitionImpl):

    service_file_system_driver = PermissibleValue(text="service_file_system_driver")
    service_kernel_driver = PermissibleValue(text="service_kernel_driver")
    service_win32_own_process = PermissibleValue(text="service_win32_own_process")
    service_win32_share_process = PermissibleValue(text="service_win32_share_process")

    _defn = EnumDefinition(
        name="WindowsServiceTypeEnum",
    )

class WindowsNetworkSecurityModeEnum(EnumDefinitionImpl):

    WEP = PermissibleValue(text="WEP")
    WPA = PermissibleValue(text="WPA")

    _defn = EnumDefinition(
        name="WindowsNetworkSecurityModeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
                PermissibleValue(text="None") )
        setattr(cls, "WPA2-PSK",
                PermissibleValue(text="WPA2-PSK") )
        setattr(cls, "WPA2-Enterprise",
                PermissibleValue(text="WPA2-Enterprise") )
        setattr(cls, "WPA3-PSK",
                PermissibleValue(text="WPA3-PSK") )
        setattr(cls, "WPA3-Enterprise",
                PermissibleValue(text="WPA3-Enterprise") )

class AccountTypeEnum(EnumDefinitionImpl):
    """
    "An account type represents the endpoint type where the account is located; for example, ADS for an
    ActiveDirectory endpoint type, or LDAP for an LDAP, etc."
    """
    ldap = PermissibleValue(text="ldap")
    nis = PermissibleValue(text="nis")
    openid = PermissibleValue(text="openid")
    radius = PermissibleValue(text="radius")
    tacacs = PermissibleValue(text="tacacs")
    unix = PermissibleValue(text="unix")
    windows_domain = PermissibleValue(text="windows_domain")
    windows_local = PermissibleValue(text="windows_local")

    _defn = EnumDefinition(
        name="AccountTypeEnum",
        description="\"An account type represents the endpoint type where the account is located; for example, ADS for an ActiveDirectory endpoint type, or LDAP for an LDAP, etc.\"",
    )

class ActionArgumentNameEnum(EnumDefinitionImpl):

    API = PermissibleValue(text="API")
    Command = PermissibleValue(text="Command")
    Flags = PermissibleValue(text="Flags")
    Hostname = PermissibleValue(text="Hostname")
    Options = PermissibleValue(text="Options")
    Password = PermissibleValue(text="Password")
    Protection = PermissibleValue(text="Protection")
    Reason = PermissibleValue(text="Reason")
    Server = PermissibleValue(text="Server")
    Username = PermissibleValue(text="Username")

    _defn = EnumDefinition(
        name="ActionArgumentNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "APC Address",
                PermissibleValue(text="APC Address") )
        setattr(cls, "APC Mode",
                PermissibleValue(text="APC Mode") )
        setattr(cls, "Access Mode",
                PermissibleValue(text="Access Mode") )
        setattr(cls, "Application Name",
                PermissibleValue(text="Application Name") )
        setattr(cls, "Base Address",
                PermissibleValue(text="Base Address") )
        setattr(cls, "Callback Address",
                PermissibleValue(text="Callback Address") )
        setattr(cls, "Code Address",
                PermissibleValue(text="Code Address") )
        setattr(cls, "Control Code",
                PermissibleValue(text="Control Code") )
        setattr(cls, "Control Parameter",
                PermissibleValue(text="Control Parameter") )
        setattr(cls, "Creation Flags",
                PermissibleValue(text="Creation Flags") )
        setattr(cls, "Database Name",
                PermissibleValue(text="Database Name") )
        setattr(cls, "Delay Time (ms)",
                PermissibleValue(text="Delay Time (ms)") )
        setattr(cls, "Destination Address",
                PermissibleValue(text="Destination Address") )
        setattr(cls, "Error Control",
                PermissibleValue(text="Error Control") )
        setattr(cls, "File Information Class",
                PermissibleValue(text="File Information Class") )
        setattr(cls, "Function Address",
                PermissibleValue(text="Function Address") )
        setattr(cls, "Function Name",
                PermissibleValue(text="Function Name") )
        setattr(cls, "Function Ordinal",
                PermissibleValue(text="Function Ordinal") )
        setattr(cls, "Hook Type",
                PermissibleValue(text="Hook Type") )
        setattr(cls, "Host Name",
                PermissibleValue(text="Host Name") )
        setattr(cls, "Initial Owner",
                PermissibleValue(text="Initial Owner") )
        setattr(cls, "Mapping Offset",
                PermissibleValue(text="Mapping Offset") )
        setattr(cls, "Number of Bytes Per Send",
                PermissibleValue(text="Number of Bytes Per Send") )
        setattr(cls, "Parameter Address",
                PermissibleValue(text="Parameter Address") )
        setattr(cls, "Privilege Name",
                PermissibleValue(text="Privilege Name") )
        setattr(cls, "Proxy Bypass",
                PermissibleValue(text="Proxy Bypass") )
        setattr(cls, "Proxy Name",
                PermissibleValue(text="Proxy Name") )
        setattr(cls, "Request Size",
                PermissibleValue(text="Request Size") )
        setattr(cls, "Requested Version",
                PermissibleValue(text="Requested Version") )
        setattr(cls, "Service Name",
                PermissibleValue(text="Service Name") )
        setattr(cls, "Service State",
                PermissibleValue(text="Service State") )
        setattr(cls, "Service Type",
                PermissibleValue(text="Service Type") )
        setattr(cls, "Share Mode",
                PermissibleValue(text="Share Mode") )
        setattr(cls, "Shutdown Flag",
                PermissibleValue(text="Shutdown Flag") )
        setattr(cls, "Size (bytes)",
                PermissibleValue(text="Size (bytes)") )
        setattr(cls, "Sleep Time (ms)",
                PermissibleValue(text="Sleep Time (ms)") )
        setattr(cls, "Source Address",
                PermissibleValue(text="Source Address") )
        setattr(cls, "Starting Address",
                PermissibleValue(text="Starting Address") )
        setattr(cls, "System Metric Index",
                PermissibleValue(text="System Metric Index") )
        setattr(cls, "Target PID",
                PermissibleValue(text="Target PID") )
        setattr(cls, "Transfer Flags",
                PermissibleValue(text="Transfer Flags") )

class ActionNameEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ActionNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Accept Socket Connection",
                PermissibleValue(text="Accept Socket Connection") )
        setattr(cls, "Add Connection to Network Share",
                PermissibleValue(text="Add Connection to Network Share") )
        setattr(cls, "Add Network Share",
                PermissibleValue(text="Add Network Share") )
        setattr(cls, "Add Scheduled Task",
                PermissibleValue(text="Add Scheduled Task") )
        setattr(cls, "Add System Call Hook",
                PermissibleValue(text="Add System Call Hook") )
        setattr(cls, "Add User",
                PermissibleValue(text="Add User") )
        setattr(cls, "Add Windows Hook",
                PermissibleValue(text="Add Windows Hook") )
        setattr(cls, "Allocate Virtual Memory in Process",
                PermissibleValue(text="Allocate Virtual Memory in Process") )
        setattr(cls, "Bind Address to Socket",
                PermissibleValue(text="Bind Address to Socket") )
        setattr(cls, "Change Service Configuration",
                PermissibleValue(text="Change Service Configuration") )
        setattr(cls, "Check for Remote Debugger",
                PermissibleValue(text="Check for Remote Debugger") )
        setattr(cls, "Close Port",
                PermissibleValue(text="Close Port") )
        setattr(cls, "Close Registry Key",
                PermissibleValue(text="Close Registry Key") )
        setattr(cls, "Close Socket",
                PermissibleValue(text="Close Socket") )
        setattr(cls, "Configure Service",
                PermissibleValue(text="Configure Service") )
        setattr(cls, "Connect to IP",
                PermissibleValue(text="Connect to IP") )
        setattr(cls, "Connect to Named Pipe",
                PermissibleValue(text="Connect to Named Pipe") )
        setattr(cls, "Connect to Network Share",
                PermissibleValue(text="Connect to Network Share") )
        setattr(cls, "Connect to Socket",
                PermissibleValue(text="Connect to Socket") )
        setattr(cls, "Connect to URL",
                PermissibleValue(text="Connect to URL") )
        setattr(cls, "Control Driver",
                PermissibleValue(text="Control Driver") )
        setattr(cls, "Control Service",
                PermissibleValue(text="Control Service") )
        setattr(cls, "Copy File",
                PermissibleValue(text="Copy File") )
        setattr(cls, "Create Dialog Box",
                PermissibleValue(text="Create Dialog Box") )
        setattr(cls, "Create Directory",
                PermissibleValue(text="Create Directory") )
        setattr(cls, "Create Event",
                PermissibleValue(text="Create Event") )
        setattr(cls, "Create File",
                PermissibleValue(text="Create File") )
        setattr(cls, "Create File Alternate Data Stream",
                PermissibleValue(text="Create File Alternate Data Stream") )
        setattr(cls, "Create File Mapping",
                PermissibleValue(text="Create File Mapping") )
        setattr(cls, "Create File Symbolic Link",
                PermissibleValue(text="Create File Symbolic Link") )
        setattr(cls, "Create Hidden File",
                PermissibleValue(text="Create Hidden File") )
        setattr(cls, "Create Mailslot",
                PermissibleValue(text="Create Mailslot") )
        setattr(cls, "Create Module",
                PermissibleValue(text="Create Module") )
        setattr(cls, "Create Mutex",
                PermissibleValue(text="Create Mutex") )
        setattr(cls, "Create Named Pipe",
                PermissibleValue(text="Create Named Pipe") )
        setattr(cls, "Create Process",
                PermissibleValue(text="Create Process") )
        setattr(cls, "Create Process as User",
                PermissibleValue(text="Create Process as User") )
        setattr(cls, "Create Registry Key",
                PermissibleValue(text="Create Registry Key") )
        setattr(cls, "Create Registry Key Value",
                PermissibleValue(text="Create Registry Key Value") )
        setattr(cls, "Create Remote Thread in Process",
                PermissibleValue(text="Create Remote Thread in Process") )
        setattr(cls, "Create Service",
                PermissibleValue(text="Create Service") )
        setattr(cls, "Create Socket",
                PermissibleValue(text="Create Socket") )
        setattr(cls, "Create Symbolic Link",
                PermissibleValue(text="Create Symbolic Link") )
        setattr(cls, "Create Thread",
                PermissibleValue(text="Create Thread") )
        setattr(cls, "Create Window",
                PermissibleValue(text="Create Window") )
        setattr(cls, "Delete Directory",
                PermissibleValue(text="Delete Directory") )
        setattr(cls, "Delete File",
                PermissibleValue(text="Delete File") )
        setattr(cls, "Delete Named Pipe",
                PermissibleValue(text="Delete Named Pipe") )
        setattr(cls, "Delete Network Share",
                PermissibleValue(text="Delete Network Share") )
        setattr(cls, "Delete Registry Key",
                PermissibleValue(text="Delete Registry Key") )
        setattr(cls, "Delete Registry Key Value",
                PermissibleValue(text="Delete Registry Key Value") )
        setattr(cls, "Delete Service",
                PermissibleValue(text="Delete Service") )
        setattr(cls, "Delete User",
                PermissibleValue(text="Delete User") )
        setattr(cls, "Disconnect from Named Pipe",
                PermissibleValue(text="Disconnect from Named Pipe") )
        setattr(cls, "Disconnect from Network Share",
                PermissibleValue(text="Disconnect from Network Share") )
        setattr(cls, "Disconnect from Socket",
                PermissibleValue(text="Disconnect from Socket") )
        setattr(cls, "Download File",
                PermissibleValue(text="Download File") )
        setattr(cls, "Enumerate DLLs",
                PermissibleValue(text="Enumerate DLLs") )
        setattr(cls, "Enumerate Network Shares",
                PermissibleValue(text="Enumerate Network Shares") )
        setattr(cls, "Enumerate Processes",
                PermissibleValue(text="Enumerate Processes") )
        setattr(cls, "Enumerate Protocols",
                PermissibleValue(text="Enumerate Protocols") )
        setattr(cls, "Enumerate Registry Key Subkeys",
                PermissibleValue(text="Enumerate Registry Key Subkeys") )
        setattr(cls, "Enumerate Registry Key Values",
                PermissibleValue(text="Enumerate Registry Key Values") )
        setattr(cls, "Enumerate Services",
                PermissibleValue(text="Enumerate Services") )
        setattr(cls, "Enumerate System Handles",
                PermissibleValue(text="Enumerate System Handles") )
        setattr(cls, "Enumerate Threads",
                PermissibleValue(text="Enumerate Threads") )
        setattr(cls, "Enumerate Threads in Process",
                PermissibleValue(text="Enumerate Threads in Process") )
        setattr(cls, "Enumerate Users",
                PermissibleValue(text="Enumerate Users") )
        setattr(cls, "Enumerate Windows",
                PermissibleValue(text="Enumerate Windows") )
        setattr(cls, "Find File",
                PermissibleValue(text="Find File") )
        setattr(cls, "Find Window",
                PermissibleValue(text="Find Window") )
        setattr(cls, "Flush Process Instruction Cache",
                PermissibleValue(text="Flush Process Instruction Cache") )
        setattr(cls, "Free Library",
                PermissibleValue(text="Free Library") )
        setattr(cls, "Free Process Virtual Memory",
                PermissibleValue(text="Free Process Virtual Memory") )
        setattr(cls, "Get Disk Free Space",
                PermissibleValue(text="Get Disk Free Space") )
        setattr(cls, "Get Disk Type",
                PermissibleValue(text="Get Disk Type") )
        setattr(cls, "Get Elapsed System Up Time",
                PermissibleValue(text="Get Elapsed System Up Time") )
        setattr(cls, "Get File Attributes",
                PermissibleValue(text="Get File Attributes") )
        setattr(cls, "Get Function Address",
                PermissibleValue(text="Get Function Address") )
        setattr(cls, "Get Host By Address",
                PermissibleValue(text="Get Host By Address") )
        setattr(cls, "Get Host By Name",
                PermissibleValue(text="Get Host By Name") )
        setattr(cls, "Get Host Name",
                PermissibleValue(text="Get Host Name") )
        setattr(cls, "Get Library File Name",
                PermissibleValue(text="Get Library File Name") )
        setattr(cls, "Get Library Handle",
                PermissibleValue(text="Get Library Handle") )
        setattr(cls, "Get NetBIOS Name",
                PermissibleValue(text="Get NetBIOS Name") )
        setattr(cls, "Get Process Current Directory",
                PermissibleValue(text="Get Process Current Directory") )
        setattr(cls, "Get Process Environment Variable",
                PermissibleValue(text="Get Process Environment Variable") )
        setattr(cls, "Get Process Startup Information",
                PermissibleValue(text="Get Process Startup Information") )
        setattr(cls, "Get Processes Snapshot",
                PermissibleValue(text="Get Processes Snapshot") )
        setattr(cls, "Get Registry Key Attributes",
                PermissibleValue(text="Get Registry Key Attributes") )
        setattr(cls, "Get Service Status",
                PermissibleValue(text="Get Service Status") )
        setattr(cls, "Get System Global Flags",
                PermissibleValue(text="Get System Global Flags") )
        setattr(cls, "Get System Host Name",
                PermissibleValue(text="Get System Host Name") )
        setattr(cls, "Get System Local Time",
                PermissibleValue(text="Get System Local Time") )
        setattr(cls, "Get System NetBIOS Name",
                PermissibleValue(text="Get System NetBIOS Name") )
        setattr(cls, "Get System Network Parameters",
                PermissibleValue(text="Get System Network Parameters") )
        setattr(cls, "Get System Time",
                PermissibleValue(text="Get System Time") )
        setattr(cls, "Get Thread Context",
                PermissibleValue(text="Get Thread Context") )
        setattr(cls, "Get Thread Username",
                PermissibleValue(text="Get Thread Username") )
        setattr(cls, "Get User Attributes",
                PermissibleValue(text="Get User Attributes") )
        setattr(cls, "Get Username",
                PermissibleValue(text="Get Username") )
        setattr(cls, "Get Windows Directory",
                PermissibleValue(text="Get Windows Directory") )
        setattr(cls, "Get Windows System Directory",
                PermissibleValue(text="Get Windows System Directory") )
        setattr(cls, "Get Windows Temporary Files Directory",
                PermissibleValue(text="Get Windows Temporary Files Directory") )
        setattr(cls, "Hide Window",
                PermissibleValue(text="Hide Window") )
        setattr(cls, "Impersonate Process",
                PermissibleValue(text="Impersonate Process") )
        setattr(cls, "Impersonate Thread",
                PermissibleValue(text="Impersonate Thread") )
        setattr(cls, "Inject Memory Page",
                PermissibleValue(text="Inject Memory Page") )
        setattr(cls, "Kill Process",
                PermissibleValue(text="Kill Process") )
        setattr(cls, "Kill Thread",
                PermissibleValue(text="Kill Thread") )
        setattr(cls, "Kill Window",
                PermissibleValue(text="Kill Window") )
        setattr(cls, "Listen on Port",
                PermissibleValue(text="Listen on Port") )
        setattr(cls, "Listen on Socket",
                PermissibleValue(text="Listen on Socket") )
        setattr(cls, "Load Driver",
                PermissibleValue(text="Load Driver") )
        setattr(cls, "Load Library",
                PermissibleValue(text="Load Library") )
        setattr(cls, "Load Module",
                PermissibleValue(text="Load Module") )
        setattr(cls, "Load and Call Driver",
                PermissibleValue(text="Load and Call Driver") )
        setattr(cls, "Lock File",
                PermissibleValue(text="Lock File") )
        setattr(cls, "Logon as User",
                PermissibleValue(text="Logon as User") )
        setattr(cls, "Map File",
                PermissibleValue(text="Map File") )
        setattr(cls, "Map Library",
                PermissibleValue(text="Map Library") )
        setattr(cls, "Map View of File",
                PermissibleValue(text="Map View of File") )
        setattr(cls, "Modify File",
                PermissibleValue(text="Modify File") )
        setattr(cls, "Modify Named Pipe",
                PermissibleValue(text="Modify Named Pipe") )
        setattr(cls, "Modify Process",
                PermissibleValue(text="Modify Process") )
        setattr(cls, "Modify Registry Key",
                PermissibleValue(text="Modify Registry Key") )
        setattr(cls, "Modify Registry Key Value",
                PermissibleValue(text="Modify Registry Key Value") )
        setattr(cls, "Modify Service",
                PermissibleValue(text="Modify Service") )
        setattr(cls, "Monitor Registry Key",
                PermissibleValue(text="Monitor Registry Key") )
        setattr(cls, "Move File",
                PermissibleValue(text="Move File") )
        setattr(cls, "Open File",
                PermissibleValue(text="Open File") )
        setattr(cls, "Open File Mapping",
                PermissibleValue(text="Open File Mapping") )
        setattr(cls, "Open Mutex",
                PermissibleValue(text="Open Mutex") )
        setattr(cls, "Open Port",
                PermissibleValue(text="Open Port") )
        setattr(cls, "Open Process",
                PermissibleValue(text="Open Process") )
        setattr(cls, "Open Registry Key",
                PermissibleValue(text="Open Registry Key") )
        setattr(cls, "Open Service",
                PermissibleValue(text="Open Service") )
        setattr(cls, "Open Service Control Manager",
                PermissibleValue(text="Open Service Control Manager") )
        setattr(cls, "Protect Virtual Memory",
                PermissibleValue(text="Protect Virtual Memory") )
        setattr(cls, "Query DNS",
                PermissibleValue(text="Query DNS") )
        setattr(cls, "Query Disk Attributes",
                PermissibleValue(text="Query Disk Attributes") )
        setattr(cls, "Query Process Virtual Memory",
                PermissibleValue(text="Query Process Virtual Memory") )
        setattr(cls, "Queue APC in Thread",
                PermissibleValue(text="Queue APC in Thread") )
        setattr(cls, "Read File",
                PermissibleValue(text="Read File") )
        setattr(cls, "Read From Named Pipe",
                PermissibleValue(text="Read From Named Pipe") )
        setattr(cls, "Read From Process Memory",
                PermissibleValue(text="Read From Process Memory") )
        setattr(cls, "Read Registry Key Value",
                PermissibleValue(text="Read Registry Key Value") )
        setattr(cls, "Receive Data on Socket",
                PermissibleValue(text="Receive Data on Socket") )
        setattr(cls, "Receive Email Message",
                PermissibleValue(text="Receive Email Message") )
        setattr(cls, "Release Mutex",
                PermissibleValue(text="Release Mutex") )
        setattr(cls, "Rename File",
                PermissibleValue(text="Rename File") )
        setattr(cls, "Revert Thread to Self",
                PermissibleValue(text="Revert Thread to Self") )
        setattr(cls, "Send Control Code to File",
                PermissibleValue(text="Send Control Code to File") )
        setattr(cls, "Send Control Code to Pipe",
                PermissibleValue(text="Send Control Code to Pipe") )
        setattr(cls, "Send Control Code to Service",
                PermissibleValue(text="Send Control Code to Service") )
        setattr(cls, "Send DNS Query",
                PermissibleValue(text="Send DNS Query") )
        setattr(cls, "Send Data on Socket",
                PermissibleValue(text="Send Data on Socket") )
        setattr(cls, "Send Data to Address on Socket",
                PermissibleValue(text="Send Data to Address on Socket") )
        setattr(cls, "Send Email Message",
                PermissibleValue(text="Send Email Message") )
        setattr(cls, "Send ICMP Request",
                PermissibleValue(text="Send ICMP Request") )
        setattr(cls, "Send Reverse DNS Query",
                PermissibleValue(text="Send Reverse DNS Query") )
        setattr(cls, "Set File Attributes",
                PermissibleValue(text="Set File Attributes") )
        setattr(cls, "Set NetBIOS Name",
                PermissibleValue(text="Set NetBIOS Name") )
        setattr(cls, "Set Process Current Directory",
                PermissibleValue(text="Set Process Current Directory") )
        setattr(cls, "Set Process Environment Variable",
                PermissibleValue(text="Set Process Environment Variable") )
        setattr(cls, "Set System Global Flags",
                PermissibleValue(text="Set System Global Flags") )
        setattr(cls, "Set System Host Name",
                PermissibleValue(text="Set System Host Name") )
        setattr(cls, "Set System Time",
                PermissibleValue(text="Set System Time") )
        setattr(cls, "Set Thread Context",
                PermissibleValue(text="Set Thread Context") )
        setattr(cls, "Show Window",
                PermissibleValue(text="Show Window") )
        setattr(cls, "Shutdown System",
                PermissibleValue(text="Shutdown System") )
        setattr(cls, "Sleep Process",
                PermissibleValue(text="Sleep Process") )
        setattr(cls, "Sleep System",
                PermissibleValue(text="Sleep System") )
        setattr(cls, "Start Service",
                PermissibleValue(text="Start Service") )
        setattr(cls, "Unload Driver",
                PermissibleValue(text="Unload Driver") )
        setattr(cls, "Unload Module",
                PermissibleValue(text="Unload Module") )
        setattr(cls, "Unlock File",
                PermissibleValue(text="Unlock File") )
        setattr(cls, "Unmap File",
                PermissibleValue(text="Unmap File") )
        setattr(cls, "Upload File",
                PermissibleValue(text="Upload File") )
        setattr(cls, "Write to File",
                PermissibleValue(text="Write to File") )
        setattr(cls, "Write to Process Virtual Memory",
                PermissibleValue(text="Write to Process Virtual Memory") )

class ActionRelationshipTypeEnum(EnumDefinitionImpl):

    Dependent_On = PermissibleValue(text="Dependent_On")
    Equivalent_To = PermissibleValue(text="Equivalent_To")
    Followed_By = PermissibleValue(text="Followed_By")
    Initiated = PermissibleValue(text="Initiated")
    Initiated_By = PermissibleValue(text="Initiated_By")
    Preceded_By = PermissibleValue(text="Preceded_By")
    Related_To = PermissibleValue(text="Related_To")

    _defn = EnumDefinition(
        name="ActionRelationshipTypeEnum",
    )

class ActionStatusTypeEnum(EnumDefinitionImpl):

    Error = PermissibleValue(text="Error")
    Fail = PermissibleValue(text="Fail")
    Ongoing = PermissibleValue(text="Ongoing")
    Pending = PermissibleValue(text="Pending")
    Success = PermissibleValue(text="Success")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ActionStatusTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete/Finish",
                PermissibleValue(text="Complete/Finish") )

class ActionTypeEnum(EnumDefinitionImpl):

    Accept = PermissibleValue(text="Accept")
    Access = PermissibleValue(text="Access")
    Add = PermissibleValue(text="Add")
    Alert = PermissibleValue(text="Alert")
    Allocate = PermissibleValue(text="Allocate")
    Archive = PermissibleValue(text="Archive")
    Assign = PermissibleValue(text="Assign")
    Audit = PermissibleValue(text="Audit")
    Backup = PermissibleValue(text="Backup")
    Bind = PermissibleValue(text="Bind")
    Block = PermissibleValue(text="Block")
    Call = PermissibleValue(text="Call")
    Change = PermissibleValue(text="Change")
    Check = PermissibleValue(text="Check")
    Clean = PermissibleValue(text="Clean")
    Click = PermissibleValue(text="Click")
    Close = PermissibleValue(text="Close")
    Compare = PermissibleValue(text="Compare")
    Compress = PermissibleValue(text="Compress")
    Configure = PermissibleValue(text="Configure")
    Connect = PermissibleValue(text="Connect")
    Control = PermissibleValue(text="Control")
    Create = PermissibleValue(text="Create")
    Decode = PermissibleValue(text="Decode")
    Decompress = PermissibleValue(text="Decompress")
    Decrypt = PermissibleValue(text="Decrypt")
    Deny = PermissibleValue(text="Deny")
    Depress = PermissibleValue(text="Depress")
    Detect = PermissibleValue(text="Detect")
    Disconnect = PermissibleValue(text="Disconnect")
    Download = PermissibleValue(text="Download")
    Draw = PermissibleValue(text="Draw")
    Drop = PermissibleValue(text="Drop")
    Encode = PermissibleValue(text="Encode")
    Encrypt = PermissibleValue(text="Encrypt")
    Enumerate = PermissibleValue(text="Enumerate")
    Execute = PermissibleValue(text="Execute")
    Extract = PermissibleValue(text="Extract")
    Filter = PermissibleValue(text="Filter")
    Find = PermissibleValue(text="Find")
    Flush = PermissibleValue(text="Flush")
    Fork = PermissibleValue(text="Fork")
    Free = PermissibleValue(text="Free")
    Get = PermissibleValue(text="Get")
    Hide = PermissibleValue(text="Hide")
    Hook = PermissibleValue(text="Hook")
    Impersonate = PermissibleValue(text="Impersonate")
    Initialize = PermissibleValue(text="Initialize")
    Inject = PermissibleValue(text="Inject")
    Install = PermissibleValue(text="Install")
    Interleave = PermissibleValue(text="Interleave")
    Join = PermissibleValue(text="Join")
    Kill = PermissibleValue(text="Kill")
    Listen = PermissibleValue(text="Listen")
    Load = PermissibleValue(text="Load")
    Lock = PermissibleValue(text="Lock")
    Map = PermissibleValue(text="Map")
    Merge = PermissibleValue(text="Merge")
    Modify = PermissibleValue(text="Modify")
    Monitor = PermissibleValue(text="Monitor")
    Move = PermissibleValue(text="Move")
    Open = PermissibleValue(text="Open")
    Pack = PermissibleValue(text="Pack")
    Pause = PermissibleValue(text="Pause")
    Press = PermissibleValue(text="Press")
    Protect = PermissibleValue(text="Protect")
    Quarantine = PermissibleValue(text="Quarantine")
    Query = PermissibleValue(text="Query")
    Queue = PermissibleValue(text="Queue")
    Raise = PermissibleValue(text="Raise")
    Read = PermissibleValue(text="Read")
    Receive = PermissibleValue(text="Receive")
    Release = PermissibleValue(text="Release")
    Rename = PermissibleValue(text="Rename")
    Replicate = PermissibleValue(text="Replicate")
    Restore = PermissibleValue(text="Restore")
    Resume = PermissibleValue(text="Resume")
    Revert = PermissibleValue(text="Revert")
    Run = PermissibleValue(text="Run")
    Save = PermissibleValue(text="Save")
    Scan = PermissibleValue(text="Scan")
    Schedule = PermissibleValue(text="Schedule")
    Search = PermissibleValue(text="Search")
    Send = PermissibleValue(text="Send")
    Set = PermissibleValue(text="Set")
    Shutdown = PermissibleValue(text="Shutdown")
    Sleep = PermissibleValue(text="Sleep")
    Snapshot = PermissibleValue(text="Snapshot")
    Start = PermissibleValue(text="Start")
    Stop = PermissibleValue(text="Stop")
    Suspend = PermissibleValue(text="Suspend")
    Synchronize = PermissibleValue(text="Synchronize")
    Throw = PermissibleValue(text="Throw")
    Transmit = PermissibleValue(text="Transmit")
    Unblock = PermissibleValue(text="Unblock")
    Unhide = PermissibleValue(text="Unhide")
    Unhook = PermissibleValue(text="Unhook")
    Uninstall = PermissibleValue(text="Uninstall")
    Unload = PermissibleValue(text="Unload")
    Unlock = PermissibleValue(text="Unlock")
    Unmap = PermissibleValue(text="Unmap")
    Unpack = PermissibleValue(text="Unpack")
    Update = PermissibleValue(text="Update")
    Upgrade = PermissibleValue(text="Upgrade")
    Upload = PermissibleValue(text="Upload")
    Write = PermissibleValue(text="Write")

    _defn = EnumDefinition(
        name="ActionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Copy/Duplicate",
                PermissibleValue(text="Copy/Duplicate") )
        setattr(cls, "Login/Logon",
                PermissibleValue(text="Login/Logon") )
        setattr(cls, "Logout/Logoff",
                PermissibleValue(text="Logout/Logoff") )
        setattr(cls, "Remove/Delete",
                PermissibleValue(text="Remove/Delete") )
        setattr(cls, "Wipe/Destroy/Purge",
                PermissibleValue(text="Wipe/Destroy/Purge") )

class BitnessEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="BitnessEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "32",
                PermissibleValue(text="32") )
        setattr(cls, "64",
                PermissibleValue(text="64") )

class CharacterEncodingEnum(EnumDefinitionImpl):

    ASCII = PermissibleValue(text="ASCII")

    _defn = EnumDefinition(
        name="CharacterEncodingEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "UTF-16",
                PermissibleValue(text="UTF-16") )
        setattr(cls, "UTF-32",
                PermissibleValue(text="UTF-32") )
        setattr(cls, "UTF-8",
                PermissibleValue(text="UTF-8") )
        setattr(cls, "Windows-1250",
                PermissibleValue(text="Windows-1250") )
        setattr(cls, "Windows-1251",
                PermissibleValue(text="Windows-1251") )
        setattr(cls, "Windows-1252",
                PermissibleValue(text="Windows-1252") )
        setattr(cls, "Windows-1253",
                PermissibleValue(text="Windows-1253") )
        setattr(cls, "Windows-1254",
                PermissibleValue(text="Windows-1254") )
        setattr(cls, "Windows-1255",
                PermissibleValue(text="Windows-1255") )
        setattr(cls, "Windows-1256",
                PermissibleValue(text="Windows-1256") )
        setattr(cls, "Windows-1257",
                PermissibleValue(text="Windows-1257") )
        setattr(cls, "Windows-1258",
                PermissibleValue(text="Windows-1258") )

class ContactAddressScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactAddressScopeEnum",
    )

class ContactEmailScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    cloud = PermissibleValue(text="cloud")

    _defn = EnumDefinition(
        name="ContactEmailScopeEnum",
    )

class ContactPhoneEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    mobile = PermissibleValue(text="mobile")
    main = PermissibleValue(text="main")
    pager = PermissibleValue(text="pager")

    _defn = EnumDefinition(
        name="ContactPhoneEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "home fax",
                PermissibleValue(text="home fax") )
        setattr(cls, "work fax",
                PermissibleValue(text="work fax") )

class ContactSIPScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")

    _defn = EnumDefinition(
        name="ContactSIPScopeEnum",
    )

class ContactURLScopeEnum(EnumDefinitionImpl):

    home = PermissibleValue(text="home")
    work = PermissibleValue(text="work")
    school = PermissibleValue(text="school")
    homepage = PermissibleValue(text="homepage")

    _defn = EnumDefinition(
        name="ContactURLScopeEnum",
    )

class DiskTypeEnum(EnumDefinitionImpl):

    CDRom = PermissibleValue(text="CDRom")
    Fixed = PermissibleValue(text="Fixed")
    RAMDisk = PermissibleValue(text="RAMDisk")
    Remote = PermissibleValue(text="Remote")
    Removable = PermissibleValue(text="Removable")

    _defn = EnumDefinition(
        name="DiskTypeEnum",
    )

class EndiannessTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="EndiannessTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Big-endian",
                PermissibleValue(text="Big-endian") )
        setattr(cls, "Little-endian",
                PermissibleValue(text="Little-endian") )
        setattr(cls, "Middle-endian",
                PermissibleValue(text="Middle-endian") )

class HashNameEnum(EnumDefinitionImpl):

    MD5 = PermissibleValue(text="MD5")
    MD6 = PermissibleValue(text="MD6")
    SHA1 = PermissibleValue(text="SHA1")
    SHA224 = PermissibleValue(text="SHA224")
    SHA256 = PermissibleValue(text="SHA256")
    SHA384 = PermissibleValue(text="SHA384")
    SHA512 = PermissibleValue(text="SHA512")
    SSDEEP = PermissibleValue(text="SSDEEP")

    _defn = EnumDefinition(
        name="HashNameEnum",
    )

class LibraryTypeEnum(EnumDefinitionImpl):

    Dynamic = PermissibleValue(text="Dynamic")
    Other = PermissibleValue(text="Other")
    Remote = PermissibleValue(text="Remote")
    Shared = PermissibleValue(text="Shared")
    Static = PermissibleValue(text="Static")

    _defn = EnumDefinition(
        name="LibraryTypeEnum",
    )

class MemoryBlockTypeEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Overlay = PermissibleValue(text="Overlay")
    Uninitialized = PermissibleValue(text="Uninitialized")

    _defn = EnumDefinition(
        name="MemoryBlockTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Bit-mapped",
                PermissibleValue(text="Bit-mapped") )
        setattr(cls, "Byte-mapped",
                PermissibleValue(text="Byte-mapped") )

class ObservableObjectRelationshipEnum(EnumDefinitionImpl):

    Allocated = PermissibleValue(text="Allocated")
    Allocated_By = PermissibleValue(text="Allocated_By")
    Attachment_Of = PermissibleValue(text="Attachment_Of")
    Bound = PermissibleValue(text="Bound")
    Bound_By = PermissibleValue(text="Bound_By")
    Characterized_By = PermissibleValue(text="Characterized_By")
    Characterizes = PermissibleValue(text="Characterizes")
    Child_Of = PermissibleValue(text="Child_Of")
    Closed = PermissibleValue(text="Closed")
    Closed_By = PermissibleValue(text="Closed_By")
    Compressed = PermissibleValue(text="Compressed")
    Compressed_By = PermissibleValue(text="Compressed_By")
    Compressed_From = PermissibleValue(text="Compressed_From")
    Compressed_Into = PermissibleValue(text="Compressed_Into")
    Connected_From = PermissibleValue(text="Connected_From")
    Connected_To = PermissibleValue(text="Connected_To")
    Contained_Within = PermissibleValue(text="Contained_Within")
    Contains = PermissibleValue(text="Contains")
    Copied = PermissibleValue(text="Copied")
    Copied_By = PermissibleValue(text="Copied_By")
    Copied_From = PermissibleValue(text="Copied_From")
    Copied_To = PermissibleValue(text="Copied_To")
    Created = PermissibleValue(text="Created")
    Created_By = PermissibleValue(text="Created_By")
    Decoded = PermissibleValue(text="Decoded")
    Decoded_By = PermissibleValue(text="Decoded_By")
    Decompressed = PermissibleValue(text="Decompressed")
    Decompressed_By = PermissibleValue(text="Decompressed_By")
    Decrypted = PermissibleValue(text="Decrypted")
    Decrypted_By = PermissibleValue(text="Decrypted_By")
    Deleted = PermissibleValue(text="Deleted")
    Deleted_By = PermissibleValue(text="Deleted_By")
    Deleted_From = PermissibleValue(text="Deleted_From")
    Downloaded = PermissibleValue(text="Downloaded")
    Downloaded_By = PermissibleValue(text="Downloaded_By")
    Downloaded_From = PermissibleValue(text="Downloaded_From")
    Downloaded_To = PermissibleValue(text="Downloaded_To")
    Dropped = PermissibleValue(text="Dropped")
    Dropped_By = PermissibleValue(text="Dropped_By")
    Encoded = PermissibleValue(text="Encoded")
    Encoded_By = PermissibleValue(text="Encoded_By")
    Encrypted = PermissibleValue(text="Encrypted")
    Encrypted_By = PermissibleValue(text="Encrypted_By")
    Encrypted_From = PermissibleValue(text="Encrypted_From")
    Encrypted_To = PermissibleValue(text="Encrypted_To")
    Extracted_From = PermissibleValue(text="Extracted_From")
    FQDN_Of = PermissibleValue(text="FQDN_Of")
    Freed = PermissibleValue(text="Freed")
    Freed_By = PermissibleValue(text="Freed_By")
    Had_Attachment = PermissibleValue(text="Had_Attachment")
    Hooked = PermissibleValue(text="Hooked")
    Hooked_By = PermissibleValue(text="Hooked_By")
    Initialized_By = PermissibleValue(text="Initialized_By")
    Initialized_To = PermissibleValue(text="Initialized_To")
    Injected = PermissibleValue(text="Injected")
    Injected_As = PermissibleValue(text="Injected_As")
    Injected_By = PermissibleValue(text="Injected_By")
    Injected_Into = PermissibleValue(text="Injected_Into")
    Installed = PermissibleValue(text="Installed")
    Installed_By = PermissibleValue(text="Installed_By")
    Joined = PermissibleValue(text="Joined")
    Joined_By = PermissibleValue(text="Joined_By")
    Killed = PermissibleValue(text="Killed")
    Killed_By = PermissibleValue(text="Killed_By")
    Listened_On = PermissibleValue(text="Listened_On")
    Listened_On_By = PermissibleValue(text="Listened_On_By")
    Loaded_From = PermissibleValue(text="Loaded_From")
    Loaded_Into = PermissibleValue(text="Loaded_Into")
    Locked = PermissibleValue(text="Locked")
    Locked_By = PermissibleValue(text="Locked_By")
    Mapped_By = PermissibleValue(text="Mapped_By")
    Mapped_Into = PermissibleValue(text="Mapped_Into")
    Merged = PermissibleValue(text="Merged")
    Merged_By = PermissibleValue(text="Merged_By")
    Modified_Properties_Of = PermissibleValue(text="Modified_Properties_Of")
    Monitored = PermissibleValue(text="Monitored")
    Monitored_By = PermissibleValue(text="Monitored_By")
    Moved = PermissibleValue(text="Moved")
    Moved_By = PermissibleValue(text="Moved_By")
    Moved_From = PermissibleValue(text="Moved_From")
    Moved_To = PermissibleValue(text="Moved_To")
    Opened = PermissibleValue(text="Opened")
    Opened_By = PermissibleValue(text="Opened_By")
    Packed = PermissibleValue(text="Packed")
    Packed_By = PermissibleValue(text="Packed_By")
    Packed_From = PermissibleValue(text="Packed_From")
    Packed_Into = PermissibleValue(text="Packed_Into")
    Parent_Of = PermissibleValue(text="Parent_Of")
    Paused = PermissibleValue(text="Paused")
    Paused_By = PermissibleValue(text="Paused_By")
    Previously_Contained = PermissibleValue(text="Previously_Contained")
    Properties_Modified_By = PermissibleValue(text="Properties_Modified_By")
    Properties_Queried = PermissibleValue(text="Properties_Queried")
    Properties_Queried_By = PermissibleValue(text="Properties_Queried_By")
    Read_From = PermissibleValue(text="Read_From")
    Read_From_By = PermissibleValue(text="Read_From_By")
    Received = PermissibleValue(text="Received")
    Received_By = PermissibleValue(text="Received_By")
    Received_From = PermissibleValue(text="Received_From")
    Received_Via_Upload = PermissibleValue(text="Received_Via_Upload")
    Redirects_To = PermissibleValue(text="Redirects_To")
    Related_To = PermissibleValue(text="Related_To")
    Renamed = PermissibleValue(text="Renamed")
    Renamed_By = PermissibleValue(text="Renamed_By")
    Renamed_From = PermissibleValue(text="Renamed_From")
    Renamed_To = PermissibleValue(text="Renamed_To")
    Resolved_To = PermissibleValue(text="Resolved_To")
    Resumed = PermissibleValue(text="Resumed")
    Resumed_By = PermissibleValue(text="Resumed_By")
    Root_Domain_Of = PermissibleValue(text="Root_Domain_Of")
    Searched_For = PermissibleValue(text="Searched_For")
    Searched_For_By = PermissibleValue(text="Searched_For_By")
    Sent = PermissibleValue(text="Sent")
    Sent_By = PermissibleValue(text="Sent_By")
    Sent_To = PermissibleValue(text="Sent_To")
    Sent_Via_Upload = PermissibleValue(text="Sent_Via_Upload")
    Set_From = PermissibleValue(text="Set_From")
    Set_To = PermissibleValue(text="Set_To")
    Suspended = PermissibleValue(text="Suspended")
    Suspended_By = PermissibleValue(text="Suspended_By")
    Unhooked = PermissibleValue(text="Unhooked")
    Unhooked_By = PermissibleValue(text="Unhooked_By")
    Unlocked = PermissibleValue(text="Unlocked")
    Unlocked_By = PermissibleValue(text="Unlocked_By")
    Unpacked = PermissibleValue(text="Unpacked")
    Unpacked_By = PermissibleValue(text="Unpacked_By")
    Uploaded = PermissibleValue(text="Uploaded")
    Uploaded_By = PermissibleValue(text="Uploaded_By")
    Uploaded_From = PermissibleValue(text="Uploaded_From")
    Uploaded_To = PermissibleValue(text="Uploaded_To")
    Used = PermissibleValue(text="Used")
    Used_By = PermissibleValue(text="Used_By")
    Values_Enumerated = PermissibleValue(text="Values_Enumerated")
    Values_Enumerated_By = PermissibleValue(text="Values_Enumerated_By")
    Written_To_By = PermissibleValue(text="Written_To_By")
    Wrote_To = PermissibleValue(text="Wrote_To")

    _defn = EnumDefinition(
        name="ObservableObjectRelationshipEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Sub-domain_Of",
                PermissibleValue(text="Sub-domain_Of") )
        setattr(cls, "Supra-domain_Of",
                PermissibleValue(text="Supra-domain_Of") )

class ObservableObjectStateEnum(EnumDefinitionImpl):

    Active = PermissibleValue(text="Active")
    Closed = PermissibleValue(text="Closed")
    Exists = PermissibleValue(text="Exists")
    Inactive = PermissibleValue(text="Inactive")
    Locked = PermissibleValue(text="Locked")
    Open = PermissibleValue(text="Open")
    Started = PermissibleValue(text="Started")
    Stopped = PermissibleValue(text="Stopped")
    Unlocked = PermissibleValue(text="Unlocked")

    _defn = EnumDefinition(
        name="ObservableObjectStateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Does Not Exist",
                PermissibleValue(text="Does Not Exist") )

class PartitionTypeEnum(EnumDefinitionImpl):

    PARTITION_ENTRY_UNUSED = PermissibleValue(text="PARTITION_ENTRY_UNUSED")
    PARTITION_EXTENDED = PermissibleValue(text="PARTITION_EXTENDED")
    PARTITION_FAT32 = PermissibleValue(text="PARTITION_FAT32")
    PARTITION_FAT32_XINT13 = PermissibleValue(text="PARTITION_FAT32_XINT13")
    PARTITION_FAT_12 = PermissibleValue(text="PARTITION_FAT_12")
    PARTITION_FAT_16 = PermissibleValue(text="PARTITION_FAT_16")
    PARTITION_HUGE = PermissibleValue(text="PARTITION_HUGE")
    PARTITION_IFS = PermissibleValue(text="PARTITION_IFS")
    PARTITION_LDM = PermissibleValue(text="PARTITION_LDM")
    PARTITION_NTFT = PermissibleValue(text="PARTITION_NTFT")
    PARTITION_OS2BOOTMGR = PermissibleValue(text="PARTITION_OS2BOOTMGR")
    PARTITION_PREP = PermissibleValue(text="PARTITION_PREP")
    PARTITION_UNIX = PermissibleValue(text="PARTITION_UNIX")
    PARTITION_XENIX_1 = PermissibleValue(text="PARTITION_XENIX_1")
    PARTITION_XENIX_2 = PermissibleValue(text="PARTITION_XENIX_2")
    PARTITION_XINT13 = PermissibleValue(text="PARTITION_XINT13")
    PARTITION_XINT13_EXTENDED = PermissibleValue(text="PARTITION_XINT13_EXTENDED")
    UNKNOWN = PermissibleValue(text="UNKNOWN")
    VALID_NTFT = PermissibleValue(text="VALID_NTFT")

    _defn = EnumDefinition(
        name="PartitionTypeEnum",
    )

class ProcessorArchEnum(EnumDefinitionImpl):

    ARM = PermissibleValue(text="ARM")
    Alpha = PermissibleValue(text="Alpha")
    MIPS = PermissibleValue(text="MIPS")
    Other = PermissibleValue(text="Other")
    PowerPC = PermissibleValue(text="PowerPC")
    SPARC = PermissibleValue(text="SPARC")

    _defn = EnumDefinition(
        name="ProcessorArchEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "IA-64",
                PermissibleValue(text="IA-64") )
        setattr(cls, "Motorola 68k",
                PermissibleValue(text="Motorola 68k") )
        setattr(cls, "eSi-RISC",
                PermissibleValue(text="eSi-RISC") )
        setattr(cls, "x86-32",
                PermissibleValue(text="x86-32") )
        setattr(cls, "x86-64",
                PermissibleValue(text="x86-64") )
        setattr(cls, "z/Architecture",
                PermissibleValue(text="z/Architecture") )

class RecoveredObjectStatusEnum(EnumDefinitionImpl):

    recovered = PermissibleValue(text="recovered")
    overwritten = PermissibleValue(text="overwritten")
    unknown = PermissibleValue(text="unknown")

    _defn = EnumDefinition(
        name="RecoveredObjectStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "partially recovered",
                PermissibleValue(text="partially recovered") )

class RegionalRegistryTypeEnum(EnumDefinitionImpl):

    APNIC = PermissibleValue(text="APNIC")
    ARIN = PermissibleValue(text="ARIN")
    AfriNIC = PermissibleValue(text="AfriNIC")
    LACNIC = PermissibleValue(text="LACNIC")

    _defn = EnumDefinition(
        name="RegionalRegistryTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "RIPE NCC",
                PermissibleValue(text="RIPE NCC") )

class RegistryDatatypeEnum(EnumDefinitionImpl):
    """
    "From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https
    //learn.microsoft.com/en-us/windows/win32/shell/hkey-type"
    """
    reg_binary = PermissibleValue(text="reg_binary",
                                           description=""Binary data in any form."")
    reg_dword = PermissibleValue(text="reg_dword",
                                         description=""A 32-bit number."")
    reg_dword_big_endian = PermissibleValue(text="reg_dword_big_endian",
                                                               description=""A 32-bit number in big-endian format. Some UNIX systems support big-endian architectures."")
    reg_expand_sz = PermissibleValue(text="reg_expand_sz",
                                                 description=""A null-terminated string that contains unexpanded references to environment Variables (for example, '%PATH%'). It will be a Unicode or ANSI string depending on wh ether you use the Unicode or ANSI functions. To expand the environment variable refere nces, use the ExpandEnvironmentStrings function."")
    reg_full_resource_descriptor = PermissibleValue(text="reg_full_resource_descriptor",
                                                                               description=""A list of hardware resources that a physical device is using, detected and written into the \HardwareDescription tree by the system."")
    reg_invalid_type = PermissibleValue(text="reg_invalid_type",
                                                       description=""Specifies an invalid key."")
    reg_link = PermissibleValue(text="reg_link",
                                       description=""A null-terminated Unicode string that contains the target path of a symboli c link that was created by calling the RegCreateKeyEx function with REG_OPTION_CREATE_ LINK."")
    reg_multi_sz = PermissibleValue(text="reg_multi_sz",
                                               description=""A sequence of null-terminated strings, terminated by an empty string (\0). The following is an example: String1\0String2\0String3\0LastString\0\0 The first \0 terminates the first string, the second to the last \0 terminates the last string, and the final \0 terminates the sequence. Note that the final terminator must be factored into the length of the string."")
    reg_none = PermissibleValue(text="reg_none",
                                       description=""No defined value type."")
    reg_qword = PermissibleValue(text="reg_qword",
                                         description=""A 64-bit number."")
    reg_resource_list = PermissibleValue(text="reg_resource_list",
                                                         description=""Device-driver resource list."")
    reg_resource_requirements_list = PermissibleValue(text="reg_resource_requirements_list",
                                                                                   description=""A device driver's list of possible hardware resources it or one of the physical devices it controls can use, from which the system writes a subset into the \ResourceMap tree"")
    reg_sz = PermissibleValue(text="reg_sz",
                                   description=""A null-terminated string. This will be either a Unicode or an ANSI string, depending on whether you use the Unicode or ANSI functions."")

    _defn = EnumDefinition(
        name="RegistryDatatypeEnum",
        description="\"From https //learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types, https //learn.microsoft.com/en-us/windows/win32/shell/hkey-type\"",
    )

class SIMFormEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SIMFormEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Full-size SIM",
                PermissibleValue(text="Full-size SIM") )
        setattr(cls, "Micro SIM",
                PermissibleValue(text="Micro SIM") )
        setattr(cls, "Nano SIM",
                PermissibleValue(text="Nano SIM") )

class SIMTypeEnum(EnumDefinitionImpl):

    SIM = PermissibleValue(text="SIM")
    UICC = PermissibleValue(text="UICC")
    USIM = PermissibleValue(text="USIM")

    _defn = EnumDefinition(
        name="SIMTypeEnum",
    )

class TaskActionTypeEnum(EnumDefinitionImpl):

    TASK_ACTION_COM_HANDLER = PermissibleValue(text="TASK_ACTION_COM_HANDLER")
    TASK_ACTION_EXEC = PermissibleValue(text="TASK_ACTION_EXEC")
    TASK_ACTION_SEND_EMAIL = PermissibleValue(text="TASK_ACTION_SEND_EMAIL")
    TASK_ACTION_SHOW_MESSAGE = PermissibleValue(text="TASK_ACTION_SHOW_MESSAGE")

    _defn = EnumDefinition(
        name="TaskActionTypeEnum",
    )

class TaskFlagEnum(EnumDefinitionImpl):

    TASK_FLAG_DELETE_WHEN_DONE = PermissibleValue(text="TASK_FLAG_DELETE_WHEN_DONE")
    TASK_FLAG_DISABLED = PermissibleValue(text="TASK_FLAG_DISABLED")
    TASK_FLAG_DONT_START_IF_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_DONT_START_IF_ON_BATTERIES")
    TASK_FLAG_HIDDEN = PermissibleValue(text="TASK_FLAG_HIDDEN")
    TASK_FLAG_INTERACTIVE = PermissibleValue(text="TASK_FLAG_INTERACTIVE")
    TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = PermissibleValue(text="TASK_FLAG_KILL_IF_GOING_ON_BATTERIES")
    TASK_FLAG_KILL_ON_IDLE_END = PermissibleValue(text="TASK_FLAG_KILL_ON_IDLE_END")
    TASK_FLAG_RESTART_ON_IDLE_RESUME = PermissibleValue(text="TASK_FLAG_RESTART_ON_IDLE_RESUME")
    TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = PermissibleValue(text="TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET")
    TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = PermissibleValue(text="TASK_FLAG_RUN_ONLY_IF_LOGGED_ON")
    TASK_FLAG_START_ONLY_IF_IDLE = PermissibleValue(text="TASK_FLAG_START_ONLY_IF_IDLE")
    TASK_FLAG_SYSTEM_REQUIRED = PermissibleValue(text="TASK_FLAG_SYSTEM_REQUIRED")
    TASK_FLAG_ZERO = PermissibleValue(text="TASK_FLAG_ZERO")

    _defn = EnumDefinition(
        name="TaskFlagEnum",
    )

class TaskPriorityEnum(EnumDefinitionImpl):

    ABOVE_NORMAL_PRIORITY_CLASS = PermissibleValue(text="ABOVE_NORMAL_PRIORITY_CLASS")
    BELOW_NORMAL_PRIORITY_CLASS = PermissibleValue(text="BELOW_NORMAL_PRIORITY_CLASS")
    HIGH_PRIORITY_CLASS = PermissibleValue(text="HIGH_PRIORITY_CLASS")
    IDLE_PRIORITY_CLASS = PermissibleValue(text="IDLE_PRIORITY_CLASS")
    NORMAL_PRIORITY_CLASS = PermissibleValue(text="NORMAL_PRIORITY_CLASS")
    REALTIME_PRIORITY_CLASS = PermissibleValue(text="REALTIME_PRIORITY_CLASS")

    _defn = EnumDefinition(
        name="TaskPriorityEnum",
    )

class TaskStatusEnum(EnumDefinitionImpl):

    SCHED_E_ACCOUNT_DBASE_CORRUPT = PermissibleValue(text="SCHED_E_ACCOUNT_DBASE_CORRUPT")
    SCHED_E_ACCOUNT_INFORMATION_NOT_SET = PermissibleValue(text="SCHED_E_ACCOUNT_INFORMATION_NOT_SET")
    SCHED_E_ACCOUNT_NAME_NOT_FOUND = PermissibleValue(text="SCHED_E_ACCOUNT_NAME_NOT_FOUND")
    SCHED_E_CANNOT_OPEN_TASK = PermissibleValue(text="SCHED_E_CANNOT_OPEN_TASK")
    SCHED_E_INVALID_TASK = PermissibleValue(text="SCHED_E_INVALID_TASK")
    SCHED_E_NO_SECURITY_SERVICES = PermissibleValue(text="SCHED_E_NO_SECURITY_SERVICES")
    SCHED_E_SERVICE_NOT_INSTALLED = PermissibleValue(text="SCHED_E_SERVICE_NOT_INSTALLED")
    SCHED_E_SERVICE_NOT_RUNNING = PermissibleValue(text="SCHED_E_SERVICE_NOT_RUNNING")
    SCHED_E_TASK_NOT_READY = PermissibleValue(text="SCHED_E_TASK_NOT_READY")
    SCHED_E_TASK_NOT_RUNNING = PermissibleValue(text="SCHED_E_TASK_NOT_RUNNING")
    SCHED_E_TRIGGER_NOT_FOUND = PermissibleValue(text="SCHED_E_TRIGGER_NOT_FOUND")
    SCHED_E_UNKNOWN_OBJECT_VERSION = PermissibleValue(text="SCHED_E_UNKNOWN_OBJECT_VERSION")
    SCHED_E_UNSUPPORTED_ACCOUNT_OPTION = PermissibleValue(text="SCHED_E_UNSUPPORTED_ACCOUNT_OPTION")
    SCHED_S_EVENT_TRIGGER = PermissibleValue(text="SCHED_S_EVENT_TRIGGER")
    SCHED_S_TASK_DISABLED = PermissibleValue(text="SCHED_S_TASK_DISABLED")
    SCHED_S_TASK_HAS_NOT_RUN = PermissibleValue(text="SCHED_S_TASK_HAS_NOT_RUN")
    SCHED_S_TASK_NOT_SCHEDULED = PermissibleValue(text="SCHED_S_TASK_NOT_SCHEDULED")
    SCHED_S_TASK_NO_MORE_RUNS = PermissibleValue(text="SCHED_S_TASK_NO_MORE_RUNS")
    SCHED_S_TASK_NO_VALID_TRIGGERS = PermissibleValue(text="SCHED_S_TASK_NO_VALID_TRIGGERS")
    SCHED_S_TASK_READY = PermissibleValue(text="SCHED_S_TASK_READY")
    SCHED_S_TASK_RUNNING = PermissibleValue(text="SCHED_S_TASK_RUNNING")
    SCHED_S_TASK_TERMINATED = PermissibleValue(text="SCHED_S_TASK_TERMINATED")
    TASK_STATE_QUEUED = PermissibleValue(text="TASK_STATE_QUEUED")
    TASK_STATE_UNKNOWN = PermissibleValue(text="TASK_STATE_UNKNOWN")

    _defn = EnumDefinition(
        name="TaskStatusEnum",
    )

class ThreadRunningStatusEnum(EnumDefinitionImpl):

    Initialized = PermissibleValue(text="Initialized")
    Ready = PermissibleValue(text="Ready")
    Running = PermissibleValue(text="Running")
    Standby = PermissibleValue(text="Standby")
    Terminated = PermissibleValue(text="Terminated")
    Transition = PermissibleValue(text="Transition")
    Unknown = PermissibleValue(text="Unknown")
    Waiting = PermissibleValue(text="Waiting")

    _defn = EnumDefinition(
        name="ThreadRunningStatusEnum",
    )

class TimestampPrecisionEnum(EnumDefinitionImpl):

    day = PermissibleValue(text="day")
    hour = PermissibleValue(text="hour")
    minute = PermissibleValue(text="minute")
    month = PermissibleValue(text="month")
    second = PermissibleValue(text="second")
    year = PermissibleValue(text="year")

    _defn = EnumDefinition(
        name="TimestampPrecisionEnum",
    )

class TrendEnum(EnumDefinitionImpl):

    Decreasing = PermissibleValue(text="Decreasing")
    Increasing = PermissibleValue(text="Increasing")

    _defn = EnumDefinition(
        name="TrendEnum",
    )

class TriggerFrequencyEnum(EnumDefinitionImpl):

    TASK_EVENT_TRIGGER_AT_LOGON = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_LOGON")
    TASK_EVENT_TRIGGER_AT_SYSTEMSTART = PermissibleValue(text="TASK_EVENT_TRIGGER_AT_SYSTEMSTART")
    TASK_EVENT_TRIGGER_ON_IDLE = PermissibleValue(text="TASK_EVENT_TRIGGER_ON_IDLE")
    TASK_TIME_TRIGGER_DAILY = PermissibleValue(text="TASK_TIME_TRIGGER_DAILY")
    TASK_TIME_TRIGGER_MONTHLYDATE = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDATE")
    TASK_TIME_TRIGGER_MONTHLYDOW = PermissibleValue(text="TASK_TIME_TRIGGER_MONTHLYDOW")
    TASK_TIME_TRIGGER_ONCE = PermissibleValue(text="TASK_TIME_TRIGGER_ONCE")
    TASK_TIME_TRIGGER_WEEKLY = PermissibleValue(text="TASK_TIME_TRIGGER_WEEKLY")

    _defn = EnumDefinition(
        name="TriggerFrequencyEnum",
    )

class TriggerTypeEnum(EnumDefinitionImpl):

    TASK_TRIGGER_BOOT = PermissibleValue(text="TASK_TRIGGER_BOOT")
    TASK_TRIGGER_EVENT = PermissibleValue(text="TASK_TRIGGER_EVENT")
    TASK_TRIGGER_IDLE = PermissibleValue(text="TASK_TRIGGER_IDLE")
    TASK_TRIGGER_LOGON = PermissibleValue(text="TASK_TRIGGER_LOGON")
    TASK_TRIGGER_REGISTRATION = PermissibleValue(text="TASK_TRIGGER_REGISTRATION")
    TASK_TRIGGER_SESSION_STATE_CHANGE = PermissibleValue(text="TASK_TRIGGER_SESSION_STATE_CHANGE")
    TASK_TRIGGER_TIME = PermissibleValue(text="TASK_TRIGGER_TIME")

    _defn = EnumDefinition(
        name="TriggerTypeEnum",
    )

class URLTransitionTypeEnum(EnumDefinitionImpl):

    link = PermissibleValue(text="link")
    typed = PermissibleValue(text="typed")
    auto_bookmark = PermissibleValue(text="auto_bookmark")
    auto_subframe = PermissibleValue(text="auto_subframe")
    manual_subframe = PermissibleValue(text="manual_subframe")
    generated = PermissibleValue(text="generated")
    auto_toplevel = PermissibleValue(text="auto_toplevel")
    form_submit = PermissibleValue(text="form_submit")
    reload = PermissibleValue(text="reload")
    keyword = PermissibleValue(text="keyword")
    keyword_generated = PermissibleValue(text="keyword_generated")

    _defn = EnumDefinition(
        name="URLTransitionTypeEnum",
    )

class UnixProcessStateEnum(EnumDefinitionImpl):

    Dead = PermissibleValue(text="Dead")
    InterruptibleSleep = PermissibleValue(text="InterruptibleSleep")
    Paging = PermissibleValue(text="Paging")
    Running = PermissibleValue(text="Running")
    Stopped = PermissibleValue(text="Stopped")
    UninterruptibleSleep = PermissibleValue(text="UninterruptibleSleep")
    Zombie = PermissibleValue(text="Zombie")

    _defn = EnumDefinition(
        name="UnixProcessStateEnum",
    )

class WhoisContactTypeEnum(EnumDefinitionImpl):

    ADMIN = PermissibleValue(text="ADMIN")
    BILLING = PermissibleValue(text="BILLING")
    TECHNICAL = PermissibleValue(text="TECHNICAL")

    _defn = EnumDefinition(
        name="WhoisContactTypeEnum",
    )

class WhoisDNSSECTypeEnum(EnumDefinitionImpl):

    Signed = PermissibleValue(text="Signed")
    Unsigned = PermissibleValue(text="Unsigned")

    _defn = EnumDefinition(
        name="WhoisDNSSECTypeEnum",
    )

class WhoisStatusTypeEnum(EnumDefinitionImpl):

    ADD_PERIOD = PermissibleValue(text="ADD_PERIOD")
    AUTO_RENEW_PERIOD = PermissibleValue(text="AUTO_RENEW_PERIOD")
    CLIENT_DELETE_PROHIBITED = PermissibleValue(text="CLIENT_DELETE_PROHIBITED")
    CLIENT_HOLD = PermissibleValue(text="CLIENT_HOLD")
    CLIENT_RENEW_PROHIBITED = PermissibleValue(text="CLIENT_RENEW_PROHIBITED")
    CLIENT_TRANSFER_PROHIBITED = PermissibleValue(text="CLIENT_TRANSFER_PROHIBITED")
    CLIENT_UPDATE_PROHIBITED = PermissibleValue(text="CLIENT_UPDATE_PROHIBITED")
    DELETE_PROHIBITED = PermissibleValue(text="DELETE_PROHIBITED")
    HOLD = PermissibleValue(text="HOLD")
    INACTIVE = PermissibleValue(text="INACTIVE")
    OK = PermissibleValue(text="OK")
    PENDING_DELETE_RESTORABLE = PermissibleValue(text="PENDING_DELETE_RESTORABLE")
    PENDING_DELETE_SCHEDULED_FOR_RELEASE = PermissibleValue(text="PENDING_DELETE_SCHEDULED_FOR_RELEASE")
    PENDING_RESTORE = PermissibleValue(text="PENDING_RESTORE")
    RENEW_PERIOD = PermissibleValue(text="RENEW_PERIOD")
    RENEW_PROHIBITED = PermissibleValue(text="RENEW_PROHIBITED")
    TRANSFER_PERIOD = PermissibleValue(text="TRANSFER_PERIOD")
    TRANSFER_PROHIBITED = PermissibleValue(text="TRANSFER_PROHIBITED")
    UPDATE_PROHIBITED = PermissibleValue(text="UPDATE_PROHIBITED")

    _defn = EnumDefinition(
        name="WhoisStatusTypeEnum",
    )

class WindowsDriveTypeEnum(EnumDefinitionImpl):

    DRIVE_CDROM = PermissibleValue(text="DRIVE_CDROM")
    DRIVE_FIXED = PermissibleValue(text="DRIVE_FIXED")
    DRIVE_NO_ROOT_DIR = PermissibleValue(text="DRIVE_NO_ROOT_DIR")
    DRIVE_RAMDISK = PermissibleValue(text="DRIVE_RAMDISK")
    DRIVE_REMOTE = PermissibleValue(text="DRIVE_REMOTE")
    DRIVE_REMOVABLE = PermissibleValue(text="DRIVE_REMOVABLE")
    DRIVE_UNKNOWN = PermissibleValue(text="DRIVE_UNKNOWN")

    _defn = EnumDefinition(
        name="WindowsDriveTypeEnum",
    )

class WindowsVolumeAttributeEnum(EnumDefinitionImpl):

    Hidden = PermissibleValue(text="Hidden")
    NoDefaultDriveLetter = PermissibleValue(text="NoDefaultDriveLetter")
    ReadOnly = PermissibleValue(text="ReadOnly")
    ShadowCopy = PermissibleValue(text="ShadowCopy")

    _defn = EnumDefinition(
        name="WindowsVolumeAttributeEnum",
    )

class WirelessNetworkSecurityModeEnum(EnumDefinitionImpl):

    WEP = PermissibleValue(text="WEP")
    WPA = PermissibleValue(text="WPA")

    _defn = EnumDefinition(
        name="WirelessNetworkSecurityModeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
                PermissibleValue(text="None") )
        setattr(cls, "WPA2-PSK",
                PermissibleValue(text="WPA2-PSK") )
        setattr(cls, "WPA2-Enterprise",
                PermissibleValue(text="WPA2-Enterprise") )
        setattr(cls, "WPA3-PSK",
                PermissibleValue(text="WPA3-PSK") )
        setattr(cls, "WPA3-Enterprise",
                PermissibleValue(text="WPA3-Enterprise") )

# Slots
class slots:
    pass

slots.action = Slot(uri=ACTION.action, name="action", curie=ACTION.curie('action'),
                   model_uri=MASTER.action, domain=None, range=Optional[Union[dict, Action]])

slots.actionCount = Slot(uri=ACTION.actionCount, name="actionCount", curie=ACTION.curie('actionCount'),
                   model_uri=MASTER.actionCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.actionStatus = Slot(uri=ACTION.actionStatus, name="actionStatus", curie=ACTION.curie('actionStatus'),
                   model_uri=MASTER.actionStatus, domain=None, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.argumentName = Slot(uri=ACTION.argumentName, name="argumentName", curie=ACTION.curie('argumentName'),
                   model_uri=MASTER.argumentName, domain=None, range=Optional[str])

slots._endTime = Slot(uri=ACTION._endTime, name="_endTime", curie=ACTION.curie('_endTime'),
                   model_uri=MASTER._endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.environment = Slot(uri=ACTION.environment, name="environment", curie=ACTION.curie('environment'),
                   model_uri=MASTER.environment, domain=None, range=Optional[Union[dict, UcoObject]])

slots.error = Slot(uri=ACTION.error, name="error", curie=ACTION.curie('error'),
                   model_uri=MASTER.error, domain=None, range=Optional[Union[dict, UcoObject]])

slots.estimatedCost = Slot(uri=ACTION.estimatedCost, name="estimatedCost", curie=ACTION.curie('estimatedCost'),
                   model_uri=MASTER.estimatedCost, domain=None, range=Optional[str])

slots.estimatedEfficacy = Slot(uri=ACTION.estimatedEfficacy, name="estimatedEfficacy", curie=ACTION.curie('estimatedEfficacy'),
                   model_uri=MASTER.estimatedEfficacy, domain=None, range=Optional[str])

slots.estimatedImpact = Slot(uri=ACTION.estimatedImpact, name="estimatedImpact", curie=ACTION.curie('estimatedImpact'),
                   model_uri=MASTER.estimatedImpact, domain=None, range=Optional[str])

slots.instrument = Slot(uri=ACTION.instrument, name="instrument", curie=ACTION.curie('instrument'),
                   model_uri=MASTER.instrument, domain=None, range=Optional[Union[dict, UcoObject]])

slots.location = Slot(uri=ACTION.location, name="location", curie=ACTION.curie('location'),
                   model_uri=MASTER.location, domain=None, range=Optional[Union[dict, Location]])

slots._object = Slot(uri=ACTION._object, name="_object", curie=ACTION.curie('_object'),
                   model_uri=MASTER._object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objective = Slot(uri=ACTION.objective, name="objective", curie=ACTION.curie('objective'),
                   model_uri=MASTER.objective, domain=None, range=Optional[str])

slots.participant = Slot(uri=ACTION.participant, name="participant", curie=ACTION.curie('participant'),
                   model_uri=MASTER.participant, domain=None, range=Optional[Union[dict, UcoObject]])

slots.performer = Slot(uri=ACTION.performer, name="performer", curie=ACTION.curie('performer'),
                   model_uri=MASTER.performer, domain=None, range=Optional[Union[dict, UcoObject]])

slots.phase = Slot(uri=ACTION.phase, name="phase", curie=ACTION.curie('phase'),
                   model_uri=MASTER.phase, domain=None, range=Optional[Union[dict, ArrayOfAction]])

slots.rate = Slot(uri=ACTION.rate, name="rate", curie=ACTION.curie('rate'),
                   model_uri=MASTER.rate, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.result = Slot(uri=ACTION.result, name="result", curie=ACTION.curie('result'),
                   model_uri=MASTER.result, domain=None, range=Optional[Union[dict, UcoObject]])

slots.scale = Slot(uri=ACTION.scale, name="scale", curie=ACTION.curie('scale'),
                   model_uri=MASTER.scale, domain=None, range=Optional[str])

slots._startTime = Slot(uri=ACTION._startTime, name="_startTime", curie=ACTION.curie('_startTime'),
                   model_uri=MASTER._startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.subaction = Slot(uri=ACTION.subaction, name="subaction", curie=ACTION.curie('subaction'),
                   model_uri=MASTER.subaction, domain=None, range=Optional[Union[dict, Action]])

slots.trend = Slot(uri=ACTION.trend, name="trend", curie=ACTION.curie('trend'),
                   model_uri=MASTER.trend, domain=None, range=Optional[Union[str, "TrendEnum"]])

slots.units = Slot(uri=ACTION.units, name="units", curie=ACTION.curie('units'),
                   model_uri=MASTER.units, domain=None, range=Optional[str])

slots.class = Slot(uri=ANALYSIS.class, name="class", curie=ANALYSIS.curie('class'),
                   model_uri=MASTER.class, domain=None, range=Optional[str])

slots.classification = Slot(uri=ANALYSIS.classification, name="classification", curie=ANALYSIS.curie('classification'),
                   model_uri=MASTER.classification, domain=None, range=Optional[Union[dict, ArtifactClassification]])

slots.classificationConfidence = Slot(uri=ANALYSIS.classificationConfidence, name="classificationConfidence", curie=ANALYSIS.curie('classificationConfidence'),
                   model_uri=MASTER.classificationConfidence, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.originatingAnalysis = Slot(uri=ANALYSIS.originatingAnalysis, name="originatingAnalysis", curie=ANALYSIS.curie('originatingAnalysis'),
                   model_uri=MASTER.originatingAnalysis, domain=None, range=Optional[Union[dict, Analysis]])

slots.resultContent = Slot(uri=ANALYSIS.resultContent, name="resultContent", curie=ANALYSIS.curie('resultContent'),
                   model_uri=MASTER.resultContent, domain=None, range=Optional[Union[dict, UcoObject]])

slots.configurationEntry = Slot(uri=CONFIGURATION.configurationEntry, name="configurationEntry", curie=CONFIGURATION.curie('configurationEntry'),
                   model_uri=MASTER.configurationEntry, domain=None, range=Optional[Union[dict, ConfigurationEntry]])

slots.dependencies = Slot(uri=CONFIGURATION.dependencies, name="dependencies", curie=CONFIGURATION.curie('dependencies'),
                   model_uri=MASTER.dependencies, domain=None, range=Optional[Union[dict, Dependency]])

slots.dependencyDescription = Slot(uri=CONFIGURATION.dependencyDescription, name="dependencyDescription", curie=CONFIGURATION.curie('dependencyDescription'),
                   model_uri=MASTER.dependencyDescription, domain=None, range=Optional[str])

slots.dependencyType = Slot(uri=CONFIGURATION.dependencyType, name="dependencyType", curie=CONFIGURATION.curie('dependencyType'),
                   model_uri=MASTER.dependencyType, domain=None, range=Optional[str])

slots.isConfigurationOf = Slot(uri=CONFIGURATION.isConfigurationOf, name="isConfigurationOf", curie=CONFIGURATION.curie('isConfigurationOf'),
                   model_uri=MASTER.isConfigurationOf, domain=None, range=Optional[Union[dict, UcoObject]])

slots.itemDescription = Slot(uri=CONFIGURATION.itemDescription, name="itemDescription", curie=CONFIGURATION.curie('itemDescription'),
                   model_uri=MASTER.itemDescription, domain=None, range=Optional[str])

slots.itemName = Slot(uri=CONFIGURATION.itemName, name="itemName", curie=CONFIGURATION.curie('itemName'),
                   model_uri=MASTER.itemName, domain=None, range=Optional[str])

slots.itemObject = Slot(uri=CONFIGURATION.itemObject, name="itemObject", curie=CONFIGURATION.curie('itemObject'),
                   model_uri=MASTER.itemObject, domain=None, range=Optional[Union[dict, UcoObject]])

slots.itemType = Slot(uri=CONFIGURATION.itemType, name="itemType", curie=CONFIGURATION.curie('itemType'),
                   model_uri=MASTER.itemType, domain=None, range=Optional[str])

slots.itemValue = Slot(uri=CONFIGURATION.itemValue, name="itemValue", curie=CONFIGURATION.curie('itemValue'),
                   model_uri=MASTER.itemValue, domain=None, range=Optional[str])

slots.usageContextAssumptions = Slot(uri=CONFIGURATION.usageContextAssumptions, name="usageContextAssumptions", curie=CONFIGURATION.curie('usageContextAssumptions'),
                   model_uri=MASTER.usageContextAssumptions, domain=None, range=Optional[str])

slots.usesConfiguration = Slot(uri=CONFIGURATION.usesConfiguration, name="usesConfiguration", curie=CONFIGURATION.curie('usesConfiguration'),
                   model_uri=MASTER.usesConfiguration, domain=None, range=Optional[Union[dict, Configuration]])

slots.confidence = Slot(uri=CORE.confidence, name="confidence", curie=CORE.curie('confidence'),
                   model_uri=MASTER.confidence, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=MASTER.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=MASTER.constrainingVocabularyReference, domain=None, range=Optional[Union[str, IriType]])

slots.context = Slot(uri=CORE.context, name="context", curie=CORE.curie('context'),
                   model_uri=MASTER.context, domain=None, range=Optional[str])

slots.createdBy = Slot(uri=CORE.createdBy, name="createdBy", curie=CORE.curie('createdBy'),
                   model_uri=MASTER.createdBy, domain=IdentityAbstraction, range=Optional[str])

slots.definingContext = Slot(uri=CORE.definingContext, name="definingContext", curie=CORE.curie('definingContext'),
                   model_uri=MASTER.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=MASTER.description, domain=None, range=Optional[str])

slots.endTime = Slot(uri=CORE.endTime, name="endTime", curie=CORE.curie('endTime'),
                   model_uri=MASTER.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.externalIdentifier = Slot(uri=CORE.externalIdentifier, name="externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=MASTER.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=CORE.externalReference, name="externalReference", curie=CORE.curie('externalReference'),
                   model_uri=MASTER.externalReference, domain=ExternalReference, range=Optional[str])

slots.hasFacet = Slot(uri=CORE.hasFacet, name="hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=MASTER.hasFacet, domain=None, range=Optional[str])

slots.isDirectional = Slot(uri=CORE.isDirectional, name="isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=MASTER.isDirectional, domain=None, range=Optional[Union[bool, BooleanType]])

slots.kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=MASTER.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=CORE.modifiedTime, name="modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=MASTER.modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=MASTER.name, domain=None, range=Optional[str])

slots.namingAuthority = Slot(uri=CORE.namingAuthority, name="namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=MASTER.namingAuthority, domain=None, range=Optional[str])

slots.object = Slot(uri=CORE.object, name="object", curie=CORE.curie('object'),
                   model_uri=MASTER.object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=MASTER.objectCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.objectMarking = Slot(uri=CORE.objectMarking, name="objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=MASTER.objectMarking, domain=None, range=Optional[Union[dict, MarkingDefinitionAbstraction]])

slots.referenceURL = Slot(uri=CORE.referenceURL, name="referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=MASTER.referenceURL, domain=None, range=Optional[Union[str, IriType]])

slots.source = Slot(uri=CORE.source, name="source", curie=CORE.curie('source'),
                   model_uri=MASTER.source, domain=None, range=Optional[Union[dict, UcoObject]])

slots.specVersion = Slot(uri=CORE.specVersion, name="specVersion", curie=CORE.curie('specVersion'),
                   model_uri=MASTER.specVersion, domain=None, range=Optional[str])

slots.startTime = Slot(uri=CORE.startTime, name="startTime", curie=CORE.curie('startTime'),
                   model_uri=MASTER.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statement = Slot(uri=CORE.statement, name="statement", curie=CORE.curie('statement'),
                   model_uri=MASTER.statement, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=MASTER.tag, domain=None, range=Optional[str])

slots.target = Slot(uri=CORE.target, name="target", curie=CORE.curie('target'),
                   model_uri=MASTER.target, domain=None, range=Optional[Union[dict, UcoObject]])

slots.value = Slot(uri=CORE.value, name="value", curie=CORE.curie('value'),
                   model_uri=MASTER.value, domain=None, range=Optional[str])

slots.address = Slot(uri=IDENTITY.address, name="address", curie=IDENTITY.curie('address'),
                   model_uri=MASTER.address, domain=None, range=Optional[Union[dict, Location]])

slots.birthdate = Slot(uri=IDENTITY.birthdate, name="birthdate", curie=IDENTITY.curie('birthdate'),
                   model_uri=MASTER.birthdate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.familyName = Slot(uri=IDENTITY.familyName, name="familyName", curie=IDENTITY.curie('familyName'),
                   model_uri=MASTER.familyName, domain=None, range=Optional[str])

slots.givenName = Slot(uri=IDENTITY.givenName, name="givenName", curie=IDENTITY.curie('givenName'),
                   model_uri=MASTER.givenName, domain=None, range=Optional[str])

slots.honorificPrefix = Slot(uri=IDENTITY.honorificPrefix, name="honorificPrefix", curie=IDENTITY.curie('honorificPrefix'),
                   model_uri=MASTER.honorificPrefix, domain=None, range=Optional[str])

slots.honorificSuffix = Slot(uri=IDENTITY.honorificSuffix, name="honorificSuffix", curie=IDENTITY.curie('honorificSuffix'),
                   model_uri=MASTER.honorificSuffix, domain=None, range=Optional[str])

slots.addressType = Slot(uri=LOCATION.addressType, name="addressType", curie=LOCATION.curie('addressType'),
                   model_uri=MASTER.addressType, domain=None, range=Optional[str])

slots.altitude = Slot(uri=LOCATION.altitude, name="altitude", curie=LOCATION.curie('altitude'),
                   model_uri=MASTER.altitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.country = Slot(uri=LOCATION.country, name="country", curie=LOCATION.curie('country'),
                   model_uri=MASTER.country, domain=None, range=Optional[str])

slots.hdop = Slot(uri=LOCATION.hdop, name="hdop", curie=LOCATION.curie('hdop'),
                   model_uri=MASTER.hdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.latitude = Slot(uri=LOCATION.latitude, name="latitude", curie=LOCATION.curie('latitude'),
                   model_uri=MASTER.latitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.locality = Slot(uri=LOCATION.locality, name="locality", curie=LOCATION.curie('locality'),
                   model_uri=MASTER.locality, domain=None, range=Optional[str])

slots.longitude = Slot(uri=LOCATION.longitude, name="longitude", curie=LOCATION.curie('longitude'),
                   model_uri=MASTER.longitude, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.pdop = Slot(uri=LOCATION.pdop, name="pdop", curie=LOCATION.curie('pdop'),
                   model_uri=MASTER.pdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.postalCode = Slot(uri=LOCATION.postalCode, name="postalCode", curie=LOCATION.curie('postalCode'),
                   model_uri=MASTER.postalCode, domain=None, range=Optional[str])

slots.region = Slot(uri=LOCATION.region, name="region", curie=LOCATION.curie('region'),
                   model_uri=MASTER.region, domain=None, range=Optional[str])

slots.street = Slot(uri=LOCATION.street, name="street", curie=LOCATION.curie('street'),
                   model_uri=MASTER.street, domain=None, range=Optional[str])

slots.tdop = Slot(uri=LOCATION.tdop, name="tdop", curie=LOCATION.curie('tdop'),
                   model_uri=MASTER.tdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.vdop = Slot(uri=LOCATION.vdop, name="vdop", curie=LOCATION.curie('vdop'),
                   model_uri=MASTER.vdop, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.authorizedIdentities = Slot(uri=MARKING.authorizedIdentities, name="authorizedIdentities", curie=MARKING.curie('authorizedIdentities'),
                   model_uri=MASTER.authorizedIdentities, domain=None, range=Optional[str])

slots.contentSelectors = Slot(uri=MARKING.contentSelectors, name="contentSelectors", curie=MARKING.curie('contentSelectors'),
                   model_uri=MASTER.contentSelectors, domain=None, range=Optional[str])

slots.definition = Slot(uri=MARKING.definition, name="definition", curie=MARKING.curie('definition'),
                   model_uri=MASTER.definition, domain=MarkingModel, range=Optional[str])

slots.definitionType = Slot(uri=MARKING.definitionType, name="definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MASTER.definitionType, domain=None, range=Optional[str])

slots.license = Slot(uri=MARKING.license, name="license", curie=MARKING.curie('license'),
                   model_uri=MASTER.license, domain=None, range=Optional[str])

slots.marking = Slot(uri=MARKING.marking, name="marking", curie=MARKING.curie('marking'),
                   model_uri=MASTER.marking, domain=MarkingDefinition, range=Optional[str])

slots.termsOfUse = Slot(uri=MARKING.termsOfUse, name="termsOfUse", curie=MARKING.curie('termsOfUse'),
                   model_uri=MASTER.termsOfUse, domain=None, range=Optional[str])

slots.messageThreadOrderedItems = Slot(uri=OBSERVABLE.messageThreadOrderedItems, name="messageThreadOrderedItems", curie=OBSERVABLE.curie('messageThreadOrderedItems'),
                   model_uri=MASTER.messageThreadOrderedItems, domain=Bag, range=Optional[Union[dict, Thread]])

slots.messageThreadOriginItems = Slot(uri=OBSERVABLE.messageThreadOriginItems, name="messageThreadOriginItems", curie=OBSERVABLE.curie('messageThreadOriginItems'),
                   model_uri=MASTER.messageThreadOriginItems, domain=Thread, range=Optional[Union[dict, "Thread"]])

slots.messageThreadTerminalItems = Slot(uri=OBSERVABLE.messageThreadTerminalItems, name="messageThreadTerminalItems", curie=OBSERVABLE.curie('messageThreadTerminalItems'),
                   model_uri=MASTER.messageThreadTerminalItems, domain=Thread, range=Optional[Union[dict, "Thread"]])

slots.messageThreadUnorderedItems = Slot(uri=OBSERVABLE.messageThreadUnorderedItems, name="messageThreadUnorderedItems", curie=OBSERVABLE.curie('messageThreadUnorderedItems'),
                   model_uri=MASTER.messageThreadUnorderedItems, domain=Collection, range=Optional[Union[dict, Thread]])

slots.ESN = Slot(uri=OBSERVABLE.ESN, name="ESN", curie=OBSERVABLE.curie('ESN'),
                   model_uri=MASTER.ESN, domain=None, range=Optional[str])

slots.ICCID = Slot(uri=OBSERVABLE.ICCID, name="ICCID", curie=OBSERVABLE.curie('ICCID'),
                   model_uri=MASTER.ICCID, domain=None, range=Optional[str])

slots.IMEI = Slot(uri=OBSERVABLE.IMEI, name="IMEI", curie=OBSERVABLE.curie('IMEI'),
                   model_uri=MASTER.IMEI, domain=None, range=Optional[str])

slots.IMSI = Slot(uri=OBSERVABLE.IMSI, name="IMSI", curie=OBSERVABLE.curie('IMSI'),
                   model_uri=MASTER.IMSI, domain=None, range=Optional[str])

slots.PIN = Slot(uri=OBSERVABLE.PIN, name="PIN", curie=OBSERVABLE.curie('PIN'),
                   model_uri=MASTER.PIN, domain=None, range=Optional[str])

slots.PUK = Slot(uri=OBSERVABLE.PUK, name="PUK", curie=OBSERVABLE.curie('PUK'),
                   model_uri=MASTER.PUK, domain=None, range=Optional[str])

slots.SIMForm = Slot(uri=OBSERVABLE.SIMForm, name="SIMForm", curie=OBSERVABLE.curie('SIMForm'),
                   model_uri=MASTER.SIMForm, domain=None, range=Optional[str])

slots.SIMType = Slot(uri=OBSERVABLE.SIMType, name="SIMType", curie=OBSERVABLE.curie('SIMType'),
                   model_uri=MASTER.SIMType, domain=None, range=Optional[str])

slots.abbreviation = Slot(uri=OBSERVABLE.abbreviation, name="abbreviation", curie=OBSERVABLE.curie('abbreviation'),
                   model_uri=MASTER.abbreviation, domain=None, range=Optional[str])

slots.accessedDirectory = Slot(uri=OBSERVABLE.accessedDirectory, name="accessedDirectory", curie=OBSERVABLE.curie('accessedDirectory'),
                   model_uri=MASTER.accessedDirectory, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.accessedFile = Slot(uri=OBSERVABLE.accessedFile, name="accessedFile", curie=OBSERVABLE.curie('accessedFile'),
                   model_uri=MASTER.accessedFile, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.accessedTime = Slot(uri=OBSERVABLE.accessedTime, name="accessedTime", curie=OBSERVABLE.curie('accessedTime'),
                   model_uri=MASTER.accessedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.account = Slot(uri=OBSERVABLE.account, name="account", curie=OBSERVABLE.curie('account'),
                   model_uri=MASTER.account, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.accountIdentifier = Slot(uri=OBSERVABLE.accountIdentifier, name="accountIdentifier", curie=OBSERVABLE.curie('accountIdentifier'),
                   model_uri=MASTER.accountIdentifier, domain=None, range=Optional[str])

slots.accountIssuer = Slot(uri=OBSERVABLE.accountIssuer, name="accountIssuer", curie=OBSERVABLE.curie('accountIssuer'),
                   model_uri=MASTER.accountIssuer, domain=None, range=Optional[Union[dict, UcoObject]])

slots.accountLogin = Slot(uri=OBSERVABLE.accountLogin, name="accountLogin", curie=OBSERVABLE.curie('accountLogin'),
                   model_uri=MASTER.accountLogin, domain=None, range=Optional[str])

slots.accountLogonType = Slot(uri=OBSERVABLE.accountLogonType, name="accountLogonType", curie=OBSERVABLE.curie('accountLogonType'),
                   model_uri=MASTER.accountLogonType, domain=None, range=Optional[str])

slots.accountRunLevel = Slot(uri=OBSERVABLE.accountRunLevel, name="accountRunLevel", curie=OBSERVABLE.curie('accountRunLevel'),
                   model_uri=MASTER.accountRunLevel, domain=None, range=Optional[str])

slots.accountType = Slot(uri=OBSERVABLE.accountType, name="accountType", curie=OBSERVABLE.curie('accountType'),
                   model_uri=MASTER.accountType, domain=None, range=Optional[str])

slots.actionID = Slot(uri=OBSERVABLE.actionID, name="actionID", curie=OBSERVABLE.curie('actionID'),
                   model_uri=MASTER.actionID, domain=None, range=Optional[str])

slots.actionList = Slot(uri=OBSERVABLE.actionList, name="actionList", curie=OBSERVABLE.curie('actionList'),
                   model_uri=MASTER.actionList, domain=None, range=Optional[Union[dict, TaskActionType]])

slots.actionType = Slot(uri=OBSERVABLE.actionType, name="actionType", curie=OBSERVABLE.curie('actionType'),
                   model_uri=MASTER.actionType, domain=None, range=Optional[str])

slots.activeDirectoryGroups = Slot(uri=OBSERVABLE.activeDirectoryGroups, name="activeDirectoryGroups", curie=OBSERVABLE.curie('activeDirectoryGroups'),
                   model_uri=MASTER.activeDirectoryGroups, domain=None, range=Optional[str])

slots.adapterName = Slot(uri=OBSERVABLE.adapterName, name="adapterName", curie=OBSERVABLE.curie('adapterName'),
                   model_uri=MASTER.adapterName, domain=None, range=Optional[str])

slots.addressOfEntryPoint = Slot(uri=OBSERVABLE.addressOfEntryPoint, name="addressOfEntryPoint", curie=OBSERVABLE.curie('addressOfEntryPoint'),
                   model_uri=MASTER.addressOfEntryPoint, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.addressValue = Slot(uri=OBSERVABLE.addressValue, name="addressValue", curie=OBSERVABLE.curie('addressValue'),
                   model_uri=MASTER.addressValue, domain=None, range=Optional[str])

slots.advertisingID = Slot(uri=OBSERVABLE.advertisingID, name="advertisingID", curie=OBSERVABLE.curie('advertisingID'),
                   model_uri=MASTER.advertisingID, domain=None, range=Optional[str])

slots.allocationStatus = Slot(uri=OBSERVABLE.allocationStatus, name="allocationStatus", curie=OBSERVABLE.curie('allocationStatus'),
                   model_uri=MASTER.allocationStatus, domain=None, range=Optional[str])

slots.alternateDataStreams = Slot(uri=OBSERVABLE.alternateDataStreams, name="alternateDataStreams", curie=OBSERVABLE.curie('alternateDataStreams'),
                   model_uri=MASTER.alternateDataStreams, domain=None, range=Optional[Union[dict, AlternateDataStream]])

slots.androidFingerprint = Slot(uri=OBSERVABLE.androidFingerprint, name="androidFingerprint", curie=OBSERVABLE.curie('androidFingerprint'),
                   model_uri=MASTER.androidFingerprint, domain=None, range=Optional[str])

slots.androidID = Slot(uri=OBSERVABLE.androidID, name="androidID", curie=OBSERVABLE.curie('androidID'),
                   model_uri=MASTER.androidID, domain=None, range=Optional[hex])

slots.androidVersion = Slot(uri=OBSERVABLE.androidVersion, name="androidVersion", curie=OBSERVABLE.curie('androidVersion'),
                   model_uri=MASTER.androidVersion, domain=None, range=Optional[str])

slots.antennaHeight = Slot(uri=OBSERVABLE.antennaHeight, name="antennaHeight", curie=OBSERVABLE.curie('antennaHeight'),
                   model_uri=MASTER.antennaHeight, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.application = Slot(uri=OBSERVABLE.application, name="application", curie=OBSERVABLE.curie('application'),
                   model_uri=MASTER.application, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.applicationFileName = Slot(uri=OBSERVABLE.applicationFileName, name="applicationFileName", curie=OBSERVABLE.curie('applicationFileName'),
                   model_uri=MASTER.applicationFileName, domain=None, range=Optional[str])

slots.applicationIdentifier = Slot(uri=OBSERVABLE.applicationIdentifier, name="applicationIdentifier", curie=OBSERVABLE.curie('applicationIdentifier'),
                   model_uri=MASTER.applicationIdentifier, domain=None, range=Optional[str])

slots.archiveType = Slot(uri=OBSERVABLE.archiveType, name="archiveType", curie=OBSERVABLE.curie('archiveType'),
                   model_uri=MASTER.archiveType, domain=None, range=Optional[str])

slots.arguments = Slot(uri=OBSERVABLE.arguments, name="arguments", curie=OBSERVABLE.curie('arguments'),
                   model_uri=MASTER.arguments, domain=None, range=Optional[str])

slots.asHandle = Slot(uri=OBSERVABLE.asHandle, name="asHandle", curie=OBSERVABLE.curie('asHandle'),
                   model_uri=MASTER.asHandle, domain=None, range=Optional[str])

slots.aslrEnabled = Slot(uri=OBSERVABLE.aslrEnabled, name="aslrEnabled", curie=OBSERVABLE.curie('aslrEnabled'),
                   model_uri=MASTER.aslrEnabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.attendant = Slot(uri=OBSERVABLE.attendant, name="attendant", curie=OBSERVABLE.curie('attendant'),
                   model_uri=MASTER.attendant, domain=None, range=Optional[Union[dict, Identity]])

slots.audioType = Slot(uri=OBSERVABLE.audioType, name="audioType", curie=OBSERVABLE.curie('audioType'),
                   model_uri=MASTER.audioType, domain=None, range=Optional[str])

slots.authorityKeyIdentifier = Slot(uri=OBSERVABLE.authorityKeyIdentifier, name="authorityKeyIdentifier", curie=OBSERVABLE.curie('authorityKeyIdentifier'),
                   model_uri=MASTER.authorityKeyIdentifier, domain=None, range=Optional[str])

slots.availableRam = Slot(uri=OBSERVABLE.availableRam, name="availableRam", curie=OBSERVABLE.curie('availableRam'),
                   model_uri=MASTER.availableRam, domain=None, range=Optional[int])

slots.azimuth = Slot(uri=OBSERVABLE.azimuth, name="azimuth", curie=OBSERVABLE.curie('azimuth'),
                   model_uri=MASTER.azimuth, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.baseOfCode = Slot(uri=OBSERVABLE.baseOfCode, name="baseOfCode", curie=OBSERVABLE.curie('baseOfCode'),
                   model_uri=MASTER.baseOfCode, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.baseStation = Slot(uri=OBSERVABLE.baseStation, name="baseStation", curie=OBSERVABLE.curie('baseStation'),
                   model_uri=MASTER.baseStation, domain=None, range=Optional[str])

slots.basicConstraints = Slot(uri=OBSERVABLE.basicConstraints, name="basicConstraints", curie=OBSERVABLE.curie('basicConstraints'),
                   model_uri=MASTER.basicConstraints, domain=None, range=Optional[str])

slots.bcc = Slot(uri=OBSERVABLE.bcc, name="bcc", curie=OBSERVABLE.curie('bcc'),
                   model_uri=MASTER.bcc, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.binary = Slot(uri=OBSERVABLE.binary, name="binary", curie=OBSERVABLE.curie('binary'),
                   model_uri=MASTER.binary, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.biosDate = Slot(uri=OBSERVABLE.biosDate, name="biosDate", curie=OBSERVABLE.curie('biosDate'),
                   model_uri=MASTER.biosDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.biosManufacturer = Slot(uri=OBSERVABLE.biosManufacturer, name="biosManufacturer", curie=OBSERVABLE.curie('biosManufacturer'),
                   model_uri=MASTER.biosManufacturer, domain=None, range=Optional[str])

slots.biosReleaseDate = Slot(uri=OBSERVABLE.biosReleaseDate, name="biosReleaseDate", curie=OBSERVABLE.curie('biosReleaseDate'),
                   model_uri=MASTER.biosReleaseDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.biosSerialNumber = Slot(uri=OBSERVABLE.biosSerialNumber, name="biosSerialNumber", curie=OBSERVABLE.curie('biosSerialNumber'),
                   model_uri=MASTER.biosSerialNumber, domain=None, range=Optional[str])

slots.biosVersion = Slot(uri=OBSERVABLE.biosVersion, name="biosVersion", curie=OBSERVABLE.curie('biosVersion'),
                   model_uri=MASTER.biosVersion, domain=None, range=Optional[str])

slots.bitRate = Slot(uri=OBSERVABLE.bitRate, name="bitRate", curie=OBSERVABLE.curie('bitRate'),
                   model_uri=MASTER.bitRate, domain=None, range=Optional[int])

slots.bitness = Slot(uri=OBSERVABLE.bitness, name="bitness", curie=OBSERVABLE.curie('bitness'),
                   model_uri=MASTER.bitness, domain=None, range=Optional[str])

slots.bitsPerPixel = Slot(uri=OBSERVABLE.bitsPerPixel, name="bitsPerPixel", curie=OBSERVABLE.curie('bitsPerPixel'),
                   model_uri=MASTER.bitsPerPixel, domain=None, range=Optional[int])

slots.blockType = Slot(uri=OBSERVABLE.blockType, name="blockType", curie=OBSERVABLE.curie('blockType'),
                   model_uri=MASTER.blockType, domain=None, range=Optional[str])

slots.bluetoothDeviceName = Slot(uri=OBSERVABLE.bluetoothDeviceName, name="bluetoothDeviceName", curie=OBSERVABLE.curie('bluetoothDeviceName'),
                   model_uri=MASTER.bluetoothDeviceName, domain=None, range=Optional[str])

slots.body = Slot(uri=OBSERVABLE.body, name="body", curie=OBSERVABLE.curie('body'),
                   model_uri=MASTER.body, domain=None, range=Optional[str])

slots.bodyMultipart = Slot(uri=OBSERVABLE.bodyMultipart, name="bodyMultipart", curie=OBSERVABLE.curie('bodyMultipart'),
                   model_uri=MASTER.bodyMultipart, domain=None, range=Optional[Union[dict, MimePartType]])

slots.bodyRaw = Slot(uri=OBSERVABLE.bodyRaw, name="bodyRaw", curie=OBSERVABLE.curie('bodyRaw'),
                   model_uri=MASTER.bodyRaw, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.bookmarkPath = Slot(uri=OBSERVABLE.bookmarkPath, name="bookmarkPath", curie=OBSERVABLE.curie('bookmarkPath'),
                   model_uri=MASTER.bookmarkPath, domain=None, range=Optional[str])

slots.browserInformation = Slot(uri=OBSERVABLE.browserInformation, name="browserInformation", curie=OBSERVABLE.curie('browserInformation'),
                   model_uri=MASTER.browserInformation, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.browserUserProfile = Slot(uri=OBSERVABLE.browserUserProfile, name="browserUserProfile", curie=OBSERVABLE.curie('browserUserProfile'),
                   model_uri=MASTER.browserUserProfile, domain=None, range=Optional[str])

slots.byteOrder = Slot(uri=OBSERVABLE.byteOrder, name="byteOrder", curie=OBSERVABLE.curie('byteOrder'),
                   model_uri=MASTER.byteOrder, domain=None, range=Optional[str])

slots.byteStringValue = Slot(uri=OBSERVABLE.byteStringValue, name="byteStringValue", curie=OBSERVABLE.curie('byteStringValue'),
                   model_uri=MASTER.byteStringValue, domain=None, range=Optional[Union[str, Base64BinaryType]])

slots.callType = Slot(uri=OBSERVABLE.callType, name="callType", curie=OBSERVABLE.curie('callType'),
                   model_uri=MASTER.callType, domain=None, range=Optional[str])

slots.camera = Slot(uri=OBSERVABLE.camera, name="camera", curie=OBSERVABLE.curie('camera'),
                   model_uri=MASTER.camera, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.canEscalatePrivs = Slot(uri=OBSERVABLE.canEscalatePrivs, name="canEscalatePrivs", curie=OBSERVABLE.curie('canEscalatePrivs'),
                   model_uri=MASTER.canEscalatePrivs, domain=None, range=Optional[Union[bool, BooleanType]])

slots.captureCellSite = Slot(uri=OBSERVABLE.captureCellSite, name="captureCellSite", curie=OBSERVABLE.curie('captureCellSite'),
                   model_uri=MASTER.captureCellSite, domain=None, range=Optional[Union[dict, CellSite]])

slots.carrier = Slot(uri=OBSERVABLE.carrier, name="carrier", curie=OBSERVABLE.curie('carrier'),
                   model_uri=MASTER.carrier, domain=None, range=Optional[Union[dict, Identity]])

slots.categories = Slot(uri=OBSERVABLE.categories, name="categories", curie=OBSERVABLE.curie('categories'),
                   model_uri=MASTER.categories, domain=None, range=Optional[str])

slots.cc = Slot(uri=OBSERVABLE.cc, name="cc", curie=OBSERVABLE.curie('cc'),
                   model_uri=MASTER.cc, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.cellSiteCountryCode = Slot(uri=OBSERVABLE.cellSiteCountryCode, name="cellSiteCountryCode", curie=OBSERVABLE.curie('cellSiteCountryCode'),
                   model_uri=MASTER.cellSiteCountryCode, domain=None, range=Optional[str])

slots.cellSiteIdentifier = Slot(uri=OBSERVABLE.cellSiteIdentifier, name="cellSiteIdentifier", curie=OBSERVABLE.curie('cellSiteIdentifier'),
                   model_uri=MASTER.cellSiteIdentifier, domain=None, range=Optional[str])

slots.cellSiteLocationAreaCode = Slot(uri=OBSERVABLE.cellSiteLocationAreaCode, name="cellSiteLocationAreaCode", curie=OBSERVABLE.curie('cellSiteLocationAreaCode'),
                   model_uri=MASTER.cellSiteLocationAreaCode, domain=None, range=Optional[str])

slots.cellSiteNetworkCode = Slot(uri=OBSERVABLE.cellSiteNetworkCode, name="cellSiteNetworkCode", curie=OBSERVABLE.curie('cellSiteNetworkCode'),
                   model_uri=MASTER.cellSiteNetworkCode, domain=None, range=Optional[str])

slots.cellSiteType = Slot(uri=OBSERVABLE.cellSiteType, name="cellSiteType", curie=OBSERVABLE.curie('cellSiteType'),
                   model_uri=MASTER.cellSiteType, domain=None, range=Optional[str])

slots.certificateIssuer = Slot(uri=OBSERVABLE.certificateIssuer, name="certificateIssuer", curie=OBSERVABLE.curie('certificateIssuer'),
                   model_uri=MASTER.certificateIssuer, domain=None, range=Optional[Union[dict, Identity]])

slots.certificatePolicies = Slot(uri=OBSERVABLE.certificatePolicies, name="certificatePolicies", curie=OBSERVABLE.curie('certificatePolicies'),
                   model_uri=MASTER.certificatePolicies, domain=None, range=Optional[str])

slots.certificateSubject = Slot(uri=OBSERVABLE.certificateSubject, name="certificateSubject", curie=OBSERVABLE.curie('certificateSubject'),
                   model_uri=MASTER.certificateSubject, domain=None, range=Optional[Union[dict, UcoObject]])

slots.characteristics = Slot(uri=OBSERVABLE.characteristics, name="characteristics", curie=OBSERVABLE.curie('characteristics'),
                   model_uri=MASTER.characteristics, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.checksum = Slot(uri=OBSERVABLE.checksum, name="checksum", curie=OBSERVABLE.curie('checksum'),
                   model_uri=MASTER.checksum, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.clockSetting = Slot(uri=OBSERVABLE.clockSetting, name="clockSetting", curie=OBSERVABLE.curie('clockSetting'),
                   model_uri=MASTER.clockSetting, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.clusterSize = Slot(uri=OBSERVABLE.clusterSize, name="clusterSize", curie=OBSERVABLE.curie('clusterSize'),
                   model_uri=MASTER.clusterSize, domain=None, range=Optional[int])

slots.columnName = Slot(uri=OBSERVABLE.columnName, name="columnName", curie=OBSERVABLE.curie('columnName'),
                   model_uri=MASTER.columnName, domain=None, range=Optional[str])

slots.comClassID = Slot(uri=OBSERVABLE.comClassID, name="comClassID", curie=OBSERVABLE.curie('comClassID'),
                   model_uri=MASTER.comClassID, domain=None, range=Optional[str])

slots.comData = Slot(uri=OBSERVABLE.comData, name="comData", curie=OBSERVABLE.curie('comData'),
                   model_uri=MASTER.comData, domain=None, range=Optional[str])

slots.comment = Slot(uri=OBSERVABLE.comment, name="comment", curie=OBSERVABLE.curie('comment'),
                   model_uri=MASTER.comment, domain=None, range=Optional[str])

slots.compressionMethod = Slot(uri=OBSERVABLE.compressionMethod, name="compressionMethod", curie=OBSERVABLE.curie('compressionMethod'),
                   model_uri=MASTER.compressionMethod, domain=None, range=Optional[str])

slots.compressionRatio = Slot(uri=OBSERVABLE.compressionRatio, name="compressionRatio", curie=OBSERVABLE.curie('compressionRatio'),
                   model_uri=MASTER.compressionRatio, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.contact = Slot(uri=OBSERVABLE.contact, name="contact", curie=OBSERVABLE.curie('contact'),
                   model_uri=MASTER.contact, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.contactAddress = Slot(uri=OBSERVABLE.contactAddress, name="contactAddress", curie=OBSERVABLE.curie('contactAddress'),
                   model_uri=MASTER.contactAddress, domain=None, range=Optional[Union[dict, ContactAddress]])

slots.contactAddressScope = Slot(uri=OBSERVABLE.contactAddressScope, name="contactAddressScope", curie=OBSERVABLE.curie('contactAddressScope'),
                   model_uri=MASTER.contactAddressScope, domain=None, range=Optional[str])

slots.contactAffiliation = Slot(uri=OBSERVABLE.contactAffiliation, name="contactAffiliation", curie=OBSERVABLE.curie('contactAffiliation'),
                   model_uri=MASTER.contactAffiliation, domain=None, range=Optional[Union[dict, ContactAffiliation]])

slots.contactEmail = Slot(uri=OBSERVABLE.contactEmail, name="contactEmail", curie=OBSERVABLE.curie('contactEmail'),
                   model_uri=MASTER.contactEmail, domain=None, range=Optional[Union[dict, ContactEmail]])

slots.contactEmailScope = Slot(uri=OBSERVABLE.contactEmailScope, name="contactEmailScope", curie=OBSERVABLE.curie('contactEmailScope'),
                   model_uri=MASTER.contactEmailScope, domain=None, range=Optional[str])

slots.contactGroup = Slot(uri=OBSERVABLE.contactGroup, name="contactGroup", curie=OBSERVABLE.curie('contactGroup'),
                   model_uri=MASTER.contactGroup, domain=None, range=Optional[str])

slots.contactID = Slot(uri=OBSERVABLE.contactID, name="contactID", curie=OBSERVABLE.curie('contactID'),
                   model_uri=MASTER.contactID, domain=None, range=Optional[str])

slots.contactMessaging = Slot(uri=OBSERVABLE.contactMessaging, name="contactMessaging", curie=OBSERVABLE.curie('contactMessaging'),
                   model_uri=MASTER.contactMessaging, domain=None, range=Optional[Union[dict, ContactMessaging]])

slots.contactMessagingPlatform = Slot(uri=OBSERVABLE.contactMessagingPlatform, name="contactMessagingPlatform", curie=OBSERVABLE.curie('contactMessagingPlatform'),
                   model_uri=MASTER.contactMessagingPlatform, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.contactNote = Slot(uri=OBSERVABLE.contactNote, name="contactNote", curie=OBSERVABLE.curie('contactNote'),
                   model_uri=MASTER.contactNote, domain=None, range=Optional[str])

slots.contactOrganization = Slot(uri=OBSERVABLE.contactOrganization, name="contactOrganization", curie=OBSERVABLE.curie('contactOrganization'),
                   model_uri=MASTER.contactOrganization, domain=None, range=Optional[Union[dict, Organization]])

slots.contactPhone = Slot(uri=OBSERVABLE.contactPhone, name="contactPhone", curie=OBSERVABLE.curie('contactPhone'),
                   model_uri=MASTER.contactPhone, domain=None, range=Optional[Union[dict, ContactPhone]])

slots.contactPhoneNumber = Slot(uri=OBSERVABLE.contactPhoneNumber, name="contactPhoneNumber", curie=OBSERVABLE.curie('contactPhoneNumber'),
                   model_uri=MASTER.contactPhoneNumber, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.contactPhoneScope = Slot(uri=OBSERVABLE.contactPhoneScope, name="contactPhoneScope", curie=OBSERVABLE.curie('contactPhoneScope'),
                   model_uri=MASTER.contactPhoneScope, domain=None, range=Optional[str])

slots.contactProfile = Slot(uri=OBSERVABLE.contactProfile, name="contactProfile", curie=OBSERVABLE.curie('contactProfile'),
                   model_uri=MASTER.contactProfile, domain=None, range=Optional[Union[dict, ContactProfile]])

slots.contactProfilePlatform = Slot(uri=OBSERVABLE.contactProfilePlatform, name="contactProfilePlatform", curie=OBSERVABLE.curie('contactProfilePlatform'),
                   model_uri=MASTER.contactProfilePlatform, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.contactSIP = Slot(uri=OBSERVABLE.contactSIP, name="contactSIP", curie=OBSERVABLE.curie('contactSIP'),
                   model_uri=MASTER.contactSIP, domain=None, range=Optional[Union[dict, ContactSIP]])

slots.contactSIPScope = Slot(uri=OBSERVABLE.contactSIPScope, name="contactSIPScope", curie=OBSERVABLE.curie('contactSIPScope'),
                   model_uri=MASTER.contactSIPScope, domain=None, range=Optional[str])

slots.contactURL = Slot(uri=OBSERVABLE.contactURL, name="contactURL", curie=OBSERVABLE.curie('contactURL'),
                   model_uri=MASTER.contactURL, domain=None, range=Optional[Union[dict, ContactURL]])

slots.contactURLScope = Slot(uri=OBSERVABLE.contactURLScope, name="contactURLScope", curie=OBSERVABLE.curie('contactURLScope'),
                   model_uri=MASTER.contactURLScope, domain=None, range=Optional[str])

slots.contentDisposition = Slot(uri=OBSERVABLE.contentDisposition, name="contentDisposition", curie=OBSERVABLE.curie('contentDisposition'),
                   model_uri=MASTER.contentDisposition, domain=None, range=Optional[str])

slots.contentRecoveredStatus = Slot(uri=OBSERVABLE.contentRecoveredStatus, name="contentRecoveredStatus", curie=OBSERVABLE.curie('contentRecoveredStatus'),
                   model_uri=MASTER.contentRecoveredStatus, domain=None, range=Optional[str])

slots.contentType = Slot(uri=OBSERVABLE.contentType, name="contentType", curie=OBSERVABLE.curie('contentType'),
                   model_uri=MASTER.contentType, domain=None, range=Optional[str])

slots.controlCode = Slot(uri=OBSERVABLE.controlCode, name="controlCode", curie=OBSERVABLE.curie('controlCode'),
                   model_uri=MASTER.controlCode, domain=None, range=Optional[str])

slots.cookieDomain = Slot(uri=OBSERVABLE.cookieDomain, name="cookieDomain", curie=OBSERVABLE.curie('cookieDomain'),
                   model_uri=MASTER.cookieDomain, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.cookieName = Slot(uri=OBSERVABLE.cookieName, name="cookieName", curie=OBSERVABLE.curie('cookieName'),
                   model_uri=MASTER.cookieName, domain=None, range=Optional[str])

slots.cookiePath = Slot(uri=OBSERVABLE.cookiePath, name="cookiePath", curie=OBSERVABLE.curie('cookiePath'),
                   model_uri=MASTER.cookiePath, domain=None, range=Optional[str])

slots.cpeid = Slot(uri=OBSERVABLE.cpeid, name="cpeid", curie=OBSERVABLE.curie('cpeid'),
                   model_uri=MASTER.cpeid, domain=None, range=Optional[str])

slots.cpu = Slot(uri=OBSERVABLE.cpu, name="cpu", curie=OBSERVABLE.curie('cpu'),
                   model_uri=MASTER.cpu, domain=None, range=Optional[str])

slots.cpuFamily = Slot(uri=OBSERVABLE.cpuFamily, name="cpuFamily", curie=OBSERVABLE.curie('cpuFamily'),
                   model_uri=MASTER.cpuFamily, domain=None, range=Optional[str])

slots.creationDate = Slot(uri=OBSERVABLE.creationDate, name="creationDate", curie=OBSERVABLE.curie('creationDate'),
                   model_uri=MASTER.creationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.creationFlags = Slot(uri=OBSERVABLE.creationFlags, name="creationFlags", curie=OBSERVABLE.curie('creationFlags'),
                   model_uri=MASTER.creationFlags, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.creationTime = Slot(uri=OBSERVABLE.creationTime, name="creationTime", curie=OBSERVABLE.curie('creationTime'),
                   model_uri=MASTER.creationTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.creator = Slot(uri=OBSERVABLE.creator, name="creator", curie=OBSERVABLE.curie('creator'),
                   model_uri=MASTER.creator, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.creatorUser = Slot(uri=OBSERVABLE.creatorUser, name="creatorUser", curie=OBSERVABLE.curie('creatorUser'),
                   model_uri=MASTER.creatorUser, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.crlDistributionPoints = Slot(uri=OBSERVABLE.crlDistributionPoints, name="crlDistributionPoints", curie=OBSERVABLE.curie('crlDistributionPoints'),
                   model_uri=MASTER.crlDistributionPoints, domain=None, range=Optional[str])

slots.currentSystemDate = Slot(uri=OBSERVABLE.currentSystemDate, name="currentSystemDate", curie=OBSERVABLE.curie('currentSystemDate'),
                   model_uri=MASTER.currentSystemDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.currentWorkingDirectory = Slot(uri=OBSERVABLE.currentWorkingDirectory, name="currentWorkingDirectory", curie=OBSERVABLE.curie('currentWorkingDirectory'),
                   model_uri=MASTER.currentWorkingDirectory, domain=None, range=Optional[str])

slots.cyberAction = Slot(uri=OBSERVABLE.cyberAction, name="cyberAction", curie=OBSERVABLE.curie('cyberAction'),
                   model_uri=MASTER.cyberAction, domain=None, range=Optional[Union[dict, ObservableAction]])

slots.data = Slot(uri=OBSERVABLE.data, name="data", curie=OBSERVABLE.curie('data'),
                   model_uri=MASTER.data, domain=None, range=Optional[str])

slots.dataPayload = Slot(uri=OBSERVABLE.dataPayload, name="dataPayload", curie=OBSERVABLE.curie('dataPayload'),
                   model_uri=MASTER.dataPayload, domain=None, range=Optional[str])

slots.dataPayloadReferenceURL = Slot(uri=OBSERVABLE.dataPayloadReferenceURL, name="dataPayloadReferenceURL", curie=OBSERVABLE.curie('dataPayloadReferenceURL'),
                   model_uri=MASTER.dataPayloadReferenceURL, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.dataType = Slot(uri=OBSERVABLE.dataType, name="dataType", curie=OBSERVABLE.curie('dataType'),
                   model_uri=MASTER.dataType, domain=None, range=Optional[str])

slots.depEnabled = Slot(uri=OBSERVABLE.depEnabled, name="depEnabled", curie=OBSERVABLE.curie('depEnabled'),
                   model_uri=MASTER.depEnabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.descriptions = Slot(uri=OBSERVABLE.descriptions, name="descriptions", curie=OBSERVABLE.curie('descriptions'),
                   model_uri=MASTER.descriptions, domain=None, range=Optional[str])

slots.destination = Slot(uri=OBSERVABLE.destination, name="destination", curie=OBSERVABLE.curie('destination'),
                   model_uri=MASTER.destination, domain=None, range=Optional[str])

slots.destinationFlags = Slot(uri=OBSERVABLE.destinationFlags, name="destinationFlags", curie=OBSERVABLE.curie('destinationFlags'),
                   model_uri=MASTER.destinationFlags, domain=None, range=Optional[str])

slots.destinationPort = Slot(uri=OBSERVABLE.destinationPort, name="destinationPort", curie=OBSERVABLE.curie('destinationPort'),
                   model_uri=MASTER.destinationPort, domain=None, range=Optional[int])

slots.deviceType = Slot(uri=OBSERVABLE.deviceType, name="deviceType", curie=OBSERVABLE.curie('deviceType'),
                   model_uri=MASTER.deviceType, domain=None, range=Optional[str])

slots.dhcpLeaseExpires = Slot(uri=OBSERVABLE.dhcpLeaseExpires, name="dhcpLeaseExpires", curie=OBSERVABLE.curie('dhcpLeaseExpires'),
                   model_uri=MASTER.dhcpLeaseExpires, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dhcpLeaseObtained = Slot(uri=OBSERVABLE.dhcpLeaseObtained, name="dhcpLeaseObtained", curie=OBSERVABLE.curie('dhcpLeaseObtained'),
                   model_uri=MASTER.dhcpLeaseObtained, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.dhcpServer = Slot(uri=OBSERVABLE.dhcpServer, name="dhcpServer", curie=OBSERVABLE.curie('dhcpServer'),
                   model_uri=MASTER.dhcpServer, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.diskPartitionType = Slot(uri=OBSERVABLE.diskPartitionType, name="diskPartitionType", curie=OBSERVABLE.curie('diskPartitionType'),
                   model_uri=MASTER.diskPartitionType, domain=None, range=Optional[str])

slots.diskSize = Slot(uri=OBSERVABLE.diskSize, name="diskSize", curie=OBSERVABLE.curie('diskSize'),
                   model_uri=MASTER.diskSize, domain=None, range=Optional[int])

slots.diskType = Slot(uri=OBSERVABLE.diskType, name="diskType", curie=OBSERVABLE.curie('diskType'),
                   model_uri=MASTER.diskType, domain=None, range=Optional[str])

slots.displayName = Slot(uri=OBSERVABLE.displayName, name="displayName", curie=OBSERVABLE.curie('displayName'),
                   model_uri=MASTER.displayName, domain=None, range=Optional[str])

slots.dllCharacteristics = Slot(uri=OBSERVABLE.dllCharacteristics, name="dllCharacteristics", curie=OBSERVABLE.curie('dllCharacteristics'),
                   model_uri=MASTER.dllCharacteristics, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.dnssec = Slot(uri=OBSERVABLE.dnssec, name="dnssec", curie=OBSERVABLE.curie('dnssec'),
                   model_uri=MASTER.dnssec, domain=None, range=Optional[str])

slots.documentInformationDictionary = Slot(uri=OBSERVABLE.documentInformationDictionary, name="documentInformationDictionary", curie=OBSERVABLE.curie('documentInformationDictionary'),
                   model_uri=MASTER.documentInformationDictionary, domain=None, range=Optional[Union[dict, ControlledDictionary]])

slots.domain = Slot(uri=OBSERVABLE.domain, name="domain", curie=OBSERVABLE.curie('domain'),
                   model_uri=MASTER.domain, domain=None, range=Optional[str])

slots.domainID = Slot(uri=OBSERVABLE.domainID, name="domainID", curie=OBSERVABLE.curie('domainID'),
                   model_uri=MASTER.domainID, domain=None, range=Optional[str])

slots.domainName = Slot(uri=OBSERVABLE.domainName, name="domainName", curie=OBSERVABLE.curie('domainName'),
                   model_uri=MASTER.domainName, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.driveLetter = Slot(uri=OBSERVABLE.driveLetter, name="driveLetter", curie=OBSERVABLE.curie('driveLetter'),
                   model_uri=MASTER.driveLetter, domain=None, range=Optional[str])

slots.driveType = Slot(uri=OBSERVABLE.driveType, name="driveType", curie=OBSERVABLE.curie('driveType'),
                   model_uri=MASTER.driveType, domain=None, range=Optional[str])

slots.dst = Slot(uri=OBSERVABLE.dst, name="dst", curie=OBSERVABLE.curie('dst'),
                   model_uri=MASTER.dst, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.dstBytes = Slot(uri=OBSERVABLE.dstBytes, name="dstBytes", curie=OBSERVABLE.curie('dstBytes'),
                   model_uri=MASTER.dstBytes, domain=None, range=Optional[int])

slots.dstPackets = Slot(uri=OBSERVABLE.dstPackets, name="dstPackets", curie=OBSERVABLE.curie('dstPackets'),
                   model_uri=MASTER.dstPackets, domain=None, range=Optional[int])

slots.dstPayload = Slot(uri=OBSERVABLE.dstPayload, name="dstPayload", curie=OBSERVABLE.curie('dstPayload'),
                   model_uri=MASTER.dstPayload, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.duration = Slot(uri=OBSERVABLE.duration, name="duration", curie=OBSERVABLE.curie('duration'),
                   model_uri=MASTER.duration, domain=None, range=Optional[int])

slots.effectiveGroup = Slot(uri=OBSERVABLE.effectiveGroup, name="effectiveGroup", curie=OBSERVABLE.curie('effectiveGroup'),
                   model_uri=MASTER.effectiveGroup, domain=None, range=Optional[str])

slots.effectiveGroupID = Slot(uri=OBSERVABLE.effectiveGroupID, name="effectiveGroupID", curie=OBSERVABLE.curie('effectiveGroupID'),
                   model_uri=MASTER.effectiveGroupID, domain=None, range=Optional[str])

slots.effectiveUser = Slot(uri=OBSERVABLE.effectiveUser, name="effectiveUser", curie=OBSERVABLE.curie('effectiveUser'),
                   model_uri=MASTER.effectiveUser, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.elevation = Slot(uri=OBSERVABLE.elevation, name="elevation", curie=OBSERVABLE.curie('elevation'),
                   model_uri=MASTER.elevation, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.emailAddress = Slot(uri=OBSERVABLE.emailAddress, name="emailAddress", curie=OBSERVABLE.curie('emailAddress'),
                   model_uri=MASTER.emailAddress, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.encoding = Slot(uri=OBSERVABLE.encoding, name="encoding", curie=OBSERVABLE.curie('encoding'),
                   model_uri=MASTER.encoding, domain=None, range=Optional[str])

slots.encodingMethod = Slot(uri=OBSERVABLE.encodingMethod, name="encodingMethod", curie=OBSERVABLE.curie('encodingMethod'),
                   model_uri=MASTER.encodingMethod, domain=None, range=Optional[str])

slots.encryptionIV = Slot(uri=OBSERVABLE.encryptionIV, name="encryptionIV", curie=OBSERVABLE.curie('encryptionIV'),
                   model_uri=MASTER.encryptionIV, domain=None, range=Optional[str])

slots.encryptionKey = Slot(uri=OBSERVABLE.encryptionKey, name="encryptionKey", curie=OBSERVABLE.curie('encryptionKey'),
                   model_uri=MASTER.encryptionKey, domain=None, range=Optional[str])

slots.encryptionMethod = Slot(uri=OBSERVABLE.encryptionMethod, name="encryptionMethod", curie=OBSERVABLE.curie('encryptionMethod'),
                   model_uri=MASTER.encryptionMethod, domain=None, range=Optional[str])

slots.encryptionMode = Slot(uri=OBSERVABLE.encryptionMode, name="encryptionMode", curie=OBSERVABLE.curie('encryptionMode'),
                   model_uri=MASTER.encryptionMode, domain=None, range=Optional[str])

slots.englishTranslation = Slot(uri=OBSERVABLE.englishTranslation, name="englishTranslation", curie=OBSERVABLE.curie('englishTranslation'),
                   model_uri=MASTER.englishTranslation, domain=None, range=Optional[str])

slots.entropy = Slot(uri=OBSERVABLE.entropy, name="entropy", curie=OBSERVABLE.curie('entropy'),
                   model_uri=MASTER.entropy, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.entryID = Slot(uri=OBSERVABLE.entryID, name="entryID", curie=OBSERVABLE.curie('entryID'),
                   model_uri=MASTER.entryID, domain=None, range=Optional[int])

slots.environmentVariables = Slot(uri=OBSERVABLE.environmentVariables, name="environmentVariables", curie=OBSERVABLE.curie('environmentVariables'),
                   model_uri=MASTER.environmentVariables, domain=None, range=Optional[Union[dict, Dictionary]])

slots.eventRecordDevice = Slot(uri=OBSERVABLE.eventRecordDevice, name="eventRecordDevice", curie=OBSERVABLE.curie('eventRecordDevice'),
                   model_uri=MASTER.eventRecordDevice, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.eventID = Slot(uri=OBSERVABLE.eventID, name="eventID", curie=OBSERVABLE.curie('eventID'),
                   model_uri=MASTER.eventID, domain=None, range=Optional[str])

slots.eventRecordID = Slot(uri=OBSERVABLE.eventRecordID, name="eventRecordID", curie=OBSERVABLE.curie('eventRecordID'),
                   model_uri=MASTER.eventRecordID, domain=None, range=Optional[str])

slots.eventRecordRaw = Slot(uri=OBSERVABLE.eventRecordRaw, name="eventRecordRaw", curie=OBSERVABLE.curie('eventRecordRaw'),
                   model_uri=MASTER.eventRecordRaw, domain=None, range=Optional[str])

slots.eventRecordServiceName = Slot(uri=OBSERVABLE.eventRecordServiceName, name="eventRecordServiceName", curie=OBSERVABLE.curie('eventRecordServiceName'),
                   model_uri=MASTER.eventRecordServiceName, domain=None, range=Optional[str])

slots.eventRecordText = Slot(uri=OBSERVABLE.eventRecordText, name="eventRecordText", curie=OBSERVABLE.curie('eventRecordText'),
                   model_uri=MASTER.eventRecordText, domain=None, range=Optional[str])

slots.eventStatus = Slot(uri=OBSERVABLE.eventStatus, name="eventStatus", curie=OBSERVABLE.curie('eventStatus'),
                   model_uri=MASTER.eventStatus, domain=None, range=Optional[str])

slots.eventType = Slot(uri=OBSERVABLE.eventType, name="eventType", curie=OBSERVABLE.curie('eventType'),
                   model_uri=MASTER.eventType, domain=None, range=Optional[str])

slots.execArguments = Slot(uri=OBSERVABLE.execArguments, name="execArguments", curie=OBSERVABLE.curie('execArguments'),
                   model_uri=MASTER.execArguments, domain=None, range=Optional[str])

slots.execProgramHashes = Slot(uri=OBSERVABLE.execProgramHashes, name="execProgramHashes", curie=OBSERVABLE.curie('execProgramHashes'),
                   model_uri=MASTER.execProgramHashes, domain=None, range=Optional[Union[dict, Hash]])

slots.execProgramPath = Slot(uri=OBSERVABLE.execProgramPath, name="execProgramPath", curie=OBSERVABLE.curie('execProgramPath'),
                   model_uri=MASTER.execProgramPath, domain=None, range=Optional[str])

slots.execWorkingDirectory = Slot(uri=OBSERVABLE.execWorkingDirectory, name="execWorkingDirectory", curie=OBSERVABLE.curie('execWorkingDirectory'),
                   model_uri=MASTER.execWorkingDirectory, domain=None, range=Optional[str])

slots.exifData = Slot(uri=OBSERVABLE.exifData, name="exifData", curie=OBSERVABLE.curie('exifData'),
                   model_uri=MASTER.exifData, domain=None, range=Optional[Union[dict, ControlledDictionary]])

slots.exitCode = Slot(uri=OBSERVABLE.exitCode, name="exitCode", curie=OBSERVABLE.curie('exitCode'),
                   model_uri=MASTER.exitCode, domain=None, range=Optional[int])

slots.exitStatus = Slot(uri=OBSERVABLE.exitStatus, name="exitStatus", curie=OBSERVABLE.curie('exitStatus'),
                   model_uri=MASTER.exitStatus, domain=None, range=Optional[int])

slots.exitTime = Slot(uri=OBSERVABLE.exitTime, name="exitTime", curie=OBSERVABLE.curie('exitTime'),
                   model_uri=MASTER.exitTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.expirationDate = Slot(uri=OBSERVABLE.expirationDate, name="expirationDate", curie=OBSERVABLE.curie('expirationDate'),
                   model_uri=MASTER.expirationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.expirationTime = Slot(uri=OBSERVABLE.expirationTime, name="expirationTime", curie=OBSERVABLE.curie('expirationTime'),
                   model_uri=MASTER.expirationTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extDeletionTime = Slot(uri=OBSERVABLE.extDeletionTime, name="extDeletionTime", curie=OBSERVABLE.curie('extDeletionTime'),
                   model_uri=MASTER.extDeletionTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extFileType = Slot(uri=OBSERVABLE.extFileType, name="extFileType", curie=OBSERVABLE.curie('extFileType'),
                   model_uri=MASTER.extFileType, domain=None, range=Optional[int])

slots.extFlags = Slot(uri=OBSERVABLE.extFlags, name="extFlags", curie=OBSERVABLE.curie('extFlags'),
                   model_uri=MASTER.extFlags, domain=None, range=Optional[int])

slots.extHardLinkCount = Slot(uri=OBSERVABLE.extHardLinkCount, name="extHardLinkCount", curie=OBSERVABLE.curie('extHardLinkCount'),
                   model_uri=MASTER.extHardLinkCount, domain=None, range=Optional[int])

slots.extInodeChangeTime = Slot(uri=OBSERVABLE.extInodeChangeTime, name="extInodeChangeTime", curie=OBSERVABLE.curie('extInodeChangeTime'),
                   model_uri=MASTER.extInodeChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.extInodeID = Slot(uri=OBSERVABLE.extInodeID, name="extInodeID", curie=OBSERVABLE.curie('extInodeID'),
                   model_uri=MASTER.extInodeID, domain=None, range=Optional[int])

slots.extPermissions = Slot(uri=OBSERVABLE.extPermissions, name="extPermissions", curie=OBSERVABLE.curie('extPermissions'),
                   model_uri=MASTER.extPermissions, domain=None, range=Optional[int])

slots.extSGID = Slot(uri=OBSERVABLE.extSGID, name="extSGID", curie=OBSERVABLE.curie('extSGID'),
                   model_uri=MASTER.extSGID, domain=None, range=Optional[int])

slots.extSUID = Slot(uri=OBSERVABLE.extSUID, name="extSUID", curie=OBSERVABLE.curie('extSUID'),
                   model_uri=MASTER.extSUID, domain=None, range=Optional[int])

slots.extendedKeyUsage = Slot(uri=OBSERVABLE.extendedKeyUsage, name="extendedKeyUsage", curie=OBSERVABLE.curie('extendedKeyUsage'),
                   model_uri=MASTER.extendedKeyUsage, domain=None, range=Optional[str])

slots.extension = Slot(uri=OBSERVABLE.extension, name="extension", curie=OBSERVABLE.curie('extension'),
                   model_uri=MASTER.extension, domain=None, range=Optional[str])

slots.favoritesCount = Slot(uri=OBSERVABLE.favoritesCount, name="favoritesCount", curie=OBSERVABLE.curie('favoritesCount'),
                   model_uri=MASTER.favoritesCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.fileAlignment = Slot(uri=OBSERVABLE.fileAlignment, name="fileAlignment", curie=OBSERVABLE.curie('fileAlignment'),
                   model_uri=MASTER.fileAlignment, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.fileHeaderHashes = Slot(uri=OBSERVABLE.fileHeaderHashes, name="fileHeaderHashes", curie=OBSERVABLE.curie('fileHeaderHashes'),
                   model_uri=MASTER.fileHeaderHashes, domain=None, range=Optional[Union[dict, Hash]])

slots.fileName = Slot(uri=OBSERVABLE.fileName, name="fileName", curie=OBSERVABLE.curie('fileName'),
                   model_uri=MASTER.fileName, domain=None, range=Optional[str])

slots.filePath = Slot(uri=OBSERVABLE.filePath, name="filePath", curie=OBSERVABLE.curie('filePath'),
                   model_uri=MASTER.filePath, domain=None, range=Optional[str])

slots.fileSystemType = Slot(uri=OBSERVABLE.fileSystemType, name="fileSystemType", curie=OBSERVABLE.curie('fileSystemType'),
                   model_uri=MASTER.fileSystemType, domain=None, range=Optional[str])

slots.firstLoginTime = Slot(uri=OBSERVABLE.firstLoginTime, name="firstLoginTime", curie=OBSERVABLE.curie('firstLoginTime'),
                   model_uri=MASTER.firstLoginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.firstName = Slot(uri=OBSERVABLE.firstName, name="firstName", curie=OBSERVABLE.curie('firstName'),
                   model_uri=MASTER.firstName, domain=None, range=Optional[str])

slots.firstRun = Slot(uri=OBSERVABLE.firstRun, name="firstRun", curie=OBSERVABLE.curie('firstRun'),
                   model_uri=MASTER.firstRun, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.firstVisit = Slot(uri=OBSERVABLE.firstVisit, name="firstVisit", curie=OBSERVABLE.curie('firstVisit'),
                   model_uri=MASTER.firstVisit, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.flags = Slot(uri=OBSERVABLE.flags, name="flags", curie=OBSERVABLE.curie('flags'),
                   model_uri=MASTER.flags, domain=None, range=Optional[str])

slots.followersCount = Slot(uri=OBSERVABLE.followersCount, name="followersCount", curie=OBSERVABLE.curie('followersCount'),
                   model_uri=MASTER.followersCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.format = Slot(uri=OBSERVABLE.format, name="format", curie=OBSERVABLE.curie('format'),
                   model_uri=MASTER.format, domain=None, range=Optional[str])

slots.fragment = Slot(uri=OBSERVABLE.fragment, name="fragment", curie=OBSERVABLE.curie('fragment'),
                   model_uri=MASTER.fragment, domain=None, range=Optional[str])

slots.fragmentIndex = Slot(uri=OBSERVABLE.fragmentIndex, name="fragmentIndex", curie=OBSERVABLE.curie('fragmentIndex'),
                   model_uri=MASTER.fragmentIndex, domain=None, range=Optional[int])

slots.freeSpace = Slot(uri=OBSERVABLE.freeSpace, name="freeSpace", curie=OBSERVABLE.curie('freeSpace'),
                   model_uri=MASTER.freeSpace, domain=None, range=Optional[int])

slots.friendsCount = Slot(uri=OBSERVABLE.friendsCount, name="friendsCount", curie=OBSERVABLE.curie('friendsCount'),
                   model_uri=MASTER.friendsCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.from = Slot(uri=OBSERVABLE.from, name="from", curie=OBSERVABLE.curie('from'),
                   model_uri=MASTER.from, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.fromURLVisit = Slot(uri=OBSERVABLE.fromURLVisit, name="fromURLVisit", curie=OBSERVABLE.curie('fromURLVisit'),
                   model_uri=MASTER.fromURLVisit, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.fullValue = Slot(uri=OBSERVABLE.fullValue, name="fullValue", curie=OBSERVABLE.curie('fullValue'),
                   model_uri=MASTER.fullValue, domain=None, range=Optional[str])

slots.geoLocationEntry = Slot(uri=OBSERVABLE.geoLocationEntry, name="geoLocationEntry", curie=OBSERVABLE.curie('geoLocationEntry'),
                   model_uri=MASTER.geoLocationEntry, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.geoLocationAddress = Slot(uri=OBSERVABLE.geoLocationAddress, name="geoLocationAddress", curie=OBSERVABLE.curie('geoLocationAddress'),
                   model_uri=MASTER.geoLocationAddress, domain=None, range=Optional[Union[dict, Location]])

slots.gid = Slot(uri=OBSERVABLE.gid, name="gid", curie=OBSERVABLE.curie('gid'),
                   model_uri=MASTER.gid, domain=None, range=Optional[int])

slots.globalFlagList = Slot(uri=OBSERVABLE.globalFlagList, name="globalFlagList", curie=OBSERVABLE.curie('globalFlagList'),
                   model_uri=MASTER.globalFlagList, domain=None, range=Optional[Union[dict, GlobalFlagType]])

slots.gpu = Slot(uri=OBSERVABLE.gpu, name="gpu", curie=OBSERVABLE.curie('gpu'),
                   model_uri=MASTER.gpu, domain=None, range=Optional[str])

slots.gpuFamily = Slot(uri=OBSERVABLE.gpuFamily, name="gpuFamily", curie=OBSERVABLE.curie('gpuFamily'),
                   model_uri=MASTER.gpuFamily, domain=None, range=Optional[str])

slots.groupName = Slot(uri=OBSERVABLE.groupName, name="groupName", curie=OBSERVABLE.curie('groupName'),
                   model_uri=MASTER.groupName, domain=None, range=Optional[str])

slots.groups = Slot(uri=OBSERVABLE.groups, name="groups", curie=OBSERVABLE.curie('groups'),
                   model_uri=MASTER.groups, domain=None, range=Optional[str])

slots.hasChanged = Slot(uri=OBSERVABLE.hasChanged, name="hasChanged", curie=OBSERVABLE.curie('hasChanged'),
                   model_uri=MASTER.hasChanged, domain=None, range=Optional[Union[bool, BooleanType]])

slots.hash = Slot(uri=OBSERVABLE.hash, name="hash", curie=OBSERVABLE.curie('hash'),
                   model_uri=MASTER.hash, domain=None, range=Optional[Union[dict, Hash]])

slots.hashes = Slot(uri=OBSERVABLE.hashes, name="hashes", curie=OBSERVABLE.curie('hashes'),
                   model_uri=MASTER.hashes, domain=None, range=Optional[Union[dict, Hash]])

slots.headerRaw = Slot(uri=OBSERVABLE.headerRaw, name="headerRaw", curie=OBSERVABLE.curie('headerRaw'),
                   model_uri=MASTER.headerRaw, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.hexadecimalValue = Slot(uri=OBSERVABLE.hexadecimalValue, name="hexadecimalValue", curie=OBSERVABLE.curie('hexadecimalValue'),
                   model_uri=MASTER.hexadecimalValue, domain=None, range=Optional[hex])

slots.hiveType = Slot(uri=OBSERVABLE.hiveType, name="hiveType", curie=OBSERVABLE.curie('hiveType'),
                   model_uri=MASTER.hiveType, domain=None, range=Optional[str])

slots.homeDirectory = Slot(uri=OBSERVABLE.homeDirectory, name="homeDirectory", curie=OBSERVABLE.curie('homeDirectory'),
                   model_uri=MASTER.homeDirectory, domain=None, range=Optional[str])

slots.horizontalBeamWidth = Slot(uri=OBSERVABLE.horizontalBeamWidth, name="horizontalBeamWidth", curie=OBSERVABLE.curie('horizontalBeamWidth'),
                   model_uri=MASTER.horizontalBeamWidth, domain=None, range=Optional[str])

slots.host = Slot(uri=OBSERVABLE.host, name="host", curie=OBSERVABLE.curie('host'),
                   model_uri=MASTER.host, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.hostname = Slot(uri=OBSERVABLE.hostname, name="hostname", curie=OBSERVABLE.curie('hostname'),
                   model_uri=MASTER.hostname, domain=None, range=Optional[str])

slots.httpMessageBodyLength = Slot(uri=OBSERVABLE.httpMessageBodyLength, name="httpMessageBodyLength", curie=OBSERVABLE.curie('httpMessageBodyLength'),
                   model_uri=MASTER.httpMessageBodyLength, domain=None, range=Optional[int])

slots.httpMessageBodyData = Slot(uri=OBSERVABLE.httpMessageBodyData, name="httpMessageBodyData", curie=OBSERVABLE.curie('httpMessageBodyData'),
                   model_uri=MASTER.httpMessageBodyData, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.httpRequestHeader = Slot(uri=OBSERVABLE.httpRequestHeader, name="httpRequestHeader", curie=OBSERVABLE.curie('httpRequestHeader'),
                   model_uri=MASTER.httpRequestHeader, domain=None, range=Optional[Union[dict, Dictionary]])

slots.iComHandlerAction = Slot(uri=OBSERVABLE.iComHandlerAction, name="iComHandlerAction", curie=OBSERVABLE.curie('iComHandlerAction'),
                   model_uri=MASTER.iComHandlerAction, domain=None, range=Optional[Union[dict, IComHandlerActionType]])

slots.iEmailAction = Slot(uri=OBSERVABLE.iEmailAction, name="iEmailAction", curie=OBSERVABLE.curie('iEmailAction'),
                   model_uri=MASTER.iEmailAction, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.iExecAction = Slot(uri=OBSERVABLE.iExecAction, name="iExecAction", curie=OBSERVABLE.curie('iExecAction'),
                   model_uri=MASTER.iExecAction, domain=None, range=Optional[Union[dict, IExecActionType]])

slots.iShowMessageAction = Slot(uri=OBSERVABLE.iShowMessageAction, name="iShowMessageAction", curie=OBSERVABLE.curie('iShowMessageAction'),
                   model_uri=MASTER.iShowMessageAction, domain=None, range=Optional[Union[dict, IShowMessageActionType]])

slots.icmpCode = Slot(uri=OBSERVABLE.icmpCode, name="icmpCode", curie=OBSERVABLE.curie('icmpCode'),
                   model_uri=MASTER.icmpCode, domain=None, range=Optional[hex])

slots.icmpType = Slot(uri=OBSERVABLE.icmpType, name="icmpType", curie=OBSERVABLE.curie('icmpType'),
                   model_uri=MASTER.icmpType, domain=None, range=Optional[hex])

slots.imageBase = Slot(uri=OBSERVABLE.imageBase, name="imageBase", curie=OBSERVABLE.curie('imageBase'),
                   model_uri=MASTER.imageBase, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.imageCompressionMethod = Slot(uri=OBSERVABLE.imageCompressionMethod, name="imageCompressionMethod", curie=OBSERVABLE.curie('imageCompressionMethod'),
                   model_uri=MASTER.imageCompressionMethod, domain=None, range=Optional[str])

slots.imageName = Slot(uri=OBSERVABLE.imageName, name="imageName", curie=OBSERVABLE.curie('imageName'),
                   model_uri=MASTER.imageName, domain=None, range=Optional[str])

slots.imageType = Slot(uri=OBSERVABLE.imageType, name="imageType", curie=OBSERVABLE.curie('imageType'),
                   model_uri=MASTER.imageType, domain=None, range=Optional[str])

slots.impHash = Slot(uri=OBSERVABLE.impHash, name="impHash", curie=OBSERVABLE.curie('impHash'),
                   model_uri=MASTER.impHash, domain=None, range=Optional[str])

slots.inReplyTo = Slot(uri=OBSERVABLE.inReplyTo, name="inReplyTo", curie=OBSERVABLE.curie('inReplyTo'),
                   model_uri=MASTER.inReplyTo, domain=None, range=Optional[str])

slots.inetLocation = Slot(uri=OBSERVABLE.inetLocation, name="inetLocation", curie=OBSERVABLE.curie('inetLocation'),
                   model_uri=MASTER.inetLocation, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.inhibitAnyPolicy = Slot(uri=OBSERVABLE.inhibitAnyPolicy, name="inhibitAnyPolicy", curie=OBSERVABLE.curie('inhibitAnyPolicy'),
                   model_uri=MASTER.inhibitAnyPolicy, domain=None, range=Optional[str])

slots.installDate = Slot(uri=OBSERVABLE.installDate, name="installDate", curie=OBSERVABLE.curie('installDate'),
                   model_uri=MASTER.installDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.installedVersionHistory = Slot(uri=OBSERVABLE.installedVersionHistory, name="installedVersionHistory", curie=OBSERVABLE.curie('installedVersionHistory'),
                   model_uri=MASTER.installedVersionHistory, domain=None, range=Optional[Union[dict, ApplicationVersion]])

slots.interceptedCallState = Slot(uri=OBSERVABLE.interceptedCallState, name="interceptedCallState", curie=OBSERVABLE.curie('interceptedCallState'),
                   model_uri=MASTER.interceptedCallState, domain=None, range=Optional[str])

slots.ip = Slot(uri=OBSERVABLE.ip, name="ip", curie=OBSERVABLE.curie('ip'),
                   model_uri=MASTER.ip, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.ipAddress = Slot(uri=OBSERVABLE.ipAddress, name="ipAddress", curie=OBSERVABLE.curie('ipAddress'),
                   model_uri=MASTER.ipAddress, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.ipGateway = Slot(uri=OBSERVABLE.ipGateway, name="ipGateway", curie=OBSERVABLE.curie('ipGateway'),
                   model_uri=MASTER.ipGateway, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.ipfix = Slot(uri=OBSERVABLE.ipfix, name="ipfix", curie=OBSERVABLE.curie('ipfix'),
                   model_uri=MASTER.ipfix, domain=None, range=Optional[Union[dict, Dictionary]])

slots.isADBRootEnabled = Slot(uri=OBSERVABLE.isADBRootEnabled, name="isADBRootEnabled", curie=OBSERVABLE.curie('isADBRootEnabled'),
                   model_uri=MASTER.isADBRootEnabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isActive = Slot(uri=OBSERVABLE.isActive, name="isActive", curie=OBSERVABLE.curie('isActive'),
                   model_uri=MASTER.isActive, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isDirectory = Slot(uri=OBSERVABLE.isDirectory, name="isDirectory", curie=OBSERVABLE.curie('isDirectory'),
                   model_uri=MASTER.isDirectory, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isDisabled = Slot(uri=OBSERVABLE.isDisabled, name="isDisabled", curie=OBSERVABLE.curie('isDisabled'),
                   model_uri=MASTER.isDisabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isEnabled = Slot(uri=OBSERVABLE.isEnabled, name="isEnabled", curie=OBSERVABLE.curie('isEnabled'),
                   model_uri=MASTER.isEnabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isEncrypted = Slot(uri=OBSERVABLE.isEncrypted, name="isEncrypted", curie=OBSERVABLE.curie('isEncrypted'),
                   model_uri=MASTER.isEncrypted, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isHidden = Slot(uri=OBSERVABLE.isHidden, name="isHidden", curie=OBSERVABLE.curie('isHidden'),
                   model_uri=MASTER.isHidden, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isInjected = Slot(uri=OBSERVABLE.isInjected, name="isInjected", curie=OBSERVABLE.curie('isInjected'),
                   model_uri=MASTER.isInjected, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isLimitAdTrackingEnabled = Slot(uri=OBSERVABLE.isLimitAdTrackingEnabled, name="isLimitAdTrackingEnabled", curie=OBSERVABLE.curie('isLimitAdTrackingEnabled'),
                   model_uri=MASTER.isLimitAdTrackingEnabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isMapped = Slot(uri=OBSERVABLE.isMapped, name="isMapped", curie=OBSERVABLE.curie('isMapped'),
                   model_uri=MASTER.isMapped, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isMimeEncoded = Slot(uri=OBSERVABLE.isMimeEncoded, name="isMimeEncoded", curie=OBSERVABLE.curie('isMimeEncoded'),
                   model_uri=MASTER.isMimeEncoded, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isMultipart = Slot(uri=OBSERVABLE.isMultipart, name="isMultipart", curie=OBSERVABLE.curie('isMultipart'),
                   model_uri=MASTER.isMultipart, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isNamed = Slot(uri=OBSERVABLE.isNamed, name="isNamed", curie=OBSERVABLE.curie('isNamed'),
                   model_uri=MASTER.isNamed, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isOptimized = Slot(uri=OBSERVABLE.isOptimized, name="isOptimized", curie=OBSERVABLE.curie('isOptimized'),
                   model_uri=MASTER.isOptimized, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isPrivate = Slot(uri=OBSERVABLE.isPrivate, name="isPrivate", curie=OBSERVABLE.curie('isPrivate'),
                   model_uri=MASTER.isPrivate, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isPrivileged = Slot(uri=OBSERVABLE.isPrivileged, name="isPrivileged", curie=OBSERVABLE.curie('isPrivileged'),
                   model_uri=MASTER.isPrivileged, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isProtected = Slot(uri=OBSERVABLE.isProtected, name="isProtected", curie=OBSERVABLE.curie('isProtected'),
                   model_uri=MASTER.isProtected, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isRead = Slot(uri=OBSERVABLE.isRead, name="isRead", curie=OBSERVABLE.curie('isRead'),
                   model_uri=MASTER.isRead, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isSURootEnabled = Slot(uri=OBSERVABLE.isSURootEnabled, name="isSURootEnabled", curie=OBSERVABLE.curie('isSURootEnabled'),
                   model_uri=MASTER.isSURootEnabled, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isSecure = Slot(uri=OBSERVABLE.isSecure, name="isSecure", curie=OBSERVABLE.curie('isSecure'),
                   model_uri=MASTER.isSecure, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isSelfSigned = Slot(uri=OBSERVABLE.isSelfSigned, name="isSelfSigned", curie=OBSERVABLE.curie('isSelfSigned'),
                   model_uri=MASTER.isSelfSigned, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isServiceAccount = Slot(uri=OBSERVABLE.isServiceAccount, name="isServiceAccount", curie=OBSERVABLE.curie('isServiceAccount'),
                   model_uri=MASTER.isServiceAccount, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isTLD = Slot(uri=OBSERVABLE.isTLD, name="isTLD", curie=OBSERVABLE.curie('isTLD'),
                   model_uri=MASTER.isTLD, domain=None, range=Optional[Union[bool, BooleanType]])

slots.isVolatile = Slot(uri=OBSERVABLE.isVolatile, name="isVolatile", curie=OBSERVABLE.curie('isVolatile'),
                   model_uri=MASTER.isVolatile, domain=None, range=Optional[Union[bool, BooleanType]])

slots.issuer = Slot(uri=OBSERVABLE.issuer, name="issuer", curie=OBSERVABLE.curie('issuer'),
                   model_uri=MASTER.issuer, domain=None, range=Optional[str])

slots.issuerAlternativeName = Slot(uri=OBSERVABLE.issuerAlternativeName, name="issuerAlternativeName", curie=OBSERVABLE.curie('issuerAlternativeName'),
                   model_uri=MASTER.issuerAlternativeName, domain=None, range=Optional[str])

slots.issuerHash = Slot(uri=OBSERVABLE.issuerHash, name="issuerHash", curie=OBSERVABLE.curie('issuerHash'),
                   model_uri=MASTER.issuerHash, domain=None, range=Optional[Union[dict, Hash]])

slots.keyUsage = Slot(uri=OBSERVABLE.keyUsage, name="keyUsage", curie=OBSERVABLE.curie('keyUsage'),
                   model_uri=MASTER.keyUsage, domain=None, range=Optional[str])

slots.keypadUnlockCode = Slot(uri=OBSERVABLE.keypadUnlockCode, name="keypadUnlockCode", curie=OBSERVABLE.curie('keypadUnlockCode'),
                   model_uri=MASTER.keypadUnlockCode, domain=None, range=Optional[str])

slots.keywordSearchTerm = Slot(uri=OBSERVABLE.keywordSearchTerm, name="keywordSearchTerm", curie=OBSERVABLE.curie('keywordSearchTerm'),
                   model_uri=MASTER.keywordSearchTerm, domain=None, range=Optional[str])

slots.labels = Slot(uri=OBSERVABLE.labels, name="labels", curie=OBSERVABLE.curie('labels'),
                   model_uri=MASTER.labels, domain=None, range=Optional[str])

slots.language = Slot(uri=OBSERVABLE.language, name="language", curie=OBSERVABLE.curie('language'),
                   model_uri=MASTER.language, domain=None, range=Optional[str])

slots.lastLoginTime = Slot(uri=OBSERVABLE.lastLoginTime, name="lastLoginTime", curie=OBSERVABLE.curie('lastLoginTime'),
                   model_uri=MASTER.lastLoginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastName = Slot(uri=OBSERVABLE.lastName, name="lastName", curie=OBSERVABLE.curie('lastName'),
                   model_uri=MASTER.lastName, domain=None, range=Optional[str])

slots.lastRun = Slot(uri=OBSERVABLE.lastRun, name="lastRun", curie=OBSERVABLE.curie('lastRun'),
                   model_uri=MASTER.lastRun, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastShutdownDate = Slot(uri=OBSERVABLE.lastShutdownDate, name="lastShutdownDate", curie=OBSERVABLE.curie('lastShutdownDate'),
                   model_uri=MASTER.lastShutdownDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastTimeContacted = Slot(uri=OBSERVABLE.lastTimeContacted, name="lastTimeContacted", curie=OBSERVABLE.curie('lastTimeContacted'),
                   model_uri=MASTER.lastTimeContacted, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lastVisit = Slot(uri=OBSERVABLE.lastVisit, name="lastVisit", curie=OBSERVABLE.curie('lastVisit'),
                   model_uri=MASTER.lastVisit, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.length = Slot(uri=OBSERVABLE.length, name="length", curie=OBSERVABLE.curie('length'),
                   model_uri=MASTER.length, domain=None, range=Optional[int])

slots.libraryType = Slot(uri=OBSERVABLE.libraryType, name="libraryType", curie=OBSERVABLE.curie('libraryType'),
                   model_uri=MASTER.libraryType, domain=None, range=Optional[str])

slots.MSISDN = Slot(uri=OBSERVABLE.MSISDN, name="MSISDN", curie=OBSERVABLE.curie('MSISDN'),
                   model_uri=MASTER.MSISDN, domain=None, range=Optional[str])

slots.MSISDNType = Slot(uri=OBSERVABLE.MSISDNType, name="MSISDNType", curie=OBSERVABLE.curie('MSISDNType'),
                   model_uri=MASTER.MSISDNType, domain=None, range=Optional[str])

slots.listedCount = Slot(uri=OBSERVABLE.listedCount, name="listedCount", curie=OBSERVABLE.curie('listedCount'),
                   model_uri=MASTER.listedCount, domain=None, range=Optional[int])

slots.loaderFlags = Slot(uri=OBSERVABLE.loaderFlags, name="loaderFlags", curie=OBSERVABLE.curie('loaderFlags'),
                   model_uri=MASTER.loaderFlags, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.localTime = Slot(uri=OBSERVABLE.localTime, name="localTime", curie=OBSERVABLE.curie('localTime'),
                   model_uri=MASTER.localTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.loginTime = Slot(uri=OBSERVABLE.loginTime, name="loginTime", curie=OBSERVABLE.curie('loginTime'),
                   model_uri=MASTER.loginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.logoutTime = Slot(uri=OBSERVABLE.logoutTime, name="logoutTime", curie=OBSERVABLE.curie('logoutTime'),
                   model_uri=MASTER.logoutTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.lookupDate = Slot(uri=OBSERVABLE.lookupDate, name="lookupDate", curie=OBSERVABLE.curie('lookupDate'),
                   model_uri=MASTER.lookupDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.macAddress = Slot(uri=OBSERVABLE.macAddress, name="macAddress", curie=OBSERVABLE.curie('macAddress'),
                   model_uri=MASTER.macAddress, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.machine = Slot(uri=OBSERVABLE.machine, name="machine", curie=OBSERVABLE.curie('machine'),
                   model_uri=MASTER.machine, domain=None, range=Optional[str])

slots.magic = Slot(uri=OBSERVABLE.magic, name="magic", curie=OBSERVABLE.curie('magic'),
                   model_uri=MASTER.magic, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.magicNumber = Slot(uri=OBSERVABLE.magicNumber, name="magicNumber", curie=OBSERVABLE.curie('magicNumber'),
                   model_uri=MASTER.magicNumber, domain=None, range=Optional[str])

slots.majorImageVersion = Slot(uri=OBSERVABLE.majorImageVersion, name="majorImageVersion", curie=OBSERVABLE.curie('majorImageVersion'),
                   model_uri=MASTER.majorImageVersion, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.majorLinkerVersion = Slot(uri=OBSERVABLE.majorLinkerVersion, name="majorLinkerVersion", curie=OBSERVABLE.curie('majorLinkerVersion'),
                   model_uri=MASTER.majorLinkerVersion, domain=None, range=Optional[Union[int, ByteType]])

slots.majorOSVersion = Slot(uri=OBSERVABLE.majorOSVersion, name="majorOSVersion", curie=OBSERVABLE.curie('majorOSVersion'),
                   model_uri=MASTER.majorOSVersion, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.majorSubsystemVersion = Slot(uri=OBSERVABLE.majorSubsystemVersion, name="majorSubsystemVersion", curie=OBSERVABLE.curie('majorSubsystemVersion'),
                   model_uri=MASTER.majorSubsystemVersion, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.manuallyEnteredCount = Slot(uri=OBSERVABLE.manuallyEnteredCount, name="manuallyEnteredCount", curie=OBSERVABLE.curie('manuallyEnteredCount'),
                   model_uri=MASTER.manuallyEnteredCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.manufacturer = Slot(uri=OBSERVABLE.manufacturer, name="manufacturer", curie=OBSERVABLE.curie('manufacturer'),
                   model_uri=MASTER.manufacturer, domain=None, range=Optional[Union[dict, Identity]])

slots.maxRunTime = Slot(uri=OBSERVABLE.maxRunTime, name="maxRunTime", curie=OBSERVABLE.curie('maxRunTime'),
                   model_uri=MASTER.maxRunTime, domain=None, range=Optional[int])

slots.messageID = Slot(uri=OBSERVABLE.messageID, name="messageID", curie=OBSERVABLE.curie('messageID'),
                   model_uri=MASTER.messageID, domain=None, range=Optional[str])

slots.messageText = Slot(uri=OBSERVABLE.messageText, name="messageText", curie=OBSERVABLE.curie('messageText'),
                   model_uri=MASTER.messageText, domain=None, range=Optional[str])

slots.messageThread = Slot(uri=OBSERVABLE.messageThread, name="messageThread", curie=OBSERVABLE.curie('messageThread'),
                   model_uri=MASTER.messageThread, domain=None, range=Optional[Union[dict, Thread]])

slots.messageType = Slot(uri=OBSERVABLE.messageType, name="messageType", curie=OBSERVABLE.curie('messageType'),
                   model_uri=MASTER.messageType, domain=None, range=Optional[str])

slots.messagingAddress = Slot(uri=OBSERVABLE.messagingAddress, name="messagingAddress", curie=OBSERVABLE.curie('messagingAddress'),
                   model_uri=MASTER.messagingAddress, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.metadataChangeTime = Slot(uri=OBSERVABLE.metadataChangeTime, name="metadataChangeTime", curie=OBSERVABLE.curie('metadataChangeTime'),
                   model_uri=MASTER.metadataChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.metadataRecoveredStatus = Slot(uri=OBSERVABLE.metadataRecoveredStatus, name="metadataRecoveredStatus", curie=OBSERVABLE.curie('metadataRecoveredStatus'),
                   model_uri=MASTER.metadataRecoveredStatus, domain=None, range=Optional[str])

slots.mftFileID = Slot(uri=OBSERVABLE.mftFileID, name="mftFileID", curie=OBSERVABLE.curie('mftFileID'),
                   model_uri=MASTER.mftFileID, domain=None, range=Optional[int])

slots.mftFileNameAccessedTime = Slot(uri=OBSERVABLE.mftFileNameAccessedTime, name="mftFileNameAccessedTime", curie=OBSERVABLE.curie('mftFileNameAccessedTime'),
                   model_uri=MASTER.mftFileNameAccessedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFileNameCreatedTime = Slot(uri=OBSERVABLE.mftFileNameCreatedTime, name="mftFileNameCreatedTime", curie=OBSERVABLE.curie('mftFileNameCreatedTime'),
                   model_uri=MASTER.mftFileNameCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFileNameLength = Slot(uri=OBSERVABLE.mftFileNameLength, name="mftFileNameLength", curie=OBSERVABLE.curie('mftFileNameLength'),
                   model_uri=MASTER.mftFileNameLength, domain=None, range=Optional[int])

slots.mftFileNameModifiedTime = Slot(uri=OBSERVABLE.mftFileNameModifiedTime, name="mftFileNameModifiedTime", curie=OBSERVABLE.curie('mftFileNameModifiedTime'),
                   model_uri=MASTER.mftFileNameModifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFileNameRecordChangeTme = Slot(uri=OBSERVABLE.mftFileNameRecordChangeTme, name="mftFileNameRecordChangeTme", curie=OBSERVABLE.curie('mftFileNameRecordChangeTme'),
                   model_uri=MASTER.mftFileNameRecordChangeTme, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mftFlags = Slot(uri=OBSERVABLE.mftFlags, name="mftFlags", curie=OBSERVABLE.curie('mftFlags'),
                   model_uri=MASTER.mftFlags, domain=None, range=Optional[int])

slots.mftParentID = Slot(uri=OBSERVABLE.mftParentID, name="mftParentID", curie=OBSERVABLE.curie('mftParentID'),
                   model_uri=MASTER.mftParentID, domain=None, range=Optional[int])

slots.mftRecordChangeTime = Slot(uri=OBSERVABLE.mftRecordChangeTime, name="mftRecordChangeTime", curie=OBSERVABLE.curie('mftRecordChangeTime'),
                   model_uri=MASTER.mftRecordChangeTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.middleName = Slot(uri=OBSERVABLE.middleName, name="middleName", curie=OBSERVABLE.curie('middleName'),
                   model_uri=MASTER.middleName, domain=None, range=Optional[str])

slots.mimeClass = Slot(uri=OBSERVABLE.mimeClass, name="mimeClass", curie=OBSERVABLE.curie('mimeClass'),
                   model_uri=MASTER.mimeClass, domain=None, range=Optional[str])

slots.mimeType = Slot(uri=OBSERVABLE.mimeType, name="mimeType", curie=OBSERVABLE.curie('mimeType'),
                   model_uri=MASTER.mimeType, domain=None, range=Optional[str])

slots.minorImageVersion = Slot(uri=OBSERVABLE.minorImageVersion, name="minorImageVersion", curie=OBSERVABLE.curie('minorImageVersion'),
                   model_uri=MASTER.minorImageVersion, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.minorLinkerVersion = Slot(uri=OBSERVABLE.minorLinkerVersion, name="minorLinkerVersion", curie=OBSERVABLE.curie('minorLinkerVersion'),
                   model_uri=MASTER.minorLinkerVersion, domain=None, range=Optional[Union[int, ByteType]])

slots.minorOSVersion = Slot(uri=OBSERVABLE.minorOSVersion, name="minorOSVersion", curie=OBSERVABLE.curie('minorOSVersion'),
                   model_uri=MASTER.minorOSVersion, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.minorSubsystemVersion = Slot(uri=OBSERVABLE.minorSubsystemVersion, name="minorSubsystemVersion", curie=OBSERVABLE.curie('minorSubsystemVersion'),
                   model_uri=MASTER.minorSubsystemVersion, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.mockLocationsAllowed = Slot(uri=OBSERVABLE.mockLocationsAllowed, name="mockLocationsAllowed", curie=OBSERVABLE.curie('mockLocationsAllowed'),
                   model_uri=MASTER.mockLocationsAllowed, domain=None, range=Optional[Union[bool, BooleanType]])

slots.model = Slot(uri=OBSERVABLE.model, name="model", curie=OBSERVABLE.curie('model'),
                   model_uri=MASTER.model, domain=None, range=Optional[str])

slots.mostRecentRunTime = Slot(uri=OBSERVABLE.mostRecentRunTime, name="mostRecentRunTime", curie=OBSERVABLE.curie('mostRecentRunTime'),
                   model_uri=MASTER.mostRecentRunTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.mountPoint = Slot(uri=OBSERVABLE.mountPoint, name="mountPoint", curie=OBSERVABLE.curie('mountPoint'),
                   model_uri=MASTER.mountPoint, domain=None, range=Optional[str])

slots.msProductID = Slot(uri=OBSERVABLE.msProductID, name="msProductID", curie=OBSERVABLE.curie('msProductID'),
                   model_uri=MASTER.msProductID, domain=None, range=Optional[str])

slots.msProductName = Slot(uri=OBSERVABLE.msProductName, name="msProductName", curie=OBSERVABLE.curie('msProductName'),
                   model_uri=MASTER.msProductName, domain=None, range=Optional[str])

slots.mutexName = Slot(uri=OBSERVABLE.mutexName, name="mutexName", curie=OBSERVABLE.curie('mutexName'),
                   model_uri=MASTER.mutexName, domain=None, range=Optional[str])

slots.nameConstraints = Slot(uri=OBSERVABLE.nameConstraints, name="nameConstraints", curie=OBSERVABLE.curie('nameConstraints'),
                   model_uri=MASTER.nameConstraints, domain=None, range=Optional[str])

slots.namePhonetic = Slot(uri=OBSERVABLE.namePhonetic, name="namePhonetic", curie=OBSERVABLE.curie('namePhonetic'),
                   model_uri=MASTER.namePhonetic, domain=None, range=Optional[str])

slots.namePrefix = Slot(uri=OBSERVABLE.namePrefix, name="namePrefix", curie=OBSERVABLE.curie('namePrefix'),
                   model_uri=MASTER.namePrefix, domain=None, range=Optional[str])

slots.nameRecoveredStatus = Slot(uri=OBSERVABLE.nameRecoveredStatus, name="nameRecoveredStatus", curie=OBSERVABLE.curie('nameRecoveredStatus'),
                   model_uri=MASTER.nameRecoveredStatus, domain=None, range=Optional[str])

slots.nameServer = Slot(uri=OBSERVABLE.nameServer, name="nameServer", curie=OBSERVABLE.curie('nameServer'),
                   model_uri=MASTER.nameServer, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.nameSuffix = Slot(uri=OBSERVABLE.nameSuffix, name="nameSuffix", curie=OBSERVABLE.curie('nameSuffix'),
                   model_uri=MASTER.nameSuffix, domain=None, range=Optional[str])

slots.netBIOSName = Slot(uri=OBSERVABLE.netBIOSName, name="netBIOSName", curie=OBSERVABLE.curie('netBIOSName'),
                   model_uri=MASTER.netBIOSName, domain=None, range=Optional[str])

slots.network = Slot(uri=OBSERVABLE.network, name="network", curie=OBSERVABLE.curie('network'),
                   model_uri=MASTER.network, domain=None, range=Optional[str])

slots.networkInterface = Slot(uri=OBSERVABLE.networkInterface, name="networkInterface", curie=OBSERVABLE.curie('networkInterface'),
                   model_uri=MASTER.networkInterface, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.newObject = Slot(uri=OBSERVABLE.newObject, name="newObject", curie=OBSERVABLE.curie('newObject'),
                   model_uri=MASTER.newObject, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.nextRunTime = Slot(uri=OBSERVABLE.nextRunTime, name="nextRunTime", curie=OBSERVABLE.curie('nextRunTime'),
                   model_uri=MASTER.nextRunTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.nickname = Slot(uri=OBSERVABLE.nickname, name="nickname", curie=OBSERVABLE.curie('nickname'),
                   model_uri=MASTER.nickname, domain=None, range=Optional[str])

slots.ntfsHardLinkCount = Slot(uri=OBSERVABLE.ntfsHardLinkCount, name="ntfsHardLinkCount", curie=OBSERVABLE.curie('ntfsHardLinkCount'),
                   model_uri=MASTER.ntfsHardLinkCount, domain=None, range=Optional[int])

slots.ntfsOwnerID = Slot(uri=OBSERVABLE.ntfsOwnerID, name="ntfsOwnerID", curie=OBSERVABLE.curie('ntfsOwnerID'),
                   model_uri=MASTER.ntfsOwnerID, domain=None, range=Optional[str])

slots.ntfsOwnerSID = Slot(uri=OBSERVABLE.ntfsOwnerSID, name="ntfsOwnerSID", curie=OBSERVABLE.curie('ntfsOwnerSID'),
                   model_uri=MASTER.ntfsOwnerSID, domain=None, range=Optional[str])

slots.number = Slot(uri=OBSERVABLE.number, name="number", curie=OBSERVABLE.curie('number'),
                   model_uri=MASTER.number, domain=None, range=Optional[int])

slots.numberOfLaunches = Slot(uri=OBSERVABLE.numberOfLaunches, name="numberOfLaunches", curie=OBSERVABLE.curie('numberOfLaunches'),
                   model_uri=MASTER.numberOfLaunches, domain=None, range=Optional[int])

slots.numberOfRVAAndSizes = Slot(uri=OBSERVABLE.numberOfRVAAndSizes, name="numberOfRVAAndSizes", curie=OBSERVABLE.curie('numberOfRVAAndSizes'),
                   model_uri=MASTER.numberOfRVAAndSizes, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.numberOfSections = Slot(uri=OBSERVABLE.numberOfSections, name="numberOfSections", curie=OBSERVABLE.curie('numberOfSections'),
                   model_uri=MASTER.numberOfSections, domain=None, range=Optional[int])

slots.numberOfSubkeys = Slot(uri=OBSERVABLE.numberOfSubkeys, name="numberOfSubkeys", curie=OBSERVABLE.curie('numberOfSubkeys'),
                   model_uri=MASTER.numberOfSubkeys, domain=None, range=Optional[int])

slots.numberOfSymbols = Slot(uri=OBSERVABLE.numberOfSymbols, name="numberOfSymbols", curie=OBSERVABLE.curie('numberOfSymbols'),
                   model_uri=MASTER.numberOfSymbols, domain=None, range=Optional[int])

slots.numberTimesContacted = Slot(uri=OBSERVABLE.numberTimesContacted, name="numberTimesContacted", curie=OBSERVABLE.curie('numberTimesContacted'),
                   model_uri=MASTER.numberTimesContacted, domain=None, range=Optional[int])

slots.objectGUID = Slot(uri=OBSERVABLE.objectGUID, name="objectGUID", curie=OBSERVABLE.curie('objectGUID'),
                   model_uri=MASTER.objectGUID, domain=None, range=Optional[str])

slots.observableCreatedTime = Slot(uri=OBSERVABLE.observableCreatedTime, name="observableCreatedTime", curie=OBSERVABLE.curie('observableCreatedTime'),
                   model_uri=MASTER.observableCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.oldObject = Slot(uri=OBSERVABLE.oldObject, name="oldObject", curie=OBSERVABLE.curie('oldObject'),
                   model_uri=MASTER.oldObject, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.openFileDescriptor = Slot(uri=OBSERVABLE.openFileDescriptor, name="openFileDescriptor", curie=OBSERVABLE.curie('openFileDescriptor'),
                   model_uri=MASTER.openFileDescriptor, domain=None, range=Optional[int])

slots.operatingSystem = Slot(uri=OBSERVABLE.operatingSystem, name="operatingSystem", curie=OBSERVABLE.curie('operatingSystem'),
                   model_uri=MASTER.operatingSystem, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.optionalHeader = Slot(uri=OBSERVABLE.optionalHeader, name="optionalHeader", curie=OBSERVABLE.curie('optionalHeader'),
                   model_uri=MASTER.optionalHeader, domain=None, range=Optional[Union[dict, WindowsPEOptionalHeader]])

slots.options = Slot(uri=OBSERVABLE.options, name="options", curie=OBSERVABLE.curie('options'),
                   model_uri=MASTER.options, domain=None, range=Optional[str])

slots.organizationDepartment = Slot(uri=OBSERVABLE.organizationDepartment, name="organizationDepartment", curie=OBSERVABLE.curie('organizationDepartment'),
                   model_uri=MASTER.organizationDepartment, domain=None, range=Optional[str])

slots.organizationLocation = Slot(uri=OBSERVABLE.organizationLocation, name="organizationLocation", curie=OBSERVABLE.curie('organizationLocation'),
                   model_uri=MASTER.organizationLocation, domain=None, range=Optional[Union[dict, ContactAddress]])

slots.organizationPosition = Slot(uri=OBSERVABLE.organizationPosition, name="organizationPosition", curie=OBSERVABLE.curie('organizationPosition'),
                   model_uri=MASTER.organizationPosition, domain=None, range=Optional[str])

slots.osInstallDate = Slot(uri=OBSERVABLE.osInstallDate, name="osInstallDate", curie=OBSERVABLE.curie('osInstallDate'),
                   model_uri=MASTER.osInstallDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.osLastUpgradeDate = Slot(uri=OBSERVABLE.osLastUpgradeDate, name="osLastUpgradeDate", curie=OBSERVABLE.curie('osLastUpgradeDate'),
                   model_uri=MASTER.osLastUpgradeDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.otherHeaders = Slot(uri=OBSERVABLE.otherHeaders, name="otherHeaders", curie=OBSERVABLE.curie('otherHeaders'),
                   model_uri=MASTER.otherHeaders, domain=None, range=Optional[Union[dict, Dictionary]])

slots.owner = Slot(uri=OBSERVABLE.owner, name="owner", curie=OBSERVABLE.curie('owner'),
                   model_uri=MASTER.owner, domain=None, range=Optional[Union[dict, UcoObject]])

slots.ownerSID = Slot(uri=OBSERVABLE.ownerSID, name="ownerSID", curie=OBSERVABLE.curie('ownerSID'),
                   model_uri=MASTER.ownerSID, domain=None, range=Optional[str])

slots.pageTitle = Slot(uri=OBSERVABLE.pageTitle, name="pageTitle", curie=OBSERVABLE.curie('pageTitle'),
                   model_uri=MASTER.pageTitle, domain=None, range=Optional[str])

slots.parameterAddress = Slot(uri=OBSERVABLE.parameterAddress, name="parameterAddress", curie=OBSERVABLE.curie('parameterAddress'),
                   model_uri=MASTER.parameterAddress, domain=None, range=Optional[hex])

slots.parameters = Slot(uri=OBSERVABLE.parameters, name="parameters", curie=OBSERVABLE.curie('parameters'),
                   model_uri=MASTER.parameters, domain=None, range=Optional[str])

slots.parent = Slot(uri=OBSERVABLE.parent, name="parent", curie=OBSERVABLE.curie('parent'),
                   model_uri=MASTER.parent, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.partition = Slot(uri=OBSERVABLE.partition, name="partition", curie=OBSERVABLE.curie('partition'),
                   model_uri=MASTER.partition, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.partitionID = Slot(uri=OBSERVABLE.partitionID, name="partitionID", curie=OBSERVABLE.curie('partitionID'),
                   model_uri=MASTER.partitionID, domain=None, range=Optional[str])

slots.partitionLength = Slot(uri=OBSERVABLE.partitionLength, name="partitionLength", curie=OBSERVABLE.curie('partitionLength'),
                   model_uri=MASTER.partitionLength, domain=None, range=Optional[int])

slots.partitionOffset = Slot(uri=OBSERVABLE.partitionOffset, name="partitionOffset", curie=OBSERVABLE.curie('partitionOffset'),
                   model_uri=MASTER.partitionOffset, domain=None, range=Optional[int])

slots.password = Slot(uri=OBSERVABLE.password, name="password", curie=OBSERVABLE.curie('password'),
                   model_uri=MASTER.password, domain=None, range=Optional[str])

slots.passwordLastChanged = Slot(uri=OBSERVABLE.passwordLastChanged, name="passwordLastChanged", curie=OBSERVABLE.curie('passwordLastChanged'),
                   model_uri=MASTER.passwordLastChanged, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.passwordType = Slot(uri=OBSERVABLE.passwordType, name="passwordType", curie=OBSERVABLE.curie('passwordType'),
                   model_uri=MASTER.passwordType, domain=None, range=Optional[str])

slots.path = Slot(uri=OBSERVABLE.path, name="path", curie=OBSERVABLE.curie('path'),
                   model_uri=MASTER.path, domain=None, range=Optional[str])

slots.pdfCreationDate = Slot(uri=OBSERVABLE.pdfCreationDate, name="pdfCreationDate", curie=OBSERVABLE.curie('pdfCreationDate'),
                   model_uri=MASTER.pdfCreationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.pdfId0 = Slot(uri=OBSERVABLE.pdfId0, name="pdfId0", curie=OBSERVABLE.curie('pdfId0'),
                   model_uri=MASTER.pdfId0, domain=None, range=Optional[str])

slots.pdfId1 = Slot(uri=OBSERVABLE.pdfId1, name="pdfId1", curie=OBSERVABLE.curie('pdfId1'),
                   model_uri=MASTER.pdfId1, domain=None, range=Optional[str])

slots.pdfModDate = Slot(uri=OBSERVABLE.pdfModDate, name="pdfModDate", curie=OBSERVABLE.curie('pdfModDate'),
                   model_uri=MASTER.pdfModDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.peType = Slot(uri=OBSERVABLE.peType, name="peType", curie=OBSERVABLE.curie('peType'),
                   model_uri=MASTER.peType, domain=None, range=Optional[str])

slots.phoneActivationTime = Slot(uri=OBSERVABLE.phoneActivationTime, name="phoneActivationTime", curie=OBSERVABLE.curie('phoneActivationTime'),
                   model_uri=MASTER.phoneActivationTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.phoneNumber = Slot(uri=OBSERVABLE.phoneNumber, name="phoneNumber", curie=OBSERVABLE.curie('phoneNumber'),
                   model_uri=MASTER.phoneNumber, domain=None, range=Optional[str])

slots.pictureHeight = Slot(uri=OBSERVABLE.pictureHeight, name="pictureHeight", curie=OBSERVABLE.curie('pictureHeight'),
                   model_uri=MASTER.pictureHeight, domain=None, range=Optional[int])

slots.pictureType = Slot(uri=OBSERVABLE.pictureType, name="pictureType", curie=OBSERVABLE.curie('pictureType'),
                   model_uri=MASTER.pictureType, domain=None, range=Optional[str])

slots.pictureWidth = Slot(uri=OBSERVABLE.pictureWidth, name="pictureWidth", curie=OBSERVABLE.curie('pictureWidth'),
                   model_uri=MASTER.pictureWidth, domain=None, range=Optional[int])

slots.pid = Slot(uri=OBSERVABLE.pid, name="pid", curie=OBSERVABLE.curie('pid'),
                   model_uri=MASTER.pid, domain=None, range=Optional[int])

slots.pointerToSymbolTable = Slot(uri=OBSERVABLE.pointerToSymbolTable, name="pointerToSymbolTable", curie=OBSERVABLE.curie('pointerToSymbolTable'),
                   model_uri=MASTER.pointerToSymbolTable, domain=None, range=Optional[hex])

slots.policyConstraints = Slot(uri=OBSERVABLE.policyConstraints, name="policyConstraints", curie=OBSERVABLE.curie('policyConstraints'),
                   model_uri=MASTER.policyConstraints, domain=None, range=Optional[str])

slots.policyMappings = Slot(uri=OBSERVABLE.policyMappings, name="policyMappings", curie=OBSERVABLE.curie('policyMappings'),
                   model_uri=MASTER.policyMappings, domain=None, range=Optional[str])

slots.port = Slot(uri=OBSERVABLE.port, name="port", curie=OBSERVABLE.curie('port'),
                   model_uri=MASTER.port, domain=None, range=Optional[int])

slots.prefetchHash = Slot(uri=OBSERVABLE.prefetchHash, name="prefetchHash", curie=OBSERVABLE.curie('prefetchHash'),
                   model_uri=MASTER.prefetchHash, domain=None, range=Optional[str])

slots.priority = Slot(uri=OBSERVABLE.priority, name="priority", curie=OBSERVABLE.curie('priority'),
                   model_uri=MASTER.priority, domain=None, range=Optional[str])

slots.privateKeyUsagePeriodNotAfter = Slot(uri=OBSERVABLE.privateKeyUsagePeriodNotAfter, name="privateKeyUsagePeriodNotAfter", curie=OBSERVABLE.curie('privateKeyUsagePeriodNotAfter'),
                   model_uri=MASTER.privateKeyUsagePeriodNotAfter, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.privateKeyUsagePeriodNotBefore = Slot(uri=OBSERVABLE.privateKeyUsagePeriodNotBefore, name="privateKeyUsagePeriodNotBefore", curie=OBSERVABLE.curie('privateKeyUsagePeriodNotBefore'),
                   model_uri=MASTER.privateKeyUsagePeriodNotBefore, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.processorArchitecture = Slot(uri=OBSERVABLE.processorArchitecture, name="processorArchitecture", curie=OBSERVABLE.curie('processorArchitecture'),
                   model_uri=MASTER.processorArchitecture, domain=None, range=Optional[str])

slots.profile = Slot(uri=OBSERVABLE.profile, name="profile", curie=OBSERVABLE.curie('profile'),
                   model_uri=MASTER.profile, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.profileAccount = Slot(uri=OBSERVABLE.profileAccount, name="profileAccount", curie=OBSERVABLE.curie('profileAccount'),
                   model_uri=MASTER.profileAccount, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.profileBackgroundHash = Slot(uri=OBSERVABLE.profileBackgroundHash, name="profileBackgroundHash", curie=OBSERVABLE.curie('profileBackgroundHash'),
                   model_uri=MASTER.profileBackgroundHash, domain=None, range=Optional[Union[dict, Hash]])

slots.profileBackgroundLocation = Slot(uri=OBSERVABLE.profileBackgroundLocation, name="profileBackgroundLocation", curie=OBSERVABLE.curie('profileBackgroundLocation'),
                   model_uri=MASTER.profileBackgroundLocation, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.profileBannerHash = Slot(uri=OBSERVABLE.profileBannerHash, name="profileBannerHash", curie=OBSERVABLE.curie('profileBannerHash'),
                   model_uri=MASTER.profileBannerHash, domain=None, range=Optional[Union[dict, Hash]])

slots.profileBannerLocation = Slot(uri=OBSERVABLE.profileBannerLocation, name="profileBannerLocation", curie=OBSERVABLE.curie('profileBannerLocation'),
                   model_uri=MASTER.profileBannerLocation, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.profileCreated = Slot(uri=OBSERVABLE.profileCreated, name="profileCreated", curie=OBSERVABLE.curie('profileCreated'),
                   model_uri=MASTER.profileCreated, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.profileIdentity = Slot(uri=OBSERVABLE.profileIdentity, name="profileIdentity", curie=OBSERVABLE.curie('profileIdentity'),
                   model_uri=MASTER.profileIdentity, domain=None, range=Optional[Union[dict, Identity]])

slots.profileImageHash = Slot(uri=OBSERVABLE.profileImageHash, name="profileImageHash", curie=OBSERVABLE.curie('profileImageHash'),
                   model_uri=MASTER.profileImageHash, domain=None, range=Optional[Union[dict, Hash]])

slots.profileImageLocation = Slot(uri=OBSERVABLE.profileImageLocation, name="profileImageLocation", curie=OBSERVABLE.curie('profileImageLocation'),
                   model_uri=MASTER.profileImageLocation, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.profileIsProtected = Slot(uri=OBSERVABLE.profileIsProtected, name="profileIsProtected", curie=OBSERVABLE.curie('profileIsProtected'),
                   model_uri=MASTER.profileIsProtected, domain=None, range=Optional[Union[bool, BooleanType]])

slots.profileIsVerified = Slot(uri=OBSERVABLE.profileIsVerified, name="profileIsVerified", curie=OBSERVABLE.curie('profileIsVerified'),
                   model_uri=MASTER.profileIsVerified, domain=None, range=Optional[Union[bool, BooleanType]])

slots.profileLanguage = Slot(uri=OBSERVABLE.profileLanguage, name="profileLanguage", curie=OBSERVABLE.curie('profileLanguage'),
                   model_uri=MASTER.profileLanguage, domain=None, range=Optional[str])

slots.profileService = Slot(uri=OBSERVABLE.profileService, name="profileService", curie=OBSERVABLE.curie('profileService'),
                   model_uri=MASTER.profileService, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.profileWebsite = Slot(uri=OBSERVABLE.profileWebsite, name="profileWebsite", curie=OBSERVABLE.curie('profileWebsite'),
                   model_uri=MASTER.profileWebsite, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.properties = Slot(uri=OBSERVABLE.properties, name="properties", curie=OBSERVABLE.curie('properties'),
                   model_uri=MASTER.properties, domain=None, range=Optional[str])

slots.propertyName = Slot(uri=OBSERVABLE.propertyName, name="propertyName", curie=OBSERVABLE.curie('propertyName'),
                   model_uri=MASTER.propertyName, domain=None, range=Optional[str])

slots.protocols = Slot(uri=OBSERVABLE.protocols, name="protocols", curie=OBSERVABLE.curie('protocols'),
                   model_uri=MASTER.protocols, domain=None, range=Optional[Union[dict, ControlledDictionary]])

slots.query = Slot(uri=OBSERVABLE.query, name="query", curie=OBSERVABLE.curie('query'),
                   model_uri=MASTER.query, domain=None, range=Optional[str])

slots.rangeOffset = Slot(uri=OBSERVABLE.rangeOffset, name="rangeOffset", curie=OBSERVABLE.curie('rangeOffset'),
                   model_uri=MASTER.rangeOffset, domain=None, range=Optional[int])

slots.rangeOffsetType = Slot(uri=OBSERVABLE.rangeOffsetType, name="rangeOffsetType", curie=OBSERVABLE.curie('rangeOffsetType'),
                   model_uri=MASTER.rangeOffsetType, domain=None, range=Optional[str])

slots.rangeSize = Slot(uri=OBSERVABLE.rangeSize, name="rangeSize", curie=OBSERVABLE.curie('rangeSize'),
                   model_uri=MASTER.rangeSize, domain=None, range=Optional[int])

slots.receivedLines = Slot(uri=OBSERVABLE.receivedLines, name="receivedLines", curie=OBSERVABLE.curie('receivedLines'),
                   model_uri=MASTER.receivedLines, domain=None, range=Optional[str])

slots.receivedTime = Slot(uri=OBSERVABLE.receivedTime, name="receivedTime", curie=OBSERVABLE.curie('receivedTime'),
                   model_uri=MASTER.receivedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.recordFieldIsNull = Slot(uri=OBSERVABLE.recordFieldIsNull, name="recordFieldIsNull", curie=OBSERVABLE.curie('recordFieldIsNull'),
                   model_uri=MASTER.recordFieldIsNull, domain=None, range=Optional[Union[bool, BooleanType]])

slots.recordFieldName = Slot(uri=OBSERVABLE.recordFieldName, name="recordFieldName", curie=OBSERVABLE.curie('recordFieldName'),
                   model_uri=MASTER.recordFieldName, domain=None, range=Optional[str])

slots.recordFieldValue = Slot(uri=OBSERVABLE.recordFieldValue, name="recordFieldValue", curie=OBSERVABLE.curie('recordFieldValue'),
                   model_uri=MASTER.recordFieldValue, domain=None, range=Optional[str])

slots.recordRowID = Slot(uri=OBSERVABLE.recordRowID, name="recordRowID", curie=OBSERVABLE.curie('recordRowID'),
                   model_uri=MASTER.recordRowID, domain=None, range=Optional[str])

slots.recurrence = Slot(uri=OBSERVABLE.recurrence, name="recurrence", curie=OBSERVABLE.curie('recurrence'),
                   model_uri=MASTER.recurrence, domain=None, range=Optional[str])

slots.references = Slot(uri=OBSERVABLE.references, name="references", curie=OBSERVABLE.curie('references'),
                   model_uri=MASTER.references, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.referralURL = Slot(uri=OBSERVABLE.referralURL, name="referralURL", curie=OBSERVABLE.curie('referralURL'),
                   model_uri=MASTER.referralURL, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.referrerURL = Slot(uri=OBSERVABLE.referrerURL, name="referrerURL", curie=OBSERVABLE.curie('referrerURL'),
                   model_uri=MASTER.referrerURL, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.regionEndAddress = Slot(uri=OBSERVABLE.regionEndAddress, name="regionEndAddress", curie=OBSERVABLE.curie('regionEndAddress'),
                   model_uri=MASTER.regionEndAddress, domain=None, range=Optional[hex])

slots.regionSize = Slot(uri=OBSERVABLE.regionSize, name="regionSize", curie=OBSERVABLE.curie('regionSize'),
                   model_uri=MASTER.regionSize, domain=None, range=Optional[int])

slots.regionStartAddress = Slot(uri=OBSERVABLE.regionStartAddress, name="regionStartAddress", curie=OBSERVABLE.curie('regionStartAddress'),
                   model_uri=MASTER.regionStartAddress, domain=None, range=Optional[hex])

slots.regionalInternetRegistry = Slot(uri=OBSERVABLE.regionalInternetRegistry, name="regionalInternetRegistry", curie=OBSERVABLE.curie('regionalInternetRegistry'),
                   model_uri=MASTER.regionalInternetRegistry, domain=None, range=Optional[str])

slots.registeredOrganization = Slot(uri=OBSERVABLE.registeredOrganization, name="registeredOrganization", curie=OBSERVABLE.curie('registeredOrganization'),
                   model_uri=MASTER.registeredOrganization, domain=None, range=Optional[Union[dict, Identity]])

slots.registeredOwner = Slot(uri=OBSERVABLE.registeredOwner, name="registeredOwner", curie=OBSERVABLE.curie('registeredOwner'),
                   model_uri=MASTER.registeredOwner, domain=None, range=Optional[Union[dict, Identity]])

slots.registrantContactInfo = Slot(uri=OBSERVABLE.registrantContactInfo, name="registrantContactInfo", curie=OBSERVABLE.curie('registrantContactInfo'),
                   model_uri=MASTER.registrantContactInfo, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.registrantIDs = Slot(uri=OBSERVABLE.registrantIDs, name="registrantIDs", curie=OBSERVABLE.curie('registrantIDs'),
                   model_uri=MASTER.registrantIDs, domain=None, range=Optional[str])

slots.registrarGUID = Slot(uri=OBSERVABLE.registrarGUID, name="registrarGUID", curie=OBSERVABLE.curie('registrarGUID'),
                   model_uri=MASTER.registrarGUID, domain=None, range=Optional[str])

slots.registrarID = Slot(uri=OBSERVABLE.registrarID, name="registrarID", curie=OBSERVABLE.curie('registrarID'),
                   model_uri=MASTER.registrarID, domain=None, range=Optional[str])

slots.registrarInfo = Slot(uri=OBSERVABLE.registrarInfo, name="registrarInfo", curie=OBSERVABLE.curie('registrarInfo'),
                   model_uri=MASTER.registrarInfo, domain=None, range=Optional[Union[dict, WhoisRegistrarInfoType]])

slots.registrarName = Slot(uri=OBSERVABLE.registrarName, name="registrarName", curie=OBSERVABLE.curie('registrarName'),
                   model_uri=MASTER.registrarName, domain=None, range=Optional[str])

slots.registryValues = Slot(uri=OBSERVABLE.registryValues, name="registryValues", curie=OBSERVABLE.curie('registryValues'),
                   model_uri=MASTER.registryValues, domain=None, range=Optional[Union[dict, WindowsRegistryValue]])

slots.remarks = Slot(uri=OBSERVABLE.remarks, name="remarks", curie=OBSERVABLE.curie('remarks'),
                   model_uri=MASTER.remarks, domain=None, range=Optional[str])

slots.remindTime = Slot(uri=OBSERVABLE.remindTime, name="remindTime", curie=OBSERVABLE.curie('remindTime'),
                   model_uri=MASTER.remindTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.requestMethod = Slot(uri=OBSERVABLE.requestMethod, name="requestMethod", curie=OBSERVABLE.curie('requestMethod'),
                   model_uri=MASTER.requestMethod, domain=None, range=Optional[str])

slots.requestValue = Slot(uri=OBSERVABLE.requestValue, name="requestValue", curie=OBSERVABLE.curie('requestValue'),
                   model_uri=MASTER.requestValue, domain=None, range=Optional[str])

slots.requestVersion = Slot(uri=OBSERVABLE.requestVersion, name="requestVersion", curie=OBSERVABLE.curie('requestVersion'),
                   model_uri=MASTER.requestVersion, domain=None, range=Optional[str])

slots.rowCondition = Slot(uri=OBSERVABLE.rowCondition, name="rowCondition", curie=OBSERVABLE.curie('rowCondition'),
                   model_uri=MASTER.rowCondition, domain=None, range=Optional[str])

slots.rowIndex = Slot(uri=OBSERVABLE.rowIndex, name="rowIndex", curie=OBSERVABLE.curie('rowIndex'),
                   model_uri=MASTER.rowIndex, domain=None, range=Optional[Union[int, PositiveIntegerType]])

slots.ruid = Slot(uri=OBSERVABLE.ruid, name="ruid", curie=OBSERVABLE.curie('ruid'),
                   model_uri=MASTER.ruid, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.runningStatus = Slot(uri=OBSERVABLE.runningStatus, name="runningStatus", curie=OBSERVABLE.curie('runningStatus'),
                   model_uri=MASTER.runningStatus, domain=None, range=Optional[str])

slots.scheme = Slot(uri=OBSERVABLE.scheme, name="scheme", curie=OBSERVABLE.curie('scheme'),
                   model_uri=MASTER.scheme, domain=None, range=Optional[str])

slots.sectionAlignment = Slot(uri=OBSERVABLE.sectionAlignment, name="sectionAlignment", curie=OBSERVABLE.curie('sectionAlignment'),
                   model_uri=MASTER.sectionAlignment, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sections = Slot(uri=OBSERVABLE.sections, name="sections", curie=OBSERVABLE.curie('sections'),
                   model_uri=MASTER.sections, domain=None, range=Optional[Union[dict, WindowsPESection]])

slots.sectorSize = Slot(uri=OBSERVABLE.sectorSize, name="sectorSize", curie=OBSERVABLE.curie('sectorSize'),
                   model_uri=MASTER.sectorSize, domain=None, range=Optional[int])

slots.securityAttributes = Slot(uri=OBSERVABLE.securityAttributes, name="securityAttributes", curie=OBSERVABLE.curie('securityAttributes'),
                   model_uri=MASTER.securityAttributes, domain=None, range=Optional[str])

slots.sender = Slot(uri=OBSERVABLE.sender, name="sender", curie=OBSERVABLE.curie('sender'),
                   model_uri=MASTER.sender, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.sentTime = Slot(uri=OBSERVABLE.sentTime, name="sentTime", curie=OBSERVABLE.curie('sentTime'),
                   model_uri=MASTER.sentTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.serialNumber = Slot(uri=OBSERVABLE.serialNumber, name="serialNumber", curie=OBSERVABLE.curie('serialNumber'),
                   model_uri=MASTER.serialNumber, domain=None, range=Optional[str])

slots.serverName = Slot(uri=OBSERVABLE.serverName, name="serverName", curie=OBSERVABLE.curie('serverName'),
                   model_uri=MASTER.serverName, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.serviceName = Slot(uri=OBSERVABLE.serviceName, name="serviceName", curie=OBSERVABLE.curie('serviceName'),
                   model_uri=MASTER.serviceName, domain=None, range=Optional[str])

slots.servicStatus = Slot(uri=OBSERVABLE.servicStatus, name="servicStatus", curie=OBSERVABLE.curie('servicStatus'),
                   model_uri=MASTER.servicStatus, domain=None, range=Optional[str])

slots.serviceType = Slot(uri=OBSERVABLE.serviceType, name="serviceType", curie=OBSERVABLE.curie('serviceType'),
                   model_uri=MASTER.serviceType, domain=None, range=Optional[str])

slots.sessionID = Slot(uri=OBSERVABLE.sessionID, name="sessionID", curie=OBSERVABLE.curie('sessionID'),
                   model_uri=MASTER.sessionID, domain=None, range=Optional[str])

slots.shell = Slot(uri=OBSERVABLE.shell, name="shell", curie=OBSERVABLE.curie('shell'),
                   model_uri=MASTER.shell, domain=None, range=Optional[str])

slots.showMessageBody = Slot(uri=OBSERVABLE.showMessageBody, name="showMessageBody", curie=OBSERVABLE.curie('showMessageBody'),
                   model_uri=MASTER.showMessageBody, domain=None, range=Optional[str])

slots.showMessageTitle = Slot(uri=OBSERVABLE.showMessageTitle, name="showMessageTitle", curie=OBSERVABLE.curie('showMessageTitle'),
                   model_uri=MASTER.showMessageTitle, domain=None, range=Optional[str])

slots.sid = Slot(uri=OBSERVABLE.sid, name="sid", curie=OBSERVABLE.curie('sid'),
                   model_uri=MASTER.sid, domain=None, range=Optional[str])

slots.signalStrength = Slot(uri=OBSERVABLE.signalStrength, name="signalStrength", curie=OBSERVABLE.curie('signalStrength'),
                   model_uri=MASTER.signalStrength, domain=None, range=Optional[str])

slots.signature = Slot(uri=OBSERVABLE.signature, name="signature", curie=OBSERVABLE.curie('signature'),
                   model_uri=MASTER.signature, domain=None, range=Optional[str])

slots.signatureAlgorithm = Slot(uri=OBSERVABLE.signatureAlgorithm, name="signatureAlgorithm", curie=OBSERVABLE.curie('signatureAlgorithm'),
                   model_uri=MASTER.signatureAlgorithm, domain=None, range=Optional[str])

slots.signatureDescription = Slot(uri=OBSERVABLE.signatureDescription, name="signatureDescription", curie=OBSERVABLE.curie('signatureDescription'),
                   model_uri=MASTER.signatureDescription, domain=None, range=Optional[str])

slots.signatureExists = Slot(uri=OBSERVABLE.signatureExists, name="signatureExists", curie=OBSERVABLE.curie('signatureExists'),
                   model_uri=MASTER.signatureExists, domain=None, range=Optional[Union[bool, BooleanType]])

slots.signatureVerified = Slot(uri=OBSERVABLE.signatureVerified, name="signatureVerified", curie=OBSERVABLE.curie('signatureVerified'),
                   model_uri=MASTER.signatureVerified, domain=None, range=Optional[Union[bool, BooleanType]])

slots.sipAddress = Slot(uri=OBSERVABLE.sipAddress, name="sipAddress", curie=OBSERVABLE.curie('sipAddress'),
                   model_uri=MASTER.sipAddress, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.obSize = Slot(uri=OBSERVABLE.obSize, name="obSize", curie=OBSERVABLE.curie('obSize'),
                   model_uri=MASTER.obSize, domain=None, range=Optional[int])

slots.sizeInBytes = Slot(uri=OBSERVABLE.sizeInBytes, name="sizeInBytes", curie=OBSERVABLE.curie('sizeInBytes'),
                   model_uri=MASTER.sizeInBytes, domain=None, range=Optional[int])

slots.sizeOfCode = Slot(uri=OBSERVABLE.sizeOfCode, name="sizeOfCode", curie=OBSERVABLE.curie('sizeOfCode'),
                   model_uri=MASTER.sizeOfCode, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfHeaders = Slot(uri=OBSERVABLE.sizeOfHeaders, name="sizeOfHeaders", curie=OBSERVABLE.curie('sizeOfHeaders'),
                   model_uri=MASTER.sizeOfHeaders, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfHeapCommit = Slot(uri=OBSERVABLE.sizeOfHeapCommit, name="sizeOfHeapCommit", curie=OBSERVABLE.curie('sizeOfHeapCommit'),
                   model_uri=MASTER.sizeOfHeapCommit, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfHeapReserve = Slot(uri=OBSERVABLE.sizeOfHeapReserve, name="sizeOfHeapReserve", curie=OBSERVABLE.curie('sizeOfHeapReserve'),
                   model_uri=MASTER.sizeOfHeapReserve, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfImage = Slot(uri=OBSERVABLE.sizeOfImage, name="sizeOfImage", curie=OBSERVABLE.curie('sizeOfImage'),
                   model_uri=MASTER.sizeOfImage, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfInitializedData = Slot(uri=OBSERVABLE.sizeOfInitializedData, name="sizeOfInitializedData", curie=OBSERVABLE.curie('sizeOfInitializedData'),
                   model_uri=MASTER.sizeOfInitializedData, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfOptionalHeader = Slot(uri=OBSERVABLE.sizeOfOptionalHeader, name="sizeOfOptionalHeader", curie=OBSERVABLE.curie('sizeOfOptionalHeader'),
                   model_uri=MASTER.sizeOfOptionalHeader, domain=None, range=Optional[int])

slots.sizeOfStackCommit = Slot(uri=OBSERVABLE.sizeOfStackCommit, name="sizeOfStackCommit", curie=OBSERVABLE.curie('sizeOfStackCommit'),
                   model_uri=MASTER.sizeOfStackCommit, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfStackReserve = Slot(uri=OBSERVABLE.sizeOfStackReserve, name="sizeOfStackReserve", curie=OBSERVABLE.curie('sizeOfStackReserve'),
                   model_uri=MASTER.sizeOfStackReserve, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.sizeOfUninitializedData = Slot(uri=OBSERVABLE.sizeOfUninitializedData, name="sizeOfUninitializedData", curie=OBSERVABLE.curie('sizeOfUninitializedData'),
                   model_uri=MASTER.sizeOfUninitializedData, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.skew = Slot(uri=OBSERVABLE.skew, name="skew", curie=OBSERVABLE.curie('skew'),
                   model_uri=MASTER.skew, domain=None, range=Optional[Union[Decimal, DecimalType]])

slots.sourceApplication = Slot(uri=OBSERVABLE.sourceApplication, name="sourceApplication", curie=OBSERVABLE.curie('sourceApplication'),
                   model_uri=MASTER.sourceApplication, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.sourceFlags = Slot(uri=OBSERVABLE.sourceFlags, name="sourceFlags", curie=OBSERVABLE.curie('sourceFlags'),
                   model_uri=MASTER.sourceFlags, domain=None, range=Optional[hex])

slots.sourcePort = Slot(uri=OBSERVABLE.sourcePort, name="sourcePort", curie=OBSERVABLE.curie('sourcePort'),
                   model_uri=MASTER.sourcePort, domain=None, range=Optional[int])

slots.spaceLeft = Slot(uri=OBSERVABLE.spaceLeft, name="spaceLeft", curie=OBSERVABLE.curie('spaceLeft'),
                   model_uri=MASTER.spaceLeft, domain=None, range=Optional[int])

slots.spaceUsed = Slot(uri=OBSERVABLE.spaceUsed, name="spaceUsed", curie=OBSERVABLE.curie('spaceUsed'),
                   model_uri=MASTER.spaceUsed, domain=None, range=Optional[int])

slots.sponsoringRegistrar = Slot(uri=OBSERVABLE.sponsoringRegistrar, name="sponsoringRegistrar", curie=OBSERVABLE.curie('sponsoringRegistrar'),
                   model_uri=MASTER.sponsoringRegistrar, domain=None, range=Optional[str])

slots.src = Slot(uri=OBSERVABLE.src, name="src", curie=OBSERVABLE.curie('src'),
                   model_uri=MASTER.src, domain=None, range=Optional[Union[dict, UcoObject]])

slots.srcBytes = Slot(uri=OBSERVABLE.srcBytes, name="srcBytes", curie=OBSERVABLE.curie('srcBytes'),
                   model_uri=MASTER.srcBytes, domain=None, range=Optional[int])

slots.srcPackets = Slot(uri=OBSERVABLE.srcPackets, name="srcPackets", curie=OBSERVABLE.curie('srcPackets'),
                   model_uri=MASTER.srcPackets, domain=None, range=Optional[int])

slots.srcPayload = Slot(uri=OBSERVABLE.srcPayload, name="srcPayload", curie=OBSERVABLE.curie('srcPayload'),
                   model_uri=MASTER.srcPayload, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.ssid = Slot(uri=OBSERVABLE.ssid, name="ssid", curie=OBSERVABLE.curie('ssid'),
                   model_uri=MASTER.ssid, domain=None, range=Optional[str])

slots.stackSize = Slot(uri=OBSERVABLE.stackSize, name="stackSize", curie=OBSERVABLE.curie('stackSize'),
                   model_uri=MASTER.stackSize, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.startAddress = Slot(uri=OBSERVABLE.startAddress, name="startAddress", curie=OBSERVABLE.curie('startAddress'),
                   model_uri=MASTER.startAddress, domain=None, range=Optional[hex])

slots.startCommandLine = Slot(uri=OBSERVABLE.startCommandLine, name="startCommandLine", curie=OBSERVABLE.curie('startCommandLine'),
                   model_uri=MASTER.startCommandLine, domain=None, range=Optional[str])

slots.startType = Slot(uri=OBSERVABLE.startType, name="startType", curie=OBSERVABLE.curie('startType'),
                   model_uri=MASTER.startType, domain=None, range=Optional[str])

slots.startupInfo = Slot(uri=OBSERVABLE.startupInfo, name="startupInfo", curie=OBSERVABLE.curie('startupInfo'),
                   model_uri=MASTER.startupInfo, domain=None, range=Optional[Union[dict, Dictionary]])

slots.state = Slot(uri=OBSERVABLE.state, name="state", curie=OBSERVABLE.curie('state'),
                   model_uri=MASTER.state, domain=None, range=Optional[str])

slots.status = Slot(uri=OBSERVABLE.status, name="status", curie=OBSERVABLE.curie('status'),
                   model_uri=MASTER.status, domain=None, range=Optional[str])

slots.statusesCount = Slot(uri=OBSERVABLE.statusesCount, name="statusesCount", curie=OBSERVABLE.curie('statusesCount'),
                   model_uri=MASTER.statusesCount, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.storageCapacityInBytes = Slot(uri=OBSERVABLE.storageCapacityInBytes, name="storageCapacityInBytes", curie=OBSERVABLE.curie('storageCapacityInBytes'),
                   model_uri=MASTER.storageCapacityInBytes, domain=None, range=Optional[int])

slots.stringValue = Slot(uri=OBSERVABLE.stringValue, name="stringValue", curie=OBSERVABLE.curie('stringValue'),
                   model_uri=MASTER.stringValue, domain=None, range=Optional[str])

slots.strings = Slot(uri=OBSERVABLE.strings, name="strings", curie=OBSERVABLE.curie('strings'),
                   model_uri=MASTER.strings, domain=None, range=Optional[Union[dict, ExtractedString]])

slots.subject = Slot(uri=OBSERVABLE.subject, name="subject", curie=OBSERVABLE.curie('subject'),
                   model_uri=MASTER.subject, domain=None, range=Optional[str])

slots.subjectAlternativeName = Slot(uri=OBSERVABLE.subjectAlternativeName, name="subjectAlternativeName", curie=OBSERVABLE.curie('subjectAlternativeName'),
                   model_uri=MASTER.subjectAlternativeName, domain=None, range=Optional[str])

slots.subjectDirectoryAttributes = Slot(uri=OBSERVABLE.subjectDirectoryAttributes, name="subjectDirectoryAttributes", curie=OBSERVABLE.curie('subjectDirectoryAttributes'),
                   model_uri=MASTER.subjectDirectoryAttributes, domain=None, range=Optional[str])

slots.subjectHash = Slot(uri=OBSERVABLE.subjectHash, name="subjectHash", curie=OBSERVABLE.curie('subjectHash'),
                   model_uri=MASTER.subjectHash, domain=None, range=Optional[Union[dict, Hash]])

slots.subjectKeyIdentifier = Slot(uri=OBSERVABLE.subjectKeyIdentifier, name="subjectKeyIdentifier", curie=OBSERVABLE.curie('subjectKeyIdentifier'),
                   model_uri=MASTER.subjectKeyIdentifier, domain=None, range=Optional[str])

slots.subjectPublicKeyAlgorithm = Slot(uri=OBSERVABLE.subjectPublicKeyAlgorithm, name="subjectPublicKeyAlgorithm", curie=OBSERVABLE.curie('subjectPublicKeyAlgorithm'),
                   model_uri=MASTER.subjectPublicKeyAlgorithm, domain=None, range=Optional[str])

slots.subjectPublicKeyExponent = Slot(uri=OBSERVABLE.subjectPublicKeyExponent, name="subjectPublicKeyExponent", curie=OBSERVABLE.curie('subjectPublicKeyExponent'),
                   model_uri=MASTER.subjectPublicKeyExponent, domain=None, range=Optional[int])

slots.subjectPublicKeyModulus = Slot(uri=OBSERVABLE.subjectPublicKeyModulus, name="subjectPublicKeyModulus", curie=OBSERVABLE.curie('subjectPublicKeyModulus'),
                   model_uri=MASTER.subjectPublicKeyModulus, domain=None, range=Optional[str])

slots.subsystem = Slot(uri=OBSERVABLE.subsystem, name="subsystem", curie=OBSERVABLE.curie('subsystem'),
                   model_uri=MASTER.subsystem, domain=None, range=Optional[Union[int, UnsignedShortType]])

slots.swid = Slot(uri=OBSERVABLE.swid, name="swid", curie=OBSERVABLE.curie('swid'),
                   model_uri=MASTER.swid, domain=None, range=Optional[str])

slots.symbolicName = Slot(uri=OBSERVABLE.symbolicName, name="symbolicName", curie=OBSERVABLE.curie('symbolicName'),
                   model_uri=MASTER.symbolicName, domain=None, range=Optional[str])

slots.systemTime = Slot(uri=OBSERVABLE.systemTime, name="systemTime", curie=OBSERVABLE.curie('systemTime'),
                   model_uri=MASTER.systemTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.tableName = Slot(uri=OBSERVABLE.tableName, name="tableName", curie=OBSERVABLE.curie('tableName'),
                   model_uri=MASTER.tableName, domain=None, range=Optional[str])

slots.tableSchema = Slot(uri=OBSERVABLE.tableSchema, name="tableSchema", curie=OBSERVABLE.curie('tableSchema'),
                   model_uri=MASTER.tableSchema, domain=None, range=Optional[str])

slots.targetFile = Slot(uri=OBSERVABLE.targetFile, name="targetFile", curie=OBSERVABLE.curie('targetFile'),
                   model_uri=MASTER.targetFile, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.taskComment = Slot(uri=OBSERVABLE.taskComment, name="taskComment", curie=OBSERVABLE.curie('taskComment'),
                   model_uri=MASTER.taskComment, domain=None, range=Optional[str])

slots.taskCreator = Slot(uri=OBSERVABLE.taskCreator, name="taskCreator", curie=OBSERVABLE.curie('taskCreator'),
                   model_uri=MASTER.taskCreator, domain=None, range=Optional[str])

slots.text = Slot(uri=OBSERVABLE.text, name="text", curie=OBSERVABLE.curie('text'),
                   model_uri=MASTER.text, domain=None, range=Optional[str])

slots.threadID = Slot(uri=OBSERVABLE.threadID, name="threadID", curie=OBSERVABLE.curie('threadID'),
                   model_uri=MASTER.threadID, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.thumbprintHash = Slot(uri=OBSERVABLE.thumbprintHash, name="thumbprintHash", curie=OBSERVABLE.curie('thumbprintHash'),
                   model_uri=MASTER.thumbprintHash, domain=None, range=Optional[Union[dict, Hash]])

slots.timeDateStamp = Slot(uri=OBSERVABLE.timeDateStamp, name="timeDateStamp", curie=OBSERVABLE.curie('timeDateStamp'),
                   model_uri=MASTER.timeDateStamp, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.timesExecuted = Slot(uri=OBSERVABLE.timesExecuted, name="timesExecuted", curie=OBSERVABLE.curie('timesExecuted'),
                   model_uri=MASTER.timesExecuted, domain=None, range=Optional[int])

slots.timezoneDST = Slot(uri=OBSERVABLE.timezoneDST, name="timezoneDST", curie=OBSERVABLE.curie('timezoneDST'),
                   model_uri=MASTER.timezoneDST, domain=None, range=Optional[str])

slots.timezoneStandard = Slot(uri=OBSERVABLE.timezoneStandard, name="timezoneStandard", curie=OBSERVABLE.curie('timezoneStandard'),
                   model_uri=MASTER.timezoneStandard, domain=None, range=Optional[str])

slots.to = Slot(uri=OBSERVABLE.to, name="to", curie=OBSERVABLE.curie('to'),
                   model_uri=MASTER.to, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.totalFragments = Slot(uri=OBSERVABLE.totalFragments, name="totalFragments", curie=OBSERVABLE.curie('totalFragments'),
                   model_uri=MASTER.totalFragments, domain=None, range=Optional[int])

slots.totalRam = Slot(uri=OBSERVABLE.totalRam, name="totalRam", curie=OBSERVABLE.curie('totalRam'),
                   model_uri=MASTER.totalRam, domain=None, range=Optional[int])

slots.totalSpace = Slot(uri=OBSERVABLE.totalSpace, name="totalSpace", curie=OBSERVABLE.curie('totalSpace'),
                   model_uri=MASTER.totalSpace, domain=None, range=Optional[int])

slots.triggerBeginTime = Slot(uri=OBSERVABLE.triggerBeginTime, name="triggerBeginTime", curie=OBSERVABLE.curie('triggerBeginTime'),
                   model_uri=MASTER.triggerBeginTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.triggerDelay = Slot(uri=OBSERVABLE.triggerDelay, name="triggerDelay", curie=OBSERVABLE.curie('triggerDelay'),
                   model_uri=MASTER.triggerDelay, domain=None, range=Optional[str])

slots.triggerEndTime = Slot(uri=OBSERVABLE.triggerEndTime, name="triggerEndTime", curie=OBSERVABLE.curie('triggerEndTime'),
                   model_uri=MASTER.triggerEndTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.triggerFrequency = Slot(uri=OBSERVABLE.triggerFrequency, name="triggerFrequency", curie=OBSERVABLE.curie('triggerFrequency'),
                   model_uri=MASTER.triggerFrequency, domain=None, range=Optional[str])

slots.triggerList = Slot(uri=OBSERVABLE.triggerList, name="triggerList", curie=OBSERVABLE.curie('triggerList'),
                   model_uri=MASTER.triggerList, domain=None, range=Optional[str])

slots.triggerMaxRunTime = Slot(uri=OBSERVABLE.triggerMaxRunTime, name="triggerMaxRunTime", curie=OBSERVABLE.curie('triggerMaxRunTime'),
                   model_uri=MASTER.triggerMaxRunTime, domain=None, range=Optional[str])

slots.triggerSessionChangeType = Slot(uri=OBSERVABLE.triggerSessionChangeType, name="triggerSessionChangeType", curie=OBSERVABLE.curie('triggerSessionChangeType'),
                   model_uri=MASTER.triggerSessionChangeType, domain=None, range=Optional[str])

slots.triggerType = Slot(uri=OBSERVABLE.triggerType, name="triggerType", curie=OBSERVABLE.curie('triggerType'),
                   model_uri=MASTER.triggerType, domain=None, range=Optional[str])

slots.twitterHandle = Slot(uri=OBSERVABLE.twitterHandle, name="twitterHandle", curie=OBSERVABLE.curie('twitterHandle'),
                   model_uri=MASTER.twitterHandle, domain=None, range=Optional[str])

slots.twitterId = Slot(uri=OBSERVABLE.twitterId, name="twitterId", curie=OBSERVABLE.curie('twitterId'),
                   model_uri=MASTER.twitterId, domain=None, range=Optional[str])

slots.uninstallDate = Slot(uri=OBSERVABLE.uninstallDate, name="uninstallDate", curie=OBSERVABLE.curie('uninstallDate'),
                   model_uri=MASTER.uninstallDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.updatedDate = Slot(uri=OBSERVABLE.updatedDate, name="updatedDate", curie=OBSERVABLE.curie('updatedDate'),
                   model_uri=MASTER.updatedDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.uptime = Slot(uri=OBSERVABLE.uptime, name="uptime", curie=OBSERVABLE.curie('uptime'),
                   model_uri=MASTER.uptime, domain=None, range=Optional[str])

slots.url = Slot(uri=OBSERVABLE.url, name="url", curie=OBSERVABLE.curie('url'),
                   model_uri=MASTER.url, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.urlHistoryEntry = Slot(uri=OBSERVABLE.urlHistoryEntry, name="urlHistoryEntry", curie=OBSERVABLE.curie('urlHistoryEntry'),
                   model_uri=MASTER.urlHistoryEntry, domain=None, range=Optional[Union[dict, URLHistoryEntry]])

slots.urlTargeted = Slot(uri=OBSERVABLE.urlTargeted, name="urlTargeted", curie=OBSERVABLE.curie('urlTargeted'),
                   model_uri=MASTER.urlTargeted, domain=None, range=Optional[Union[str, IriType]])

slots.urlTransitionType = Slot(uri=OBSERVABLE.urlTransitionType, name="urlTransitionType", curie=OBSERVABLE.curie('urlTransitionType'),
                   model_uri=MASTER.urlTransitionType, domain=None, range=Optional[str])

slots.userLocationString = Slot(uri=OBSERVABLE.userLocationString, name="userLocationString", curie=OBSERVABLE.curie('userLocationString'),
                   model_uri=MASTER.userLocationString, domain=None, range=Optional[str])

slots.userName = Slot(uri=OBSERVABLE.userName, name="userName", curie=OBSERVABLE.curie('userName'),
                   model_uri=MASTER.userName, domain=None, range=Optional[str])

slots.validityNotAfter = Slot(uri=OBSERVABLE.validityNotAfter, name="validityNotAfter", curie=OBSERVABLE.curie('validityNotAfter'),
                   model_uri=MASTER.validityNotAfter, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.validityNotBefore = Slot(uri=OBSERVABLE.validityNotBefore, name="validityNotBefore", curie=OBSERVABLE.curie('validityNotBefore'),
                   model_uri=MASTER.validityNotBefore, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.values = Slot(uri=OBSERVABLE.values, name="values", curie=OBSERVABLE.curie('values'),
                   model_uri=MASTER.values, domain=None, range=Optional[str])

slots.version = Slot(uri=OBSERVABLE.version, name="version", curie=OBSERVABLE.curie('version'),
                   model_uri=MASTER.version, domain=None, range=Optional[str])

slots.visibility = Slot(uri=OBSERVABLE.visibility, name="visibility", curie=OBSERVABLE.curie('visibility'),
                   model_uri=MASTER.visibility, domain=None, range=Optional[Union[bool, BooleanType]])

slots.visitCount = Slot(uri=OBSERVABLE.visitCount, name="visitCount", curie=OBSERVABLE.curie('visitCount'),
                   model_uri=MASTER.visitCount, domain=None, range=Optional[int])

slots.visitDuration = Slot(uri=OBSERVABLE.visitDuration, name="visitDuration", curie=OBSERVABLE.curie('visitDuration'),
                   model_uri=MASTER.visitDuration, domain=None, range=Optional[Union[int, DurationType]])

slots.visitTime = Slot(uri=OBSERVABLE.visitTime, name="visitTime", curie=OBSERVABLE.curie('visitTime'),
                   model_uri=MASTER.visitTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.volume = Slot(uri=OBSERVABLE.volume, name="volume", curie=OBSERVABLE.curie('volume'),
                   model_uri=MASTER.volume, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.volumeID = Slot(uri=OBSERVABLE.volumeID, name="volumeID", curie=OBSERVABLE.curie('volumeID'),
                   model_uri=MASTER.volumeID, domain=None, range=Optional[str])

slots.whoisContactType = Slot(uri=OBSERVABLE.whoisContactType, name="whoisContactType", curie=OBSERVABLE.curie('whoisContactType'),
                   model_uri=MASTER.whoisContactType, domain=None, range=Optional[str])

slots.whoisServer = Slot(uri=OBSERVABLE.whoisServer, name="whoisServer", curie=OBSERVABLE.curie('whoisServer'),
                   model_uri=MASTER.whoisServer, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.win32VersionValue = Slot(uri=OBSERVABLE.win32VersionValue, name="win32VersionValue", curie=OBSERVABLE.curie('win32VersionValue'),
                   model_uri=MASTER.win32VersionValue, domain=None, range=Optional[Union[int, UnsignedIntegerType]])

slots.windowTitle = Slot(uri=OBSERVABLE.windowTitle, name="windowTitle", curie=OBSERVABLE.curie('windowTitle'),
                   model_uri=MASTER.windowTitle, domain=None, range=Optional[str])

slots.windowsDirectory = Slot(uri=OBSERVABLE.windowsDirectory, name="windowsDirectory", curie=OBSERVABLE.curie('windowsDirectory'),
                   model_uri=MASTER.windowsDirectory, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.windowsSystemDirectory = Slot(uri=OBSERVABLE.windowsSystemDirectory, name="windowsSystemDirectory", curie=OBSERVABLE.curie('windowsSystemDirectory'),
                   model_uri=MASTER.windowsSystemDirectory, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.windowsTempDirectory = Slot(uri=OBSERVABLE.windowsTempDirectory, name="windowsTempDirectory", curie=OBSERVABLE.curie('windowsTempDirectory'),
                   model_uri=MASTER.windowsTempDirectory, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.windowsVolumeAttributes = Slot(uri=OBSERVABLE.windowsVolumeAttributes, name="windowsVolumeAttributes", curie=OBSERVABLE.curie('windowsVolumeAttributes'),
                   model_uri=MASTER.windowsVolumeAttributes, domain=None, range=Optional[str])

slots.wirelessNetworkSecurityMode = Slot(uri=OBSERVABLE.wirelessNetworkSecurityMode, name="wirelessNetworkSecurityMode", curie=OBSERVABLE.curie('wirelessNetworkSecurityMode'),
                   model_uri=MASTER.wirelessNetworkSecurityMode, domain=None, range=Optional[str])

slots.workItemData = Slot(uri=OBSERVABLE.workItemData, name="workItemData", curie=OBSERVABLE.curie('workItemData'),
                   model_uri=MASTER.workItemData, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.workingDirectory = Slot(uri=OBSERVABLE.workingDirectory, name="workingDirectory", curie=OBSERVABLE.curie('workingDirectory'),
                   model_uri=MASTER.workingDirectory, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.x509v3extensions = Slot(uri=OBSERVABLE.x509v3extensions, name="x509v3extensions", curie=OBSERVABLE.curie('x509v3extensions'),
                   model_uri=MASTER.x509v3extensions, domain=None, range=Optional[Union[dict, X509V3ExtensionsFacet]])

slots.xMailer = Slot(uri=OBSERVABLE.xMailer, name="xMailer", curie=OBSERVABLE.curie('xMailer'),
                   model_uri=MASTER.xMailer, domain=None, range=Optional[str])

slots.xOriginatingIP = Slot(uri=OBSERVABLE.xOriginatingIP, name="xOriginatingIP", curie=OBSERVABLE.curie('xOriginatingIP'),
                   model_uri=MASTER.xOriginatingIP, domain=None, range=Optional[Union[dict, ObservableObject]])

slots.patternExpression = Slot(uri=PATTERN.patternExpression, name="patternExpression", curie=PATTERN.curie('patternExpression'),
                   model_uri=MASTER.patternExpression, domain=None, range=Optional[str])

slots.buildConfiguration = Slot(uri=TOOL.buildConfiguration, name="buildConfiguration", curie=TOOL.curie('buildConfiguration'),
                   model_uri=MASTER.buildConfiguration, domain=None, range=Optional[Union[dict, Configuration]])

slots.buildID = Slot(uri=TOOL.buildID, name="buildID", curie=TOOL.curie('buildID'),
                   model_uri=MASTER.buildID, domain=None, range=Optional[str])

slots.buildInformation = Slot(uri=TOOL.buildInformation, name="buildInformation", curie=TOOL.curie('buildInformation'),
                   model_uri=MASTER.buildInformation, domain=None, range=Optional[Union[dict, BuildInformationType]])

slots.buildLabel = Slot(uri=TOOL.buildLabel, name="buildLabel", curie=TOOL.curie('buildLabel'),
                   model_uri=MASTER.buildLabel, domain=None, range=Optional[str])

slots.buildOutputLog = Slot(uri=TOOL.buildOutputLog, name="buildOutputLog", curie=TOOL.curie('buildOutputLog'),
                   model_uri=MASTER.buildOutputLog, domain=None, range=Optional[str])

slots.buildProject = Slot(uri=TOOL.buildProject, name="buildProject", curie=TOOL.curie('buildProject'),
                   model_uri=MASTER.buildProject, domain=None, range=Optional[str])

slots.buildScript = Slot(uri=TOOL.buildScript, name="buildScript", curie=TOOL.curie('buildScript'),
                   model_uri=MASTER.buildScript, domain=None, range=Optional[str])

slots.buildUtility = Slot(uri=TOOL.buildUtility, name="buildUtility", curie=TOOL.curie('buildUtility'),
                   model_uri=MASTER.buildUtility, domain=None, range=Optional[Union[dict, BuildUtilityType]])

slots.buildUtilityName = Slot(uri=TOOL.buildUtilityName, name="buildUtilityName", curie=TOOL.curie('buildUtilityName'),
                   model_uri=MASTER.buildUtilityName, domain=None, range=Optional[str])

slots.buildVersion = Slot(uri=TOOL.buildVersion, name="buildVersion", curie=TOOL.curie('buildVersion'),
                   model_uri=MASTER.buildVersion, domain=None, range=Optional[str])

slots.compilationDate = Slot(uri=TOOL.compilationDate, name="compilationDate", curie=TOOL.curie('compilationDate'),
                   model_uri=MASTER.compilationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.compilerInformalDescription = Slot(uri=TOOL.compilerInformalDescription, name="compilerInformalDescription", curie=TOOL.curie('compilerInformalDescription'),
                   model_uri=MASTER.compilerInformalDescription, domain=None, range=Optional[str])

slots.compilers = Slot(uri=TOOL.compilers, name="compilers", curie=TOOL.curie('compilers'),
                   model_uri=MASTER.compilers, domain=None, range=Optional[Union[dict, CompilerType]])

slots._cpeid = Slot(uri=TOOL._cpeid, name="_cpeid", curie=TOOL.curie('_cpeid'),
                   model_uri=MASTER._cpeid, domain=None, range=Optional[str])

slots._creator = Slot(uri=TOOL._creator, name="_creator", curie=TOOL.curie('_creator'),
                   model_uri=MASTER._creator, domain=None, range=Optional[Union[dict, Identity]])

slots.libraries = Slot(uri=TOOL.libraries, name="libraries", curie=TOOL.curie('libraries'),
                   model_uri=MASTER.libraries, domain=None, range=Optional[Union[dict, LibraryType]])

slots.libraryName = Slot(uri=TOOL.libraryName, name="libraryName", curie=TOOL.curie('libraryName'),
                   model_uri=MASTER.libraryName, domain=None, range=Optional[str])

slots.libraryVersion = Slot(uri=TOOL.libraryVersion, name="libraryVersion", curie=TOOL.curie('libraryVersion'),
                   model_uri=MASTER.libraryVersion, domain=None, range=Optional[str])

slots._references = Slot(uri=TOOL._references, name="_references", curie=TOOL.curie('_references'),
                   model_uri=MASTER._references, domain=None, range=Optional[Union[str, IriType]])

slots.servicePack = Slot(uri=TOOL.servicePack, name="servicePack", curie=TOOL.curie('servicePack'),
                   model_uri=MASTER.servicePack, domain=None, range=Optional[str])

slots._swid = Slot(uri=TOOL._swid, name="_swid", curie=TOOL.curie('_swid'),
                   model_uri=MASTER._swid, domain=None, range=Optional[str])

slots.toolType = Slot(uri=TOOL.toolType, name="toolType", curie=TOOL.curie('toolType'),
                   model_uri=MASTER.toolType, domain=None, range=Optional[str])

slots._version = Slot(uri=TOOL._version, name="_version", curie=TOOL.curie('_version'),
                   model_uri=MASTER._version, domain=None, range=Optional[str])

slots.list = Slot(uri=TYPES.list, name="list", curie=TYPES.curie('list'),
                   model_uri=MASTER.list, domain=None, range=Optional[Union[dict, List]])

slots.listItem = Slot(uri=TYPES.listItem, name="listItem", curie=TYPES.curie('listItem'),
                   model_uri=MASTER.listItem, domain=None, range=Optional[Union[dict, ListItem]])

slots.identifier = Slot(uri=TYPES.identifier, name="identifier", curie=TYPES.curie('identifier'),
                   model_uri=MASTER.identifier, domain=None, range=Optional[str])

slots.nativeFormatString = Slot(uri=TYPES.nativeFormatString, name="nativeFormatString", curie=TYPES.curie('nativeFormatString'),
                   model_uri=MASTER.nativeFormatString, domain=None, range=Optional[str])

slots.structuredText = Slot(uri=TYPES.structuredText, name="structuredText", curie=TYPES.curie('structuredText'),
                   model_uri=MASTER.structuredText, domain=None, range=Optional[str])

slots.entry = Slot(uri=TYPES.entry, name="entry", curie=TYPES.curie('entry'),
                   model_uri=MASTER.entry, domain=None, range=Optional[Union[dict, DictionaryEntry]])

slots.hashMethod = Slot(uri=TYPES.hashMethod, name="hashMethod", curie=TYPES.curie('hashMethod'),
                   model_uri=MASTER.hashMethod, domain=None, range=Optional[str])

slots.hashValue = Slot(uri=TYPES.hashValue, name="hashValue", curie=TYPES.curie('hashValue'),
                   model_uri=MASTER.hashValue, domain=None, range=Optional[hex])

slots.key = Slot(uri=TYPES.key, name="key", curie=TYPES.curie('key'),
                   model_uri=MASTER.key, domain=None, range=Optional[str])

slots.threadNextItem = Slot(uri=TYPES.threadNextItem, name="threadNextItem", curie=TYPES.curie('threadNextItem'),
                   model_uri=MASTER.threadNextItem, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadOriginItem = Slot(uri=TYPES.threadOriginItem, name="threadOriginItem", curie=TYPES.curie('threadOriginItem'),
                   model_uri=MASTER.threadOriginItem, domain=Thread, range=Optional[Union[dict, "ThreadItem"]])

slots.threadPredecessor = Slot(uri=TYPES.threadPredecessor, name="threadPredecessor", curie=TYPES.curie('threadPredecessor'),
                   model_uri=MASTER.threadPredecessor, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadPreviousItem = Slot(uri=TYPES.threadPreviousItem, name="threadPreviousItem", curie=TYPES.curie('threadPreviousItem'),
                   model_uri=MASTER.threadPreviousItem, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadSuccessor = Slot(uri=TYPES.threadSuccessor, name="threadSuccessor", curie=TYPES.curie('threadSuccessor'),
                   model_uri=MASTER.threadSuccessor, domain=ThreadItem, range=Optional[Union[dict, "ThreadItem"]])

slots.threadTerminalItem = Slot(uri=TYPES.threadTerminalItem, name="threadTerminalItem", curie=TYPES.curie('threadTerminalItem'),
                   model_uri=MASTER.threadTerminalItem, domain=Thread, range=Optional[Union[dict, "ThreadItem"]])

slots._value = Slot(uri=TYPES._value, name="_value", curie=TYPES.curie('_value'),
                   model_uri=MASTER._value, domain=None, range=Optional[str])

slots.AccountTypeVocab = Slot(uri=VOCABULARY.AccountTypeVocab, name="AccountTypeVocab", curie=VOCABULARY.curie('AccountTypeVocab'),
                   model_uri=MASTER.AccountTypeVocab, domain=None, range=Optional[Union[str, "AccountTypeEnum"]])

slots.ActionArgumentNameVocab = Slot(uri=VOCABULARY.ActionArgumentNameVocab, name="ActionArgumentNameVocab", curie=VOCABULARY.curie('ActionArgumentNameVocab'),
                   model_uri=MASTER.ActionArgumentNameVocab, domain=None, range=Optional[Union[str, "ActionArgumentNameEnum"]])

slots.ActionNameVocab = Slot(uri=VOCABULARY.ActionNameVocab, name="ActionNameVocab", curie=VOCABULARY.curie('ActionNameVocab'),
                   model_uri=MASTER.ActionNameVocab, domain=None, range=Optional[str])

slots.ActionRelationshipTypeVocab = Slot(uri=VOCABULARY.ActionRelationshipTypeVocab, name="ActionRelationshipTypeVocab", curie=VOCABULARY.curie('ActionRelationshipTypeVocab'),
                   model_uri=MASTER.ActionRelationshipTypeVocab, domain=None, range=Optional[Union[str, "ActionRelationshipTypeEnum"]])

slots.ActionStatusTypeVocab = Slot(uri=VOCABULARY.ActionStatusTypeVocab, name="ActionStatusTypeVocab", curie=VOCABULARY.curie('ActionStatusTypeVocab'),
                   model_uri=MASTER.ActionStatusTypeVocab, domain=None, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.ActionTypeVocab = Slot(uri=VOCABULARY.ActionTypeVocab, name="ActionTypeVocab", curie=VOCABULARY.curie('ActionTypeVocab'),
                   model_uri=MASTER.ActionTypeVocab, domain=None, range=Optional[Union[str, "ActionTypeEnum"]])

slots.BitnessVocab = Slot(uri=VOCABULARY.BitnessVocab, name="BitnessVocab", curie=VOCABULARY.curie('BitnessVocab'),
                   model_uri=MASTER.BitnessVocab, domain=None, range=Optional[Union[str, "BitnessEnum"]])

slots.CharacterEncodingVocab = Slot(uri=VOCABULARY.CharacterEncodingVocab, name="CharacterEncodingVocab", curie=VOCABULARY.curie('CharacterEncodingVocab'),
                   model_uri=MASTER.CharacterEncodingVocab, domain=None, range=Optional[Union[str, "CharacterEncodingEnum"]])

slots.ContactAddressScopeVocab = Slot(uri=VOCABULARY.ContactAddressScopeVocab, name="ContactAddressScopeVocab", curie=VOCABULARY.curie('ContactAddressScopeVocab'),
                   model_uri=MASTER.ContactAddressScopeVocab, domain=None, range=Optional[Union[str, "ContactAddressScopeEnum"]])

slots.ContactEmailScopeVocab = Slot(uri=VOCABULARY.ContactEmailScopeVocab, name="ContactEmailScopeVocab", curie=VOCABULARY.curie('ContactEmailScopeVocab'),
                   model_uri=MASTER.ContactEmailScopeVocab, domain=None, range=Optional[Union[str, "ContactEmailScopeEnum"]])

slots.ContactPhoneScopeVocab = Slot(uri=VOCABULARY.ContactPhoneScopeVocab, name="ContactPhoneScopeVocab", curie=VOCABULARY.curie('ContactPhoneScopeVocab'),
                   model_uri=MASTER.ContactPhoneScopeVocab, domain=None, range=Optional[Union[str, "ContactPhoneEnum"]])

slots.ContactSIPScopeVocab = Slot(uri=VOCABULARY.ContactSIPScopeVocab, name="ContactSIPScopeVocab", curie=VOCABULARY.curie('ContactSIPScopeVocab'),
                   model_uri=MASTER.ContactSIPScopeVocab, domain=None, range=Optional[Union[str, "ContactSIPScopeEnum"]])

slots.ContactURLScopeVocab = Slot(uri=VOCABULARY.ContactURLScopeVocab, name="ContactURLScopeVocab", curie=VOCABULARY.curie('ContactURLScopeVocab'),
                   model_uri=MASTER.ContactURLScopeVocab, domain=None, range=Optional[Union[str, "ContactURLScopeEnum"]])

slots.DiskTypeVocab = Slot(uri=VOCABULARY.DiskTypeVocab, name="DiskTypeVocab", curie=VOCABULARY.curie('DiskTypeVocab'),
                   model_uri=MASTER.DiskTypeVocab, domain=None, range=Optional[Union[str, "DiskTypeEnum"]])

slots.EndiannessTypeVocab = Slot(uri=VOCABULARY.EndiannessTypeVocab, name="EndiannessTypeVocab", curie=VOCABULARY.curie('EndiannessTypeVocab'),
                   model_uri=MASTER.EndiannessTypeVocab, domain=None, range=Optional[Union[str, "EndiannessTypeEnum"]])

slots.HashNameVocab = Slot(uri=VOCABULARY.HashNameVocab, name="HashNameVocab", curie=VOCABULARY.curie('HashNameVocab'),
                   model_uri=MASTER.HashNameVocab, domain=None, range=Optional[Union[str, "HashNameEnum"]])

slots.LibraryTypeVocab = Slot(uri=VOCABULARY.LibraryTypeVocab, name="LibraryTypeVocab", curie=VOCABULARY.curie('LibraryTypeVocab'),
                   model_uri=MASTER.LibraryTypeVocab, domain=None, range=Optional[Union[str, "LibraryTypeEnum"]])

slots.MemoryBlockTypeVocab = Slot(uri=VOCABULARY.MemoryBlockTypeVocab, name="MemoryBlockTypeVocab", curie=VOCABULARY.curie('MemoryBlockTypeVocab'),
                   model_uri=MASTER.MemoryBlockTypeVocab, domain=None, range=Optional[Union[str, "MemoryBlockTypeEnum"]])

slots.ObservableObjectRelationshipVocab = Slot(uri=VOCABULARY.ObservableObjectRelationshipVocab, name="ObservableObjectRelationshipVocab", curie=VOCABULARY.curie('ObservableObjectRelationshipVocab'),
                   model_uri=MASTER.ObservableObjectRelationshipVocab, domain=None, range=Optional[Union[str, "ObservableObjectRelationshipEnum"]])

slots.ObservableObjectStateVocab = Slot(uri=VOCABULARY.ObservableObjectStateVocab, name="ObservableObjectStateVocab", curie=VOCABULARY.curie('ObservableObjectStateVocab'),
                   model_uri=MASTER.ObservableObjectStateVocab, domain=None, range=Optional[Union[str, "ObservableObjectStateEnum"]])

slots.PartitionTypeVocab = Slot(uri=VOCABULARY.PartitionTypeVocab, name="PartitionTypeVocab", curie=VOCABULARY.curie('PartitionTypeVocab'),
                   model_uri=MASTER.PartitionTypeVocab, domain=None, range=Optional[Union[str, "PartitionTypeEnum"]])

slots.ProcessorArchVocab = Slot(uri=VOCABULARY.ProcessorArchVocab, name="ProcessorArchVocab", curie=VOCABULARY.curie('ProcessorArchVocab'),
                   model_uri=MASTER.ProcessorArchVocab, domain=None, range=Optional[Union[str, "ProcessorArchEnum"]])

slots.RecoveredObjectStatusVocab = Slot(uri=VOCABULARY.RecoveredObjectStatusVocab, name="RecoveredObjectStatusVocab", curie=VOCABULARY.curie('RecoveredObjectStatusVocab'),
                   model_uri=MASTER.RecoveredObjectStatusVocab, domain=None, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.RegionalRegistry_typeVocab = Slot(uri=VOCABULARY.RegionalRegistry_typeVocab, name="RegionalRegistry typeVocab", curie=VOCABULARY.curie('RegionalRegistry_typeVocab'),
                   model_uri=MASTER.RegionalRegistry_typeVocab, domain=None, range=Optional[Union[str, "RegionalRegistryTypeEnum"]])

slots.RegistryDatatypeVocab = Slot(uri=VOCABULARY.RegistryDatatypeVocab, name="RegistryDatatypeVocab", curie=VOCABULARY.curie('RegistryDatatypeVocab'),
                   model_uri=MASTER.RegistryDatatypeVocab, domain=None, range=Optional[Union[str, "RegistryDatatypeEnum"]])

slots.SIMFormVocab = Slot(uri=VOCABULARY.SIMFormVocab, name="SIMFormVocab", curie=VOCABULARY.curie('SIMFormVocab'),
                   model_uri=MASTER.SIMFormVocab, domain=None, range=Optional[Union[str, "SIMFormEnum"]])

slots.SIMTypeVocab = Slot(uri=VOCABULARY.SIMTypeVocab, name="SIMTypeVocab", curie=VOCABULARY.curie('SIMTypeVocab'),
                   model_uri=MASTER.SIMTypeVocab, domain=None, range=Optional[Union[str, "SIMTypeEnum"]])

slots.TaskActionTypeVocab = Slot(uri=VOCABULARY.TaskActionTypeVocab, name="TaskActionTypeVocab", curie=VOCABULARY.curie('TaskActionTypeVocab'),
                   model_uri=MASTER.TaskActionTypeVocab, domain=None, range=Optional[Union[str, "TaskActionTypeEnum"]])

slots.TaskFlagVocab = Slot(uri=VOCABULARY.TaskFlagVocab, name="TaskFlagVocab", curie=VOCABULARY.curie('TaskFlagVocab'),
                   model_uri=MASTER.TaskFlagVocab, domain=None, range=Optional[Union[str, "TaskFlagEnum"]])

slots.TaskPriorityVocab = Slot(uri=VOCABULARY.TaskPriorityVocab, name="TaskPriorityVocab", curie=VOCABULARY.curie('TaskPriorityVocab'),
                   model_uri=MASTER.TaskPriorityVocab, domain=None, range=Optional[Union[str, "TaskPriorityEnum"]])

slots.TaskStatusVocab = Slot(uri=VOCABULARY.TaskStatusVocab, name="TaskStatusVocab", curie=VOCABULARY.curie('TaskStatusVocab'),
                   model_uri=MASTER.TaskStatusVocab, domain=None, range=Optional[Union[str, "TaskStatusEnum"]])

slots.ThreadRunningStatusVocab = Slot(uri=VOCABULARY.ThreadRunningStatusVocab, name="ThreadRunningStatusVocab", curie=VOCABULARY.curie('ThreadRunningStatusVocab'),
                   model_uri=MASTER.ThreadRunningStatusVocab, domain=None, range=Optional[Union[str, "ThreadRunningStatusEnum"]])

slots.TimestampPrecisionVocab = Slot(uri=VOCABULARY.TimestampPrecisionVocab, name="TimestampPrecisionVocab", curie=VOCABULARY.curie('TimestampPrecisionVocab'),
                   model_uri=MASTER.TimestampPrecisionVocab, domain=None, range=Optional[Union[str, "TimestampPrecisionEnum"]])

slots.TrendVocab = Slot(uri=VOCABULARY.TrendVocab, name="TrendVocab", curie=VOCABULARY.curie('TrendVocab'),
                   model_uri=MASTER.TrendVocab, domain=None, range=Optional[Union[str, "TrendEnum"]])

slots.TriggerFrequencyVocab = Slot(uri=VOCABULARY.TriggerFrequencyVocab, name="TriggerFrequencyVocab", curie=VOCABULARY.curie('TriggerFrequencyVocab'),
                   model_uri=MASTER.TriggerFrequencyVocab, domain=None, range=Optional[Union[str, "TriggerFrequencyEnum"]])

slots.TriggerTypeVocab = Slot(uri=VOCABULARY.TriggerTypeVocab, name="TriggerTypeVocab", curie=VOCABULARY.curie('TriggerTypeVocab'),
                   model_uri=MASTER.TriggerTypeVocab, domain=None, range=Optional[Union[str, "TriggerTypeEnum"]])

slots.URLTransitionTypeVocab = Slot(uri=VOCABULARY.URLTransitionTypeVocab, name="URLTransitionTypeVocab", curie=VOCABULARY.curie('URLTransitionTypeVocab'),
                   model_uri=MASTER.URLTransitionTypeVocab, domain=None, range=Optional[Union[str, "URLTransitionTypeEnum"]])

slots.UnixProcessStateVocab = Slot(uri=VOCABULARY.UnixProcessStateVocab, name="UnixProcessStateVocab", curie=VOCABULARY.curie('UnixProcessStateVocab'),
                   model_uri=MASTER.UnixProcessStateVocab, domain=None, range=Optional[Union[str, "UnixProcessStateEnum"]])

slots.WhoisContactTypeVocab = Slot(uri=VOCABULARY.WhoisContactTypeVocab, name="WhoisContactTypeVocab", curie=VOCABULARY.curie('WhoisContactTypeVocab'),
                   model_uri=MASTER.WhoisContactTypeVocab, domain=None, range=Optional[Union[str, "WhoisContactTypeEnum"]])

slots.WhoisDNSSECTypeVocab = Slot(uri=VOCABULARY.WhoisDNSSECTypeVocab, name="WhoisDNSSECTypeVocab", curie=VOCABULARY.curie('WhoisDNSSECTypeVocab'),
                   model_uri=MASTER.WhoisDNSSECTypeVocab, domain=None, range=Optional[Union[str, "WhoisDNSSECTypeEnum"]])

slots.WhoisStatusTypeVocab = Slot(uri=VOCABULARY.WhoisStatusTypeVocab, name="WhoisStatusTypeVocab", curie=VOCABULARY.curie('WhoisStatusTypeVocab'),
                   model_uri=MASTER.WhoisStatusTypeVocab, domain=None, range=Optional[Union[str, "WhoisStatusTypeEnum"]])

slots.WindowsDriveTypeVocab = Slot(uri=VOCABULARY.WindowsDriveTypeVocab, name="WindowsDriveTypeVocab", curie=VOCABULARY.curie('WindowsDriveTypeVocab'),
                   model_uri=MASTER.WindowsDriveTypeVocab, domain=None, range=Optional[Union[str, "WindowsDriveTypeEnum"]])

slots.WindowsVolumeAttributeVocab = Slot(uri=VOCABULARY.WindowsVolumeAttributeVocab, name="WindowsVolumeAttributeVocab", curie=VOCABULARY.curie('WindowsVolumeAttributeVocab'),
                   model_uri=MASTER.WindowsVolumeAttributeVocab, domain=None, range=Optional[Union[str, "WindowsVolumeAttributeEnum"]])

slots.WirelessNetworkSecurityModeVocab = Slot(uri=VOCABULARY.WirelessNetworkSecurityModeVocab, name="WirelessNetworkSecurityModeVocab", curie=VOCABULARY.curie('WirelessNetworkSecurityModeVocab'),
                   model_uri=MASTER.WirelessNetworkSecurityModeVocab, domain=None, range=Optional[Union[str, "WirelessNetworkSecurityModeEnum"]])

slots.element = Slot(uri=COLLECTIONS.element, name="element", curie=COLLECTIONS.curie('element'),
                   model_uri=MASTER.element, domain=Collection, range=Optional[Union[dict, "Thing"]])

slots.elementOf = Slot(uri=COLLECTIONS.elementOf, name="elementOf", curie=COLLECTIONS.curie('elementOf'),
                   model_uri=MASTER.elementOf, domain=Thing, range=Optional[Union[dict, Collection]])

slots.firstItem = Slot(uri=COLLECTIONS.firstItem, name="firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=MASTER.firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.firstItemOf = Slot(uri=COLLECTIONS.firstItemOf, name="firstItemOf", curie=COLLECTIONS.curie('firstItemOf'),
                   model_uri=MASTER.firstItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.followedBy = Slot(uri=COLLECTIONS.followedBy, name="followedBy", curie=COLLECTIONS.curie('followedBy'),
                   model_uri=MASTER.followedBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.item = Slot(uri=COLLECTIONS.item, name="item", curie=COLLECTIONS.curie('item'),
                   model_uri=MASTER.item, domain=Bag, range=Optional[Union[dict, "CoItem"]])

slots.itemContent = Slot(uri=COLLECTIONS.itemContent, name="itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=MASTER.itemContent, domain=CoItem, range=Optional[Union[dict, "CoItem"]])

slots.itemContentOf = Slot(uri=COLLECTIONS.itemContentOf, name="itemContentOf", curie=COLLECTIONS.curie('itemContentOf'),
                   model_uri=MASTER.itemContentOf, domain=CoItem, range=Optional[Union[dict, CoItem]])

slots.itemOf = Slot(uri=COLLECTIONS.itemOf, name="itemOf", curie=COLLECTIONS.curie('itemOf'),
                   model_uri=MASTER.itemOf, domain=CoItem, range=Optional[Union[dict, Bag]])

slots.lastItem = Slot(uri=COLLECTIONS.lastItem, name="lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=MASTER.lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.lastItemOf = Slot(uri=COLLECTIONS.lastItemOf, name="lastItemOf", curie=COLLECTIONS.curie('lastItemOf'),
                   model_uri=MASTER.lastItemOf, domain=ListItem, range=Optional[Union[dict, List]])

slots.nextItem = Slot(uri=COLLECTIONS.nextItem, name="nextItem", curie=COLLECTIONS.curie('nextItem'),
                   model_uri=MASTER.nextItem, domain=Thing, range=Optional[Union[dict, ListItem]])

slots.precededBy = Slot(uri=COLLECTIONS.precededBy, name="precededBy", curie=COLLECTIONS.curie('precededBy'),
                   model_uri=MASTER.precededBy, domain=ListItem, range=Optional[Union[dict, "ListItem"]])

slots.previousItem = Slot(uri=COLLECTIONS.previousItem, name="previousItem", curie=COLLECTIONS.curie('previousItem'),
                   model_uri=MASTER.previousItem, domain=ListItem, range=Optional[Union[dict, "Thing"]])

slots._index = Slot(uri=COLLECTIONS._index, name="_index", curie=COLLECTIONS.curie('_index'),
                   model_uri=MASTER._index, domain=ListItem, range=Optional[Union[int, PositiveInteger]])

slots.size = Slot(uri=COLLECTIONS.size, name="size", curie=COLLECTIONS.curie('size'),
                   model_uri=MASTER.size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.Action_subaction = Slot(uri=ACTION.subaction, name="Action_subaction", curie=ACTION.curie('subaction'),
                   model_uri=MASTER.Action_subaction, domain=Action, range=Optional[Union[Union[dict, "Action"], List[Union[dict, "Action"]]]])

slots.Action_error = Slot(uri=ACTION.error, name="Action_error", curie=ACTION.curie('error'),
                   model_uri=MASTER.Action_error, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_instrument = Slot(uri=ACTION.instrument, name="Action_instrument", curie=ACTION.curie('instrument'),
                   model_uri=MASTER.Action_instrument, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_object = Slot(uri=CORE.object, name="Action_object", curie=CORE.curie('object'),
                   model_uri=MASTER.Action_object, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_participant = Slot(uri=ACTION.participant, name="Action_participant", curie=ACTION.curie('participant'),
                   model_uri=MASTER.Action_participant, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_result = Slot(uri=ACTION.result, name="Action_result", curie=ACTION.curie('result'),
                   model_uri=MASTER.Action_result, domain=Action, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.Action_location = Slot(uri=ACTION.location, name="Action_location", curie=ACTION.curie('location'),
                   model_uri=MASTER.Action_location, domain=Action, range=Optional[Union[Union[dict, "Location"], List[Union[dict, "Location"]]]])

slots.Action_endTime = Slot(uri=CORE.endTime, name="Action_endTime", curie=CORE.curie('endTime'),
                   model_uri=MASTER.Action_endTime, domain=Action, range=Optional[Union[str, XSDDateTime]])

slots.Action_startTime = Slot(uri=CORE.startTime, name="Action_startTime", curie=CORE.curie('startTime'),
                   model_uri=MASTER.Action_startTime, domain=Action, range=Optional[Union[str, XSDDateTime]])

slots.ActionArgumentFacet_argumentName = Slot(uri=ACTION.argumentName, name="ActionArgumentFacet_argumentName", curie=ACTION.curie('argumentName'),
                   model_uri=MASTER.ActionArgumentFacet_argumentName, domain=ActionArgumentFacet, range=str)

slots.ActionArgumentFacet_value = Slot(uri=CORE.value, name="ActionArgumentFacet_value", curie=CORE.curie('value'),
                   model_uri=MASTER.ActionArgumentFacet_value, domain=ActionArgumentFacet, range=str)

slots.ActionFrequencyFacet_rate = Slot(uri=ACTION.rate, name="ActionFrequencyFacet_rate", curie=ACTION.curie('rate'),
                   model_uri=MASTER.ActionFrequencyFacet_rate, domain=ActionFrequencyFacet, range=Union[Decimal, DecimalType])

slots.ActionFrequencyFacet_scale = Slot(uri=ACTION.scale, name="ActionFrequencyFacet_scale", curie=ACTION.curie('scale'),
                   model_uri=MASTER.ActionFrequencyFacet_scale, domain=ActionFrequencyFacet, range=str)

slots.ActionFrequencyFacet_units = Slot(uri=ACTION.units, name="ActionFrequencyFacet_units", curie=ACTION.curie('units'),
                   model_uri=MASTER.ActionFrequencyFacet_units, domain=ActionFrequencyFacet, range=str)

slots.ActionFrequencyFacet_trend = Slot(uri=ACTION.trend, name="ActionFrequencyFacet_trend", curie=ACTION.curie('trend'),
                   model_uri=MASTER.ActionFrequencyFacet_trend, domain=ActionFrequencyFacet, range=Union[str, "TrendEnum"])

slots.ActionLifecycle_phase = Slot(uri=ACTION.phase, name="ActionLifecycle_phase", curie=ACTION.curie('phase'),
                   model_uri=MASTER.ActionLifecycle_phase, domain=ActionLifecycle, range=Union[dict, "ArrayOfAction"])

slots.ActionLifecycle_error = Slot(uri=ACTION.error, name="ActionLifecycle_error", curie=ACTION.curie('error'),
                   model_uri=MASTER.ActionLifecycle_error, domain=ActionLifecycle, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ActionLifecycle_endTime = Slot(uri=CORE.endTime, name="ActionLifecycle_endTime", curie=CORE.curie('endTime'),
                   model_uri=MASTER.ActionLifecycle_endTime, domain=ActionLifecycle, range=Optional[Union[str, XSDDateTime]])

slots.ActionLifecycle_startTime = Slot(uri=CORE.startTime, name="ActionLifecycle_startTime", curie=CORE.curie('startTime'),
                   model_uri=MASTER.ActionLifecycle_startTime, domain=ActionLifecycle, range=Optional[Union[str, XSDDateTime]])

slots.ActionLifecycle_actionCount = Slot(uri=ACTION.actionCount, name="ActionLifecycle_actionCount", curie=ACTION.curie('actionCount'),
                   model_uri=MASTER.ActionLifecycle_actionCount, domain=ActionLifecycle, range=Optional[Union[int, NonNegativeIntegerType]])

slots.ActionLifecycle_actionStatus = Slot(uri=ACTION.actionStatus, name="ActionLifecycle_actionStatus", curie=ACTION.curie('actionStatus'),
                   model_uri=MASTER.ActionLifecycle_actionStatus, domain=ActionLifecycle, range=Optional[Union[str, "ActionStatusTypeEnum"]])

slots.ArrayOfAction_action = Slot(uri=ACTION.action, name="ArrayOfAction_action", curie=ACTION.curie('action'),
                   model_uri=MASTER.ArrayOfAction_action, domain=ArrayOfAction, range=Optional[Union[dict, Action]])

slots.AnalyticResult_resultContent = Slot(uri=ANALYSIS.resultContent, name="AnalyticResult_resultContent", curie=ANALYSIS.curie('resultContent'),
                   model_uri=MASTER.AnalyticResult_resultContent, domain=AnalyticResult, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ArtifactClassificationResultFacet_classification = Slot(uri=ANALYSIS.classification, name="ArtifactClassificationResultFacet_classification", curie=ANALYSIS.curie('classification'),
                   model_uri=MASTER.ArtifactClassificationResultFacet_classification, domain=ArtifactClassificationResultFacet, range=Optional[Union[Union[dict, ArtifactClassification], List[Union[dict, ArtifactClassification]]]])

slots.Configuration_configurationEntry = Slot(uri=CONFIGURATION.configurationEntry, name="Configuration_configurationEntry", curie=CONFIGURATION.curie('configurationEntry'),
                   model_uri=MASTER.Configuration_configurationEntry, domain=Configuration, range=Optional[Union[Union[dict, "ConfigurationEntry"], List[Union[dict, "ConfigurationEntry"]]]])

slots.Configuration_dependencies = Slot(uri=CONFIGURATION.dependencies, name="Configuration_dependencies", curie=CONFIGURATION.curie('dependencies'),
                   model_uri=MASTER.Configuration_dependencies, domain=Configuration, range=Optional[Union[Union[dict, "Dependency"], List[Union[dict, "Dependency"]]]])

slots.Configuration_usageContextAssumptions = Slot(uri=CONFIGURATION.usageContextAssumptions, name="Configuration_usageContextAssumptions", curie=CONFIGURATION.curie('usageContextAssumptions'),
                   model_uri=MASTER.Configuration_usageContextAssumptions, domain=Configuration, range=Optional[Union[str, List[str]]])

slots.ConfigurationEntry_itemDescription = Slot(uri=CONFIGURATION.itemDescription, name="ConfigurationEntry_itemDescription", curie=CONFIGURATION.curie('itemDescription'),
                   model_uri=MASTER.ConfigurationEntry_itemDescription, domain=ConfigurationEntry, range=Optional[str])

slots.ConfigurationEntry_itemName = Slot(uri=CONFIGURATION.itemName, name="ConfigurationEntry_itemName", curie=CONFIGURATION.curie('itemName'),
                   model_uri=MASTER.ConfigurationEntry_itemName, domain=ConfigurationEntry, range=Optional[str])

slots.ConfigurationEntry_itemObject = Slot(uri=CONFIGURATION.itemObject, name="ConfigurationEntry_itemObject", curie=CONFIGURATION.curie('itemObject'),
                   model_uri=MASTER.ConfigurationEntry_itemObject, domain=ConfigurationEntry, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ConfigurationEntry_itemType = Slot(uri=CONFIGURATION.itemType, name="ConfigurationEntry_itemType", curie=CONFIGURATION.curie('itemType'),
                   model_uri=MASTER.ConfigurationEntry_itemType, domain=ConfigurationEntry, range=Optional[str])

slots.ConfigurationEntry_itemValue = Slot(uri=CONFIGURATION.itemValue, name="ConfigurationEntry_itemValue", curie=CONFIGURATION.curie('itemValue'),
                   model_uri=MASTER.ConfigurationEntry_itemValue, domain=ConfigurationEntry, range=Optional[Union[str, List[str]]])

slots.Dependency_dependencyDescription = Slot(uri=CONFIGURATION.dependencyDescription, name="Dependency_dependencyDescription", curie=CONFIGURATION.curie('dependencyDescription'),
                   model_uri=MASTER.Dependency_dependencyDescription, domain=Dependency, range=Optional[str])

slots.Dependency_dependencyType = Slot(uri=CONFIGURATION.dependencyType, name="Dependency_dependencyType", curie=CONFIGURATION.curie('dependencyType'),
                   model_uri=MASTER.Dependency_dependencyType, domain=Dependency, range=Optional[str])

slots.Annotation_object = Slot(uri=CORE.object, name="Annotation_object", curie=CORE.curie('object'),
                   model_uri=MASTER.Annotation_object, domain=Annotation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Assertion_statement = Slot(uri=CORE.statement, name="Assertion_statement", curie=CORE.curie('statement'),
                   model_uri=MASTER.Assertion_statement, domain=Assertion, range=Optional[Union[str, List[str]]])

slots.AttributedName_namingAuthority = Slot(uri=CORE.namingAuthority, name="AttributedName_namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=MASTER.AttributedName_namingAuthority, domain=AttributedName, range=Optional[str])

slots.ConfidenceFacet_confidence = Slot(uri=CORE.confidence, name="ConfidenceFacet_confidence", curie=CORE.curie('confidence'),
                   model_uri=MASTER.ConfidenceFacet_confidence, domain=ConfidenceFacet, range=Union[int, NonNegativeIntegerType])

slots.ContextualCompilation_object = Slot(uri=CORE.object, name="ContextualCompilation_object", curie=CORE.curie('object'),
                   model_uri=MASTER.ContextualCompilation_object, domain=ContextualCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.ControlledVocabulary_constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="ControlledVocabulary_constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=MASTER.ControlledVocabulary_constrainingVocabularyReference, domain=ControlledVocabulary, range=Optional[Union[str, IriType]])

slots.ControlledVocabulary_constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="ControlledVocabulary_constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=MASTER.ControlledVocabulary_constrainingVocabularyName, domain=ControlledVocabulary, range=Optional[str])

slots.ControlledVocabulary_value = Slot(uri=CORE.value, name="ControlledVocabulary_value", curie=CORE.curie('value'),
                   model_uri=MASTER.ControlledVocabulary_value, domain=ControlledVocabulary, range=str)

slots.EnclosingCompilation_object = Slot(uri=CORE.object, name="EnclosingCompilation_object", curie=CORE.curie('object'),
                   model_uri=MASTER.EnclosingCompilation_object, domain=EnclosingCompilation, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ExternalReference_referenceURL = Slot(uri=CORE.referenceURL, name="ExternalReference_referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=MASTER.ExternalReference_referenceURL, domain=ExternalReference, range=Optional[Union[str, IriType]])

slots.ExternalReference_definingContext = Slot(uri=CORE.definingContext, name="ExternalReference_definingContext", curie=CORE.curie('definingContext'),
                   model_uri=MASTER.ExternalReference_definingContext, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_externalIdentifier = Slot(uri=CORE.externalIdentifier, name="ExternalReference_externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=MASTER.ExternalReference_externalIdentifier, domain=ExternalReference, range=Optional[str])

slots.Grouping_context = Slot(uri=CORE.context, name="Grouping_context", curie=CORE.curie('context'),
                   model_uri=MASTER.Grouping_context, domain=Grouping, range=Optional[Union[str, List[str]]])

slots.Relationship_endTime = Slot(uri=CORE.endTime, name="Relationship_endTime", curie=CORE.curie('endTime'),
                   model_uri=MASTER.Relationship_endTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.Relationship_isDirectional = Slot(uri=CORE.isDirectional, name="Relationship_isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=MASTER.Relationship_isDirectional, domain=Relationship, range=Union[bool, BooleanType])

slots.Relationship_kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="Relationship_kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=MASTER.Relationship_kindOfRelationship, domain=Relationship, range=Optional[str])

slots.Relationship_target = Slot(uri=CORE.target, name="Relationship_target", curie=CORE.curie('target'),
                   model_uri=MASTER.Relationship_target, domain=Relationship, range=Union[dict, "UcoObject"])

slots.Relationship_source = Slot(uri=CORE.source, name="Relationship_source", curie=CORE.curie('source'),
                   model_uri=MASTER.Relationship_source, domain=Relationship, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Relationship_startTime = Slot(uri=CORE.startTime, name="Relationship_startTime", curie=CORE.curie('startTime'),
                   model_uri=MASTER.Relationship_startTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_description = Slot(uri=DCTERMS.description, name="UcoObject_description", curie=DCTERMS.curie('description'),
                   model_uri=MASTER.UcoObject_description, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_createdBy = Slot(uri=CORE.createdBy, name="UcoObject_createdBy", curie=CORE.curie('createdBy'),
                   model_uri=MASTER.UcoObject_createdBy, domain=UcoObject, range=Optional[str])

slots.UcoObject_externalReference = Slot(uri=CORE.externalReference, name="UcoObject_externalReference", curie=CORE.curie('externalReference'),
                   model_uri=MASTER.UcoObject_externalReference, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_hasFacet = Slot(uri=CORE.hasFacet, name="UcoObject_hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=MASTER.UcoObject_hasFacet, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_modifiedTime = Slot(uri=CORE.modifiedTime, name="UcoObject_modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=MASTER.UcoObject_modifiedTime, domain=UcoObject, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_name = Slot(uri=RDFS.label, name="UcoObject_name", curie=RDFS.curie('label'),
                   model_uri=MASTER.UcoObject_name, domain=UcoObject, range=Optional[str])

slots.UcoObject_objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="UcoObject_objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=MASTER.UcoObject_objectCreatedTime, domain=UcoObject, range=Optional[Union[str, XSDDateTime]])

slots.UcoObject_objectMarking = Slot(uri=CORE.objectMarking, name="UcoObject_objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=MASTER.UcoObject_objectMarking, domain=UcoObject, range=Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]])

slots.UcoObject_specVersion = Slot(uri=CORE.specVersion, name="UcoObject_specVersion", curie=CORE.curie('specVersion'),
                   model_uri=MASTER.UcoObject_specVersion, domain=UcoObject, range=Optional[str])

slots.UcoObject_tag = Slot(uri=CORE.tag, name="UcoObject_tag", curie=CORE.curie('tag'),
                   model_uri=MASTER.UcoObject_tag, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.AddressFacet_address = Slot(uri=IDENTITY.address, name="AddressFacet_address", curie=IDENTITY.curie('address'),
                   model_uri=MASTER.AddressFacet_address, domain=AddressFacet, range=Optional[Union[dict, "Location"]])

slots.BirthInformationFacet_birthdate = Slot(uri=IDENTITY.birthdate, name="BirthInformationFacet_birthdate", curie=IDENTITY.curie('birthdate'),
                   model_uri=MASTER.BirthInformationFacet_birthdate, domain=BirthInformationFacet, range=Optional[Union[str, XSDDateTime]])

slots.SimpleNameFacet_familyName = Slot(uri=IDENTITY.familyName, name="SimpleNameFacet_familyName", curie=IDENTITY.curie('familyName'),
                   model_uri=MASTER.SimpleNameFacet_familyName, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.SimpleNameFacet_givenName = Slot(uri=IDENTITY.givenName, name="SimpleNameFacet_givenName", curie=IDENTITY.curie('givenName'),
                   model_uri=MASTER.SimpleNameFacet_givenName, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.SimpleNameFacet_honorificPrefix = Slot(uri=IDENTITY.honorificPrefix, name="SimpleNameFacet_honorificPrefix", curie=IDENTITY.curie('honorificPrefix'),
                   model_uri=MASTER.SimpleNameFacet_honorificPrefix, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.SimpleNameFacet_honorificSuffix = Slot(uri=IDENTITY.honorificSuffix, name="SimpleNameFacet_honorificSuffix", curie=IDENTITY.curie('honorificSuffix'),
                   model_uri=MASTER.SimpleNameFacet_honorificSuffix, domain=SimpleNameFacet, range=Optional[Union[str, List[str]]])

slots.GPSCoordinatesFacet_hdop = Slot(uri=LOCATION.hdop, name="GPSCoordinatesFacet_hdop", curie=LOCATION.curie('hdop'),
                   model_uri=MASTER.GPSCoordinatesFacet_hdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_pdop = Slot(uri=LOCATION.pdop, name="GPSCoordinatesFacet_pdop", curie=LOCATION.curie('pdop'),
                   model_uri=MASTER.GPSCoordinatesFacet_pdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_tdop = Slot(uri=LOCATION.tdop, name="GPSCoordinatesFacet_tdop", curie=LOCATION.curie('tdop'),
                   model_uri=MASTER.GPSCoordinatesFacet_tdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.GPSCoordinatesFacet_vdop = Slot(uri=LOCATION.vdop, name="GPSCoordinatesFacet_vdop", curie=LOCATION.curie('vdop'),
                   model_uri=MASTER.GPSCoordinatesFacet_vdop, domain=GPSCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_altitude = Slot(uri=LOCATION.altitude, name="LatLongCoordinatesFacet_altitude", curie=LOCATION.curie('altitude'),
                   model_uri=MASTER.LatLongCoordinatesFacet_altitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_latitude = Slot(uri=LOCATION.latitude, name="LatLongCoordinatesFacet_latitude", curie=LOCATION.curie('latitude'),
                   model_uri=MASTER.LatLongCoordinatesFacet_latitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.LatLongCoordinatesFacet_longitude = Slot(uri=LOCATION.longitude, name="LatLongCoordinatesFacet_longitude", curie=LOCATION.curie('longitude'),
                   model_uri=MASTER.LatLongCoordinatesFacet_longitude, domain=LatLongCoordinatesFacet, range=Optional[Union[Decimal, DecimalType]])

slots.SimpleAddressFacet_addressType = Slot(uri=LOCATION.addressType, name="SimpleAddressFacet_addressType", curie=LOCATION.curie('addressType'),
                   model_uri=MASTER.SimpleAddressFacet_addressType, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_country = Slot(uri=LOCATION.country, name="SimpleAddressFacet_country", curie=LOCATION.curie('country'),
                   model_uri=MASTER.SimpleAddressFacet_country, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_locality = Slot(uri=LOCATION.locality, name="SimpleAddressFacet_locality", curie=LOCATION.curie('locality'),
                   model_uri=MASTER.SimpleAddressFacet_locality, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_postalCode = Slot(uri=LOCATION.postalCode, name="SimpleAddressFacet_postalCode", curie=LOCATION.curie('postalCode'),
                   model_uri=MASTER.SimpleAddressFacet_postalCode, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_region = Slot(uri=LOCATION.region, name="SimpleAddressFacet_region", curie=LOCATION.curie('region'),
                   model_uri=MASTER.SimpleAddressFacet_region, domain=SimpleAddressFacet, range=Optional[str])

slots.SimpleAddressFacet_street = Slot(uri=LOCATION.street, name="SimpleAddressFacet_street", curie=LOCATION.curie('street'),
                   model_uri=MASTER.SimpleAddressFacet_street, domain=SimpleAddressFacet, range=Optional[str])

slots.GranularMarking_marking = Slot(uri=MARKING.marking, name="GranularMarking_marking", curie=MARKING.curie('marking'),
                   model_uri=MASTER.GranularMarking_marking, domain=GranularMarking, range=Optional[Union[str, List[str]]])

slots.GranularMarking_contentSelectors = Slot(uri=MARKING.contentSelectors, name="GranularMarking_contentSelectors", curie=MARKING.curie('contentSelectors'),
                   model_uri=MASTER.GranularMarking_contentSelectors, domain=GranularMarking, range=Optional[Union[str, List[str]]])

slots.LicenseMarking_definitionType = Slot(uri=MARKING.definitionType, name="LicenseMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MASTER.LicenseMarking_definitionType, domain=LicenseMarking, range=Optional[Union[str, List[str]]])

slots.LicenseMarking_license = Slot(uri=MARKING.license, name="LicenseMarking_license", curie=MARKING.curie('license'),
                   model_uri=MASTER.LicenseMarking_license, domain=LicenseMarking, range=str)

slots.MarkingDefinition_definition = Slot(uri=MARKING.definition, name="MarkingDefinition_definition", curie=MARKING.curie('definition'),
                   model_uri=MASTER.MarkingDefinition_definition, domain=MarkingDefinition, range=Optional[Union[str, List[str]]])

slots.MarkingDefinition_definitionType = Slot(uri=MARKING.definitionType, name="MarkingDefinition_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MASTER.MarkingDefinition_definitionType, domain=MarkingDefinition, range=str)

slots.ReleaseToMarking_definitionType = Slot(uri=MARKING.definitionType, name="ReleaseToMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MASTER.ReleaseToMarking_definitionType, domain=ReleaseToMarking, range=Optional[Union[str, List[str]]])

slots.ReleaseToMarking_authorizedIdentities = Slot(uri=MARKING.authorizedIdentities, name="ReleaseToMarking_authorizedIdentities", curie=MARKING.curie('authorizedIdentities'),
                   model_uri=MASTER.ReleaseToMarking_authorizedIdentities, domain=ReleaseToMarking, range=Union[str, List[str]])

slots.StatementMarking_definitionType = Slot(uri=MARKING.definitionType, name="StatementMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MASTER.StatementMarking_definitionType, domain=StatementMarking, range=Optional[Union[str, List[str]]])

slots.StatementMarking_statement = Slot(uri=CORE.statement, name="StatementMarking_statement", curie=CORE.curie('statement'),
                   model_uri=MASTER.StatementMarking_statement, domain=StatementMarking, range=str)

slots.TermsOfUseMarking_definitionType = Slot(uri=MARKING.definitionType, name="TermsOfUseMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MASTER.TermsOfUseMarking_definitionType, domain=TermsOfUseMarking, range=Optional[Union[str, List[str]]])

slots.TermsOfUseMarking_termsOfUse = Slot(uri=MARKING.termsOfUse, name="TermsOfUseMarking_termsOfUse", curie=MARKING.curie('termsOfUse'),
                   model_uri=MASTER.TermsOfUseMarking_termsOfUse, domain=TermsOfUseMarking, range=str)

slots.AntennaFacet_horizontalBeamWidth = Slot(uri=OBSERVABLE.horizontalBeamWidth, name="AntennaFacet_horizontalBeamWidth", curie=OBSERVABLE.curie('horizontalBeamWidth'),
                   model_uri=MASTER.AntennaFacet_horizontalBeamWidth, domain=AntennaFacet, range=Optional[Union[Decimal, DecimalType]])

slots.AntennaFacet_signalStrength = Slot(uri=OBSERVABLE.signalStrength, name="AntennaFacet_signalStrength", curie=OBSERVABLE.curie('signalStrength'),
                   model_uri=MASTER.AntennaFacet_signalStrength, domain=AntennaFacet, range=Optional[Union[Decimal, DecimalType]])

slots.ApplicationFacet_installedVersionHistory = Slot(uri=OBSERVABLE.installedVersionHistory, name="ApplicationFacet_installedVersionHistory", curie=OBSERVABLE.curie('installedVersionHistory'),
                   model_uri=MASTER.ApplicationFacet_installedVersionHistory, domain=ApplicationFacet, range=Optional[Union[Union[dict, "ApplicationVersion"], List[Union[dict, "ApplicationVersion"]]]])

slots.BrowserBookmarkFacet_urlTargeted = Slot(uri=OBSERVABLE.urlTargeted, name="BrowserBookmarkFacet_urlTargeted", curie=OBSERVABLE.curie('urlTargeted'),
                   model_uri=MASTER.BrowserBookmarkFacet_urlTargeted, domain=BrowserBookmarkFacet, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.CalendarEntryFacet_attendant = Slot(uri=OBSERVABLE.attendant, name="CalendarEntryFacet_attendant", curie=OBSERVABLE.curie('attendant'),
                   model_uri=MASTER.CalendarEntryFacet_attendant, domain=CalendarEntryFacet, range=Optional[Union[Union[dict, Identity], List[Union[dict, Identity]]]])

slots.CalendarEntryFacet_location = Slot(uri=ACTION.location, name="CalendarEntryFacet_location", curie=ACTION.curie('location'),
                   model_uri=MASTER.CalendarEntryFacet_location, domain=CalendarEntryFacet, range=Optional[Union[dict, Location]])

slots.CallFacet_participant = Slot(uri=ACTION.participant, name="CallFacet_participant", curie=ACTION.curie('participant'),
                   model_uri=MASTER.CallFacet_participant, domain=CallFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.CallFacet_to = Slot(uri=OBSERVABLE.to, name="CallFacet_to", curie=OBSERVABLE.curie('to'),
                   model_uri=MASTER.CallFacet_to, domain=CallFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.CapturedTelecommunicationsInformationFacet_captureCellSite = Slot(uri=OBSERVABLE.captureCellSite, name="CapturedTelecommunicationsInformationFacet_captureCellSite", curie=OBSERVABLE.curie('captureCellSite'),
                   model_uri=MASTER.CapturedTelecommunicationsInformationFacet_captureCellSite, domain=CapturedTelecommunicationsInformationFacet, range=Union[dict, "CellSite"])

slots.ComputerSpecificationFacet_networkInterface = Slot(uri=OBSERVABLE.networkInterface, name="ComputerSpecificationFacet_networkInterface", curie=OBSERVABLE.curie('networkInterface'),
                   model_uri=MASTER.ComputerSpecificationFacet_networkInterface, domain=ComputerSpecificationFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.ContactAffiliation_organizationLocation = Slot(uri=OBSERVABLE.organizationLocation, name="ContactAffiliation_organizationLocation", curie=OBSERVABLE.curie('organizationLocation'),
                   model_uri=MASTER.ContactAffiliation_organizationLocation, domain=ContactAffiliation, range=Optional[Union[dict, ContactAddress]])

slots.ContactAffiliation_contactEmail = Slot(uri=OBSERVABLE.contactEmail, name="ContactAffiliation_contactEmail", curie=OBSERVABLE.curie('contactEmail'),
                   model_uri=MASTER.ContactAffiliation_contactEmail, domain=ContactAffiliation, range=Optional[Union[dict, "ContactEmail"]])

slots.ContactAffiliation_contactMessaging = Slot(uri=OBSERVABLE.contactMessaging, name="ContactAffiliation_contactMessaging", curie=OBSERVABLE.curie('contactMessaging'),
                   model_uri=MASTER.ContactAffiliation_contactMessaging, domain=ContactAffiliation, range=Optional[Union[dict, "ContactMessaging"]])

slots.ContactAffiliation_contactPhone = Slot(uri=OBSERVABLE.contactPhone, name="ContactAffiliation_contactPhone", curie=OBSERVABLE.curie('contactPhone'),
                   model_uri=MASTER.ContactAffiliation_contactPhone, domain=ContactAffiliation, range=Optional[Union[dict, "ContactPhone"]])

slots.ContactAffiliation_contactProfile = Slot(uri=OBSERVABLE.contactProfile, name="ContactAffiliation_contactProfile", curie=OBSERVABLE.curie('contactProfile'),
                   model_uri=MASTER.ContactAffiliation_contactProfile, domain=ContactAffiliation, range=Optional[Union[dict, "ContactProfile"]])

slots.ContactAffiliation_contactURL = Slot(uri=OBSERVABLE.contactURL, name="ContactAffiliation_contactURL", curie=OBSERVABLE.curie('contactURL'),
                   model_uri=MASTER.ContactAffiliation_contactURL, domain=ContactAffiliation, range=Optional[Union[dict, "ContactURL"]])

slots.ContactEmail_contactEmailScope = Slot(uri=OBSERVABLE.contactEmailScope, name="ContactEmail_contactEmailScope", curie=OBSERVABLE.curie('contactEmailScope'),
                   model_uri=MASTER.ContactEmail_contactEmailScope, domain=ContactEmail, range=Optional[Union[str, "ContactEmailScopeEnum"]])

slots.ContactFacet_contactAddress = Slot(uri=OBSERVABLE.contactAddress, name="ContactFacet_contactAddress", curie=OBSERVABLE.curie('contactAddress'),
                   model_uri=MASTER.ContactFacet_contactAddress, domain=ContactFacet, range=Optional[Union[dict, ContactAddress]])

slots.ContactFacet_contactAffiliation = Slot(uri=OBSERVABLE.contactAffiliation, name="ContactFacet_contactAffiliation", curie=OBSERVABLE.curie('contactAffiliation'),
                   model_uri=MASTER.ContactFacet_contactAffiliation, domain=ContactFacet, range=Optional[Union[dict, ContactAffiliation]])

slots.ContactFacet_contactEmail = Slot(uri=OBSERVABLE.contactEmail, name="ContactFacet_contactEmail", curie=OBSERVABLE.curie('contactEmail'),
                   model_uri=MASTER.ContactFacet_contactEmail, domain=ContactFacet, range=Optional[Union[dict, ContactEmail]])

slots.ContactFacet_contactMessaging = Slot(uri=OBSERVABLE.contactMessaging, name="ContactFacet_contactMessaging", curie=OBSERVABLE.curie('contactMessaging'),
                   model_uri=MASTER.ContactFacet_contactMessaging, domain=ContactFacet, range=Optional[Union[dict, "ContactMessaging"]])

slots.ContactFacet_contactPhone = Slot(uri=OBSERVABLE.contactPhone, name="ContactFacet_contactPhone", curie=OBSERVABLE.curie('contactPhone'),
                   model_uri=MASTER.ContactFacet_contactPhone, domain=ContactFacet, range=Optional[Union[dict, "ContactPhone"]])

slots.ContactFacet_contactProfile = Slot(uri=OBSERVABLE.contactProfile, name="ContactFacet_contactProfile", curie=OBSERVABLE.curie('contactProfile'),
                   model_uri=MASTER.ContactFacet_contactProfile, domain=ContactFacet, range=Optional[Union[dict, "ContactProfile"]])

slots.ContactFacet_contactSIP = Slot(uri=OBSERVABLE.contactSIP, name="ContactFacet_contactSIP", curie=OBSERVABLE.curie('contactSIP'),
                   model_uri=MASTER.ContactFacet_contactSIP, domain=ContactFacet, range=Optional[Union[dict, "ContactSIP"]])

slots.ContactFacet_contactURL = Slot(uri=OBSERVABLE.contactURL, name="ContactFacet_contactURL", curie=OBSERVABLE.curie('contactURL'),
                   model_uri=MASTER.ContactFacet_contactURL, domain=ContactFacet, range=Optional[Union[dict, "ContactURL"]])

slots.ContactFacet_contactGroup = Slot(uri=OBSERVABLE.contactGroup, name="ContactFacet_contactGroup", curie=OBSERVABLE.curie('contactGroup'),
                   model_uri=MASTER.ContactFacet_contactGroup, domain=ContactFacet, range=Optional[str])

slots.ContactFacet_contactNote = Slot(uri=OBSERVABLE.contactNote, name="ContactFacet_contactNote", curie=OBSERVABLE.curie('contactNote'),
                   model_uri=MASTER.ContactFacet_contactNote, domain=ContactFacet, range=Optional[str])

slots.ContactFacet_nickname = Slot(uri=OBSERVABLE.nickname, name="ContactFacet_nickname", curie=OBSERVABLE.curie('nickname'),
                   model_uri=MASTER.ContactFacet_nickname, domain=ContactFacet, range=Optional[str])

slots.ContactListFacet_contact = Slot(uri=OBSERVABLE.contact, name="ContactListFacet_contact", curie=OBSERVABLE.curie('contact'),
                   model_uri=MASTER.ContactListFacet_contact, domain=ContactListFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.ContentDataFacet_hash = Slot(uri=OBSERVABLE.hash, name="ContentDataFacet_hash", curie=OBSERVABLE.curie('hash'),
                   model_uri=MASTER.ContentDataFacet_hash, domain=ContentDataFacet, range=Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]])

slots.ContentDataFacet_mimeType = Slot(uri=OBSERVABLE.mimeType, name="ContentDataFacet_mimeType", curie=OBSERVABLE.curie('mimeType'),
                   model_uri=MASTER.ContentDataFacet_mimeType, domain=ContentDataFacet, range=Optional[Union[str, List[str]]])

slots.DigitalAccountFacet_accountLogin = Slot(uri=OBSERVABLE.accountLogin, name="DigitalAccountFacet_accountLogin", curie=OBSERVABLE.curie('accountLogin'),
                   model_uri=MASTER.DigitalAccountFacet_accountLogin, domain=DigitalAccountFacet, range=Optional[Union[str, List[str]]])

slots.DiskFacet_partition = Slot(uri=OBSERVABLE.partition, name="DiskFacet_partition", curie=OBSERVABLE.curie('partition'),
                   model_uri=MASTER.DiskFacet_partition, domain=DiskFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.EXIFFacet_exifData = Slot(uri=OBSERVABLE.exifData, name="EXIFFacet_exifData", curie=OBSERVABLE.curie('exifData'),
                   model_uri=MASTER.EXIFFacet_exifData, domain=EXIFFacet, range=Optional[Union[Union[dict, "ControlledDictionary"], List[Union[dict, "ControlledDictionary"]]]])

slots.EmailMessageFacet_bodyMultipart = Slot(uri=OBSERVABLE.bodyMultipart, name="EmailMessageFacet_bodyMultipart", curie=OBSERVABLE.curie('bodyMultipart'),
                   model_uri=MASTER.EmailMessageFacet_bodyMultipart, domain=EmailMessageFacet, range=Optional[Union[Union[dict, "MimePartType"], List[Union[dict, "MimePartType"]]]])

slots.EmailMessageFacet_bcc = Slot(uri=OBSERVABLE.bcc, name="EmailMessageFacet_bcc", curie=OBSERVABLE.curie('bcc'),
                   model_uri=MASTER.EmailMessageFacet_bcc, domain=EmailMessageFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.EmailMessageFacet_cc = Slot(uri=OBSERVABLE.cc, name="EmailMessageFacet_cc", curie=OBSERVABLE.curie('cc'),
                   model_uri=MASTER.EmailMessageFacet_cc, domain=EmailMessageFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.EmailMessageFacet_references = Slot(uri=OBSERVABLE.references, name="EmailMessageFacet_references", curie=OBSERVABLE.curie('references'),
                   model_uri=MASTER.EmailMessageFacet_references, domain=EmailMessageFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.EmailMessageFacet_to = Slot(uri=OBSERVABLE.to, name="EmailMessageFacet_to", curie=OBSERVABLE.curie('to'),
                   model_uri=MASTER.EmailMessageFacet_to, domain=EmailMessageFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.EmailMessageFacet_categories = Slot(uri=OBSERVABLE.categories, name="EmailMessageFacet_categories", curie=OBSERVABLE.curie('categories'),
                   model_uri=MASTER.EmailMessageFacet_categories, domain=EmailMessageFacet, range=Optional[Union[str, List[str]]])

slots.EmailMessageFacet_labels = Slot(uri=OBSERVABLE.labels, name="EmailMessageFacet_labels", curie=OBSERVABLE.curie('labels'),
                   model_uri=MASTER.EmailMessageFacet_labels, domain=EmailMessageFacet, range=Optional[Union[str, List[str]]])

slots.EmailMessageFacet_receivedLines = Slot(uri=OBSERVABLE.receivedLines, name="EmailMessageFacet_receivedLines", curie=OBSERVABLE.curie('receivedLines'),
                   model_uri=MASTER.EmailMessageFacet_receivedLines, domain=EmailMessageFacet, range=Optional[Union[str, List[str]]])

slots.EncryptedStreamFacet_encryptionKey = Slot(uri=OBSERVABLE.encryptionKey, name="EncryptedStreamFacet_encryptionKey", curie=OBSERVABLE.curie('encryptionKey'),
                   model_uri=MASTER.EncryptedStreamFacet_encryptionKey, domain=EncryptedStreamFacet, range=Optional[Union[str, List[str]]])

slots.EncryptedStreamFacet_encryptionIV = Slot(uri=OBSERVABLE.encryptionIV, name="EncryptedStreamFacet_encryptionIV", curie=OBSERVABLE.curie('encryptionIV'),
                   model_uri=MASTER.EncryptedStreamFacet_encryptionIV, domain=EncryptedStreamFacet, range=Optional[Union[str, List[str]]])

slots.ExtractedStringsFacet_strings = Slot(uri=OBSERVABLE.strings, name="ExtractedStringsFacet_strings", curie=OBSERVABLE.curie('strings'),
                   model_uri=MASTER.ExtractedStringsFacet_strings, domain=ExtractedStringsFacet, range=Optional[Union[Union[dict, ExtractedString], List[Union[dict, ExtractedString]]]])

slots.FileFacet_isDirectory = Slot(uri=OBSERVABLE.isDirectory, name="FileFacet_isDirectory", curie=OBSERVABLE.curie('isDirectory'),
                   model_uri=MASTER.FileFacet_isDirectory, domain=FileFacet, range=Optional[Union[Union[bool, BooleanType], List[Union[bool, BooleanType]]]])

slots.FileFacet_sizeInBytes = Slot(uri=OBSERVABLE.sizeInBytes, name="FileFacet_sizeInBytes", curie=OBSERVABLE.curie('sizeInBytes'),
                   model_uri=MASTER.FileFacet_sizeInBytes, domain=FileFacet, range=Optional[int])

slots.FileFacet_fileName = Slot(uri=OBSERVABLE.fileName, name="FileFacet_fileName", curie=OBSERVABLE.curie('fileName'),
                   model_uri=MASTER.FileFacet_fileName, domain=FileFacet, range=Optional[Union[str, List[str]]])

slots.FileFacet_filePath = Slot(uri=OBSERVABLE.filePath, name="FileFacet_filePath", curie=OBSERVABLE.curie('filePath'),
                   model_uri=MASTER.FileFacet_filePath, domain=FileFacet, range=Optional[Union[str, List[str]]])

slots.FragmentFacet_fragmentIndex = Slot(uri=OBSERVABLE.fragmentIndex, name="FragmentFacet_fragmentIndex", curie=OBSERVABLE.curie('fragmentIndex'),
                   model_uri=MASTER.FragmentFacet_fragmentIndex, domain=FragmentFacet, range=Optional[Union[int, List[int]]])

slots.FragmentFacet_totalFragments = Slot(uri=OBSERVABLE.totalFragments, name="FragmentFacet_totalFragments", curie=OBSERVABLE.curie('totalFragments'),
                   model_uri=MASTER.FragmentFacet_totalFragments, domain=FragmentFacet, range=Optional[Union[int, List[int]]])

slots.GeoLocationEntryFacet_location = Slot(uri=ACTION.location, name="GeoLocationEntryFacet_location", curie=ACTION.curie('location'),
                   model_uri=MASTER.GeoLocationEntryFacet_location, domain=GeoLocationEntryFacet, range=Optional[Union[dict, Location]])

slots.GeoLocationTrackFacet_geoLocationEntry = Slot(uri=OBSERVABLE.geoLocationEntry, name="GeoLocationTrackFacet_geoLocationEntry", curie=OBSERVABLE.curie('geoLocationEntry'),
                   model_uri=MASTER.GeoLocationTrackFacet_geoLocationEntry, domain=GeoLocationTrackFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.GlobalFlagType_hexadecimalValue = Slot(uri=OBSERVABLE.hexadecimalValue, name="GlobalFlagType_hexadecimalValue", curie=OBSERVABLE.curie('hexadecimalValue'),
                   model_uri=MASTER.GlobalFlagType_hexadecimalValue, domain=GlobalFlagType, range=Optional[Union[hex, List[hex]]])

slots.ICMPConnectionFacet_icmpCode = Slot(uri=OBSERVABLE.icmpCode, name="ICMPConnectionFacet_icmpCode", curie=OBSERVABLE.curie('icmpCode'),
                   model_uri=MASTER.ICMPConnectionFacet_icmpCode, domain=ICMPConnectionFacet, range=Optional[Union[hex, List[hex]]])

slots.ICMPConnectionFacet_icmpType = Slot(uri=OBSERVABLE.icmpType, name="ICMPConnectionFacet_icmpType", curie=OBSERVABLE.curie('icmpType'),
                   model_uri=MASTER.ICMPConnectionFacet_icmpType, domain=ICMPConnectionFacet, range=Optional[Union[hex, List[hex]]])

slots.IExecActionType_execProgramHashes = Slot(uri=OBSERVABLE.execProgramHashes, name="IExecActionType_execProgramHashes", curie=OBSERVABLE.curie('execProgramHashes'),
                   model_uri=MASTER.IExecActionType_execProgramHashes, domain=IExecActionType, range=Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]])

slots.MemoryFacet_regionEndAddress = Slot(uri=OBSERVABLE.regionEndAddress, name="MemoryFacet_regionEndAddress", curie=OBSERVABLE.curie('regionEndAddress'),
                   model_uri=MASTER.MemoryFacet_regionEndAddress, domain=MemoryFacet, range=Optional[Union[hex, List[hex]]])

slots.MemoryFacet_regionStartAddress = Slot(uri=OBSERVABLE.regionStartAddress, name="MemoryFacet_regionStartAddress", curie=OBSERVABLE.curie('regionStartAddress'),
                   model_uri=MASTER.MemoryFacet_regionStartAddress, domain=MemoryFacet, range=Optional[Union[hex, List[hex]]])

slots.MemoryFacet_blockType = Slot(uri=OBSERVABLE.blockType, name="MemoryFacet_blockType", curie=OBSERVABLE.curie('blockType'),
                   model_uri=MASTER.MemoryFacet_blockType, domain=MemoryFacet, range=Optional[Union[str, "MemoryBlockTypeEnum"]])

slots.MessageFacet_from = Slot(uri=OBSERVABLE.from, name="MessageFacet_from", curie=OBSERVABLE.curie('from'),
                   model_uri=MASTER.MessageFacet_from, domain=MessageFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.MessageFacet_to = Slot(uri=OBSERVABLE.to, name="MessageFacet_to", curie=OBSERVABLE.curie('to'),
                   model_uri=MASTER.MessageFacet_to, domain=MessageFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.MessageThreadFacet_participant = Slot(uri=ACTION.participant, name="MessageThreadFacet_participant", curie=ACTION.curie('participant'),
                   model_uri=MASTER.MessageThreadFacet_participant, domain=MessageThreadFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.NTFSFileFacet_alternateDataStreams = Slot(uri=OBSERVABLE.alternateDataStreams, name="NTFSFileFacet_alternateDataStreams", curie=OBSERVABLE.curie('alternateDataStreams'),
                   model_uri=MASTER.NTFSFileFacet_alternateDataStreams, domain=NTFSFileFacet, range=Optional[Union[Union[dict, AlternateDataStream], List[Union[dict, AlternateDataStream]]]])

slots.NetworkConnectionFacet_src = Slot(uri=OBSERVABLE.src, name="NetworkConnectionFacet_src", curie=OBSERVABLE.curie('src'),
                   model_uri=MASTER.NetworkConnectionFacet_src, domain=NetworkConnectionFacet, range=Optional[Union[Union[dict, UcoObject], List[Union[dict, UcoObject]]]])

slots.NetworkConnectionFacet_dst = Slot(uri=OBSERVABLE.dst, name="NetworkConnectionFacet_dst", curie=OBSERVABLE.curie('dst'),
                   model_uri=MASTER.NetworkConnectionFacet_dst, domain=NetworkConnectionFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.NetworkInterfaceFacet_dhcpServer = Slot(uri=OBSERVABLE.dhcpServer, name="NetworkInterfaceFacet_dhcpServer", curie=OBSERVABLE.curie('dhcpServer'),
                   model_uri=MASTER.NetworkInterfaceFacet_dhcpServer, domain=NetworkInterfaceFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.NetworkInterfaceFacet_ip = Slot(uri=OBSERVABLE.ip, name="NetworkInterfaceFacet_ip", curie=OBSERVABLE.curie('ip'),
                   model_uri=MASTER.NetworkInterfaceFacet_ip, domain=NetworkInterfaceFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.NetworkInterfaceFacet_ipGateway = Slot(uri=OBSERVABLE.ipGateway, name="NetworkInterfaceFacet_ipGateway", curie=OBSERVABLE.curie('ipGateway'),
                   model_uri=MASTER.NetworkInterfaceFacet_ipGateway, domain=NetworkInterfaceFacet, range=Optional[Union[Union[dict, "ObservableObject"], List[Union[dict, "ObservableObject"]]]])

slots.Observation_name = Slot(uri=RDFS.label, name="Observation_name", curie=RDFS.curie('label'),
                   model_uri=MASTER.Observation_name, domain=Observation, range=str)

slots.OnlineServiceFacet_location = Slot(uri=ACTION.location, name="OnlineServiceFacet_location", curie=ACTION.curie('location'),
                   model_uri=MASTER.OnlineServiceFacet_location, domain=OnlineServiceFacet, range=Optional[Union[dict, Location]])

slots.OnlineServiceFacet_inetLocation = Slot(uri=OBSERVABLE.inetLocation, name="OnlineServiceFacet_inetLocation", curie=OBSERVABLE.curie('inetLocation'),
                   model_uri=MASTER.OnlineServiceFacet_inetLocation, domain=OnlineServiceFacet, range=Optional[Union[dict, ObservableObject]])

slots.OperatingSystemFacet_advertisingID = Slot(uri=OBSERVABLE.advertisingID, name="OperatingSystemFacet_advertisingID", curie=OBSERVABLE.curie('advertisingID'),
                   model_uri=MASTER.OperatingSystemFacet_advertisingID, domain=OperatingSystemFacet, range=Optional[Union[str, List[str]]])

slots.PDFFileFacet_pdfId0 = Slot(uri=OBSERVABLE.pdfId0, name="PDFFileFacet_pdfId0", curie=OBSERVABLE.curie('pdfId0'),
                   model_uri=MASTER.PDFFileFacet_pdfId0, domain=PDFFileFacet, range=Optional[Union[str, List[str]]])

slots.PathRelationFacet_path = Slot(uri=OBSERVABLE.path, name="PathRelationFacet_path", curie=OBSERVABLE.curie('path'),
                   model_uri=MASTER.PathRelationFacet_path, domain=PathRelationFacet, range=Optional[Union[str, List[str]]])

slots.ProcessFacet_arguments = Slot(uri=OBSERVABLE.arguments, name="ProcessFacet_arguments", curie=OBSERVABLE.curie('arguments'),
                   model_uri=MASTER.ProcessFacet_arguments, domain=ProcessFacet, range=Optional[Union[str, List[str]]])

slots.RecoveredObjectFacet_contentRecoveredStatus = Slot(uri=OBSERVABLE.contentRecoveredStatus, name="RecoveredObjectFacet_contentRecoveredStatus", curie=OBSERVABLE.curie('contentRecoveredStatus'),
                   model_uri=MASTER.RecoveredObjectFacet_contentRecoveredStatus, domain=RecoveredObjectFacet, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.RecoveredObjectFacet_metadataRecoveredStatus = Slot(uri=OBSERVABLE.metadataRecoveredStatus, name="RecoveredObjectFacet_metadataRecoveredStatus", curie=OBSERVABLE.curie('metadataRecoveredStatus'),
                   model_uri=MASTER.RecoveredObjectFacet_metadataRecoveredStatus, domain=RecoveredObjectFacet, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.RecoveredObjectFacet_nameRecoveredStatus = Slot(uri=OBSERVABLE.nameRecoveredStatus, name="RecoveredObjectFacet_nameRecoveredStatus", curie=OBSERVABLE.curie('nameRecoveredStatus'),
                   model_uri=MASTER.RecoveredObjectFacet_nameRecoveredStatus, domain=RecoveredObjectFacet, range=Optional[Union[str, "RecoveredObjectStatusEnum"]])

slots.SQLiteBlobFacet_rowIndex = Slot(uri=OBSERVABLE.rowIndex, name="SQLiteBlobFacet_rowIndex", curie=OBSERVABLE.curie('rowIndex'),
                   model_uri=MASTER.SQLiteBlobFacet_rowIndex, domain=SQLiteBlobFacet, range=Optional[Union[Union[int, PositiveIntegerType], List[Union[int, PositiveIntegerType]]]])

slots.TCPConnectionFacet_sourceFlags = Slot(uri=OBSERVABLE.sourceFlags, name="TCPConnectionFacet_sourceFlags", curie=OBSERVABLE.curie('sourceFlags'),
                   model_uri=MASTER.TCPConnectionFacet_sourceFlags, domain=TCPConnectionFacet, range=Optional[Union[hex, List[hex]]])

slots.TCPConnectionFacet_destinationFlags = Slot(uri=OBSERVABLE.destinationFlags, name="TCPConnectionFacet_destinationFlags", curie=OBSERVABLE.curie('destinationFlags'),
                   model_uri=MASTER.TCPConnectionFacet_destinationFlags, domain=TCPConnectionFacet, range=Optional[Union[str, List[str]]])

slots.TableFieldFacet_recordFieldValue = Slot(uri=OBSERVABLE.recordFieldValue, name="TableFieldFacet_recordFieldValue", curie=OBSERVABLE.curie('recordFieldValue'),
                   model_uri=MASTER.TableFieldFacet_recordFieldValue, domain=TableFieldFacet, range=Optional[str])

slots.TableFieldFacet_recordRowID = Slot(uri=OBSERVABLE.recordRowID, name="TableFieldFacet_recordRowID", curie=OBSERVABLE.curie('recordRowID'),
                   model_uri=MASTER.TableFieldFacet_recordRowID, domain=TableFieldFacet, range=Optional[str])

slots.TaskActionType_actionType = Slot(uri=OBSERVABLE.actionType, name="TaskActionType_actionType", curie=OBSERVABLE.curie('actionType'),
                   model_uri=MASTER.TaskActionType_actionType, domain=TaskActionType, range=Optional[Union[str, "TaskActionTypeEnum"]])

slots.TriggerType_triggerFrequency = Slot(uri=OBSERVABLE.triggerFrequency, name="TriggerType_triggerFrequency", curie=OBSERVABLE.curie('triggerFrequency'),
                   model_uri=MASTER.TriggerType_triggerFrequency, domain=TriggerType, range=Optional[Union[str, "TriggerFrequencyEnum"]])

slots.TriggerType_triggerType = Slot(uri=OBSERVABLE.triggerType, name="TriggerType_triggerType", curie=OBSERVABLE.curie('triggerType'),
                   model_uri=MASTER.TriggerType_triggerType, domain=TriggerType, range=Optional[Union[str, "TriggerTypeEnum"]])

slots.UNIXProcessFacet_openFileDescriptor = Slot(uri=OBSERVABLE.openFileDescriptor, name="UNIXProcessFacet_openFileDescriptor", curie=OBSERVABLE.curie('openFileDescriptor'),
                   model_uri=MASTER.UNIXProcessFacet_openFileDescriptor, domain=UNIXProcessFacet, range=Optional[Union[int, List[int]]])

slots.UNIXProcessFacet_ruid = Slot(uri=OBSERVABLE.ruid, name="UNIXProcessFacet_ruid", curie=OBSERVABLE.curie('ruid'),
                   model_uri=MASTER.UNIXProcessFacet_ruid, domain=UNIXProcessFacet, range=Optional[Union[Union[int, NonNegativeIntegerType], List[Union[int, NonNegativeIntegerType]]]])

slots.URLHistoryFacet_urlHistoryEntry = Slot(uri=OBSERVABLE.urlHistoryEntry, name="URLHistoryFacet_urlHistoryEntry", curie=OBSERVABLE.curie('urlHistoryEntry'),
                   model_uri=MASTER.URLHistoryFacet_urlHistoryEntry, domain=URLHistoryFacet, range=Optional[Union[Union[dict, URLHistoryEntry], List[Union[dict, URLHistoryEntry]]]])

slots.URLVisitFacet_urlTransitionType = Slot(uri=OBSERVABLE.urlTransitionType, name="URLVisitFacet_urlTransitionType", curie=OBSERVABLE.curie('urlTransitionType'),
                   model_uri=MASTER.URLVisitFacet_urlTransitionType, domain=URLVisitFacet, range=Optional[Union[str, "URLTransitionTypeEnum"]])

slots.WhoisFacet_nameServer = Slot(uri=OBSERVABLE.nameServer, name="WhoisFacet_nameServer", curie=OBSERVABLE.curie('nameServer'),
                   model_uri=MASTER.WhoisFacet_nameServer, domain=WhoisFacet, range=Optional[Union[Union[dict, ObservableObject], List[Union[dict, ObservableObject]]]])

slots.WhoisFacet_registrantIDs = Slot(uri=OBSERVABLE.registrantIDs, name="WhoisFacet_registrantIDs", curie=OBSERVABLE.curie('registrantIDs'),
                   model_uri=MASTER.WhoisFacet_registrantIDs, domain=WhoisFacet, range=Optional[Union[str, List[str]]])

slots.WhoisFacet_status = Slot(uri=OBSERVABLE.status, name="WhoisFacet_status", curie=OBSERVABLE.curie('status'),
                   model_uri=MASTER.WhoisFacet_status, domain=WhoisFacet, range=Optional[Union[str, "WhoisStatusTypeEnum"]])

slots.WhoisContactFacet_whoisContactType = Slot(uri=OBSERVABLE.whoisContactType, name="WhoisContactFacet_whoisContactType", curie=OBSERVABLE.curie('whoisContactType'),
                   model_uri=MASTER.WhoisContactFacet_whoisContactType, domain=WhoisContactFacet, range=Optional[Union[str, "WhoisContactTypeEnum"]])

slots.WindowsAccountFacet_groups = Slot(uri=OBSERVABLE.groups, name="WindowsAccountFacet_groups", curie=OBSERVABLE.curie('groups'),
                   model_uri=MASTER.WindowsAccountFacet_groups, domain=WindowsAccountFacet, range=Optional[Union[str, List[str]]])

slots.WindowsActiveDirectoryAccountFacet_activeDirectoryGroups = Slot(uri=OBSERVABLE.activeDirectoryGroups, name="WindowsActiveDirectoryAccountFacet_activeDirectoryGroups", curie=OBSERVABLE.curie('activeDirectoryGroups'),
                   model_uri=MASTER.WindowsActiveDirectoryAccountFacet_activeDirectoryGroups, domain=WindowsActiveDirectoryAccountFacet, range=Optional[Union[str, List[str]]])

slots.WindowsComputerSpecificationFacet_globalFlagList = Slot(uri=OBSERVABLE.globalFlagList, name="WindowsComputerSpecificationFacet_globalFlagList", curie=OBSERVABLE.curie('globalFlagList'),
                   model_uri=MASTER.WindowsComputerSpecificationFacet_globalFlagList, domain=WindowsComputerSpecificationFacet, range=Optional[Union[Union[dict, GlobalFlagType], List[Union[dict, GlobalFlagType]]]])

slots.WindowsComputerSpecificationFacet_domain = Slot(uri=OBSERVABLE.domain, name="WindowsComputerSpecificationFacet_domain", curie=OBSERVABLE.curie('domain'),
                   model_uri=MASTER.WindowsComputerSpecificationFacet_domain, domain=WindowsComputerSpecificationFacet, range=Optional[Union[str, List[str]]])

slots.WindowsPEBinaryFileFacet_sections = Slot(uri=OBSERVABLE.sections, name="WindowsPEBinaryFileFacet_sections", curie=OBSERVABLE.curie('sections'),
                   model_uri=MASTER.WindowsPEBinaryFileFacet_sections, domain=WindowsPEBinaryFileFacet, range=Optional[Union[Union[dict, "WindowsPESection"], List[Union[dict, "WindowsPESection"]]]])

slots.WindowsPEBinaryFileFacet_fileHeaderHashes = Slot(uri=OBSERVABLE.fileHeaderHashes, name="WindowsPEBinaryFileFacet_fileHeaderHashes", curie=OBSERVABLE.curie('fileHeaderHashes'),
                   model_uri=MASTER.WindowsPEBinaryFileFacet_fileHeaderHashes, domain=WindowsPEBinaryFileFacet, range=Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]])

slots.WindowsPEBinaryFileFacet_pointerToSymbolTable = Slot(uri=OBSERVABLE.pointerToSymbolTable, name="WindowsPEBinaryFileFacet_pointerToSymbolTable", curie=OBSERVABLE.curie('pointerToSymbolTable'),
                   model_uri=MASTER.WindowsPEBinaryFileFacet_pointerToSymbolTable, domain=WindowsPEBinaryFileFacet, range=Optional[Union[hex, List[hex]]])

slots.WindowsPEBinaryFileFacet_machine = Slot(uri=OBSERVABLE.machine, name="WindowsPEBinaryFileFacet_machine", curie=OBSERVABLE.curie('machine'),
                   model_uri=MASTER.WindowsPEBinaryFileFacet_machine, domain=WindowsPEBinaryFileFacet, range=Optional[Union[str, List[str]]])

slots.WindowsPEBinaryFileFacet_characteristics = Slot(uri=OBSERVABLE.characteristics, name="WindowsPEBinaryFileFacet_characteristics", curie=OBSERVABLE.curie('characteristics'),
                   model_uri=MASTER.WindowsPEBinaryFileFacet_characteristics, domain=WindowsPEBinaryFileFacet, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_majorLinkerVersion = Slot(uri=OBSERVABLE.majorLinkerVersion, name="WindowsPEOptionalHeader_majorLinkerVersion", curie=OBSERVABLE.curie('majorLinkerVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_majorLinkerVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, ByteType], List[Union[int, ByteType]]]])

slots.WindowsPEOptionalHeader_minorLinkerVersion = Slot(uri=OBSERVABLE.minorLinkerVersion, name="WindowsPEOptionalHeader_minorLinkerVersion", curie=OBSERVABLE.curie('minorLinkerVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_minorLinkerVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, ByteType], List[Union[int, ByteType]]]])

slots.WindowsPEOptionalHeader_addressOfEntryPoint = Slot(uri=OBSERVABLE.addressOfEntryPoint, name="WindowsPEOptionalHeader_addressOfEntryPoint", curie=OBSERVABLE.curie('addressOfEntryPoint'),
                   model_uri=MASTER.WindowsPEOptionalHeader_addressOfEntryPoint, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_baseOfCode = Slot(uri=OBSERVABLE.baseOfCode, name="WindowsPEOptionalHeader_baseOfCode", curie=OBSERVABLE.curie('baseOfCode'),
                   model_uri=MASTER.WindowsPEOptionalHeader_baseOfCode, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_checksum = Slot(uri=OBSERVABLE.checksum, name="WindowsPEOptionalHeader_checksum", curie=OBSERVABLE.curie('checksum'),
                   model_uri=MASTER.WindowsPEOptionalHeader_checksum, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_fileAlignment = Slot(uri=OBSERVABLE.fileAlignment, name="WindowsPEOptionalHeader_fileAlignment", curie=OBSERVABLE.curie('fileAlignment'),
                   model_uri=MASTER.WindowsPEOptionalHeader_fileAlignment, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_imageBase = Slot(uri=OBSERVABLE.imageBase, name="WindowsPEOptionalHeader_imageBase", curie=OBSERVABLE.curie('imageBase'),
                   model_uri=MASTER.WindowsPEOptionalHeader_imageBase, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_loaderFlags = Slot(uri=OBSERVABLE.loaderFlags, name="WindowsPEOptionalHeader_loaderFlags", curie=OBSERVABLE.curie('loaderFlags'),
                   model_uri=MASTER.WindowsPEOptionalHeader_loaderFlags, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_numberOfRVAAndSizes = Slot(uri=OBSERVABLE.numberOfRVAAndSizes, name="WindowsPEOptionalHeader_numberOfRVAAndSizes", curie=OBSERVABLE.curie('numberOfRVAAndSizes'),
                   model_uri=MASTER.WindowsPEOptionalHeader_numberOfRVAAndSizes, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sectionAlignment = Slot(uri=OBSERVABLE.sectionAlignment, name="WindowsPEOptionalHeader_sectionAlignment", curie=OBSERVABLE.curie('sectionAlignment'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sectionAlignment, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfCode = Slot(uri=OBSERVABLE.sizeOfCode, name="WindowsPEOptionalHeader_sizeOfCode", curie=OBSERVABLE.curie('sizeOfCode'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfCode, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfHeaders = Slot(uri=OBSERVABLE.sizeOfHeaders, name="WindowsPEOptionalHeader_sizeOfHeaders", curie=OBSERVABLE.curie('sizeOfHeaders'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfHeaders, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfHeapCommit = Slot(uri=OBSERVABLE.sizeOfHeapCommit, name="WindowsPEOptionalHeader_sizeOfHeapCommit", curie=OBSERVABLE.curie('sizeOfHeapCommit'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfHeapCommit, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfHeapReserve = Slot(uri=OBSERVABLE.sizeOfHeapReserve, name="WindowsPEOptionalHeader_sizeOfHeapReserve", curie=OBSERVABLE.curie('sizeOfHeapReserve'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfHeapReserve, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfImage = Slot(uri=OBSERVABLE.sizeOfImage, name="WindowsPEOptionalHeader_sizeOfImage", curie=OBSERVABLE.curie('sizeOfImage'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfImage, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfInitializedData = Slot(uri=OBSERVABLE.sizeOfInitializedData, name="WindowsPEOptionalHeader_sizeOfInitializedData", curie=OBSERVABLE.curie('sizeOfInitializedData'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfInitializedData, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfStackCommit = Slot(uri=OBSERVABLE.sizeOfStackCommit, name="WindowsPEOptionalHeader_sizeOfStackCommit", curie=OBSERVABLE.curie('sizeOfStackCommit'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfStackCommit, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfStackReserve = Slot(uri=OBSERVABLE.sizeOfStackReserve, name="WindowsPEOptionalHeader_sizeOfStackReserve", curie=OBSERVABLE.curie('sizeOfStackReserve'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfStackReserve, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_sizeOfUninitializedData = Slot(uri=OBSERVABLE.sizeOfUninitializedData, name="WindowsPEOptionalHeader_sizeOfUninitializedData", curie=OBSERVABLE.curie('sizeOfUninitializedData'),
                   model_uri=MASTER.WindowsPEOptionalHeader_sizeOfUninitializedData, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_win32VersionValue = Slot(uri=OBSERVABLE.win32VersionValue, name="WindowsPEOptionalHeader_win32VersionValue", curie=OBSERVABLE.curie('win32VersionValue'),
                   model_uri=MASTER.WindowsPEOptionalHeader_win32VersionValue, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsPEOptionalHeader_dllCharacteristics = Slot(uri=OBSERVABLE.dllCharacteristics, name="WindowsPEOptionalHeader_dllCharacteristics", curie=OBSERVABLE.curie('dllCharacteristics'),
                   model_uri=MASTER.WindowsPEOptionalHeader_dllCharacteristics, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_magic = Slot(uri=OBSERVABLE.magic, name="WindowsPEOptionalHeader_magic", curie=OBSERVABLE.curie('magic'),
                   model_uri=MASTER.WindowsPEOptionalHeader_magic, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_majorImageVersion = Slot(uri=OBSERVABLE.majorImageVersion, name="WindowsPEOptionalHeader_majorImageVersion", curie=OBSERVABLE.curie('majorImageVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_majorImageVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_majorOSVersion = Slot(uri=OBSERVABLE.majorOSVersion, name="WindowsPEOptionalHeader_majorOSVersion", curie=OBSERVABLE.curie('majorOSVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_majorOSVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_majorSubsystemVersion = Slot(uri=OBSERVABLE.majorSubsystemVersion, name="WindowsPEOptionalHeader_majorSubsystemVersion", curie=OBSERVABLE.curie('majorSubsystemVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_majorSubsystemVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_minorImageVersion = Slot(uri=OBSERVABLE.minorImageVersion, name="WindowsPEOptionalHeader_minorImageVersion", curie=OBSERVABLE.curie('minorImageVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_minorImageVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_minorOSVersion = Slot(uri=OBSERVABLE.minorOSVersion, name="WindowsPEOptionalHeader_minorOSVersion", curie=OBSERVABLE.curie('minorOSVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_minorOSVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_minorSubsystemVersion = Slot(uri=OBSERVABLE.minorSubsystemVersion, name="WindowsPEOptionalHeader_minorSubsystemVersion", curie=OBSERVABLE.curie('minorSubsystemVersion'),
                   model_uri=MASTER.WindowsPEOptionalHeader_minorSubsystemVersion, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPEOptionalHeader_subsystem = Slot(uri=OBSERVABLE.subsystem, name="WindowsPEOptionalHeader_subsystem", curie=OBSERVABLE.curie('subsystem'),
                   model_uri=MASTER.WindowsPEOptionalHeader_subsystem, domain=WindowsPEOptionalHeader, range=Optional[Union[Union[int, UnsignedShortType], List[Union[int, UnsignedShortType]]]])

slots.WindowsPESection_hashes = Slot(uri=OBSERVABLE.hashes, name="WindowsPESection_hashes", curie=OBSERVABLE.curie('hashes'),
                   model_uri=MASTER.WindowsPESection_hashes, domain=WindowsPESection, range=Optional[Union[Union[dict, "Hash"], List[Union[dict, "Hash"]]]])

slots.WindowsPrefetchFacet_accessedDirectory = Slot(uri=OBSERVABLE.accessedDirectory, name="WindowsPrefetchFacet_accessedDirectory", curie=OBSERVABLE.curie('accessedDirectory'),
                   model_uri=MASTER.WindowsPrefetchFacet_accessedDirectory, domain=WindowsPrefetchFacet, range=Optional[Union[Union[dict, ObservableObject], List[Union[dict, ObservableObject]]]])

slots.WindowsPrefetchFacet_accessedFile = Slot(uri=OBSERVABLE.accessedFile, name="WindowsPrefetchFacet_accessedFile", curie=OBSERVABLE.curie('accessedFile'),
                   model_uri=MASTER.WindowsPrefetchFacet_accessedFile, domain=WindowsPrefetchFacet, range=Optional[Union[Union[dict, ObservableObject], List[Union[dict, ObservableObject]]]])

slots.WindowsRegistrykeyFacet_registryValues = Slot(uri=OBSERVABLE.registryValues, name="WindowsRegistrykeyFacet_registryValues", curie=OBSERVABLE.curie('registryValues'),
                   model_uri=MASTER.WindowsRegistrykeyFacet_registryValues, domain=WindowsRegistrykeyFacet, range=Optional[Union[Union[dict, "WindowsRegistryValue"], List[Union[dict, "WindowsRegistryValue"]]]])

slots.WindowsServiceFacet_descriptions = Slot(uri=OBSERVABLE.descriptions, name="WindowsServiceFacet_descriptions", curie=OBSERVABLE.curie('descriptions'),
                   model_uri=MASTER.WindowsServiceFacet_descriptions, domain=WindowsServiceFacet, range=Optional[Union[str, List[str]]])

slots.WindowsTaskFacet_actionList = Slot(uri=OBSERVABLE.actionList, name="WindowsTaskFacet_actionList", curie=OBSERVABLE.curie('actionList'),
                   model_uri=MASTER.WindowsTaskFacet_actionList, domain=WindowsTaskFacet, range=Optional[Union[Union[dict, TaskActionType], List[Union[dict, TaskActionType]]]])

slots.WindowsTaskFacet_triggerList = Slot(uri=OBSERVABLE.triggerList, name="WindowsTaskFacet_triggerList", curie=OBSERVABLE.curie('triggerList'),
                   model_uri=MASTER.WindowsTaskFacet_triggerList, domain=WindowsTaskFacet, range=Optional[Union[str, List[str]]])

slots.WindowsTaskFacet_flags = Slot(uri=OBSERVABLE.flags, name="WindowsTaskFacet_flags", curie=OBSERVABLE.curie('flags'),
                   model_uri=MASTER.WindowsTaskFacet_flags, domain=WindowsTaskFacet, range=Optional[Union[str, "TaskFlagEnum"]])

slots.WindowsTaskFacet_priority = Slot(uri=OBSERVABLE.priority, name="WindowsTaskFacet_priority", curie=OBSERVABLE.curie('priority'),
                   model_uri=MASTER.WindowsTaskFacet_priority, domain=WindowsTaskFacet, range=Optional[Union[str, "TaskPriorityEnum"]])

slots.WindowsTaskFacet_status = Slot(uri=OBSERVABLE.status, name="WindowsTaskFacet_status", curie=OBSERVABLE.curie('status'),
                   model_uri=MASTER.WindowsTaskFacet_status, domain=WindowsTaskFacet, range=Optional[Union[str, "TaskStatusEnum"]])

slots.WindowsThreadFacet_parameterAddress = Slot(uri=OBSERVABLE.parameterAddress, name="WindowsThreadFacet_parameterAddress", curie=OBSERVABLE.curie('parameterAddress'),
                   model_uri=MASTER.WindowsThreadFacet_parameterAddress, domain=WindowsThreadFacet, range=Optional[Union[hex, List[hex]]])

slots.WindowsThreadFacet_startAddress = Slot(uri=OBSERVABLE.startAddress, name="WindowsThreadFacet_startAddress", curie=OBSERVABLE.curie('startAddress'),
                   model_uri=MASTER.WindowsThreadFacet_startAddress, domain=WindowsThreadFacet, range=Optional[Union[hex, List[hex]]])

slots.WindowsThreadFacet_stackSize = Slot(uri=OBSERVABLE.stackSize, name="WindowsThreadFacet_stackSize", curie=OBSERVABLE.curie('stackSize'),
                   model_uri=MASTER.WindowsThreadFacet_stackSize, domain=WindowsThreadFacet, range=Optional[Union[Union[int, NonNegativeIntegerType], List[Union[int, NonNegativeIntegerType]]]])

slots.WindowsThreadFacet_threadID = Slot(uri=OBSERVABLE.threadID, name="WindowsThreadFacet_threadID", curie=OBSERVABLE.curie('threadID'),
                   model_uri=MASTER.WindowsThreadFacet_threadID, domain=WindowsThreadFacet, range=Optional[Union[Union[int, NonNegativeIntegerType], List[Union[int, NonNegativeIntegerType]]]])

slots.WindowsThreadFacet_creationFlags = Slot(uri=OBSERVABLE.creationFlags, name="WindowsThreadFacet_creationFlags", curie=OBSERVABLE.curie('creationFlags'),
                   model_uri=MASTER.WindowsThreadFacet_creationFlags, domain=WindowsThreadFacet, range=Optional[Union[Union[int, UnsignedIntegerType], List[Union[int, UnsignedIntegerType]]]])

slots.WindowsVolumeFacet_driveType = Slot(uri=OBSERVABLE.driveType, name="WindowsVolumeFacet_driveType", curie=OBSERVABLE.curie('driveType'),
                   model_uri=MASTER.WindowsVolumeFacet_driveType, domain=WindowsVolumeFacet, range=Optional[Union[str, "WindowsDriveTypeEnum"]])

slots.WindowsVolumeFacet_windowsVolumeAttributes = Slot(uri=OBSERVABLE.windowsVolumeAttributes, name="WindowsVolumeFacet_windowsVolumeAttributes", curie=OBSERVABLE.curie('windowsVolumeAttributes'),
                   model_uri=MASTER.WindowsVolumeFacet_windowsVolumeAttributes, domain=WindowsVolumeFacet, range=Optional[str])

slots.WirelessNetworkConnectionFacet_wirelessNetworkSecurityMode = Slot(uri=OBSERVABLE.wirelessNetworkSecurityMode, name="WirelessNetworkConnectionFacet_wirelessNetworkSecurityMode", curie=OBSERVABLE.curie('wirelessNetworkSecurityMode'),
                   model_uri=MASTER.WirelessNetworkConnectionFacet_wirelessNetworkSecurityMode, domain=WirelessNetworkConnectionFacet, range=Optional[Union[str, "WirelessNetworkSecurityModeEnum"]])

slots.LogicalPattern_patternExpression = Slot(uri=PATTERN.patternExpression, name="LogicalPattern_patternExpression", curie=PATTERN.curie('patternExpression'),
                   model_uri=MASTER.LogicalPattern_patternExpression, domain=LogicalPattern, range=Optional[str])

slots.BuildInformationType_compilers = Slot(uri=TOOL.compilers, name="BuildInformationType_compilers", curie=TOOL.curie('compilers'),
                   model_uri=MASTER.BuildInformationType_compilers, domain=BuildInformationType, range=Optional[Union[Union[dict, "CompilerType"], List[Union[dict, "CompilerType"]]]])

slots.BuildInformationType_libraries = Slot(uri=TOOL.libraries, name="BuildInformationType_libraries", curie=TOOL.curie('libraries'),
                   model_uri=MASTER.BuildInformationType_libraries, domain=BuildInformationType, range=Optional[Union[Union[dict, "LibraryType"], List[Union[dict, "LibraryType"]]]])

slots.Tool__references = Slot(uri=TOOL._references, name="Tool__references", curie=TOOL.curie('_references'),
                   model_uri=MASTER.Tool__references, domain=Tool, range=Optional[Union[Union[str, IriType], List[Union[str, IriType]]]])

slots.ControlledDictionary_entry = Slot(uri=TYPES.entry, name="ControlledDictionary_entry", curie=TYPES.curie('entry'),
                   model_uri=MASTER.ControlledDictionary_entry, domain=ControlledDictionary, range=Optional[Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]]])

slots.Dictionary_entry = Slot(uri=TYPES.entry, name="Dictionary_entry", curie=TYPES.curie('entry'),
                   model_uri=MASTER.Dictionary_entry, domain=Dictionary, range=Union[Union[dict, "DictionaryEntry"], List[Union[dict, "DictionaryEntry"]]])

slots.DictionaryEntry_key = Slot(uri=TYPES.key, name="DictionaryEntry_key", curie=TYPES.curie('key'),
                   model_uri=MASTER.DictionaryEntry_key, domain=DictionaryEntry, range=str)

slots.DictionaryEntry_value = Slot(uri=CORE.value, name="DictionaryEntry_value", curie=CORE.curie('value'),
                   model_uri=MASTER.DictionaryEntry_value, domain=DictionaryEntry, range=str)

slots.Hash_hashValue = Slot(uri=TYPES.hashValue, name="Hash_hashValue", curie=TYPES.curie('hashValue'),
                   model_uri=MASTER.Hash_hashValue, domain=Hash, range=hex)

slots.Hash_hashMethod = Slot(uri=TYPES.hashMethod, name="Hash_hashMethod", curie=TYPES.curie('hashMethod'),
                   model_uri=MASTER.Hash_hashMethod, domain=Hash, range=str)

slots.Thread_item = Slot(uri=COLLECTIONS.item, name="Thread_item", curie=COLLECTIONS.curie('item'),
                   model_uri=MASTER.Thread_item, domain=Thread, range=Optional[Union[Union[dict, "ThreadItem"], List[Union[dict, "ThreadItem"]]]])

slots.ThreadItem_itemContent = Slot(uri=COLLECTIONS.itemContent, name="ThreadItem_itemContent", curie=COLLECTIONS.curie('itemContent'),
                   model_uri=MASTER.ThreadItem_itemContent, domain=ThreadItem, range=Optional[Union[Union[dict, "CoItem"], List[Union[dict, "CoItem"]]]])

slots.Collection_element = Slot(uri=COLLECTIONS.element, name="Collection_element", curie=COLLECTIONS.curie('element'),
                   model_uri=MASTER.Collection_element, domain=Collection, range=Optional[Union[Union[dict, "Thing"], List[Union[dict, "Thing"]]]])

slots.Collection_size = Slot(uri=COLLECTIONS.size, name="Collection_size", curie=COLLECTIONS.curie('size'),
                   model_uri=MASTER.Collection_size, domain=Collection, range=Optional[Union[int, PositiveInteger]])

slots.List_lastItem = Slot(uri=COLLECTIONS.lastItem, name="List_lastItem", curie=COLLECTIONS.curie('lastItem'),
                   model_uri=MASTER.List_lastItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_firstItem = Slot(uri=COLLECTIONS.firstItem, name="List_firstItem", curie=COLLECTIONS.curie('firstItem'),
                   model_uri=MASTER.List_firstItem, domain=List, range=Optional[Union[dict, "ListItem"]])

slots.List_item = Slot(uri=COLLECTIONS.item, name="List_item", curie=COLLECTIONS.curie('item'),
                   model_uri=MASTER.List_item, domain=List, range=Optional[Union[Union[dict, "ListItem"], List[Union[dict, "ListItem"]]]])

slots.ListItem__index = Slot(uri=COLLECTIONS._index, name="ListItem__index", curie=COLLECTIONS.curie('_index'),
                   model_uri=MASTER.ListItem__index, domain=ListItem, range=Union[int, PositiveInteger])