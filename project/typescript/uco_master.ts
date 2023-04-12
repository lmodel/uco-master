/**
 * Collection that can have a number of copies of each object
 */
export interface Bag  extends Collection  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * A group of objects that can be considered as a whole.
 */
export interface Collection  extends Thing  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * Element belonging to a bag
 */
export interface CoItem  extends Thing  {
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
}
/**
 * An ordered array of items, that can be present in multiple copies
 */
export interface List  extends Bag  {
    /**
     * The link to every item of the bag
     */item?: ListItem[],
    /**
     * The link to the last item of the list.
     */lastItem?: ListItem,
    /**
     * The link to the first item of the list.
     */firstItem?: ListItem,
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * element belonging to a list
 */
export interface ListItem  extends CoItem  {
    /**
     * A number identifying the position, starting from 1, of a particular list item within a list.
     */_index?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
}
/**
 * A collection that cannot contain duplicate elements.
 */
export interface Set  extends Collection  {
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}

export interface Thing  {
}
/**
 * "A victim is a role played by a person or organization that is/was the target of some malicious action."
 */
export interface Victim  extends NeutralRole  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A victim targeting is a grouping of characteristics unique to people or organizations that are the target of some malicious activity."
 */
export interface VictimTargeting  extends Victim  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A benevolent role is a role with positive and/or beneficial intent.
 */
export interface BenevolentRole  extends Role  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A malicious role is a role with malevolent intent.
 */
export interface MaliciousRole  extends Role  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A neutral role is a role with impartial intent.
 */
export interface NeutralRole  extends Role  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A role is a usual or customary function based on contextual perspective.
 */
export interface Role  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An annotation is an assertion made in relation to one or more objects.
 */
export interface Annotation  extends Assertion  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * A textual statement of an assertion.
     */statement?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An assertion is a statement declared to be true.
 */
export interface Assertion  extends UcoObject  {
    /**
     * A textual statement of an assertion.
     */statement?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An attributed name is a name of an entity issued by some attributed naming authority.
 */
export interface AttributedName  extends UcoObject  {
    /**
     * Specifies the naming authority that issued the name of the entity.
     */namingAuthority?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A bundle is a container for a grouping of UCO content with no presumption of shared context.
 */
export interface Bundle  extends EnclosingCompilation  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A compilation is a grouping of things.
 */
export interface Compilation  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some information.
 */
export interface ConfidenceFacet  extends Facet  {
    /**
     * An asserted level of certainty in the accuracy of some information.
     */confidence?: string,
}
/**
 * A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed on a given day, all accounts associated with a given person).
 */
export interface ContextualCompilation  extends Compilation  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A controlled vocabulary is an explicitly constrained set of string values.
 */
export interface ControlledVocabulary  extends UcoObject  {
    /**
     * A reference to a specification for an explicitly constrained set of string values. The specification may be unstructured (e.g., web page listing string values) or structured (e.g. RDF/OWL enumeration).
     */constrainingVocabularyReference?: string,
    /**
     * The name of an explicitly constrained set of string values.
     */constrainingVocabularyName?: string,
    /**
     * A string value.
     */value?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An enclosing compilation is a container for a grouping of things.
 */
export interface EnclosingCompilation  extends Compilation  {
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * Characteristics of a reference to a resource outside of the UCO.
 */
export interface ExternalReference  extends UcoInherentCharacterizationThing  {
    /**
     * A URL for some information defined external to the UCO context.
     */referenceURL?: string,
    /**
     * A description of the context relevant to the definition of a particular external reference identifier.
     */definingContext?: string,
    /**
     * An identifier for some information defined external to the UCO context.
     */externalIdentifier?: string,
}
/**
 * A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
 */
export interface Facet  extends UcoInherentCharacterizationThing  {
}
/**
 * A grouping is a compilation of referenced UCO content with a shared context.
 */
export interface Grouping  extends ContextualCompilation  {
    /**
     * A description of particular contextual affinity.
     */context?: string,
    /**
     * Specifies one or more UcoObjects.
     */object?: UcoObject[],
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This class is an ontological structural abstraction for this concept. Implementations of this concept should utilize the identity:Identity class.
 */
export interface IdentityAbstraction  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An item is a distinct article or unit.
 */
export interface Item  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This class is an ontological structural abstraction for this concept. Implementations of this concept should utilize the marking MarkingDefinition class.
 */
export interface MarkingDefinitionAbstraction  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
 */
export interface ModusOperandi  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to another object in some way.
 */
export interface Relationship  extends UcoObject  {
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * A specification whether or not a relationship assertion is limited to the context FROM a source object(s) TO a target object.
     */isDirectional?: string,
    /**
     * A characterization of the nature of a relationship between objects.
     */kindOfRelationship?: string,
    /**
     * The originating node of a specified relationship.
     */source?: UcoObject[],
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * The terminating node of a specified relationship.
     */target?: UcoObject,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a UCO domain object.
 */
export interface UcoInherentCharacterizationThing  extends UcoThing  {
}
/**
 * A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent, unifying and interoperable foundation for all explicit and inter-relatable content objects.
 */
export interface UcoObject  extends UcoThing  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * UcoThing is the top-level class within UCO.
 */
export interface UcoThing  {
}
/**
 * "A controlled dictionary is a list of (term/key, value) pairs where each term/key exists no more than once and is constrained to an explicitly defined set of values."
 */
export interface ControlledDictionary  extends Dictionary  {
    /**
     * "A dictionary entry."
     */entry?: DictionaryEntry[],
}
/**
 * "A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an explicitly defined set of values."
 */
export interface ControlledDictionaryEntry  extends DictionaryEntry  {
    /**
     * "A key property of a single dictionary entry."
     */key?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "A dictionary is list of (term/key, value) pairs with each term/key existing no more than once."
 */
export interface Dictionary  extends UcoInherentCharacterizationThing  {
    /**
     * "A dictionary entry."
     */entry?: DictionaryEntry[],
}
/**
 * "A dictionary entry is a single (term/key, value) pair."
 */
export interface DictionaryEntry  extends UcoInherentCharacterizationThing  {
    /**
     * "A key property of a single dictionary entry."
     */key?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "A hash is a grouping of characteristics unique to the result of applying a mathematical algorithm that maps data of arbitrary size to a bit string (the 'hash') and is a one-way function, that is, a function which is practically infeasible to invert. This is commonly used for integrity checking of data. [based on https://en.wikipedia.org/wiki/Cryptographic_hash_function]"
 */
export interface Hash  extends UcoInherentCharacterizationThing  {
    /**
     * "A cryptographic hash value."
     */hashValue?: string,
    /**
     * "A particular cryptographic hashing method (e.g., MD5)."
     */hashMethod?: string,
}
/**
 * "A semi-ordered array of items, that can be present in multiple copies.  Implemetation of a UCO Thread is similar to a Collections Ontology List, except a Thread may fork and merge - that is, one of its members may have two or more direct successors, and two or more direct predecessors."
 */
export interface Thread  extends Bag, UcoThing  {
    /**
     * The link to every item of the bag
     */item?: ThreadItem[],
    /**
     * The link to the members of a collection
     */element?: Thing[],
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * "A ThreadItem is a member of a thread."
 */
export interface ThreadItem  extends UcoThing  {
    /**
     * The link to the actual resource to which the item refers.
     */itemContent?: CoItem[],
}
/**
 * "An analytic tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of explanation, interpretation or logical reasoning."
 */
export interface AnalyticTool  extends Tool  {
    /**
     * "The creator organization for a particular tool."
     */_creator?: Identity,
    /**
     * "References to information describing a particular tool."
     */_references?: string,
    /**
     * "An appropriate service pack descriptor for a particular tool."
     */servicePack?: string,
    /**
     * "The type of tool."
     */toolType?: string,
    /**
     * "An appropriate version descriptor of a particular tool."
     */_version?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A build facet is a grouping of characteristics unique to a particular version of a software."
 */
export interface BuildFacet  extends Facet  {
    /**
     * "Describes how a particular tool was built."
     */buildInformation?: BuildInformationType,
}
/**
 * "A build information type is a grouping of characteristics that describe how a particular version of software was converted from source code to executable code."
 */
export interface BuildInformationType  extends UcoInherentCharacterizationThing  {
    /**
     * "How the build utility was configured for a particular build of a particular software."
     */buildConfiguration?: Configuration,
    /**
     * "Identifies the utility used to build a software."
     */buildUtility?: BuildUtilityType,
    /**
     * "The compilers utilized during a particular build of a particular software."
     */compilers?: CompilerType[],
    /**
     * "The libraries incorporated into a particular build of a software."
     */libraries?: LibraryType[],
    /**
     * "The compilation date for the build of a software."
     */compilationDate?: string,
    /**
     * "An externally defined unique identifier for a particular build of a software."
     */buildID?: string,
    /**
     * "Relevant label for a particular build of a particular software."
     */buildLabel?: string,
    /**
     * "The output log of the build process for a software."
     */buildOutputLog?: string,
    /**
     * "The project name of a build of a software."
     */buildProject?: string,
    /**
     * "The actual build script for a particular build of a particular software."
     */buildScript?: string,
    /**
     * "The appropriate version descriptor of a particular build of a particular software."
     */buildVersion?: string,
}
/**
 * "A build utility type characterizes the tool used to convert from source code to executable code for a particular version of software."
 */
export interface BuildUtilityType  extends UcoInherentCharacterizationThing  {
    /**
     * "The informally defined name of the utility used to build a particular software."
     */buildUtilityName?: string,
    /**
     * "Specifies the Common Platform Enumeration identifier for the software."
     */_cpeid?: string,
    /**
     * "Specifies the SWID tag for the software."
     */_swid?: string,
}
/**
 * "A compiler type is a grouping of characteristics unique to a specific program that translates computer code written in one programming language (the source language) into another language (the target language). Typically a program that translates source code from a high-level programming language to a lower-level language (e.g., assembly language, object code, or machine code) to create an executable program. [based on https://en.wikipedia.org/wiki/Compiler]"
 */
export interface CompilerType  extends UcoInherentCharacterizationThing  {
    /**
     * "An informal description of a compiler."
     */compilerInformalDescription?: string,
    /**
     * "Specifies the Common Platform Enumeration identifier for the software."
     */_cpeid?: string,
    /**
     * "Specifies the SWID tag for the software."
     */_swid?: string,
}
/**
 * "A ConfiguredTool is a Tool that is known to be configured to run in a more specified manner than some unconfigured or less-configured Tool."
 */
export interface ConfiguredTool  extends Tool  {
    /**
     * A configuration used by an object.
     */usesConfiguration?: Configuration,
    /**
     * The object which has been configured to run in a more specified manner than another object.  This property is expected to have a more specific range when associated with a class, such as a configured Tool having this property have a range of a Tool.
     */isConfigurationOf?: UcoObject,
    /**
     * "The creator organization for a particular tool."
     */_creator?: Identity,
    /**
     * "References to information describing a particular tool."
     */_references?: string,
    /**
     * "An appropriate service pack descriptor for a particular tool."
     */servicePack?: string,
    /**
     * "The type of tool."
     */toolType?: string,
    /**
     * "An appropriate version descriptor of a particular tool."
     */_version?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A defensive tool is an artifact of hardware and/or software utilized to accomplish a task or purpose of guarding."
 */
export interface DefensiveTool  extends Tool  {
    /**
     * "The creator organization for a particular tool."
     */_creator?: Identity,
    /**
     * "References to information describing a particular tool."
     */_references?: string,
    /**
     * "An appropriate service pack descriptor for a particular tool."
     */servicePack?: string,
    /**
     * "The type of tool."
     */toolType?: string,
    /**
     * "An appropriate version descriptor of a particular tool."
     */_version?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A library type is a grouping of characteristics unique to a collection of resources incorporated into the build of a software."
 */
export interface LibraryType  extends UcoInherentCharacterizationThing  {
    /**
     * "The name of the library."
     */libraryName?: string,
    /**
     * "The version of the library."
     */libraryVersion?: string,
}
/**
 * "A malicious tool is an artifact of hardware and/or software utilized to accomplish a malevolent task or purpose."
 */
export interface MaliciousTool  extends Tool  {
    /**
     * "The creator organization for a particular tool."
     */_creator?: Identity,
    /**
     * "References to information describing a particular tool."
     */_references?: string,
    /**
     * "An appropriate service pack descriptor for a particular tool."
     */servicePack?: string,
    /**
     * "The type of tool."
     */toolType?: string,
    /**
     * "An appropriate version descriptor of a particular tool."
     */_version?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A tool is an element of hardware and/or software utilized to carry out a particular function."
 */
export interface Tool  extends UcoObject  {
    /**
     * "The creator organization for a particular tool."
     */_creator?: Identity,
    /**
     * "References to information describing a particular tool."
     */_references?: string,
    /**
     * "An appropriate service pack descriptor for a particular tool."
     */servicePack?: string,
    /**
     * "The type of tool."
     */toolType?: string,
    /**
     * "An appropriate version descriptor of a particular tool."
     */_version?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An Address Facet is a grouping of characteristics unique to an administrative identifier for a geolocation associated with a specific identity.
 */
export interface AddressFacet  extends IdentityFacet  {
    address?: Location,
}
/**
 * An affiliation is a grouping of characteristics unique to the established affiliations of an entity.
 */
export interface AffiliationFacet  extends IdentityFacet  {
}
/**
 * Birth information is a grouping of characteristics unique to information pertaining to the birth of an entity.
 */
export interface BirthInformationFacet  extends IdentityFacet  {
    birthdate?: string,
}
/**
 * Country of residence is a grouping of characteristics unique to information related to the country, or countries, where an entity resides.
 */
export interface CountryOfResidenceFacet  extends IdentityFacet  {
}
/**
 * Events is a grouping of characteristics unique to information related to specific relevant things that happen in the lifetime of an entity.
 */
export interface EventsFacet  extends IdentityFacet  {
}
/**
 * Identifier is a grouping of characteristics unique to information that uniquely and specifically identities an entity.
 */
export interface IdentifierFacet  extends IdentityFacet  {
}
/**
 * An identity is a grouping of identifying characteristics unique to an individual or organization.
 */
export interface Identity  extends IdentityAbstraction  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * An IdentityFacet is a grouping of characteristics unique to a particular aspect of an identity.
 */
export interface IdentityFacet  extends Facet  {
}
/**
 * Languages is a grouping of characteristics unique to specific syntactically and grammatically standardized forms of communication (human or computer) in which an entity has proficiency (comprehends, speaks, reads, or writes).
 */
export interface LanguagesFacet  extends IdentityFacet  {
}
/**
 * Nationality is a grouping of characteristics unique to the condition of an entity belonging to a particular nation.
 */
export interface NationalityFacet  extends IdentityFacet  {
}
/**
 * Occupation is a grouping of characteristics unique to the job or profession of an entity.
 */
export interface OccupationFacet  extends IdentityFacet  {
}
/**
 * An organization is a grouping of identifying characteristics unique to a group of people who work together in an organized way for a shared purpose. [based on https://dictionary.cambridge.org/us/dictionary/english/organization]
 */
export interface Organization  extends Identity  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * Organization details is a grouping of characteristics unique to an identity representing an administrative and functional structure.
 */
export interface OrganizationDetailsFacet  extends IdentityFacet  {
}
/**
 * A person is a grouping of identifying characteristics unique to a human being regarded as an individual. [based on https://www.lexico.com/en/definition/person]
 */
export interface Person  extends Identity  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * Personal details is a grouping of characteristics unique to an identity representing an individual person.
 */
export interface PersonalDetailsFacet  extends IdentityFacet  {
}
/**
 * Physical info is a grouping of characteristics unique to the outwardly observable nature of an individual person.
 */
export interface PhysicalInfoFacet  extends IdentityFacet  {
}
/**
 * Qualification is a grouping of characteristics unique to particular skills, capabilities or their related achievements (educational, professional, etc.) of an entity.
 */
export interface QualificationFacet  extends IdentityFacet  {
}
/**
 * <Needs fleshed out from CIQ>
 */
export interface RelatedIdentityFacet  extends IdentityFacet  {
}
/**
 * A simple name facet is a grouping of characteristics unique to the personal name (e.g., Dr. John Smith Jr.) held by an identity.
 */
export interface SimpleNameFacet  extends IdentityFacet  {
    familyName?: string,
    givenName?: string,
    honorificPrefix?: string,
    honorificSuffix?: string,
}
/**
 * Visa is a grouping of characteristics unique to information related to a person's ability to enter, leave, or stay for a specified period of time in a country.
 */
export interface VisaFacet  extends IdentityFacet  {
}
/**
 * A GPS coordinates facet is a grouping of characteristics unique to the expression of quantified dilution of precision (DOP) for an asserted set of geolocation coordinates typically associated with satellite navigation such as the Global Positioning System (GPS).
 */
export interface GPSCoordinatesFacet  extends Facet  {
    /**
     * The horizontal dilution of precision of the GPS location.
     */hdop?: number,
    /**
     * The positional (3D) dilution of precision of the GPS location.
     */pdop?: number,
    /**
     * The temporal dilution of precision of the GPS location.
     */tdop?: number,
    /**
     * The vertical dilution of precision of the GPS location.
     */vdop?: number,
}
/**
 * A lat long coordinates facet is a grouping of characteristics unique to the expression of a geolocation as the intersection of specific latitude, longitude, and altitude values.
 */
export interface LatLongCoordinatesFacet  extends Facet  {
    /**
     * The altitude coordinate of a geolocation.
     */altitude?: number,
    /**
     * The latitude coordinate of a geolocation.
     */latitude?: number,
    /**
     * The longitude coordinate of a geolocation.
     */longitude?: number,
}
/**
 * A location is a geospatial place, site, or position.
 */
export interface Location  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A simple address facet is a grouping of characteristics unique to a geolocation expressed as an administrative address.
 */
export interface SimpleAddressFacet  extends Facet  {
    /**
     * The type of the address, for instance home or work.
     */addressType?: string,
    /**
     * The name of the geolocation country.
     */country?: string,
    /**
     * The name of the geolocation locality (e.g., city).
     */locality?: string,
    /**
     * The zip-code.
     */postalCode?: string,
    /**
     * The name of the geolocation region (e.g., state).
     */region?: string,
    /**
     * The name of the street.
     */street?: string,
}
/**
 * A configuration is a grouping of characteristics unique to a set of parameters or initial settings for the use of a tool, application, software, or other cyber object.
 */
export interface Configuration  extends UcoObject  {
    /**
     * A single configuration setting entry item for a tool or other software.
     */configurationEntry?: ConfigurationEntry[],
    /**
     * The relevant configuration dependencies for a tool, application, software, or other cyber object.
     */dependencies?: Dependency[],
    /**
     * Description of the various relevant usage context assumptions for a tool or other software .
     */usageContextAssumptions?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A configuration entry is a grouping of characteristics unique to a particular parameter or initial setting for the use of a tool, application, software, or other cyber object.
 */
export interface ConfigurationEntry  extends UcoInherentCharacterizationThing  {
    /**
     * The structured value of a configuration setting entry instance.
     */itemObject?: UcoObject[],
    /**
     * A description of a configuration setting entry item.
     */itemDescription?: string,
    /**
     * The name of a configuration setting entry item.
     */itemName?: string,
    /**
     * The type of a configuration setting entry item.
     */itemType?: string,
    /**
     * The value of a configuration setting entry instance.
     */itemValue?: string,
}
/**
 * A dependency is a grouping of characteristics unique to something that a tool or other software relies on to function as intended.
 */
export interface Dependency  extends UcoInherentCharacterizationThing  {
    /**
     * A description of a tool or other software dependency.
     */dependencyDescription?: string,
    /**
     * The type of a tool or other software dependency.
     */dependencyType?: string,
}

export interface Time  {
}

export interface TimeRange  {
}

export interface TimeStamp  {
}
/**
 * A logical pattern is a grouping of characteristics unique to an informational pattern expressed via a structured pattern expression following the rules of logic.
 */
export interface LogicalPattern  extends Pattern  {
    /**
     * An explicit logical pattern expression.
     */patternExpression?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A pattern is a combination of properties, acts, tendencies, etc., forming a consistent or characteristic arrangement.
 */
export interface Pattern  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A pattern expression is a grouping of characteristics unique to an explicit logical expression defining a pattern (e.g., regular expression, SQL Select expression, etc.).
 */
export interface PatternExpression  extends UcoInherentCharacterizationThing  {
}
/**
 * "An API (application programming interface) is a computing interface that defines interactions between multiple software or mixed hardware-software intermediaries. It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used, the conventions to follow, etc. [based on https://en.wikipedia.org/wiki/API]"
 */
export interface API  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An ARP cache is a collection of Address Resolution Protocol (ARP) entries (mostly dynamic) that are created when an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on https://en.wikipedia.org/wiki/ARP_cache]"
 */
export interface ARPCache  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An ARP cache entry is a single Address Resolution Protocol (ARP) response record that is created when an IP address is resolved to a MAC address (so the computer can effectively communicate with the IP address). [based on https://en.wikipedia.org/wiki/ARP_cache]"
 */
export interface ARPCacheEntry  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An account is an arrangement with an entity to enable and control the provision of some capability or service."
 */
export interface Account  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An account authentication facet is a grouping of characteristics unique to the mechanism of accessing an account."
 */
export interface AccountAuthenticationFacet  extends Facet  {
    /**
     * "The date and time that the password was last changed."
     */passwordLastChanged?: string,
    /**
     * "Specifies an authentication password."
     */password?: string,
    /**
     * "The type of password, for instance plain-text or encrypted."
     */passwordType?: string,
}
/**
 * "An account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service."
 */
export interface AccountFacet  extends Facet  {
    /**
     * "The issuer of this account."
     */accountIssuer?: UcoObject,
    /**
     * "Specifies the owner of an observable Object."
     */owner?: UcoObject,
    /**
     * "Indicates whether the network connection is still active."
     */isActive?: string,
    /**
     * "Specifies the date in which the registered domain will expire."
     */expirationDate?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "The unique identifier for the account."
     */accountIdentifier?: string,
    /**
     * "The type of account, for instance bank, phone, application, service, etc."
     */accountType?: string,
}
/**
 * "An adaptor is a device that physically converts the pin outputs but does not alter the underlying protocol (e.g. uSD to SD, CF to ATA, etc.)"
 */
export interface Adaptor  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An address is an identifier assigned to enable routing and management of information."
 */
export interface Address  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An alternate data stream is data content stored within an NTFS file that is independent of the standard content stream of the file and isHidden from access by default NTFS file viewing mechanisms."
 */
export interface AlternateDataStream  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An alternate data stream facet is a grouping of characteristics unique to data content stored within an NTFS file that is independent of the standard content stream of the file and isHidden from access by default NTFS file viewing mechanisms."
 */
export interface AlternateDataStreamFacet  extends Facet  {
    /**
     * "Specifies any hashes computed over the section."
     */hashes?: Hash,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * The number of item belonging to a collection.
     */size?: string,
}
/**
 * "An Android device is a device running the Android operating system. [based on https://en.wikipedia.org/wiki/Android_(operating_system)]"
 */
export interface AndroidDevice  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An Android device facet is a grouping of characteristics unique to an Android device. [based on https://en.wikipedia.org/wiki/Android_(operating_system)]"
 */
export interface AndroidDeviceFacet  extends Facet  {
    /**
     * "A string that uniquely identifies a build of the Android operating system. [based on https://developer.android.com/reference/android/os/Build#FINGERPRINT]"
     */androidFingerprint?: string,
    /**
     * "The user-visible version string. E.g., '1.0' or '3.4b5' or 'bananas'. This field is an opaque string. Do not assume that its value has any particular structure or that values of RELEASE from different releases can be somehow ordered. [based on https://developer.android.com/reference/android/os/Build.VERSION#RELEASE]"
     */androidVersion?: string,
    /**
     * "A 64-bit number (expressed as a hexadecimal string), unique to each combination of app-signing key, user, and device. [based on https://developer.android.com/reference/android/provider/Settings.Secure#ANDROID_ID"
     */androidID?: string,
    /**
     * "Root access through the Android Debug Bridge (ADB) daemon observed to be enabled. [based on https://developer.android.com/studio/command-line/adb]"
     */isADBRootEnabled?: string,
    /**
     * "Root access through Linux SU binary observed to be enabled. [based on https://en.wikipedia.org/wiki/Rooting_(Android)]"
     */isSURootEnabled?: string,
}
/**
 * An android phone is a smart phone that applies the Android mobile operating system.
 */
export interface AndroidPhone  extends AndroidDevice, SmartPhone  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An antenna alignment facet contains the metadata surrounding the cell tower's antenna position."
 */
export interface AntennaFacet  extends Facet  {
    /**
     * "The height (in meters) of the antenna from the ground."
     */antennaHeight?: number,
    /**
     * "The median rotation in degrees around a vertical axis of the cell antenna sector accessed."
     */azimuth?: number,
    /**
     * "The angle in degrees of the antenna from the local horizontal plane."
     */elevation?: number,
    /**
     * "The width of the antenna beam in degrees."
     */horizontalBeamWidth?: number,
    /**
     * "The strength of the antenna signal."
     */signalStrength?: number,
    /**
     * "The angle in degrees of the radial rotation around its main beam direction."
     */skew?: number,
}
/**
 * "An apple device is a smart device that applies either the MacOS or iOS operating system"
 */
export interface AppleDevice  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An appliance is a purpose-built computer with software or firmware that is designed to provide a specific computing capability or resource. [based on https://en.wikipedia.org/wiki/computer_appliance]"
 */
export interface Appliance  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An application is a particular software program designed for end users."
 */
export interface Application  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An application account is an account within a particular software program designed for end users."
 */
export interface ApplicationAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An application account facet is a grouping of characteristics unique to an account within a particular software program designed for end users."
 */
export interface ApplicationAccountFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
}
/**
 * "An application facet is a grouping of characteristics unique to a particular software program designed for end users."
 */
export interface ApplicationFacet  extends Facet  {
    numberOfLaunches?: number,
    applicationIdentifier?: string,
    /**
     * "Specifies the history of installed application version(s)."
     */installedVersionHistory?: ApplicationVersion[],
    operatingSystem?: ObservableObject,
    version?: string,
}
/**
 * "An application version is a grouping of characteristics unique to a particular software program version."
 */
export interface ApplicationVersion  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the date the operating sytem or application was installed."
     */installDate?: string,
    /**
     * "Specifies the date the operating system or application was uninstalled."
     */uninstallDate?: string,
    version?: string,
}
/**
 * "An archive file is a file that is composed of one or more computer files along with metadata."
 */
export interface ArchiveFile  extends File  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An archive file facet is a grouping of characteristics unique to a file that is composed of one or more computer files along with metadata."
 */
export interface ArchiveFileFacet  extends Facet  {
    /**
     * "The type of a file archive, e.g. ZIP, GZIP or RAR."
     */archiveType?: string,
    comment?: string,
    version?: string,
}
/**
 * "audio is a digital representation of sound."
 */
export interface Audio  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An audio facet is a grouping of characteristics unique to a digital representation of sound."
 */
export interface AudioFacet  extends Facet  {
    /**
     * "The bitrate of the audio in bits per second."
     */bitRate?: number,
    /**
     * "The duration of the phone call in seconds."
     */duration?: number,
    /**
     * "The type of a audio. For example: music or speech."
     */audioType?: string,
    /**
     * "The format of the audio. For example: mp3 or flac."
     */format?: string,
}
/**
 * "An autonomous system is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the Internet. [based on https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]"
 */
export interface AutonomousSystem  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An autonomous system facet is a grouping of characteristics unique to a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the Internet. [based on https://en.wikipedia.org/wiki/Autonomous_system_(Internet)]"
 */
export interface AutonomousSystemFacet  extends Facet  {
    number?: number,
    asHandle?: string,
    /**
     * "specifies the name of the Regional Internet Registry (RIR) which allocated the IP address contained in a WHOIS entry."
     */regionalInternetRegistry?: string,
}
/**
 * "A blackberry phone is a smart phone that applies the Blackberry OS mobile operating system. (Blackberry 10 re-introduces Blackberry OS, prior to that the OS was Android.)"
 */
export interface BlackBerryPhone  extends SmartPhone  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A block device node is a UNIX filesystem special file that serves as a conduit to communicate with devices, providing buffered randomly accesible input and output. Block device nodes are used to apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]"
 */
export interface BlockDeviceNode  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Bluetooth address is a Bluetooth standard conformant identifier assigned to a Bluetooth device to enable routing and management of Bluetooth standards conformant communication to or from that device."
 */
export interface BluetoothAddress  extends MACAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Bluetooth address facet is a grouping of characteristics unique to a Bluetooth standard conformant identifier assigned to a Bluetooth device to enable routing and management of Bluetooth standards conformant communication to or from that device."
 */
export interface BluetoothAddressFacet  extends MACAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "A bot configuration is a set of contextual settings for a software application that runs automated tasks (scripts) over the Internet at a much higher rate than would be possible for a human alone."
 */
export interface BotConfiguration  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A browser bookmark is a saved shortcut that directs a WWW (World Wide Web) browser software program to a particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]"
 */
export interface BrowserBookmark  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A browser bookmark facet is a grouping of characteristics unique to a saved shortcut that directs a WWW (World Wide Web) browser software program to a particular WWW accessible resource. [based on https://techterms.com/definition/bookmark]"
 */
export interface BrowserBookmarkFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The date and time at which the Object was accessed."
     */accessedTime?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "The target of the bookmark."
     */urlTargeted?: string,
    /**
     * "Specifies the number of times a URL has been visited by a particular web browser."
     */visitCount?: number,
    /**
     * "The folder containing the bookmark."
     */bookmarkPath?: string,
}
/**
 * "A browser cookie is a piece of of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]"
 */
export interface BrowserCookie  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A browser cookie facet is a grouping of characteristics unique to a piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing. [based on https://en.wikipedia.org/wiki/HTTP_cookie]"
 */
export interface BrowserCookieFacet  extends Facet  {
    /**
     * "The date and time at which the Object was accessed."
     */accessedTime?: string,
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The domain for which the cookie is stored, for example nfi.minjus.nl."
     */cookieDomain?: ObservableObject,
    /**
     * "The name of the cookie."
     */cookieName?: string,
    /**
     * "String representation of the path of the cookie."
     */cookiePath?: string,
    /**
     * "The date and time at which the validity of the object expires."
     */expirationTime?: string,
    /**
     * "Is the cookie secure? If the cookie isSecure it cannot be delivered over an unencrypted session such as http."
     */isSecure?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
}
/**
 * "A calendar is a collection of appointments, meetings, and events."
 */
export interface Calendar  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A calendar entry is an appointment, meeting or event within a collection of appointments, meetings and events."
 */
export interface CalendarEntry  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A calendar entry facet is a grouping of characteristics unique to an appointment, meeting, or event within a collection of appointments, meetings, and events."
 */
export interface CalendarEntryFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The attendants of the event."
     */attendant?: Identity[],
    /**
     * "Is the event marked as private?"
     */isPrivate?: string,
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * "An associated location."
     */location?: Location,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "Specifies the owner of an observable Object."
     */owner?: UcoObject,
    remindTime?: string,
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * "The duration of the phone call in seconds."
     */duration?: number,
    /**
     * "The status of the event, for instance accepted, pending or cancelled."
     */eventStatus?: string,
    /**
     * "The type of the event, for example 'information', 'warning' or 'error'."
     */eventType?: string,
    /**
     * "Recurrence of the event."
     */recurrence?: string,
    /**
     * "The subject of the email."
     */subject?: string,
}
/**
 * "A calendar facet is a grouping of characteristics unique to a collection of appointments, meetings, and events."
 */
export interface CalendarFacet  extends Facet  {
    /**
     * "Specifies the owner of an observable Object."
     */owner?: UcoObject,
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
}
/**
 * "A call is a connection as part of a realtime cyber communication between one or more parties."
 */
export interface Call  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A call facet is a grouping of characteristics unique to a connection as part of a realtime cyber communication between one or more parties."
 */
export interface CallFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * "The duration of the phone call in seconds."
     */duration?: number,
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: ObservableObject[],
    /**
     * "The type of a phone call,for example incoming, outgoing, missed."
     */callType?: string,
    /**
     * "The phone number of the initiating party."
     */from?: ObservableObject,
    /**
     * "The receiver's phone number."
     */to?: ObservableObject[],
}

export interface CapturedTelecommunicationsInformation  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A captured telecommunications information facet represents certain information within captured or intercepted telecommunications data."
 */
export interface CapturedTelecommunicationsInformationFacet  extends Facet  {
    /**
     * "Specifies the cell site accessed."
     */captureCellSite?: CellSite,
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * "State of the call in a call Detail Record (e.g. idle)."
     */interceptedCallState?: string,
}

export interface CellSite  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A cell site facet contains the metadata surrounding the cell site."
 */
export interface CellSiteFacet  extends Facet  {
    /**
     * "The country code represents the country of the cell site. For GSM, this is the Mobile Country Code (MCC)."
     */cellSiteCountryCode?: string,
    /**
     * "Specifies the unique number used to identify each Cell Site within a location area code."
     */cellSiteIdentifier?: string,
    /**
     * "The location area code is a unique number of current location area of the cell site. A location area is a set of cell site that are grouped together to optimize signalling. For GSM, this is the LAC."
     */cellSiteLocationAreaCode?: string,
    /**
     * "This code identifies the mobile operator of the cell site. For GSM, this is the Mobile network  Code (MNC) and for CMDA this is the network identifier (NID)."
     */cellSiteNetworkCode?: string,
    /**
     * "Specifies the technology used by the Cell Site (e.g., GSM, CDMA, or LTE)."
     */cellSiteType?: string,
}
/**
 * "A character device node is a UNIX filesystem special file that serves as a conduit to communicate with devices, providing only a serial stream of input or accepting a serial stream of output. Character device nodes are used to apply access rights to the devices and to direct operations on the files to the appropriate device drivers. [based on https://en.wikipedia.org/wiki/Unix_file_types]"
 */
export interface CharacterDeviceNode  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "Code is a direct representation (source, byte or binary) of a collection of computer instructions that form software which tell a computer how to work. [based on https://en.wikipedia.org/wiki/Software]"
 */
export interface Code  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A compressed stream facet is a grouping of characteristics unique to the application of a size-reduction process to a body of data content."
 */
export interface CompressedStreamFacet  extends Facet  {
    /**
     * "The compressionRatio of the compressed data."
     */compressionRatio?: number,
    /**
     * "The algorithm used to compress the data."
     */compressionMethod?: string,
}
/**
 * "A computer is an electronic device for storing and processing data, typically in binary, according to instructions given to it in a variable program. [based on 'computer.' Oxford English Dictionary, Oxford University Press, 2022.]"
 */
export interface Computer  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A computer specification is the hardware and software of a programmable electronic device that can store, retrieve, and process data. {based on merriam-webster.com/dictionary/computer]"
 */
export interface ComputerSpecification  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A computer specificaiton facet is a grouping of characteristics unique to the hardware and software of a programmable electronic device that can store, retrieve, and process data. [based on merriam-webster.com/dictionary/computer]"
 */
export interface ComputerSpecificationFacet  extends Facet  {
    /**
     * "Specifies the date of the BIOS (e.g. the datestamp of the BIOS revision)."
     */biosDate?: string,
    /**
     * "Specifies the date the BIOS was released."
     */biosReleaseDate?: string,
    /**
     * "Specifies the current date on the system."
     */currentSystemDate?: string,
    /**
     * "Specifies the localTime on the system."
     */localTime?: string,
    systemTime?: string,
    /**
     * "Specifies the amount of physical memory available on the system, in bytes."
     */availableRam?: number,
    /**
     * "Specifies the total amount of physical memory present on the system, in bytes."
     */totalRam?: number,
    /**
     * "Specifies the manufacturer of the BIOS."
     */biosManufacturer?: string,
    /**
     * "Specifies the serialNumber of the BIOS."
     */biosSerialNumber?: string,
    /**
     * "Specifies the version of the BIOS."
     */biosVersion?: string,
    /**
     * "Specifies the name of the CPU used by the system."
     */cpu?: string,
    /**
     * "Specifies the name of the CPU family used by the system."
     */cpuFamily?: string,
    /**
     * "Specifies the name of the GPU used by the system."
     */gpu?: string,
    /**
     * "Specifies the name of the GPU family used by the system."
     */gpuFamily?: string,
    /**
     * "Specifies the hostname of the system."
     */hostname?: string,
    /**
     * "Specifies the list of networkInterfaces present on the system."
     */networkInterface?: ObservableObject[],
    /**
     * "Specifies the specific architecture (e.g. x86) used by the CPU of the system."
     */processorArchitecture?: string,
    /**
     * "Specifies the time zone used by the system, taking daylight savings time (DST) into account."
     */timezoneDST?: string,
    /**
     * "Specifies the time zone used by the system, without taking daylight savings time (DST) into account."
     */timezoneStandard?: string,
    /**
     * "Specifies the duration that represents the current amount of time that the system has been up."
     */uptime?: string,
}
/**
 * "A configured software is a Software that is known to be configured to run in a more specified manner than some unconfigured or less-configured Software."
 */
export interface ConfiguredSoftware  extends Software  {
    /**
     * A configuration used by an object.
     */usesConfiguration?: Configuration,
    /**
     * The object which has been configured to run in a more specified manner than another object.  This property is expected to have a more specific range when associated with a class, such as a configured Tool having this property have a range of a Tool.
     */isConfigurationOf?: UcoObject,
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A contact is a set of identification and communication related details for a single entity."
 */
export interface Contact  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A contact address is a grouping of characteristics unique to a geolocation address of a contact entity."
 */
export interface ContactAddress  extends UcoInherentCharacterizationThing  {
    /**
     * "An administrative address for a particular geolocation."
     */geoLocationAddress?: Location,
    /**
     * "contactAddressScope specifies the relevant scope (home, work, school, etc) for a geolocation address of a contact entity."
     */contactAddressScope?: string,
}
/**
 * "A contact affiliation is a grouping of characteristics unique to details of an organizational affiliation for a single contact entity."
 */
export interface ContactAffiliation  extends UcoInherentCharacterizationThing  {
    /**
     * "The name of the organization a contact works for or is assocciated with."
     */contactOrganization?: Organization,
    /**
     * "Specifies a geolocation address of an organization."
     */organizationLocation?: ContactAddress,
    /**
     * "contactEmail specifies information characterizing details for contacting a contact entity by email."
     */contactEmail?: ContactEmail,
    /**
     * "contactMessaging specifies information characterizing details for contacting a contact entity by digital messaging."
     */contactMessaging?: ContactMessaging,
    /**
     * "contactPhone specifies information characterizing details for contacting a contact entity by telephone."
     */contactPhone?: ContactPhone,
    /**
     * "contactProfile specifies information characterizing details for contacting a contact entity by online service."
     */contactProfile?: ContactProfile,
    /**
     * "contactURL specifies information characterizing details for contacting a contact entity by Uniform Resource Locator (URL)."
     */contactURL?: ContactURL,
    /**
     * "Specifies a particular suborganization (division, branch, office, etc.) that exists within a larger organization."
     */organizationDepartment?: string,
    /**
     * "Specifies the title or role that a person plays within an organization."
     */organizationPosition?: string,
}
/**
 * "A contact email is a grouping of characteristics unique to details for contacting a contact entity by email."
 */
export interface ContactEmail  extends UcoInherentCharacterizationThing  {
    /**
     * "An emailAddress."
     */emailAddress?: ObservableObject,
    /**
     * "contactEmailScope specifies the relevant scope (home, work, school, etc) of details for contacting a contact entity by email."
     */contactEmailScope?: string,
}
/**
 * "A contact facet is a grouping of characteristics unique to a set of identification and communication related details for a single entity."
 */
export interface ContactFacet  extends Facet  {
    /**
     * "contactAddress specifies information characterizing a geolocation address of a contact entity."
     */contactAddress?: ContactAddress,
    /**
     * "contactAffiliation specifies information characterizing details of an organizational affiliation for a single contact entity."
     */contactAffiliation?: ContactAffiliation,
    /**
     * "contactEmail specifies information characterizing details for contacting a contact entity by email."
     */contactEmail?: ContactEmail,
    /**
     * "contactMessaging specifies information characterizing details for contacting a contact entity by digital messaging."
     */contactMessaging?: ContactMessaging,
    /**
     * "contactPhone specifies information characterizing details for contacting a contact entity by telephone."
     */contactPhone?: ContactPhone,
    /**
     * "contactProfile specifies information characterizing details for contacting a contact entity by online service."
     */contactProfile?: ContactProfile,
    /**
     * "contactSIP specifies information characterizing details for contacting a contact entity by Session Initiation Protocol (SIP)."
     */contactSIP?: ContactSIP,
    /**
     * "contactURL specifies information characterizing details for contacting a contact entity by Uniform Resource Locator (URL)."
     */contactURL?: ContactURL,
    /**
     * "Source application specifies the software application that a particular contact or contact list is associated with."
     */sourceApplication?: ObservableObject,
    birthdate?: string,
    /**
     * "Last time contacted specifies the date and time that a particular contact was last contacted."
     */lastTimeContacted?: string,
    /**
     * "Number times contacted specifies the number of times a particular contact has been contacted."
     */numberTimesContacted?: number,
    /**
     * "Specifies an ID for the contact."
     */contactID?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
    /**
     * "The firstName of a person."
     */firstName?: string,
    /**
     * "The lastName of a person."
     */lastName?: string,
    /**
     * "The middleName of a person."
     */middleName?: string,
    /**
     * "Name phonetic specifies the phonetic pronunciation of the name of a person."
     */namePhonetic?: string,
    /**
     * "Name prefix specifies an honorific prefix (coming ordinally before first/given name) for the name of a person."
     */namePrefix?: string,
    /**
     * "Name suffix specifies an suffix (coming ordinally after last/family name) for the name of a person."
     */nameSuffix?: string,
    /**
     * "contactGroup specifies the name/tag of a particular named/tagged grouping of contacts."
     */contactGroup?: string,
    /**
     * "contactNote specifies a comment/note associated with a given contact."
     */contactNote?: string,
    /**
     * "Nickname specifies an alternate, unofficial and typically informal name for a person independent of their official name."
     */nickname?: string,
}
/**
 * "A contact list is a set of multiple individual contacts such as that found in a digital address book."
 */
export interface ContactList  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A contact list facet is a grouping of characteristics unique to a set of multiple individual contacts such as that found in a digital address book."
 */
export interface ContactListFacet  extends Facet  {
    /**
     * "Source application specifies the software application that a particular contact or contact list is associated with."
     */sourceApplication?: ObservableObject,
    /**
     * "contact specifies information characterizing contact details for a single entity."
     */contact?: ObservableObject[],
}
/**
 * "A contactMessaging is a grouping of characteristics unique to details for contacting a contact entity by digital messaging."
 */
export interface ContactMessaging  extends UcoInherentCharacterizationThing  {
    /**
     * "A contactMessagingPlatform specifies a digital messaging platform associated with a contact."
     */contactMessagingPlatform?: ObservableObject,
    /**
     * "A messagingAddress specifies details of an identifier for digital messsaging communication."
     */messagingAddress?: ObservableObject,
}
/**
 * "A contactPhone is a grouping of characteristics unique to details for contacting a contact entity by telephone."
 */
export interface ContactPhone  extends UcoInherentCharacterizationThing  {
    /**
     * "contactPhoneNumber specifies a telephone service account number for contacting a contact entity by telephone."
     */contactPhoneNumber?: ObservableObject,
    /**
     * "contactPhoneScope specifies the relevant scope (home, work, school, etc) of details for contacting a contact entity by telephone."
     */contactPhoneScope?: string,
}
/**
 * "A contactProfile is a grouping of characteristics unique to details for contacting a contact entity by online service."
 */
export interface ContactProfile  extends UcoInherentCharacterizationThing  {
    /**
     * "A contactProfile platform specifies an online service platform associated with a contact."
     */contactProfilePlatform?: ObservableObject,
    /**
     * "A profile specifies a particular online service profile."
     */profile?: ObservableObject,
}
/**
 * "A contactSIP is a grouping of characteristics unique to details for contacting a contact entity by Session Initiation Protocol (SIP)."
 */
export interface ContactSIP  extends UcoInherentCharacterizationThing  {
    /**
     * "A SIP address specifies Session Initiation Protocol (SIP) identifier."
     */sipAddress?: ObservableObject,
    /**
     * "contactSIPScope specifies the relevant scope (home, work, school, etc) of details for contacting a contact entity by Session Initiation Protocol (SIP)."
     */contactSIPScope?: string,
}
/**
 * "A contactURL is a grouping of characteristics unique to details for contacting a contact entity by Uniform Resource Locator (URL)."
 */
export interface ContactURL  extends UcoInherentCharacterizationThing  {
    /**
     * "contact url scope specifies the relevant scope (homepage, home, work, school, etc) of details for contacting a contact entity by Uniform Resource Locator (URL)."
     */contactURLScope?: string,
    /**
     * "Specifies a URL associated with a particular observable object or facet."
     */url?: ObservableObject,
}
/**
 * "Content data is a block of digital data."
 */
export interface ContentData  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A content data facet is a grouping of characteristics unique to a block of digital data."
 */
export interface ContentDataFacet  extends Facet  {
    dataPayloadReferenceURL?: ObservableObject,
    /**
     * "Hash values of the data."
     */hash?: Hash[],
    isEncrypted?: string,
    /**
     * "Shannon entropy (a measure of randomness) of the data."
     */entropy?: number,
    /**
     * "The size of the data in bytes."
     */sizeInBytes?: number,
    dataPayload?: string,
    magicNumber?: string,
    mimeClass?: string,
    /**
     * "MIME type of the data. For example 'text/html' or 'audio/mp3'."
     */mimeType?: string,
    byteOrder?: string,
}
/**
 * "A cookie history is the stored web cookie history for a particular web browser."
 */
export interface CookieHistory  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A credential is a single specific login and password combination for authorization of access to a digital account or system."
 */
export interface Credential  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A credential dump is a collection (typically forcibly extracted from a system) of specific login and password combinations for authorization of access to a digital account or system."
 */
export interface CredentialDump  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An DNS cache is a temporary locally stored collection of previous Domain Name System (DNS) query results (created when an domainName is resolved to a IP address) for a particular computer."
 */
export interface DNSCache  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A DNS record is a single Domain Name System (DNS) artifact specifying information of a particular type (routing, authority, responsibility, security, etc.) for a specific Internet domainName."
 */
export interface DNSRecord  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A data range facet is a grouping of characteristics unique to a particular contiguous scope within a block of digital data."
 */
export interface DataRangeFacet  extends Facet  {
    /**
     * "The offset at which the start of data can be found, relative to the rangeOffsetType defined."
     */rangeOffset?: number,
    /**
     * "The size of the data in bytes."
     */rangeSize?: number,
    /**
     * "The type of offset defined for the range (e.g., image, file, address)."
     */rangeOffsetType?: string,
}
/**
 * "A defined effect facet is a grouping of characteristics unique to the effect of an observable action in relation to one or more observable objects."
 */
export interface DefinedEffectFacet  extends Facet  {
}
/**
 * "A device is a piece of equipment or a mechanism designed to serve a special purpose or perform a special function. [based on https://www.merriam-webster.com/dictionary/device]"
 */
export interface Device  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A device facet is a grouping of characteristics unique to a piece of equipment or a mechanism designed to serve a special purpose or perform a special function. [based on https://www.merriam-webster.com/dictionary/device]"
 */
export interface DeviceFacet  extends Facet  {
    manufacturer?: Identity,
    deviceType?: string,
    model?: string,
    serialNumber?: string,
}
/**
 * "A digital account is an arrangement with an entity to enable and control the provision of some capability or service within the digital domain."
 */
export interface DigitalAccount  extends Account  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A digital account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service within the digital domain."
 */
export interface DigitalAccountFacet  extends Facet  {
    /**
     * "Is the digital account disabled?"
     */isDisabled?: string,
    /**
     * "The date and time of the first login of the account."
     */firstLoginTime?: string,
    /**
     * "The date and time of the last login of the account."
     */lastLoginTime?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
    /**
     * "The login identifier for the digital account."
     */accountLogin?: string,
}
/**
 * "A digital address is an identifier assigned to enable routing and management of digital communication."
 */
export interface DigitalAddress  extends Address  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A digital address facet is a grouping of characteristics unique to an identifier assigned to enable routing and management of digital communication."
 */
export interface DigitalAddressFacet  extends Facet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "A digital camera is a camera that captures photographs in digital memory as opposed to capturing images on photographic film"
 */
export interface DigitalCamera  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A digital signature info is a value calculated via a mathematical scheme for demonstrating the authenticity of an electronic message or document."
 */
export interface DigitalSignatureInfo  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A digital signature info facet is a grouping of characteristics unique to a value calculated via a mathematical scheme for demonstrating the authenticity of an electronic message or document."
 */
export interface DigitalSignatureInfoFacet  extends Facet  {
    certificateSubject?: UcoObject,
    certificateIssuer?: Identity,
    signatureExists?: string,
    signatureVerified?: string,
    signatureDescription?: string,
}
/**
 * "A directory is a file system cataloging structure which contains references to other computer files, and possibly other directories. On many computers, directories are known as folders, or drawers, analogous to a workbench or the traditional office filing cabinet. In UNIX a directory is implemented as a special file. [based on https://en.wikipedia.org/wiki/Directory_(computing)]"
 */
export interface Directory  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A disk is a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks."
 */
export interface Disk  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A disk facet is a grouping of characteristics unique to a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks."
 */
export interface DiskFacet  extends Facet  {
    /**
     * "The partitions that reside on the disk."
     */partition?: ObservableObject[],
    /**
     * "The size of the disk, in bytes."
     */diskSize?: number,
    /**
     * "The amount of freeSpace on the disk, in bytes."
     */freeSpace?: number,
    /**
     * "The type of disk being characterized, e.g., removable."
     */diskType?: string,
}
/**
 * "A disk partition is a particular managed region on a storage mechanism where data is recorded by various electronic, magnetic, optical, or mechanical changes to a surface layer of one or more rotating disks. [based on https://en.wikipedia.org/wiki/disk_storage]"
 */
export interface DiskPartition  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A disk partition facet is a grouping of characteristics unique to a particular managed region on a storage mechanism."
 */
export interface DiskPartitionFacet  extends Facet  {
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "Specifies the length of the partition, in bytes."
     */partitionLength?: number,
    /**
     * "Specifies the starting offset of the partition, in bytes."
     */partitionOffset?: number,
    /**
     * "Specifies the amount of spaceLeft on the partition, in bytes."
     */spaceLeft?: number,
    /**
     * "Specifies the amount of spaceUsed on the partition, in bytes."
     */spaceUsed?: number,
    /**
     * "Specifies the total amount of space available on the partition, in bytes."
     */totalSpace?: number,
    /**
     * "Specifies the type of partition being characterized."
     */diskPartitionType?: string,
    /**
     * "Specifies the mountPoint of the partition."
     */mountPoint?: string,
    /**
     * "Specifies the identifier of the partition, as provided by the containing partition table.  This identifier is the index value within the partition table, and is expected to be an incrementing alphanumeric value (numeric in most partition systems), not a GUID or UUID.  Sorting partitions by this index should first attempt to sort a numeric cast of the value."
     */partitionID?: string,
}
/**
 * "A domainName is an identification string that defines a realm of administrative autonomy, authority or control within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]"
 */
export interface DomainName  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A domainName facet is a grouping of characteristics unique to an identification string that defines a realm of administrative autonomy, authority or control within the Internet. [based on https://en.wikipedia.org/wiki/Domain_name]"
 */
export interface DomainNameFacet  extends Facet  {
    isTLD?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "A drone, unmanned aerial vehicle (UAV), is an aircraft without a human pilot, crew, or passengers that typically involve a ground-based controller and a system for communications with the UAV"
 */
export interface Drone  extends MobileDevice  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An EXIF (exchangeable image file format) facet is a grouping of characteristics unique to the formats for images, sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling image and sound files recorded by digital cameras conformant to JEIDA/JEITA/CIPA specifications. [based on https://en.wikipedia.org/wiki/Exif]"
 */
export interface EXIFFacet  extends Facet  {
    exifData?: ControlledDictionary[],
}
/**
 * "An email account is an arrangement with an entity to enable and control the provision of electronic mail (email) capabilities or services."
 */
export interface EmailAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An email account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of electronic mail (email) capabilities or services."
 */
export interface EmailAccountFacet  extends Facet  {
    /**
     * "An emailAddress."
     */emailAddress?: ObservableObject,
}
/**
 * "An emailAddress is an identifier for an electronic mailbox to which electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to."
 */
export interface EmailAddress  extends DigitalAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An emailAddress facet is a grouping of characteristics unique to an identifier for an electronic mailbox to which electronic mail messages (conformant to the Simple Mail Transfer Protocol (SMTP)) are sent from and delivered to."
 */
export interface EmailAddressFacet  extends DigitalAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "An email message is a message that is an instance of an electronic mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs."
 */
export interface EmailMessage  extends Message  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An email message facet is a grouping of characteristics unique to a message that is an instance of an electronic mail correspondence conformant to the internet message format described in RFC 5322 and related RFCs."
 */
export interface EmailMessageFacet  extends Facet  {
    /**
     * "A list of the MIME parts that make up the email body. This field MAY only be used if isMultipart is true."
     */bodyMultipart?: MimePartType[],
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    bodyRaw?: ObservableObject,
    /**
     * "The phone number of the initiating party."
     */from?: ObservableObject,
    headerRaw?: ObservableObject,
    sender?: ObservableObject,
    xOriginatingIP?: ObservableObject,
    /**
     * "Allows the sender of a message to conceal the person entered in the BCC field from the other recipients"
     */bcc?: ObservableObject[],
    /**
     * "Carbon copy: technique of producing one or more copies simultaneously."
     */cc?: ObservableObject[],
    /**
     * "A list of email message identifiers this email relates to."
     */references?: ObservableObject[],
    /**
     * "The receiver's phone number."
     */to?: ObservableObject[],
    otherHeaders?: Dictionary,
    isMimeEncoded?: string,
    isMultipart?: string,
    isRead?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * "The date and time at which the message received."
     */receivedTime?: string,
    /**
     * "The date and time at which the message sent."
     */sentTime?: string,
    /**
     * "Text forming the main content of a printed or digital work (as opposed to additional elements such as headlines, images, charts, footnotes)"
     */body?: string,
    contentDisposition?: string,
    contentType?: string,
    /**
     * "One of more unique identifiers for identifying the email(s) this email is a reply to."
     */inReplyTo?: string,
    /**
     * "An unique identifier for the message."
     */messageID?: string,
    /**
     * "The priority of the email."
     */priority?: string,
    /**
     * "The subject of the email."
     */subject?: string,
    xMailer?: string,
    /**
     * "Categories applied to the object."
     */categories?: string,
    /**
     * "Named and colored label."
     */labels?: string,
    receivedLines?: string,
}
/**
 * "An embedded device is a highly specialized microprocessor device meant for one or very few specific purposes and is usually embedded or included within another object or as part of a larger system. Examples include answer machine, door access logger, card scanner, etc"
 */
export interface EmbeddedDevice  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An encoded stream facet is a grouping of characteristics unique to the conversion of a body of data content from one form to another form."
 */
export interface EncodedStreamFacet  extends Facet  {
    encodingMethod?: string,
}
/**
 * "An encrypted stream facet is a grouping of characteristics unique to the conversion of a body of data content from one form to another obfuscated form in such a way that reversing the conversion to obtain the original data form can only be accomplished through possession and use of a specific key."
 */
export interface EncryptedStreamFacet  extends Facet  {
    encryptionMethod?: string,
    encryptionMode?: string,
    encryptionIV?: string,
    encryptionKey?: string,
}
/**
 * "An environment variable is a grouping of characteristics unique to a dynamic-named value that can affect the way running processes will behave on a computer. [based on https://en.wikipedia.org/wiki/Environment_variable]"
 */
export interface EnvironmentVariable  extends UcoInherentCharacterizationThing  {
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "An event log is a collection of event records."
 */
export interface EventLog  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An event record is something that happens in a digital context (e.g., operating system events)."
 */
export interface EventRecord  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An event record facet is a grouping of characteristics unique to something that happens in a digital context (e.g., operating system events)."
 */
export interface EventRecordFacet  extends Facet  {
    /**
     * "The action taken in response to the event."
     */cyberAction?: ObservableAction,
    /**
     * "Specifies the account referenced in an event log entry or used to run the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381228(v=vs.85).aspx."
     */account?: ObservableObject,
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The device on which the log entry was generated."
     */eventRecordDevice?: ObservableObject,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * The initial time of a time range.
     */startTime?: string,
    eventID?: string,
    /**
     * "The identifier of the event record."
     */eventRecordID?: string,
    /**
     * "The complete raw content of the event record."
     */eventRecordRaw?: string,
    /**
     * "The service that generated the event record. A single application can have multiple services generating event records."
     */eventRecordServiceName?: string,
    /**
     * "The textual representation of the event."
     */eventRecordText?: string,
    /**
     * "The type of the event, for example 'information', 'warning' or 'error'."
     */eventType?: string,
}
/**
 * "An extInode facet is a grouping of characteristics unique to a file system object (file, directory, etc.) conformant to the extended file system (EXT or related derivations) specification."
 */
export interface ExtInodeFacet  extends Facet  {
    /**
     * "Specifies the time at which the file represented by an Inode was 'deleted'."
     */extDeletionTime?: string,
    /**
     * "The date and time at which the file Inode metadata was last modified."
     */extInodeChangeTime?: string,
    /**
     * "Specifies the EXT file type (FIFO, Directory, Regular file, Symbolic link, etc) for the Inode."
     */extFileType?: number,
    /**
     * "Specifies user flags to further protect (limit its use and modification) the file represented by an Inode."
     */extFlags?: number,
    /**
     * "Specifies a count of how many hard links point to an Inode."
     */extHardLinkCount?: number,
    /**
     * "Specifies a single Inode identifier."
     */extInodeID?: number,
    /**
     * "Specifies the read/write/execute permissions for the file represented by an EXT Inode."
     */extPermissions?: number,
    /**
     * "Specifies the group ID for the file represented by an Inode."
     */extSGID?: number,
    /**
     * "Specifies the user ID that 'owns' the file represented by an Inode."
     */extSUID?: number,
}
/**
 * "An extracted string is a grouping of characteristics unique to a series of characters pulled from an observable object."
 */
export interface ExtractedString  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the length, in characters, of the extracted string."
     */length?: number,
    /**
     * "Specifies the raw, byte-string representation of the extracted string."
     */byteStringValue?: string,
    /**
     * "The encodingMethod used for the extracted string."
     */encoding?: string,
    /**
     * "Specifies the English translation of the string, if it is not written in English."
     */englishTranslation?: string,
    /**
     * "Specifies the language the string is written in, e.g. English.
    For consistency, it is strongly recommended to use the ISO 639-2 language code, if available. Please see http://www.loc.gov/standards/iso639-2/php/code_list.php for a list of ISO 639-2 codes."
     */language?: string,
    /**
     * "Specifies the actual value of the extracted string."
     */stringValue?: string,
}
/**
 * "An extracted strings facet is a grouping of characteristics unique to one or more sequences of characters pulled from an observable object."
 */
export interface ExtractedStringsFacet  extends Facet  {
    strings?: ExtractedString[],
}
/**
 * "A file is a computer resource for recording data discretely on a computer storage device."
 */
export interface File  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A file facet is a grouping of characteristics unique to the storage of a file (computer resource for recording data discretely in a computer storage device) on a file system (process that manages how and where data on a storage device is stored, accessed and managed). [based on https://en.wikipedia.org/computer_file and https://www.techopedia.com/definition/5510/file-system]"
 */
export interface FileFacet  extends Facet  {
    /**
     * "Specifies whether a file entry represents a directory."
     */isDirectory?: string,
    /**
     * "The date and time at which the Object was accessed."
     */accessedTime?: string,
    /**
     * "The date and time at which the file metadata was last modified."
     */metadataChangeTime?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "When used to characterize a file the sizeInBytes property conveys the recorded size of a file in a file system."
     */sizeInBytes?: number,
    /**
     * "The allocation status of a file."
     */allocationStatus?: string,
    /**
     * "The fileName extension: everything after the last dot. Not present if the file has no dot in its name."
     */extension?: string,
    /**
     * "Specifies the name associated with a file in a file system."
     */fileName?: string,
    /**
     * "Specifies the filePath for the location of a file within a filesystem."
     */filePath?: string,
}
/**
 * "A file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on a file system."
 */
export interface FilePermissionsFacet  extends Facet  {
    /**
     * "Specifies the owner of an observable Object."
     */owner?: UcoObject,
}
/**
 * "A file system is the process that manages how and where data on a storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]"
 */
export interface FileSystem  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A file system facet is a grouping of characteristics unique to the process that manages how and where data on a storage medium is stored, accessed and managed. [based on https://www.techopedia.com/definition/5510/file-system]"
 */
export interface FileSystemFacet  extends Facet  {
    /**
     * "The size of cluster allocation units in a file system."
     */clusterSize?: number,
    /**
     * "The specific type of a file system."
     */fileSystemType?: string,
}
/**
 * "A file system object is an informational object represented and managed within a file system."
 */
export interface FileSystemObject  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A forum post is message submitted by a user account to an online forum where the message content (and typically metadata including who posted it and when) is viewable by any party with viewing permissions on the forum."
 */
export interface ForumPost  extends Message  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A forum private message (aka PM or DM (direct message)) is a one-to-one message from one specific user account to another specific user account on an online form where transmission is managed by the online forum platform and the message is only viewable by the parties directly involved."
 */
export interface ForumPrivateMessage  extends Message  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A fragment facet is a grouping of characteristics unique to an individual piece of the content of a file."
 */
export interface FragmentFacet  extends Facet  {
    fragmentIndex?: number,
    totalFragments?: number,
}
/**
 * "A GUI is a graphical user interface that allows users to interact with electronic devices through graphical icons and audio indicators such as primary notation, instead of text-based user interfaces, typed command labels or text navigation. [based on https://en.wikipedia.org/wiki/Graphical_user_interface]"
 */
export interface GUI  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A gaming console (video game console or game console) is an electronic system that connects to a display, typically a TV or computer monitor, for the primary purpose of playing video games"
 */
export interface GamingConsole  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A generic observable object is an article or unit within the digital domain."
 */
export interface GenericObservableObject  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A geolocation entry is a single application-specific geolocation entry."
 */
export interface GeoLocationEntry  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A geolocation entry facet is a grouping of characteristics unique to a single application-specific geolocation entry."
 */
export interface GeoLocationEntryFacet  extends Facet  {
    /**
     * "An associated location."
     */location?: Location,
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
}
/**
 * "A geolocation log is a record containing geolocation tracks and/or geolocation entries."
 */
export interface GeoLocationLog  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A geolocation log facet is a grouping of characteristics unique to a record containing geolocation tracks and/or geolocation entries."
 */
export interface GeoLocationLogFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
}
/**
 * "A geolocation track is a set of contiguous geolocation entries representing a path/track taken."
 */
export interface GeoLocationTrack  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A geolocation track facet is a grouping of characteristics unique to a set of contiguous geolocation entries representing a path/track taken."
 */
export interface GeoLocationTrackFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    geoLocationEntry?: ObservableObject[],
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * The initial time of a time range.
     */startTime?: string,
}
/**
 * 'A globalFlagType is a grouping of characteristics unique to the Windows systemwide global variable named NtGlobalFlag that enables various internal debugging, tracing, and validation support in the operating system. [based on "Windows Global Flags, Chapter 3: System Mechanisms of Windows Internals by Solomon, Russinovich, and Ionescu]'
 */
export interface GlobalFlagType  extends UcoInherentCharacterizationThing  {
    /**
     * "The hexadecimalValue of a global flag. See also: http://msdn.microsoft.com/en-us/library/windows/hardware/ff549646(v=vs.85).aspx."
     */hexadecimalValue?: string,
    /**
     * "The abbreviation of a global flag. See also: http://msdn.microsoft.com/en-us/library/windows/hardware/ff549646(v=vs.85).aspx."
     */abbreviation?: string,
    /**
     * "The destination of a global flag. See also: http://msdn.microsoft.com/en-us/library/windows/hardware/ff549646(v=vs.85).aspx."
     */destination?: string,
    /**
     * "The symbolicName of a global flag. See also: http://msdn.microsoft.com/en-us/library/windows/hardware/ff549646(v=vs.85).aspx."
     */symbolicName?: string,
}
/**
 * "An HTTP connection is network connection that is conformant to the Hypertext Transfer Protocol (HTTP) standard."
 */
export interface HTTPConnection  extends NetworkConnection  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An HTTP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Hypertext Transfer Protocol (HTTP) standard."
 */
export interface HTTPConnectionFacet  extends Facet  {
    /**
     * "Specifies the data contained in an HTTP message body."
     */httpMessageBodyData?: ObservableObject,
    /**
     * "Specifies the length of an HTTP message body in bytes."
     */httpMessageBodyLength?: number,
    /**
     * "Specifies all of the HTTP header fields that may be found in the HTTP client request"
     */httpRequestHeader?: Dictionary,
    /**
     * "Specifies the HTTP method portion of the HTTP request line, as a lowercase string."
     */requestMethod?: string,
    /**
     * "Specifies the value (typically a resource path) portion of the HTTP request line."
     */requestValue?: string,
    /**
     * "Specifies the HTTP version portion of the HTTP request line, as a lowercase string."
     */requestVersion?: string,
}
/**
 * "A hostname is a label that is assigned to a device connected to a computer network and that is used to identify the device in various forms of electronic communication, such as the World Wide Web. A hostname may be a domainName, if it is properly organized into the domainName system. A domainName may be a hostname if it has been assigned to an Internet host and associated with the host's IP address. [based on https://en.wikipedia.org/wiki/hostname]"
 */
export interface Hostname  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An ICMP connection is a network connection that is conformant to the Internet Control message Protocol (ICMP) standard."
 */
export interface ICMPConnection  extends NetworkConnection  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An ICMP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Internet Control message Protocol (ICMP) standard."
 */
export interface ICMPConnectionFacet  extends Facet  {
    /**
     * "Specifies the ICMP code byte."
     */icmpCode?: string,
    /**
     * "Specifies the ICMP type byte."
     */icmpType?: string,
}
/**
 * "An IComHandler action type is a grouping of characteristics unique to a Windows Task-related action that fires a Windows COM handler (smart code in the client address space that can optimize calls between a client and server). [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/comhandleraction]"
 */
export interface IComHandlerActionType  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the ID of the COM action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380613(v=vs.85).aspx."
     */comClassID?: string,
    /**
     * "Specifies the data associated with the COM handler. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380613(v=vs.85).aspx."
     */comData?: string,
}
/**
 * "An IExec action type is a grouping of characteristics unique to an action that executes a command-line operation on a Windows operating system. [based on https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-iexecaction?redirectedfrom=MSDN]"
 */
export interface IExecActionType  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the hashes of the executable file launched by the action."
     */execProgramHashes?: Hash[],
    /**
     * "Specifies the arguments associated with the command-line operation launched by the action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380715(v=vs.85).aspx."
     */execArguments?: string,
    /**
     * "Specifies the path to the executable file launched by the action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380715(v=vs.85).aspx."
     */execProgramPath?: string,
    /**
     * "Specifies the directory that contains either the executable file or the files that are used by the executable file launched by the action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380715(v=vs.85).aspx."
     */execWorkingDirectory?: string,
}
/**
 * "An IP address is an Internet Protocol (IP) standards conformant identifier assigned to a device to enable routing and management of IP standards conformant communication to or from that device."
 */
export interface IPAddress  extends DigitalAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An IP address facet is a grouping of characteristics unique to an Internet Protocol (IP) standards conformant identifier assigned to a device to enable routing and management of IP standards conformant communication to or from that device."
 */
export interface IPAddressFacet  extends DigitalAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "An IP netmask is a 32-bit 'mask' used to divide an IP address into subnets and specify the network's available hosts."
 */
export interface IPNetmask  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}

export interface IPhone  extends AppleDevice, SmartPhone  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An IPv4 (Internet Protocol version 4) address is an IPv4 standards conformant identifier assigned to a device to enable routing and management of IPv4 standards conformant communication to or from that device."
 */
export interface IPv4Address  extends IPAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An IPv4 (Internet Protocol version 4) address facet is a grouping of characteristics unique to an IPv4 standards conformant identifier assigned to a device to enable routing and management of IPv4 standards conformant communication to or from that device."
 */
export interface IPv4AddressFacet  extends IPAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "An IPv6 (Internet Protocol version 6) address is an IPv6 standards conformant identifier assigned to a device to enable routing and management of IPv6 standards conformant communication to or from that device."
 */
export interface IPv6Address  extends IPAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An IPv6 (Internet Protocol version 6) address facet is a grouping of characteristics unique to an IPv6 standards conformant identifier assigned to a device to enable routing and management of IPv6 standards conformant communication to or from that device."
 */
export interface IPv6AddressFacet  extends IPAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "An IShow message action type is a grouping of characteristics unique to an action that shows a message box when a task is activate. [based on https://docs.microsoft.com/en-us/windows/win32/api/taskschd/nn-taskschd-ishowmessageaction?redirectedfrom=MSDN]"
 */
export interface IShowMessageActionType  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the messageText that is displayed in the body of the message box by the action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381302(v=vs.85).aspx."
     */showMessageBody?: string,
    /**
     * "Specifies the title of the message box shown by the action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381302(v=vs.85).aspx."
     */showMessageTitle?: string,
}
/**
 * "An image is a complete copy of a hard disk, memory, or other digital media."
 */
export interface Image  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An image facet is a grouping of characteristics unique to a complete copy of a hard disk, memory, or other digital media."
 */
export interface ImageFacet  extends Facet  {
    /**
     * "The type of the image, e.g. EnCase, RAW or LocalFolder."
     */imageType?: string,
}
/**
 * ""
 */
export interface InstantMessagingAddress  extends DigitalAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An instant messagingAddress facet is a grouping of characteristics unique to an identifier assigned to enable routing and management of instant messaging digital communication."
 */
export interface InstantMessagingAddressFacet  extends DigitalAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "A junction is a specific NTFS (New Technology file System) reparse point to redirect a directory access to another directory which can be on the same volume or another volume. A junction is similar to a directory symbolic link but may differ on whether they are processed on the local system or on the remote file server. [based on https://jp-andre.pagesperso-orange.fr/junctions.html]"
 */
export interface Junction  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A laptop, laptop computer, or notebook computer is a small, portable personal computer with a screen and alphanumeric keyboard. These typically have a clam shell form factor with the screen mounted on the inside of the upper lid and the keyboard on the inside of the lower lid, although 2-in-1 PCs with a detachable keyboard are often marketed as laptops or as having a laptop mode. (Devices categorized by their manufacturer as a laptop)"
 */
export interface Laptop  extends Computer  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A library is a suite of data and programming code that is used to develop software programs and applications. [based on https://www.techopedia.com/definition/3828/software-library]"
 */
export interface Library  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A library facet is a grouping of characteristics unique to a suite of data and programming code that is used to develop software programs and applications. [based on https://www.techopedia.com/definition/3828/software-library]"
 */
export interface LibraryFacet  extends Facet  {
    /**
     * "Specifies the type of library being characterized."
     */libraryType?: string,
}
/**
 * "A MAC address is a media access control standards conformant identifier assigned to a networkInterface to enable routing and management of communications at the data link layer of a network segment."
 */
export interface MACAddress  extends DigitalAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A MAC address facet is a grouping of characteristics unique to a media access control standards conformant identifier assigned to a networkInterface to enable routing and management of communications at the data link layer of a network segment."
 */
export interface MACAddressFacet  extends DigitalAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "memory is a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only memory)) on a digital device."
 */
export interface Memory  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A memory facet is a grouping of characteristics unique to a particular region of temporary information storage (e.g., RAM (random access memory), ROM (read only memory)) on a digital device."
 */
export interface MemoryFacet  extends Facet  {
    /**
     * "The isInjected property specifies whether or not the particular memory object has had data/code injected into it by another process."
     */isInjected?: string,
    /**
     * "The isMapped property specifies whether or not the particular memory object has been assigned a byte-for-byte correlation with some portion of a file or file-like resource."
     */isMapped?: string,
    /**
     * "The isProtected property specifies whether or not the particular memory object isProtected (read/write only from the process that allocated it)."
     */isProtected?: string,
    /**
     * "The isVolatile property specifies whether or not the particular memory object isVolatile."
     */isVolatile?: string,
    /**
     * "The regionEndAddress property specifies the ending address of the particular memory region."
     */regionEndAddress?: string,
    /**
     * """The regionStartAddress property specifies the starting address of the particular memory region.
    """
     */regionStartAddress?: string,
    /**
     * "The regionSize property specifies the size of the particular memory region, in bytes."
     */regionSize?: number,
    /**
     * "The blockType property specifies the blockType of a particular memory object."
     */blockType?: string,
}
/**
 * "A message is a discrete unit of electronic communication intended by the source for consumption by some recipient or group of recipients. [based on https://en.wikipedia.org/wiki/message]"
 */
export interface Message  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A message facet is a grouping of characteristics unique to a discrete unit of electronic communication intended by the source for consumption by some recipient or group of recipients. [based on https://en.wikipedia.org/wiki/message]"
 */
export interface MessageFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "The phone number of the initiating party."
     */from?: ObservableObject[],
    /**
     * "The receiver's phone number."
     */to?: ObservableObject[],
    /**
     * "The date and time at which the message sent."
     */sentTime?: string,
    /**
     * "An unique identifier for the message."
     */messageID?: string,
    /**
     * "The contents of the message."
     */messageText?: string,
    /**
     * "messageType specifies what sort of message (email, chat, SMS, etc) a message is."
     */messageType?: string,
    /**
     * "An identifier for the session from which the message originates."
     */sessionID?: string,
}
/**
 * "A messageThread facet is a grouping of characteristics unique to a running commentary of electronic messages pertaining to one topic or question."
 */
export interface MessageThreadFacet  extends Facet  {
    /**
     * "The contents of ordered items in the Thread linked by messageThread must be Message objects."
     */messageThreadOrderedItems?: Thread,
    /**
     * "The contents of origin items in the Thread linked by messageThread must be Message objects."
     */messageThreadOriginItems?: Thread,
    /**
     * "The contents of terminal items in the Thread linked by messageThread must be Message objects."
     */messageThreadTerminalItems?: Thread,
    /**
     * "The contents of unordered items in the Thread linked by messageThread must be Message objects."
     */messageThreadUnorderedItems?: Thread,
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: ObservableObject[],
    messageThread?: Thread,
    visibility?: string,
}
/**
 * "An MFT record facet is a grouping of characteristics unique to the details of a single file as managed in an NTFS (new technology filesystem) master file table (which is a collection of information about all files on an NTFS filesystem). [based on https://docs.microsoft.com/en-us/windows/win32/devnotes/master-file-table]"
 */
export interface MftRecordFacet  extends Facet  {
    /**
     * "The access date and time recorded in an MFT entry $ file_Name attribute."
     */mftFileNameAccessedTime?: string,
    /**
     * "The creationDate and time recorded in an MFT entry $ file_Name attribute."
     */mftFileNameCreatedTime?: string,
    /**
     * "The modification date and time recorded in an MFT entry $ file_Name attribute."
     */mftFileNameModifiedTime?: string,
    /**
     * "The metadata modification date and time recorded in an MFT entry $ file_Name attribute."
     */mftFileNameRecordChangeTme?: string,
    /**
     * "The date and time at which an NTFS file metadata was last modified."
     */mftRecordChangeTime?: string,
    /**
     * "Specifies the record number for the file within an NTFS Master file Table."
     */mftFileID?: number,
    /**
     * " Specifies the length of an NTFS fileName, in unicode characters."
     */mftFileNameLength?: number,
    /**
     * "Specifies basic permissions for the file (Read-Only, Hidden, Archive, Compressed, etc.)."
     */mftFlags?: number,
    /**
     * "Specifies the record number within an NTFS Master file Table for parent directory of the file."
     */mftParentID?: number,
    /**
     * "Specifies the number of directory entries that reference an NTFS file record."
     */ntfsHardLinkCount?: number,
    /**
     * "Specifies the identifier of the file owner, from the security index."
     */ntfsOwnerID?: string,
    /**
     * "Specifies the security ID (key in the $SII Index and $SDS DataStream in the file $Secure) for an NTFS file."
     */ntfsOwnerSID?: string,
}
/**
 * "A mime part type is a grouping of characteristics unique to a component of a multi-part email body."
 */
export interface MimePartType  extends UcoInherentCharacterizationThing  {
    bodyRaw?: ObservableObject,
    /**
     * "Text forming the main content of a printed or digital work (as opposed to additional elements such as headlines, images, charts, footnotes)"
     */body?: string,
    contentDisposition?: string,
    contentType?: string,
}
/**
 * "A mobile account is an arrangement with an entity to enable and control the provision of some capability or service on a portable computing device. [based on https://www.lexico.com/definition/mobile_device]"
 */
export interface MobileAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A mobile account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of some capability or service on a portable computing device. [based on https://www.lexico.com/definition/mobile_device]"
 */
export interface MobileAccountFacet  extends Facet  {
    /**
     * "An International Mobile Subscriber Identity (IMSI) is a unique identification associated with all GSM and UMTS network mobile phone users. It is stored as a 64-bit field in the SIM inside the phone and is sent by the phone to the network."
     */IMSI?: string,
    /**
     * "Mobile Station International Subscriber Directory Number (MSISDN) is a number used to identify a mobile phone number internationally. MSISDN is defined by the E.164 numbering plan. This number includes a country code and a National Destination Code which identifies the subscriber's operator."
     */MSISDN?: string,
    /**
     * "???."
     */MSISDNType?: string,
}
/**
 * "A mobile device is a portable computing device. [based on https://www.lexico.com.definition/mobile_device]"
 */
export interface MobileDevice  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A mobile device facet is a grouping of characteristics unique to a portable computing device. [based on https://www.lexico.com/definition/mobile_device]"
 */
export interface MobileDeviceFacet  extends Facet  {
    /**
     * "???."
     */mockLocationsAllowed?: string,
    /**
     * "The generalizedTime value on the mobile device when it was processed."
     */clockSetting?: string,
    /**
     * "The date and time that a device was activated."
     */phoneActivationTime?: string,
    /**
     * "The number of bytes that can be stored on a SIM card."
     */storageCapacityInBytes?: number,
    /**
     * "Electronic Serial Number."
     */ESN?: string,
    /**
     * "International Mobile Equipment Identity (IMEI)."
     */IMEI?: string,
    /**
     * "Name configured withing Bluetooth settings on a device."
     */bluetoothDeviceName?: string,
    /**
     * "A code or password set on a device for security that must be entered to gain access to the device."
     */keypadUnlockCode?: string,
    /**
     * Network allowing computers to share resources and communicate with each other
     */network?: string,
}
/**
 * "A mobile phone is a portable telephone that at least can make and receive calls over a radio frequency link while the user is moving within a telephone service area. This category encompasses all types of mobiles, simple and smart and satellite ones all together"
 */
export interface MobilePhone  extends MobileDevice  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A mutex is a mechanism that enforces limits on access to a resource when there are many threads of execution. A mutex is designed to enforce a mutual exclusion concurrency control policy, and with a variety of possible methods there exists multiple unique implementations for different applications. [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]"
 */
export interface Mutex  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A mutex facet is a grouping of characteristics unique to a mechanism that enforces limits on access to a resource when there are many threads of execution. A mutex is designed to enforce a mutual exclusion concurrency control policy, and with a variety of possible methods there exists multiple unique implementations for different applications. [based on https://en.wikipedia.org/wiki/Lock_(computer_science)]"
 */
export interface MutexFacet  extends Facet  {
    isNamed?: string,
    /**
     * "Specifies the name identifier for a specific instance of a mechanism that enforces limits on access to a resource when there are many threads of execution ."
     */mutexName?: string,
}
/**
 * "An NTFS file is a New Technology file System (NTFS) file."
 */
export interface NTFSFile  extends File  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An NTFS file facet is a grouping of characteristics unique to a file on an NTFS (new technology filesystem) file system."
 */
export interface NTFSFileFacet  extends Facet  {
    alternateDataStreams?: AlternateDataStream[],
    /**
     * "A unique identifier for the file within the filesystem."
     */entryID?: number,
    sid?: string,
}
/**
 * "An NTFS file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on an NTFS (new technology filesystem) file system."
 */
export interface NTFSFilePermissionsFacet  extends Facet  {
}
/**
 * "A named pipe is a mechanism for FIFO (first-in-first-out) inter-process communication. It is persisted as a filesystem object (that can be deleted like any other file), can be written to or read from by any process and exists beyond the lifespan of any process interacting with it (unlike simple anonymous pipes). [based on https://en.wikipedia.org/wiki/Named_pipe]"
 */
export interface NamedPipe  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A network appliance is a purpose-built computer with software or firmware that is designed to provide a specific network management function."
 */
export interface NetworkAppliance  extends Appliance  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A network connection is a connection (completed or attempted) across a digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]"
 */
export interface NetworkConnection  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A network connection facet is a grouping of characteristics unique to a connection (complete or attempted) accross a digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]"
 */
export interface NetworkConnectionFacet  extends Facet  {
    /**
     * "Specifies the source(s) of the network connection."
     */src?: UcoObject[],
    /**
     * "Specifies the destination(s) of the network connection."
     */dst?: ObservableObject[],
    /**
     * "Specifies the protocols involved in the network connection, along with their corresponding state."
     */protocols?: ControlledDictionary,
    /**
     * "Indicates whether the network connection is still active."
     */isActive?: string,
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * "Specifies the destinationPort used in the connection, as an integer in the range of 0 - 65535."
     */destinationPort?: number,
    /**
     * "Specifies the sourcePort used in the connection, as an integer in the range of 0 - 65535."
     */sourcePort?: number,
}
/**
 * "A network flow is a sequence of data transiting one or more digital network (a group or two or more computer systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]"
 */
export interface NetworkFlow  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A network flow facet is a grouping of characteristics unique to a sequence of data transiting one or more digital network (a group of two or more computer systems linked together) connections. [based on https://www.webopedia.com/TERM/N/network.html]"
 */
export interface NetworkFlowFacet  extends Facet  {
    dstPayload?: ObservableObject,
    srcPayload?: ObservableObject,
    /**
     * "Specifies any IP Flow Information Export (IPFIX) data for the network traffic flow."
     */ipfix?: Dictionary,
    dstBytes?: number,
    dstPackets?: number,
    srcBytes?: number,
    srcPackets?: number,
}
/**
 * "A networkInterface is a software or hardware interface between two pieces of equipment or protocol layers in a computer network."
 */
export interface NetworkInterface  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A networkInterface facet is a grouping of characteristics unique to a software or hardware interface between two pieces of equipment or protocol layers in a computer network."
 */
export interface NetworkInterfaceFacet  extends Facet  {
    /**
     * "Specifies the MAC or hardware address of the physical network card."
     */macAddress?: ObservableObject,
    /**
     * "Specifies the list of DHCP server IP Addresses used by the networkInterface."
     */dhcpServer?: ObservableObject[],
    /**
     * "Specifies the list of IP addresses used by the networkInterface."
     */ip?: ObservableObject[],
    /**
     * "Specifies the list of IP Gateway IP Addresses used by the networkInterface."
     */ipGateway?: ObservableObject[],
    /**
     * "Specifies the date/time that the DHCP lease obtained on the networkInterface expires."
     */dhcpLeaseExpires?: string,
    /**
     * "Specifies the date/time that the DHCP lease was obtained on the networkInterface."
     */dhcpLeaseObtained?: string,
    /**
     * "Specifies the name of the network adapter used by the networkInterface."
     */adapterName?: string,
}
/**
 * "A network protocol is an established set of structured rules that determine how data is transmitted between different devices in the same network. Essentially, it allows connected devices to communicate with each other, regardless of any differences in their internal processes, structure or design. [based on https://www.comptia.org/content/guides/what-is-a-network-protocol]"
 */
export interface NetworkProtocol  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A network route is a specific path (of specific network nodes, connections and protocols) for traffic in a network or between or across multiple networks."
 */
export interface NetworkRoute  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "The address family parameter on a socket() API determines the format of the address structure to be used on socket APIs."
 */
export interface NetworkSocketAddressFamily  {
}
/**
 * "The protocol family specifies the protocol scheme that is used by the Socket class to resolve an address."
 */
export interface NetworkSocketProtocolFamily  {
}
/**
 * "Depending on the type and importance of data exchanged between the applications via sockets, different types of network sockets are implemented."
 */
export interface NetworkSocketType  {
}
/**
 * "A network subnet is a logical subdivision of an IP network. [based on https://en.wikipedia.org/wiki/Subnetwork]"
 */
export interface NetworkSubnet  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A note is a brief textual record."
 */
export interface Note  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A note facet is a grouping of characteristics unique to a brief textual record."
 */
export interface NoteFacet  extends Facet  {
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    text?: string,
}
/**
 * "An observable is a characterizable item or action within the digital domain."
 */
export interface Observable  extends UcoObject  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An observable action is a grouping of characteristics unique to something that may be done or performed within the digital domain."
 */
export interface ObservableAction  extends Action, Observable  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An observable object is a grouping of characteristics unique to a distinct article or unit within the digital domain."
 */
export interface ObservableObject  extends CoItem, Observable  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An observable pattern is a grouping of characteristics unique to a logical pattern composed of observable object and observable action properties."
 */
export interface ObservablePattern  extends Observable  {
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An observable relationship is a grouping of characteristics unique to an assertion of an association between two observable objects."
 */
export interface ObservableRelationship  extends Relationship, Observable  {
    /**
     * The ending time of a time range.
     */endTime?: string,
    /**
     * A specification whether or not a relationship assertion is limited to the context FROM a source object(s) TO a target object.
     */isDirectional?: string,
    /**
     * A characterization of the nature of a relationship between objects.
     */kindOfRelationship?: string,
    /**
     * The originating node of a specified relationship.
     */source?: UcoObject[],
    /**
     * The initial time of a time range.
     */startTime?: string,
    /**
     * The terminating node of a specified relationship.
     */target?: UcoObject,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An observation is a temporal perception of an observable."
 */
export interface Observation  extends Action  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An online service is a particular provision mechanism of information access, distribution or manipulation over the Internet."
 */
export interface OnlineService  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An online service facet is a grouping of characteristics unique to a particular provision mechanism of information access, distribution or manipulation over the Internet"
 */
export interface OnlineServiceFacet  extends Facet  {
    /**
     * "An associated location."
     */location?: Location,
    /**
     * "Specifies a location on the Internet"
     */inetLocation?: ObservableObject,
    /**
     * The name of a particular concept characterization.
     */name?: string,
}
/**
 * "An operating system is the software that manages computer hardware, software resources, and provides common services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]"
 */
export interface OperatingSystem  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An operating system facet is a grouping of characteristics unique to the software that manages computer hardware, software resources, and provides common services for computer programs. [based on https://en.wikipedia.org/wiki/Operating_system]"
 */
export interface OperatingSystemFacet  extends Facet  {
    manufacturer?: Identity,
    /**
     * "A list of environmentVariables associated with the process."
     */environmentVariables?: Dictionary,
    /**
     * "Limits advertising tracking if enabled. [based on https://developer.android.com/reference/androidx/ads/identifier/AdvertisingIdInfo]"
     */isLimitAdTrackingEnabled?: string,
    /**
     * "Specifies the date the operating sytem or application was installed."
     */installDate?: string,
    /**
     * "Specifies the bitness of the operating system (i.e. 32 or 64). Note that this is potentially different from the word size of the underlying hardware or CPU. A 32-bit operating sytem can be installed on a machine running a 64-bit processor."
     */bitness?: string,
    version?: string,
    /**
     * "Advertising ID as a UUID. [based on https://developer.android.com/reference/androidx/ads/identifier/AdvertisingIdInfo]"
     */advertisingID?: string,
}
/**
 * "A PDF file is a Portable Document Format (PDF) file."
 */
export interface PDFFile  extends File  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A PDF file facet is a grouping of characteristics unique to a PDF (Portable Document Format) file."
 */
export interface PDFFileFacet  extends Facet  {
    documentInformationDictionary?: ControlledDictionary,
    isOptimized?: string,
    /**
     * "The PDF CreationDate property is defined in ISO 32000-1:2008 as 'The date and time the document was created, in human-readable form' (Table 317).  As a UCO property, its value is converted to xsd:dateTime."
     */pdfCreationDate?: string,
    /**
     * "The PDF ModDate property is defined in ISO 32000-1:2008 as 'The date and time the document was most recently modified, in human-readable form' (Table 317).  As a UCO property, its value is converted to xsd:dateTime."
     */pdfModDate?: string,
    pdfId1?: string,
    version?: string,
    pdfId0?: string,
}
/**
 * "A path relation facet is a grouping of characteristics unique to the location of one object within another containing object."
 */
export interface PathRelationFacet  extends Facet  {
    /**
     * "Specifies the location of one object within another containing object."
     */path?: string,
}
/**
 * "A payment card is a physical token that is part of a payment system issued by financial institutions, such as a bank, to a customer that enables its owner (the cardholder) to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs). [based on https://en.wikipedia.org/wiki/Payment_card]"
 */
export interface PaymentCard  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A phone account is an arrangement with an entity to enable and control the provision of a telephony capability or service."
 */
export interface PhoneAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A phone account facet is a grouping of characteristics unique to an arrangement with an entity to enable and control the provision of a telephony capability or service."
 */
export interface PhoneAccountFacet  extends Facet  {
    /**
     * "A phoneNumber(account)."
     */phoneNumber?: string,
}
/**
 * "A pipe is a mechanism for one-way inter-process communication using message passing where data written by one process is buffered by the operating system until it isRead by the next process, and this uni-directional channel disappears when the processes are completed. [based on https://en.wikipedia.org/wiki/Pipeline_(Unix) ; https://en.wikipedia.org/wiki/Anonymous_pipe]"
 */
export interface Pipe  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A post is message submitted to an online discussion/publishing site (forum, blog, etc.)."
 */
export interface Post  extends Message  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A process is an instance of a computer program executed on an operating system."
 */
export interface Process  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A process facet is a grouping of characteristics unique to an instance of a computer program executed on an operating system."
 */
export interface ProcessFacet  extends Facet  {
    binary?: ObservableObject,
    /**
     * "The user that created/owns the process."
     */creatorUser?: ObservableObject,
    /**
     * "The process that created this process."
     */parent?: ObservableObject,
    /**
     * "A list of environmentVariables associated with the process."
     */environmentVariables?: Dictionary,
    /**
     * "The isHidden property specifies whether the process isHidden or not."
     */isHidden?: string,
    /**
     * "The time at which the process exited."
     */exitTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "A small number passed from the process to the parent process when it has finished executing. In general, 0 indicates successful termination, any other number indicates a failure."
     */exitStatus?: number,
    /**
     * "The process ID, or PID, of the process."
     */pid?: number,
    currentWorkingDirectory?: string,
    /**
     * "Specifies a list of statuses for a given Whois entry."
     */status?: string,
    /**
     * "A list of arguments utilized in initiating the process."
     */arguments?: string,
}
/**
 * "A process thread is the smallest sequence of programmed instructions that can be managed independently by a scheduler on a computer, which is typically a part of the operating system. It is a component of a process. Multiple threads can exist within one process, executing concurrently and sharing resources such as memory, while different processes do not share these resources. In particular, the threads of a process share its executable code and the values of its dynamically allocated variables and non-thread-local global variables at any given time. [based on https://en.wikipedia.org/wiki/Thread_(computing)]"
 */
export interface ProcessThread  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A profile is an explicit digital representation of identity and characteristics of the owner of a single user account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]"
 */
export interface Profile  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A profile facet is a grouping of characteristics unique to an explicit digital representation of identity and characteristics of the owner of a single user account associated with an online service or application. [based on https://en.wikipedia.org/wiki/User_profile]"
 */
export interface ProfileFacet  extends Facet  {
    /**
     * "Specifies the identity associated with the profile"
     */profileIdentity?: Identity,
    /**
     * "contactAddress specifies information characterizing a geolocation address of a contact entity."
     */contactAddress?: ContactAddress,
    /**
     * "contactEmail specifies information characterizing details for contacting a contact entity by email."
     */contactEmail?: ContactEmail,
    /**
     * "contactMessaging specifies information characterizing details for contacting a contact entity by digital messaging."
     */contactMessaging?: ContactMessaging,
    /**
     * "contactPhone specifies information characterizing details for contacting a contact entity by telephone."
     */contactPhone?: ContactPhone,
    /**
     * "contactURL specifies information characterizing details for contacting a contact entity by Uniform Resource Locator (URL)."
     */contactURL?: ContactURL,
    /**
     * "Specifies the online service account associated with the profile"
     */profileAccount?: ObservableObject,
    /**
     * "Specifies the online service associated with the profile"
     */profileService?: ObservableObject,
    /**
     * "Specifies the website URL associated with the profile"
     */profileWebsite?: ObservableObject,
    /**
     * "Specifies the date and time the profile was created"
     */profileCreated?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "A properties enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a characteristic of the observable object is enumerated. An example of this would be startup parameters for a process."
 */
export interface PropertiesEnumeratedEffectFacet  extends DefinedEffectFacet, Facet  {
    /**
     * "Specifies the properties that were enumerated as a result of the action on the observable object."
     */properties?: string,
}
/**
 * "A properties read effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a characteristic isRead from an observable object. An example of this would be the current running state of a process."
 */
export interface PropertyReadEffectFacet  extends DefinedEffectFacet  {
    /**
     * "Specifies the Name of the property being read."
     */propertyName?: string,
    /**
     * A string value.
     */value?: string,
}
/**
 * "A protocol converter is a device that converts from one protocol to another (e.g. SD to USB, SATA to USB, etc"
 */
export interface ProtocolConverter  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A raster picture is a raster (or bitmap) image."
 */
export interface RasterPicture  extends File  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A raster picture facet is a grouping of characteristics unique to a raster (or bitmap) image."
 */
export interface RasterPictureFacet  extends Facet  {
    /**
     * "The name/make of the camera that was used for taking the picture."
     */camera?: ObservableObject,
    bitsPerPixel?: number,
    pictureHeight?: number,
    /**
     * "The width of the picture in pixels."
     */pictureWidth?: number,
    imageCompressionMethod?: string,
    /**
     * "The type of a picture, for example a thumbnail."
     */pictureType?: string,
}
/**
 * "An observable object that was the result of a recovery operation."
 */
export interface RecoveredObject  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "Recoverability status of name, metadata, and content."
 */
export interface RecoveredObjectFacet  extends Facet  {
    /**
     * "Specifies the recoverability status of the content of an object."
     */contentRecoveredStatus?: string,
    /**
     * "Specifies the recoverability status of the metadata of an object."
     */metadataRecoveredStatus?: string,
    /**
     * "Specifies the recoverability status of the name of an object."
     */nameRecoveredStatus?: string,
}
/**
 * "Data types used in Windows operating systems Registry, and the earlier IBM/Microsoft OS/2 operating system"
 */
export interface RegistryDatatype  {
}
/**
 * "A reparse point is a type of NTFS (New Technology file System) object which is an optional attribute of files and directories meant to define some sort of preprocessing before accessing the said file or directory. For instance reparse points can be used to redirect access to files which have been moved to long term storage so that some application would retrieve them and make them directly accessible. A reparse point contains a reparse tag and data that are interpreted by a filesystem filter identified by the tag. [based on https://jp-andre.pagesperso-orange.fr/junctions.html ; https://en.wikipedia.org/wiki/NTFS_reparse_point]"
 */
export interface ReparsePoint  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A SIM card is a subscriber identification module card intended to securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on mobile telephony. [based on https://en.wikipedia.org/wiki/SIM_card]"
 */
export interface SIMCard  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A SIM card facet is a grouping of characteristics unique to a subscriber identification module card intended to securely store the international mobile subscriber identity (IMSI) number and its related key, which are used to identify and authenticate subscribers on mobile telephony devices (such as mobile phones and computers). [based on https://en.wikipedia.org/wiki/SIM_card]"
 */
export interface SIMCardFacet  extends Facet  {
    /**
     * "Telecommunications service provider that sold the SIM card."
     */carrier?: Identity,
    /**
     * "The number of bytes that can be stored on a SIM card."
     */storageCapacityInBytes?: number,
    /**
     * "Integrated circuit card identifier (http://www.itu.int/)."
     */ICCID?: string,
    /**
     * "An International Mobile Subscriber Identity (IMSI) is a unique identification associated with all GSM and UMTS network mobile phone users. It is stored as a 64-bit field in the SIM inside the phone and is sent by the phone to the network."
     */IMSI?: string,
    /**
     * "Personal Identification Number (PIN)."
     */PIN?: string,
    /**
     * "Personal Unlocking Key (PUK) to unlock the SIM card."
     */PUK?: string,
    /**
     * "The form of SIM card such as SIM, Micro SIM, Nano SIM."
     */SIMForm?: string,
    /**
     * "The type of SIM card such as SIM, USIM, UICC."
  broad_mappings:
- wikidata:Q41349  # smart card
     */SIMType?: string,
}
/**
 * "A SIP address is an identifier for Session Initiation Protocol (SIP) communication."
 */
export interface SIPAaddress  extends DigitalAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A SIP address facet is a grouping of characteristics unique to a Session Initiation Protocol (SIP) standards conformant identifier assigned to a user to enable routing and management of SIP standards conformant communication to or from that user loosely coupled from any particular devices."
 */
export interface SIPAddressFacet  extends DigitalAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "An SMS message is a message conformant to the short message service (SMS) communication protocol standards."
 */
export interface SMSMessage  extends Message  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A SMS message facet is a grouping of characteristics unique to a message conformant to the short message service (SMS) communication protocol standards."
 */
export interface SMSMessageFacet  extends Facet  {
    isRead?: string,
}
/**
 * "An SQLite blob is a blob (binary large object) of data within an SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]"
 */
export interface SQLiteBlob  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An SQLite blob facet is a grouping of characteristics unique to a blob (binary large object) of data within an SQLite database. [based on https://en.wikipedia.org/wiki/SQLite]"
 */
export interface SQLiteBlobFacet  extends Facet  {
    rowIndex?: string,
    /**
     * "Identifier, Column name expressions"
     */columnName?: string,
    rowCondition?: string,
    /**
     * "The table containing a specified database record."
     */tableName?: string,
}
/**
 * "A security appliance is a purpose-built computer with software or firmware that is designed to provide a specific security function to protect computer networks."
 */
export interface SecurityAppliance  extends Appliance  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A semaphore is a variable or abstract dataType used to control access to a common resource by multiple processes and avoid critical section problems in a concurrent system such as a multitasking operating system. [based on https://en.wikipedia.org/wiki/semaphore_(programming)]"
 */
export interface Semaphore  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A send controlCode effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a controlCode, or other control-oriented communication signal, is sent to the observable object. An example of this would be an action sending a controlCode changing the running state of a process."
 */
export interface SendControlCodeEffectFacet  extends DefinedEffectFacet  {
    /**
     * "Specifies the actual controlCode that was sent to the observable object."
     */controlCode?: string,
}
/**
 * "A server is a server rack-mount based computer, minicomputer, supercomputer, etc"
 */
export interface Server  extends Computer  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A shop listing is a listing of offered products on an online marketplace/shop."
 */
export interface ShopListing  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A smart device is a microprocessor IoT device that is expected to be connected directly to cloud-based networks or via smartphone"
 */
export interface SmartDevice  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A smartphone is a portable device that combines mobile telephone and computing functions into one unit.  Examples include iPhone, Samsung Galaxy, Huawei, Blackberry. (Inferred by model and OperatingSystemFacet)"
 */
export interface SmartPhone  extends SmartDevice, MobilePhone, Computer  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A snapshot is a file system object representing a snapshot of the contents of a part of a file system at a point in time."
 */
export interface Snapshot  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A socket is a special file used for inter-process communication, which enables communication between two processes. In addition to sending data, processes can send file descriptors across a Unix domain socket connection using the sendmsg() and recvmsg() system calls. Unlike named pipes which allow only unidirectional data flow, sockets are fully duplex-capable. [based on https://en.wikipedia.org/wiki/Unix_file_types]"
 */
export interface Socket  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A socket address (combining and IP address and a port number) is a composite identifier for a network socket endpoint supporting internet protocol communications."
 */
export interface SocketAddress  extends Address  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "Software is a definitely scoped instance of a collection of data or computer instructions that tell the computer how to work. [based on https://en.wikipedia.org/wiki/Software]"
 */
export interface Software  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A software facet is a grouping of characteristics unique to a software program (a definitively scoped instance of a collection of data or computer instructions that tell the computer how to work). [based on https://en.wikipedia.org/wiki/Software]"
 */
export interface SoftwareFacet  extends Facet  {
    manufacturer?: Identity,
    /**
     * "Specifies the Common Platform Enumeration identifier for the software."
     */cpeid?: string,
    /**
     * "Specifies the language the string is written in, e.g. English.
    For consistency, it is strongly recommended to use the ISO 639-2 language code, if available. Please see http://www.loc.gov/standards/iso639-2/php/code_list.php for a list of ISO 639-2 codes."
     */language?: string,
    /**
     * "Specifies the SWID tag for the software."
     */swid?: string,
    version?: string,
}
/**
 * "A state change effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a state of the observable object is changed."
 */
export interface StateChangeEffectFacet  extends DefinedEffectFacet  {
    /**
     * "Specifies the observable object and its properties as they are after the state change effect occurred."
     */newObject?: ObservableObject,
    /**
     * "Specifies the observable object and its properties as they were before the state change effect occurred."
     */oldObject?: ObservableObject,
}
/**
 * "A storage medium is any digital storage device that applies electromagnetic or optical surfaces, or depends solely on electronic circuits as solid state storage, for storing digital data. Examples include HDD (PATA), SATA, SSD, Optical, memory_Card, Tape, etc"
 */
export interface StorageMedium  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A symbolic link is a file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]"
 */
export interface SymbolicLink  extends FileSystemObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A symbolic link facet is a grouping of characteristics unique to a file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. [based on https://en.wikipedia.org/wiki/Symbolic_link]"
 */
export interface SymbolicLinkFacet  extends Facet  {
    /**
     * "Specifies the file targeted by a symbolic link."
     */targetFile?: ObservableObject,
}
/**
 * "A TCP connection is a network connection that is conformant to the Transfer"
 */
export interface TCPConnection  extends NetworkConnection  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A TCP connection facet is a grouping of characteristics unique to portions of a network connection that are conformant to the Transmission Control Protocl (TCP) standard."
 */
export interface TCPConnectionFacet  extends Facet  {
    /**
     * "Specifies the source TCP flags."
     */sourceFlags?: string,
    /**
     * "Specifies the destination TCP flags. "
     */destinationFlags?: string,
}
/**
 * "A database table field and its associated value contained within a relational database."
 */
export interface TableField  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A database record facet contains properties associated with a specific table record value from a database."
 */
export interface TableFieldFacet  extends Facet  {
    /**
     * "Whether the specified database record field is null."
     */recordFieldIsNull?: string,
    /**
     * "A field name of a database record value being identified."
     */recordFieldName?: string,
    /**
     * "The table containing a specified database record."
     */tableName?: string,
    /**
     * "The schema that contains the identified database record."
     */tableSchema?: string,
    /**
     * "The field value of a specified database record."
     */recordFieldValue?: string,
    /**
     * "The unique ID that identifies a database record, supplied by the originating database engine."
     */recordRowID?: string,
}
/**
 * "A tablet is a mobile computer that is primarily operated by touching the screen. (Devices categorized by their manufacturer as a Tablet"
 */
export interface Tablet  extends Computer, SmartDevice, MobileDevice  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A task action type is a grouping of characteristics for a scheduled action to be completed."
 */
export interface TaskActionType  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the data associated with the task action-fired COM handler."
     */iComHandlerAction?: IComHandlerActionType,
    /**
     * "Specifies an action that executes a command-line operation. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380715(v=vs.85).aspx."
     */iExecAction?: IExecActionType,
    /**
     * "Specifies an action that shows a message box when a task is activated. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381302(v=vs.85).aspx."
     */iShowMessageAction?: IShowMessageActionType,
    /**
     * "Specifies an action that sends an e-mail, which in this context refers to actual email message sent. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380693(v=vs.85).aspx."
     */iEmailAction?: ObservableObject,
    /**
     * "Specifies the user-defined identifier for the action. This identifier is used by the Task Scheduler for logging purposes. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380590(v=vs.85).aspx."
     */actionID?: string,
    /**
     * "Specifies the type of the action. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa380596(v=vs.85).aspx."
     */actionType?: string,
}
/**
 * "A triggerType is a grouping of characterizes unique to a set of criteria that, when met, starts the execution of a task within a Windows operating system. [based on https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers]"
 */
export interface TriggerType  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies whether the trigger isEnabled."
     */isEnabled?: string,
    /**
     * "Specifies the date/time that the trigger is activated."
     */triggerBeginTime?: string,
    /**
     * "Specifies the date/time that the trigger is deactivated."
     */triggerEndTime?: string,
    /**
     * "Specifies the delay that takes place between when the task is registered and when the task is started."
     */triggerDelay?: string,
    /**
     * "The maximum amount of time that the task launched by the trigger is allowed to run. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383868(v=vs.85).aspx."
     */triggerMaxRunTime?: string,
    /**
     * "Specifies the type of Terminal Server session change that would trigger a task launch. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381298(v=vs.85).aspx."
     */triggerSessionChangeType?: string,
    /**
     * "Specifies the frequency at which the trigger repeats."
     */triggerFrequency?: string,
    /**
     * "Specifies the type of the task trigger."
     */triggerType?: string,
}
/**
 * "A tweet is message submitted by a Twitter user account to the Twitter microblogging platform."
 */
export interface Tweet  extends Message  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A twitter profile facet is a grouping of characteristics unique to an explicit digital representation of identity and characteristics of the owner of a single Twitter user account. [based on https://en.wikipedia.org/wiki/User_profile]"
 */
export interface TwitterProfileFacet  extends Facet  {
    /**
     * "Specifies the network location of the background associated with the profile"
     */profileBackgroundLocation?: ObservableObject,
    /**
     * "Specifies the network location of the banner associated with the profile"
     */profileBannerLocation?: ObservableObject,
    /**
     * "Specifies the network location of the profile image associated with the profile"
     */profileImageLocation?: ObservableObject,
    /**
     * "Specifies hashes of the background associated with the profile"
     */profileBackgroundHash?: Hash,
    /**
     * "Specifies hashes of the banner associated with the profile"
     */profileBannerHash?: Hash,
    /**
     * "Specifies hashes of the profile image associated with the profile"
     */profileImageHash?: Hash,
    /**
     * "Specifies whether the twitter profileIsProtected"
     */profileIsProtected?: string,
    /**
     * "Specifies whether the twitter profileIsVerified"
     */profileIsVerified?: string,
    /**
     * "Specifies the number of public lists that this profile is associated with."
     */listedCount?: number,
    /**
     * "Specifies the number of times that this profile has favorited a tweet"
     */favoritesCount?: string,
    /**
     * "Specifies the followersCount associated with the twitter profile"
     */followersCount?: string,
    /**
     * "Specifies the friendsCount associated with the twitter profile"
     */friendsCount?: string,
    /**
     * "Specifies the number of tweets that this profile has issued"
     */statusesCount?: string,
    /**
     * "Specifies the twitterHandle associated with the profile"
     */twitterHandle?: string,
    /**
     * "Specifies the twitter id associated with the profile"
     */twitterId?: string,
    /**
     * "Specifies the user-provided location string associated with the profile"
     */userLocationString?: string,
}
/**
 * "A UNIX account is an account on a UNIX operating system."
 */
export interface UNIXAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A UNIX account facet is a grouping of characteristics unique to an account on a UNIX operating system."
 */
export interface UNIXAccountFacet  extends Facet  {
    gid?: number,
    shell?: string,
}
/**
 * "A UNIX file is a file pertaining to the UNIX operating system."
 */
export interface UNIXFile  extends File  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A UNIX file permissions facet is a grouping of characteristics unique to the access rights (e.g., view, change, navigate, execute) of a file on a UNIX file system."
 */
export interface UNIXFilePermissionsFacet  extends Facet  {
}
/**
 * "A UNIX process is an instance of a computer program executed on a UNIX operating system."
 */
export interface UNIXProcess  extends Process  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A UNIX process facet is a grouping of characteristics unique to an instance of a computer program executed on a UNIX operating system."
 */
export interface UNIXProcessFacet  extends Facet  {
    /**
     * "Specifies a listing of the current file descriptors used by the Unix process."
     */openFileDescriptor?: number,
    /**
     * "Specifies the real user ID, which represents the Unix user who created the process."
     */ruid?: string,
}
/**
 * "A UNIX volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single UNIX file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
 */
export interface UNIXVolumeFacet  extends Facet  {
    /**
     * "Specifies the mountPoint of the partition."
     */mountPoint?: string,
    /**
     * "Specifies any options used when mounting the volume."
     */options?: string,
}
/**
 * "A URL is a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web) accessible resource."
 */
export interface URL  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A URL facet is a grouping of characteristics unique to a uniform resource locator (URL) acting as a resolvable address to a particular WWW (World Wide Web) accessible resource."
 */
export interface URLFacet  extends Facet  {
    /**
     * "Domain name or IP address where the resource is located."
     */host?: ObservableObject,
    /**
     * "Port on which communication takes place."
     */port?: number,
    /**
     * "fragment pointing to a specific part in the resource."
     */fragment?: string,
    /**
     * "The full stringValue of the URL."
     */fullValue?: string,
    /**
     * "Specifies an authentication password."
     */password?: string,
    /**
     * "Specifies the location of one object within another containing object."
     */path?: string,
    /**
     * "Query passed to the resource."
     */query?: string,
    /**
     * "Identifies the type of URL."
     */scheme?: string,
    /**
     * "Username used to authenticate to this resource."
     */userName?: string,
}
/**
 * "A URL history characterizes the stored URL history for a particular web browser"
 */
export interface URLHistory  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A URL history entry is a grouping of characteristics unique to the properties of a single URL history entry for a particular browser"
 */
export interface URLHistoryEntry  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies a URL associated with a particular observable object or facet."
     */url?: ObservableObject,
    /**
     * "Specifies the origination point (i.e., URL) of a URL request."
     */referrerURL?: ObservableObject,
    /**
     * "The date and time at which the validity of the object expires."
     */expirationTime?: string,
    /**
     * "Specifies the date/time that the URL referred to by the URL field was first visited"
     */firstVisit?: string,
    /**
     * "Specifies the date/time that the URL referred to by the URL field was lastVisited."
     */lastVisit?: string,
    /**
     * "Specifies the number of times a URL has been visited by a particular web browser."
     */visitCount?: number,
    /**
     * "Specifies the number of times the URL referred to by the URL field was manually entered into the browser's address field by the user. This field is only applicable for URL history entries generated by Google's Chrome browser."
     */manuallyEnteredCount?: string,
    /**
     * "Specifies the web browserUserProfile for which the URL history entry was created."
     */browserUserProfile?: string,
    /**
     * "Specifies the hostname of the system."
     */hostname?: string,
    /**
     * "Specifies the title of a web page."
     */pageTitle?: string,
    /**
     * "Specifies a string representing a keywordSearchTerm contained within the URL field."
     */keywordSearchTerm?: string,
}
/**
 * "A URL history facet is a grouping of characteristics unique to the stored URL history for a particular web browser"
 */
export interface URLHistoryFacet  extends Facet  {
    /**
     * "Specifies information about the particular Web Browser."
     */browserInformation?: ObservableObject,
    /**
     * "Specifies a URL history record stored in the browser's history."
     */urlHistoryEntry?: URLHistoryEntry[],
}
/**
 * "A URL visit characterizes the properties of a visit of a URL within a particular browser."
 */
export interface URLVisit  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A URL visit facet is a grouping of characteristics unique to the properties of a visit of a URL within a particular browser."
 */
export interface URLVisitFacet  extends Facet  {
    /**
     * "Specifies information about the particular Web Browser."
     */browserInformation?: ObservableObject,
    /**
     * "Specifies the URL visit origination point (i.e., URL) of the URL captured in the URL history entry, if applicable."
     */fromURLVisit?: ObservableObject,
    /**
     * "Specifies a URL associated with a particular observable object or facet."
     */url?: ObservableObject,
    /**
     * "Specifies the date/time of a specific visit of a URL within a particular browser."
     */visitTime?: string,
    /**
     * "Specifies the duration of a specific visit of a URL within a particular browser."
     */visitDuration?: string,
    /**
     * "Specifies how a browser navigated to a particular URL on a particular visit."
     */urlTransitionType?: string,
}
/**
 * "A user account is an account controlling a user's access to a network, system or platform."
 */
export interface UserAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A user account facet is a grouping of characteristics unique to an account controlling a user's access to a network, system, or platform."
 */
export interface UserAccountFacet  extends Facet  {
    canEscalatePrivs?: string,
    isPrivileged?: string,
    isServiceAccount?: string,
    homeDirectory?: string,
}
/**
 * "A user session is a temporary and interactive information interchange between two or more communicating devices within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]"
 */
export interface UserSession  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A user session facet is a grouping of characteristics unique to a temporary and interactive information interchange between two or more communicating devices within the managed scope of a single user. [based on https://en.wikipedia.org/wiki/Session_(computer_science)]"
 */
export interface UserSessionFacet  extends Facet  {
    /**
     * "Specifies the effectiveUser details used in the user session."
     */effectiveUser?: ObservableObject,
    /**
     * "Specifies the date/time of the login for the user session."
     */loginTime?: string,
    /**
     * "Specifies the date/time of the logout for the user session."
     */logoutTime?: string,
    /**
     * "Specifies the name of the effectiveGroup used in the user session."
     */effectiveGroup?: string,
    /**
     * "Specifies the effectiveGroupID of the group used in the user session."
     */effectiveGroupID?: string,
}
/**
 * "A values enumerated effect facet is a grouping of characteristics unique to the effects of actions upon observable objects where a value of the observable object is enumerated. An example of this would be the values of a registry key."
 */
export interface ValuesEnumeratedEffectFacet  extends DefinedEffectFacet  {
    /**
     * "The values that were enumerated as a result of the action on the object."
     */values?: string,
}
/**
 * "A volume is a single accessible storage area (volume) with a single file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
 */
export interface Volume  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
 */
export interface VolumeFacet  extends Facet  {
    /**
     * "The sectorSize of the volume in bytes."
     */sectorSize?: number,
    /**
     * "The unique identifier of the volume."
     */volumeID?: string,
}
/**
 * "A wearable device is an electronic device that is designed to be worn on a person's body"
 */
export interface WearableDevice  extends SmartDevice  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A web page is a specific collection of information provided by a website and displayed to a user in a web browser. A website typically consists of many web pages linked together in a coherent fashion. [based on https://en.wikipedia.org/wiki/Web_page]"
 */
export interface WebPage  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "Whois is a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]"
 */
export interface Whois  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Whois facet is a grouping of characteristics unique to a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]"
 */
export interface WhoisFacet  extends Facet  {
    /**
     * "Specifies the corresponding domainName for a Whois entry."
     */domainName?: ObservableObject,
    /**
     * "Specifies the corresponding ip address for a Whois entry. Usually corresponds to a nameServer lookup."
     */ipAddress?: ObservableObject,
    /**
     * "Specifies contact info for the registrant of a domain within a WHOIS entity."
     */registrantContactInfo?: ObservableObject,
    /**
     * "Specifies the corresponding serverName for a Whois entry. This usually corresponds to a nameServer lookup."
     */serverName?: ObservableObject,
    /**
     * "Specifies a list of nameServer entries for a Whois entry."
     */nameServer?: ObservableObject[],
    /**
     * "Specifies registrarInfo that would be returned from a registrar lookup."
     */registrarInfo?: WhoisRegistrarInfoType,
    /**
     * "Specifies the date in which the registered domain was created."
     */creationDate?: string,
    /**
     * "Specifies the date in which the registered domain will expire."
     */expirationDate?: string,
    /**
     * "Specifies the date and time that the Whois record was queried."
     */lookupDate?: string,
    /**
     * "Specifies the date in which the registered domain information was last updated."
     */updatedDate?: string,
    /**
     * "Specifies the domain id for the domain associated with a Whois entry."
     */domainID?: string,
    /**
     * "Specifies any remarks associated with this Whois entry."
     */remarks?: string,
    /**
     * "Specifies the name of the sponsoringRegistrar for a domain."
     */sponsoringRegistrar?: string,
    /**
     * "Specifies the registrantIDs associated with a domain lookup."
     */registrantIDs?: string,
    /**
     * "Specifies the DNSSEC property associated with a Whois entry. Acceptable values are: 'Signed' or 'Unsigned'."
     */dnssec?: string,
    /**
     * "Specifies a list of statuses for a given Whois entry."
     */status?: string,
    /**
     * "specifies the name of the Regional Internet Registry (RIR) which allocated the IP address contained in a WHOIS entry."
     */regionalInternetRegistry?: string,
}
/**
 * "A Whois contact type is a grouping of characteristics unique to contact-related information present in a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]"
 */
export interface WhoisContactFacet  extends ContactFacet  {
    /**
     * "Specifies what type of WHOIS contact this is."
     */whoisContactType?: string,
    /**
     * "contactAddress specifies information characterizing a geolocation address of a contact entity."
     */contactAddress?: ContactAddress,
    /**
     * "contactAffiliation specifies information characterizing details of an organizational affiliation for a single contact entity."
     */contactAffiliation?: ContactAffiliation,
    /**
     * "contactEmail specifies information characterizing details for contacting a contact entity by email."
     */contactEmail?: ContactEmail,
    /**
     * "contactMessaging specifies information characterizing details for contacting a contact entity by digital messaging."
     */contactMessaging?: ContactMessaging,
    /**
     * "contactPhone specifies information characterizing details for contacting a contact entity by telephone."
     */contactPhone?: ContactPhone,
    /**
     * "contactProfile specifies information characterizing details for contacting a contact entity by online service."
     */contactProfile?: ContactProfile,
    /**
     * "contactSIP specifies information characterizing details for contacting a contact entity by Session Initiation Protocol (SIP)."
     */contactSIP?: ContactSIP,
    /**
     * "contactURL specifies information characterizing details for contacting a contact entity by Uniform Resource Locator (URL)."
     */contactURL?: ContactURL,
    /**
     * "Source application specifies the software application that a particular contact or contact list is associated with."
     */sourceApplication?: ObservableObject,
    birthdate?: string,
    /**
     * "Last time contacted specifies the date and time that a particular contact was last contacted."
     */lastTimeContacted?: string,
    /**
     * "Number times contacted specifies the number of times a particular contact has been contacted."
     */numberTimesContacted?: number,
    /**
     * "Specifies an ID for the contact."
     */contactID?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
    /**
     * "The firstName of a person."
     */firstName?: string,
    /**
     * "The lastName of a person."
     */lastName?: string,
    /**
     * "The middleName of a person."
     */middleName?: string,
    /**
     * "Name phonetic specifies the phonetic pronunciation of the name of a person."
     */namePhonetic?: string,
    /**
     * "Name prefix specifies an honorific prefix (coming ordinally before first/given name) for the name of a person."
     */namePrefix?: string,
    /**
     * "Name suffix specifies an suffix (coming ordinally after last/family name) for the name of a person."
     */nameSuffix?: string,
    /**
     * "contactGroup specifies the name/tag of a particular named/tagged grouping of contacts."
     */contactGroup?: string,
    /**
     * "contactNote specifies a comment/note associated with a given contact."
     */contactNote?: string,
    /**
     * "Nickname specifies an alternate, unofficial and typically informal name for a person independent of their official name."
     */nickname?: string,
}
/**
 * "A Whois registrarInfo type is a grouping of characteristics unique to registrar-related information present in a response record conformant to the WHOIS protocol standard (RFC 3912). [based on https://en.wikipedia.org/wiki/WHOIS]"
 */
export interface WhoisRegistrarInfoType  extends UcoInherentCharacterizationThing  {
    /**
     * "An administrative address for a particular geolocation."
     */geoLocationAddress?: Location,
    /**
     * "contactPhoneNumber specifies a telephone service account number for contacting a contact entity by telephone."
     */contactPhoneNumber?: ObservableObject,
    /**
     * "An emailAddress."
     */emailAddress?: ObservableObject,
    /**
     * "Specifies the corresponding referralURL for a registrar."
     */referralURL?: ObservableObject,
    /**
     * "Specifies the corresponding Whois server for a registrar."
     */whoisServer?: ObservableObject,
    /**
     * "Specifies the Registrar GUID field of a Whois entry."
     */registrarGUID?: string,
    /**
     * "Specifies the Registrar ID field of a Whois entry."
     */registrarID?: string,
    /**
     * "The name of the registrar organization."
     */registrarName?: string,
}
/**
 * "A Wi-Fi address is a media access control (MAC) standards-conformant identifier assigned to a device networkInterface to enable routing and management of IEEE 802.11 standards-conformant communications to and from that device."
 */
export interface WifiAddress  extends MACAddress  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Wi-Fi address facet is a grouping of characteristics unique to a media access control (MAC) standards conformant identifier assigned to a device networkInterface to enable routing and management of IEEE 802.11 standards-conformant communications to and from that device."
 */
export interface WifiAddressFacet  extends MACAddressFacet  {
    /**
     * "The value of an address."
     */addressValue?: string,
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
}
/**
 * "A wiki is an online hypertext publication collaboratively edited and managed by its own audience directly using a web browser. A typical wiki contains multiple pages/articles for the subjects or scope of the project and could be either open to the public or limited to use within an organization for maintaining its internal knowledge base. [based on https://en.wikipedia.org/wiki/Wiki]"
 */
export interface Wiki  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A wiki article is one or more pages in a wiki focused on characterizing a particular topic."
 */
export interface WikiArticle  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows account is a user account on a Windows operating system."
 */
export interface WindowsAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows account facet is a grouping of characteristics unique to a user account on a Windows operating system."
 */
export interface WindowsAccountFacet  extends Facet  {
    groups?: string,
}
/**
 * "A Windows Active Directory account is an account managed by directory-based identity-related services of a Windows operating system."
 */
export interface WindowsActiveDirectoryAccount  extends DigitalAccount  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows Active Directory account facet is a grouping of characteristics unique to an account managed by directory-based identity-related services of a Windows operating system."
 */
export interface WindowsActiveDirectoryAccountFacet  extends Facet  {
    objectGUID?: string,
    activeDirectoryGroups?: string,
}
/**
 * "A Windows computer specification is the hardware ans software of a programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating system. [based on merriam-webster.com/dictionary/computer]"
 */
export interface WindowsComputerSpecification  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows computer specification facet is a grouping of characteristics unique to the hardware and software of a programmable electronic device that can store, retrieve, and process data running a Microsoft Windows operating system. [based on merriam-webster.com/dictionary/computer]"
 */
export interface WindowsComputerSpecificationFacet  extends Facet  {
    /**
     * "The organization that this copy of Windows is registered to."
     */registeredOrganization?: Identity,
    /**
     * "The person or organization that is the registeredOwner of this copy of Windows."
     */registeredOwner?: Identity,
    /**
     * "A list of global flags. See also: http://msdn.microsoft.com/en-us/library/windows/hardware/ff549557(v=vs.85).aspx."
     */globalFlagList?: GlobalFlagType[],
    /**
     * "The Windows_Directory field specifies the fully-qualified path to the Windows install directory."
     */windowsDirectory?: ObservableObject,
    /**
     * "The Windows_System_Directory field specifies the fully-qualified path to the Windows system directory."
     */windowsSystemDirectory?: ObservableObject,
    /**
     * "The Windows_Temp_Directory field specifies the fully-qualified path to the Windows temporary files directory."
     */windowsTempDirectory?: ObservableObject,
    /**
     * "Specifies the date on which the device was last shutdown."
     */lastShutdownDate?: string,
    /**
     * "Specifies the date on which the operating system (OS) was installed."
     */osInstallDate?: string,
    /**
     * "Specifies the date on which the operating system (OS) was last upgraded."
     */osLastUpgradeDate?: string,
    /**
     * "The Microsoft Product ID. See also: http://support.microsoft.com/gp/pidwin."
     */msProductID?: string,
    /**
     * "The Microsoft ProductName of the current installation of Windows. This is typically found in HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion!ProductName."
     */msProductName?: string,
    /**
     * "Specifies the NetBIOS (network  Basic Input/Output System) name of the Windows system. This is not the same as the host name."
     */netBIOSName?: string,
    /**
     * "The domain(s) that the system belongs to."
     */domain?: string,
}
/**
 * "A Windows critical section is a Windows object that provides synchronization similar to that provided by a mutex object, except that a critical section can be used only by the threads of a single process. Critical section objects cannot be shared across processes. Event, mutex, and semaphore objects can also be used in a single-process application, but critical section objects provide a slightly faster, more efficient mechanism for mutual-exclusion synchronization (a processor-specific test and set instruction). Like a mutex object, a critical section object can be owned by only one thread at a time, which makes it useful for protecting a shared resource from simultaneous access. Unlike a mutex object, there is no way to tell whether a critical section has been abandoned. [based on https://docs.microsoft.com/en-us/windows/win32/sync/critical-section-objects]"
 */
export interface WindowsCriticalSection  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows event is a notification record of an occurance of interest (system, security, application, etc.) on a Windows operating system."
 */
export interface WindowsEvent  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A windows file mapping is the association of a file's contents with a portion of the virtual address space of a process within a Windows operating system. The system creates a file mapping object (also known as a section object) to maintain this association. A file view is the portion of virtual address space that a process uses to access the file's contents. file mapping allows the process to use both random input and output (I/O) and sequential I/O. It also allows the process to work efficiently with a large data file, such as a database, without having to map the whole file into memory. Multiple processes can also use memory-mapped files to share data. processes read from and write to the file view using pointers, just as they would with dynamically allocated memory. The use of file mapping improves efficiency because the file resides on disk, but the file view resides in memory.[based on https://docs.microsoft.com/en-us/windows/win32/memory/file-mapping]"
 */
export interface WindowsFileMapping  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows handle is an abstract reference to a resource within the Windows operating system, such as a window, memory, an open file or a pipe. It is the mechanism by which applications interact with such resources in the Windows operating system."
 */
export interface WindowsHandle  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows hook is a mechanism by which an application can intercept events, such as messages, mouse actions, and keystrokes within the Windows operating system. A function that intercepts a particular type of event is known as a hook procedure. A hook procedure can act on each event it receives, and then modify or discard the event. [based on https://docs.microsoft.com/en-us/windows/win32/winmsg/about-hooks]"
 */
export interface WindowsHook  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows mailslot is is a pseudofile that resides in memory, and may be accessed using standard file functions. The data in a mailslot message can be in any form, but cannot be larger than 424 bytes when sent between computers. Unlike disk files, mailslots are temporary. When all handles to a mailslot are closed, the mailslot and all the data it contains are deleted. [based on https://docs.microsoft.com/en-us/windows/win32/ipc/about-mailslots]"
 */
export interface WindowsMailSlot  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows network share is a Windows computer resource made available from one host to other hosts on a computer network. It is a device or piece of information on a computer that can be remotely accessed from another computer transparently as if it were a resource in the local machine. network  sharing is made possible by inter-process communication over the network. [based on https://en.wikipedia.org/wiki/Shared_resource]"
 */
export interface WindowsNetworkShare  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows PE binary file is a Windows portable executable (PE) file."
 */
export interface WindowsPEBinaryFile  extends File  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows PE binary file facet is a grouping of characteristics unique to a Windows portable executable (PE) file."
 */
export interface WindowsPEBinaryFileFacet  extends Facet  {
    /**
     * "Specifies the PE optional header of the PE binary."
     */optionalHeader?: WindowsPEOptionalHeader,
    /**
     * "Specifies metadata about the sections in the PE file."
     */sections?: WindowsPESection[],
    /**
     * "Specifies any hashes that were computed for the file header."
     */fileHeaderHashes?: Hash[],
    /**
     * "Specifies the time when the PE binary was created."
     */timeDateStamp?: string,
    /**
     * "Specifies the file offset of the COFF symbol table."
     */pointerToSymbolTable?: string,
    /**
     * "Specifies the numberOfSections in the PE binary, as a non-negative integer."
     */numberOfSections?: number,
    /**
     * "Specifies the number of entries in the symbol table of the PE binary, as a non-negative integer."
     */numberOfSymbols?: number,
    /**
     * "Specifies the size of the optionalHeader of the PE binary."
     */sizeOfOptionalHeader?: number,
    /**
     * "Specifies the special import hash, or â€˜imphashâ€™, calculated for the PE Binary based on its imported libraries and functions."
     */impHash?: string,
    /**
     * "Specifies the type of the PE binary."
     */peType?: string,
    /**
     * "Specifies the type of target machine."
     */machine?: string,
    /**
     * "Specifies the flags that indicate the fileâ€™s characteristics."
     */characteristics?: string,
}

export interface WindowsPEBinaryType  {
}
/**
 * "A Windows PE file header is a grouping of characteristics unique to the 'header' of a Windows PE (Portable Executable) file, consisting of a collection of metadata about the overall nature and structure of the file."
 */
export interface WindowsPEFileHheader  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the time when the PE binary was created."
     */timeDateStamp?: string,
}
/**
 * "A Windows PE optional header is a grouping of characteristics unique to the 'optionalHeader' of a Windows PE (Portable Executable) file, consisting of a collection of metadata about the executable code structure of the file."
 */
export interface WindowsPEOptionalHeader  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies the linker major version number."
     */majorLinkerVersion?: string,
    /**
     * "Specifies the linker minor version number."
     */minorLinkerVersion?: string,
    /**
     * "Specifies the address of the entry point relative to the imageBase when the executable is loaded into memory."
     */addressOfEntryPoint?: string,
    /**
     * "Specifies the address that is relative to the imageBase of the beginning-of-code section when it is loaded into memory."
     */baseOfCode?: string,
    /**
     * "Specifies the checksum of the PE binary."
     */checksum?: string,
    /**
     * "Specifies the factor (in bytes) that is used to align the raw data of sections in the image file."
     */fileAlignment?: string,
    /**
     * "Specifies the address that is relative to the imageBase of the beginning-of-data section when it is loaded into memory."
     */imageBase?: string,
    /**
     * "Specifies the reserved loaderFlags"
     */loaderFlags?: string,
    /**
     * "Specifies the number of data-directory entries in the remainder of the optionalHeader."
     */numberOfRVAAndSizes?: string,
    /**
     * "Specifies the alignment (in bytes) of PE sections when they are loaded into memory."
     */sectionAlignment?: string,
    /**
     * "Specifies the size of the code (text) section. If there are multiple such sections, this refers to the sum of the sizes of each section."
     */sizeOfCode?: string,
    /**
     * "Specifies the combined size of the MS-DOS, PE header, and section headers, rounded up a multiple of the value specified in the file_alignment header."
     */sizeOfHeaders?: string,
    /**
     * "Specifies the size of the local heap space to commit."
     */sizeOfHeapCommit?: string,
    /**
     * "Specifies the size of the local heap space to reserve."
     */sizeOfHeapReserve?: string,
    /**
     * "Specifies the size, in bytes, of the image, including all headers, as the image is loaded in memory."
     */sizeOfImage?: string,
    /**
     * "Specifies the size of the initialized data section. If there are multiple such sections, this refers to the sum of the sizes of each section."
     */sizeOfInitializedData?: string,
    /**
     * "Specifies the size of the stack to commit."
     */sizeOfStackCommit?: string,
    /**
     * "Specifies the size of the stack to reserve."
     */sizeOfStackReserve?: string,
    /**
     * "Specifies the size of the uninitialized data section. If there are multiple such sections, this refers to the sum of the sizes of each section."
     */sizeOfUninitializedData?: string,
    /**
     * "Specifies the reserved win32VersionValue."
     */win32VersionValue?: string,
    /**
     * "Specifies the flags that characterize the PE binary."
     */dllCharacteristics?: string,
    /**
     * "Specifies the value that indicates the type of the PE binary."
     */magic?: string,
    /**
     * "Specifies the major version number of the image."
     */majorImageVersion?: string,
    /**
     * "Specifies the major version number of the required operating system."
     */majorOSVersion?: string,
    /**
     * "Specifies the major version number of the subsystem."
     */majorSubsystemVersion?: string,
    /**
     * "Specifies the minor version number of the image."
     */minorImageVersion?: string,
    /**
     * "Specifies the minor version number of the required operating system."
     */minorOSVersion?: string,
    /**
     * "Specifies the minor version number of the subsystem."
     */minorSubsystemVersion?: string,
    /**
     * "Specifies the subsystem (e.g., GUI, device driver, etc.) that is required to run this image."
     */subsystem?: string,
}
/**
 * "A Windows PE section is a grouping of characteristics unique to a specific default or custom-defined region of a Windows PE (Portable Executable) file, consisting of an individual portion of the actual executable content of the file delineated according to unique purpose and memory protection requirements."
 */
export interface WindowsPESection  extends UcoInherentCharacterizationThing  {
    /**
     * "Specifies any hashes computed over the section."
     */hashes?: Hash[],
    /**
     * "Shannon entropy (a measure of randomness) of the data."
     */entropy?: number,
    /**
     * The number of item belonging to a collection.
     */size?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
}
/**
 * "The Windows prefetch contains entries in a Windows prefetch file (used to speed up application startup starting with Windows XP)."
 */
export interface WindowsPrefetch  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows prefetch facet is a grouping of characteristics unique to entries in the Windows prefetch file (used to speed up application startup starting with Windows XP)."
 */
export interface WindowsPrefetchFacet  extends Facet  {
    /**
     * "The volume from which the prefetch application was run. If the applicatin was run from multiple volumes, there will be a separate prefetch file for each."
     */volume?: ObservableObject,
    /**
     * "Directories accessed by the prefetch application during startup."
     */accessedDirectory?: ObservableObject[],
    /**
     * " files (e.g., DLLs and other support files) used by the application during startup."
     */accessedFile?: ObservableObject[],
    /**
     * "Timestamp of when the prefetch application was firstRun."
     */firstRun?: string,
    /**
     * "Timestamp of when the prefetch application was lastRun."
     */lastRun?: string,
    /**
     * "The number of times the prefetch application has executed."
     */timesExecuted?: number,
    /**
     * "Name of the executable of the prefetch file."
     */applicationFileName?: string,
    /**
     * "An eight character hash of the location from which the application was run."
     */prefetchHash?: string,
}
/**
 * "A Windows process is a program running on a Windows operating system."
 */
export interface WindowsProcess  extends Process  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows process facet is a grouping of characteristics unique to a program running on a Windows operating system."
 */
export interface WindowsProcessFacet  extends Facet  {
    startupInfo?: Dictionary,
    aslrEnabled?: string,
    depEnabled?: string,
    ownerSID?: string,
    /**
     * "The priority of the email."
     */priority?: string,
    windowTitle?: string,
}
/**
 * "The Windows registry hive is a particular logical group of keys, subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]"
 */
export interface WindowsRegistryHive  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows registry hive facet is a grouping of characteristics unique to a particular logical group of keys, subkeys, and values in a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]"
 */
export interface WindowsRegistryHiveFacet  extends Facet  {
    /**
     * "The type of a registry hive."
     */hiveType?: string,
}
/**
 * "A Windows registry key is a particular key within a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]"
 */
export interface WindowsRegistryKey  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows registry key facet is a grouping of characteristics unique to a particular key within a Windows registry (A hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for applications that opt to use the registry). [based on https://en.wikipedia.org/wiki/Windows_Registry]"
 */
export interface WindowsRegistrykeyFacet  extends Facet  {
    /**
     * "Specifies the name of the creator of the registry key."
     */creator?: ObservableObject,
    /**
     * "The values that were enumerated as a result of the action on the object."
     */registryValues?: WindowsRegistryValue[],
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    numberOfSubkeys?: number,
    /**
     * "A key property of a single dictionary entry."
     */key?: string,
}
/**
 * "A Windows registry value is a grouping of characteristics unique to a particular value within a Windows registry (a hierarchical database that stores low-level settings for the Microsoft Windows operating sytem and for applications that opt to use the registry. [based on https://en.wikipedia.org/wiki/Windows_Registry]"
 */
export interface WindowsRegistryValue  extends UcoInherentCharacterizationThing  {
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Information arranged for automatic processing
     */data?: string,
    dataType?: string,
}
/**
 * "A Windows service is a specific Windows service (a computer program that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX ). [based on https://en.wikipedia.org/wiki/Windows_service]"
 */
export interface WindowsService  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows service facet is a grouping of characteristics unique to a specific Windows service (a computer program that operates in the background of a Windows operating system, similar to the way a UNIX daemon runs on UNIX ). [based on https://en.wikipedia.org/wiki/Windows_service]"
 */
export interface WindowsServiceFacet  extends Facet  {
    /**
     * "Display name specifies the name to display for some entity within a user interface."
     */displayName?: string,
    groupName?: string,
    serviceName?: string,
    servicStatus?: string,
    serviceType?: string,
    startCommandLine?: string,
    startType?: string,
    descriptions?: string,
}

export interface WindowsServiceStartType  {
}

export interface WindowsServiceStatus  {
}

export interface WindowsServiceType  {
}
/**
 * "A Windows system restore is a capture of a Windows computer's state (including system files, installed applications, Windows Registry, and system settings) at a particular point in time such that the computer can be reverted to that state in the event of system malfunctions or other problems. [based on https://en.wikipedia.org/wiki/System_Restore]"
 */
export interface WindowsSystemRestore  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows task is a process that is scheduled to execute on a Windows operating system by the Windows Task Scheduler. [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]"
 */
export interface WindowsTask  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows Task facet is a grouping of characteristics unique to a Windows Task (a process that is scheduled to execute on a Windows operating system by the Windows Task Scheduler). [based on http://msdn.microsoft.com/en-us/library/windows/desktop/aa381311(v=vs.85).aspx]"
 */
export interface WindowsTaskFacet  extends Facet  {
    /**
     * "Specifies the account referenced in an event log entry or used to run the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381228(v=vs.85).aspx."
     */account?: ObservableObject,
    /**
     * "The application associated with this object."
     */application?: ObservableObject,
    /**
     * "Specifies application defined data associated with the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381271(v=vs.85).aspx."
     */workItemData?: ObservableObject,
    /**
     * 'Specifies the workingDirectory for the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381878(v=vs.85).aspx'
     */workingDirectory?: ObservableObject,
    /**
     * "Specifies a list of actions to be performed by the scheduled task."
     */actionList?: TaskActionType[],
    /**
     * "Specifies a set of triggers used by the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383264(v=vs.85).aspx."
     */triggerList?: string,
    /**
     * "Specifies the most recent run date/time of this scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381254(v=vs.85).aspx."
     */mostRecentRunTime?: string,
    /**
     * "Specifies the next run date/time of the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381257(v=vs.85).aspx."
     */nextRunTime?: string,
    /**
     * "The date and time at which the observable object being characterized was created. This time pertains to an intrinsic characteristic of the observable object, and would be consistent across independent characterizations or observations of the observable object."
     */observableCreatedTime?: string,
    /**
     * "Specifies the last exitCode of the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381245(v=vs.85).aspx."
     */exitCode?: number,
    /**
     * "Specifies the maximum run time of the scheduled task before terminating, in milliseconds. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381874(v=vs.85).aspx."
     */maxRunTime?: number,
    /**
     * "Specifies the security logon method required to run the tasks associated with the account. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa383013(v=vs.85).aspx."
     */accountLogonType?: string,
    /**
     * "Specifies the permission level of the account that the task will be run at."
     */accountRunLevel?: string,
    /**
     * "Specifies the imageName for the task."
     */imageName?: string,
    /**
     * "Specifies the command line parameters used to launch the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381875(v=vs.85).aspx."
     */parameters?: string,
    /**
     * "Specifies a comment for the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381232(v=vs.85).aspx."
     */taskComment?: string,
    /**
     * "Specifies the name of the creator of the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381235(v=vs.85).aspx."
     */taskCreator?: string,
    /**
     * "Specifies any flags that modify the behavior of the scheduled task. See also: http://msdn.microsoft.com/en-us/library/windows/desktop/aa381248(v=vs.85).aspx."
     */flags?: string,
    /**
     * "The priority of the email."
     */priority?: string,
    /**
     * "Specifies a list of statuses for a given Whois entry."
     */status?: string,
}
/**
 * "A Windows thread is a single thread of execution within a Windows process."
 */
export interface WindowsThread  extends ProcessThread  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A Windows thread facet is a grouping os characteristics unique to a single thread of execution within a Windows process."
 */
export interface WindowsThreadFacet  extends Facet  {
    creationTime?: string,
    parameterAddress?: string,
    startAddress?: string,
    /**
     * "The priority of the email."
     */priority?: string,
    stackSize?: string,
    threadID?: string,
    /**
     * A description of particular contextual affinity.
     */context?: string,
    runningStatus?: string,
    securityAttributes?: string,
    creationFlags?: string,
}
/**
 * "A Windows volume facet is a grouping of characteristics unique to a single accessible storage area (volume) with a single windows file system. [based on https://en.wikipedia.org/wiki/volume_(computing)]"
 */
export interface WindowsVolumeFacet  extends Facet  {
    /**
     * "Specifies the driveLetter of a windows volume."
     */driveLetter?: string,
    /**
     * "Specifies the driveType of a windows volume."
     */driveType?: string,
    /**
     * "Specifies the attributes of a windows volume."
     */windowsVolumeAttributes?: string,
}
/**
 * "A Windows waitable timer is a synchronization object within the Windows operating system whose state is set to signaled when a specified due time arrives. There are two types of waitable timers that can be created: manual-reset and synchronization. A timer of either type can also be a periodic timer. [based on https://docs.microsoft.com/en-us/windows/win32/sync/waitable-timer-objects]"
 */
export interface WindowsWaitableTime  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A wireless network connection is a connection (completed or attempted) across an IEEE 802.11 standards-confromant digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]"
 */
export interface WirelessNetworkConnection  extends NetworkConnection  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A wireless network connection facet is a grouping of characteristics unique to a connection (completed or attempted) across an IEEE 802.11 standards-conformant digital network (a group of two or more computer systems linked together). [based on https://www.webopedia.com/TERM/N/network.html]"
 */
export interface WirelessNetworkConnectionFacet  extends Facet  {
    /**
     * "The baseStation."
  close_mappings:
- wikidata:Q1332343  # cell site
     */baseStation?: string,
    /**
     * "Specifies an authentication password."
     */password?: string,
    /**
     * "network  identifier."
     */ssid?: string,
    /**
     * "Specifies the security mode of a wireless network (None, WEP, WPA, etc)."
     */wirelessNetworkSecurityMode?: string,
}
/**
 * "A write blocker is a device that allows read-only access to storage mediums in order to preserve the integrity of the data being analyzed. Examples include Tableau, Cellibrite, Talon, etc"
 */
export interface WriteBlocker  extends Device  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A X.509 certificate is a public key digital identity certificate conformant to the X.509 PKI (Public Key Infrastructure) standard."
 */
export interface X509Certificate  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "A X.509 certificate facet is a grouping of characteristics unique to a public key digital identity certificate conformant to the X.509 PKI (Public Key Infrastructure) standard."
 */
export interface X509CertificateFacet  extends Facet  {
    x509v3extensions?: X509V3ExtensionsFacet,
    /**
     * "A hash calculated on the certificate Issuer name."
     */issuerHash?: Hash,
    /**
     * "A hash calculated on the certificate subject name."
     */subjectHash?: Hash,
    /**
     * "A hash calculated on the entire certificate including signature."
     */thumbprintHash?: Hash,
    isSelfSigned?: string,
    validityNotAfter?: string,
    validityNotBefore?: string,
    subjectPublicKeyExponent?: number,
    issuer?: string,
    serialNumber?: string,
    /**
     * "A"
     */signature?: string,
    signatureAlgorithm?: string,
    /**
     * "The subject of the email."
     */subject?: string,
    subjectPublicKeyAlgorithm?: string,
    subjectPublicKeyModulus?: string,
    version?: string,
}
/**
 * "An X.509 v3 certificate is a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard."
 */
export interface X509V3Certificate  extends ObservableObject  {
    hasChanged?: string,
    /**
     * the particular condition that someone or something is in at a specific time.
     */state?: string,
    /**
     * The link to a bag in which the item is member.
     */itemOf?: Bag,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An X.509 v3 certificate extensions facet is a grouping of characteristics unique to a public key digital identity certificate conformant to the X.509 v3 PKI (Public Key Infrastructure) standard."
 */
export interface X509V3ExtensionsFacet  extends Facet  {
    privateKeyUsagePeriodNotAfter?: string,
    privateKeyUsagePeriodNotBefore?: string,
    authorityKeyIdentifier?: string,
    basicConstraints?: string,
    /**
     * "Object identifiers (OIDS), comma separated"
     */certificatePolicies?: string,
    crlDistributionPoints?: string,
    extendedKeyUsage?: string,
    inhibitAnyPolicy?: string,
    issuerAlternativeName?: string,
    keyUsage?: string,
    nameConstraints?: string,
    policyConstraints?: string,
    policyMappings?: string,
    subjectAlternativeName?: string,
    subjectDirectoryAttributes?: string,
    subjectKeyIdentifier?: string,
}
/**
 * "An action is something that may be done or performed."
 */
export interface Action  extends UcoObject  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An action argument facet is a grouping of characteristics unique to a single parameter of an action."
 */
export interface ActionArgumentFacet  extends Facet  {
    /**
     * "The identifying label of an argument."
     */argumentName?: string,
    /**
     * "The value of an action parameter."
     */value?: string,
}
/**
 * "An action estimation facet is a grouping of characteristics unique to decision-focused approximation aspects for an action that may potentially be performed."
 */
export interface ActionEstimationFacet  extends Facet  {
    /**
     * "An estimation of the cost if the action is performed."
     */estimatedCost?: string,
    /**
     * "An estimation of the effectiveness of the action at achieving its objective if the action is performed."
     */estimatedEfficacy?: string,
    /**
     * "An estimation of the impact if the action is performed."
     */estimatedImpact?: string,
    /**
     * "The intended purpose for performing the action."
     */objective?: string,
}
/**
 * "An action frequency facet is a grouping of characteristics unique to the frequency of occurrence for an action."
 */
export interface ActionFrequencyFacet  extends Facet  {
    /**
     * "The frequency rate for the occurence of an action."
     */rate?: number,
    /**
     * "The time scale utilized for the frequency rate count for the occurence of an action."
     */scale?: string,
    /**
     * "The units of measure utilized for the frequency rate count for the occurence of an action."
     */units?: string,
    /**
     * "A characterization of the frequency trend for the occurence of an action."
     */trend?: string,
}
/**
 * "An action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action lifecycles."
 */
export interface ActionLifecycle  extends Action  {
    /**
     * "The ordered set of actions or sub action-lifecycles that represent the action lifecycle."
     */phase?: ArrayOfAction,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An action pattern is a grouping of characteristics unique to a combination of actions forming a consistent or characteristic arrangement."
 */
export interface ActionPattern  extends Action, Pattern  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An array of action is an ordered list of references to things that may be done or performed."
 */
export interface ArrayOfAction  extends UcoInherentCharacterizationThing  {
    /**
     * "A characterization of a single action."
     */action?: Action,
}
/**
 * A granular marking is a grouping of characteristics unique to specification of MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) that apply to particular portions of a particular UCO object.
 */
export interface GranularMarking  extends UcoInherentCharacterizationThing  {
    /**
     * Represents specific MarkingDefinitions to be applied to UCO data.
     */marking?: string,
    /**
     * "Explicit specification of exactly which portions of a UCO object to apply MarkingDefinitions to.  Specific syntax for how to specify the UCO object portions is dependent on the particular syntactic serialization implementation (XML, JSON, etc.) of UCO and MUST be explicitly specified in a separate binding specification for that syntactic serialization implementation (e.g. a UCO XML Binding Specification)."
     */contentSelectors?: string,
}
/**
 * A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared.
 */
export interface LicenseMarking  extends MarkingModel  {
    /**
     * Specifies the Marking Model for a Marking Definition.
     */definitionType?: string,
    /**
     * Specifies the identifier for the type of license
     */license?: string,
}
/**
 * A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared.
 */
export interface MarkingDefinition  extends MarkingDefinitionAbstraction  {
    /**
     * Explicit specification of a data marking instance.
     */definition?: string,
    /**
     * Specifies the Marking Model for a Marking Definition.
     */definitionType?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * A MarkingModel is a grouping of characteristics unique to the expression of a particular form of data MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared)
 */
export interface MarkingModel  extends UcoInherentCharacterizationThing  {
}
/**
 * A release-to marking is a grouping of characteristics unique to the expression of data MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of authorized persons and/or organizations to which to the associated content may be released. The existence of the Release-To marking restricts access to ONLY those identities explicitly listed, regardless of whether another data marking exists that allows sharing with other members of the community.
 */
export interface ReleaseToMarking  extends MarkingModel  {
    /**
     * Specifies the identities that are authorized to access the data to which the data marking is associated.  The list of authorized identities are represented as UUIDs.
     */authorizedIdentities?: string,
    /**
     * Specifies the Marking Model for a Marking Definition.
     */definitionType?: string,
}
/**
 * A statement marking is a grouping of characteristics unique to the expression of data MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement markings are generally not machine-readable. An example of this would be a simple marking to apply copyright information, such as 'Copyright 2014 Acme Inc.'.
 */
export interface StatementMarking  extends MarkingModel  {
    /**
     * Specifies the Marking Model for a Marking Definition.
     */definitionType?: string,
    /**
     * Specifies the statement to apply to the structure for which the Marking is to be applied.
     */statement?: string,
}
/**
 * A terms of use marking is a grouping of characteristics unique to the expression of data MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual statement specifying the Terms of Use (that is, the conditions under which the content may be shared, applied, or otherwise used) of the marked content. An example of this would be used to communicate a simple statement, such as 'Acme Inc. is not responsible for the content of this file'.
 */
export interface TermsOfUseMarking  extends MarkingModel  {
    /**
     * Specifies the Marking Model for a Marking Definition.
     */definitionType?: string,
    /**
     * Specifies the terms of use that apply to the structure for which the Marking is to be applied.
     */termsOfUse?: string,
}
/**
 * "An analysis is an action of detailed examination of something in order to understand its nature, context or essential features."
 */
export interface Analysis  extends Action  {
    /**
     * "References to other actions that make up part of a larger more complex action."
     */subaction?: Action[],
    /**
     * "The environment wherein an action occurs."
     */environment?: UcoObject,
    /**
     * "The primary performer of an action."
     */performer?: UcoObject,
    /**
     * "A characterization of the differences between the expected and the actual performance of the action."
     */error?: UcoObject[],
    /**
     * "The things used to perform an action."
     */instrument?: UcoObject[],
    /**
     * "The things that the action is performed on/against."
     */object?: UcoObject[],
    /**
     * "The supporting (non-primary) performers of an action."
     */participant?: UcoObject[],
    /**
     * "The things resulting from performing an action."
     */result?: UcoObject[],
    /**
     * "The locations where an action occurs."
     */location?: Location[],
    /**
     * "The time at which performance of the action ended."
     */endTime?: string,
    /**
     * "The time at which performance of the action began."
     */startTime?: string,
    /**
     * "The number of times that the action was performed."
     */actionCount?: string,
    /**
     * "The current state of the action."
     */actionStatus?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An analytic result is a characterization of the understanding resulting from an analysis action."
 */
export interface AnalyticResult  extends Assertion  {
    /**
     * "The analysis action that resulted in an analytic result."
     */originatingAnalysis?: Analysis,
    /**
     * "Structured content expressing the results of an analysis action."
     */resultContent?: UcoObject[],
    /**
     * A textual statement of an assertion.
     */statement?: string,
    /**
     * The identity that created a characterization of a concept.
     */createdBy?: string,
    /**
     * A human-readable description of an entity
     */description?: string,
    /**
     * Specifies a reference to a resource outside of the UCO.
     */externalReference?: string,
    /**
     * Further sets of properties characterizing a concept based on the particular context of the class and of the particular instance of the concept being characterized.
     */hasFacet?: string,
    /**
     * Specifies the time that this particular version of the object was modified. The object creator can use the time it deems most appropriate as the time this version of the object was modified. The value of the modified property for a given object version MUST be later than or equal to the value of the created property. Object creators MUST update the modified property when creating a new version of an object. The modified timestamp MUST be precise to the nearest millisecond (exactly three digits after the decimal place in seconds).
     */modifiedTime?: string,
    /**
     * The name of a particular concept characterization.
     */name?: string,
    /**
     * Marking definitions to be applied to a particular concept characterization in its entirety.
     */objectMarking?: MarkingDefinitionAbstraction[],
    /**
     * The time at which a characterization of a concept is created. This time pertains to the time of creating the record object, and is not an intrinsic characteristic of the concept.
     */objectCreatedTime?: string,
    /**
     * The version of UCO ontology or subontology specification used to characterize a concept.
     */specVersion?: string,
    /**
     * A generic tag/label.
     */tag?: string,
}
/**
 * "An analytic result facet is a grouping of characteristics unique to the results of an analysis action."
 */
export interface AnalyticResultFacet  extends Facet  {
}
/**
 * "An artifact classification is a single specific assertion that a particular class of a classification taxonomy applies to something."
 */
export interface ArtifactClassification  extends UcoInherentCharacterizationThing  {
    /**
     * "The level of confidence that a classification assertion is correct."
     */classificationConfidence?: number,
    /**
     * "A specific classification class."
     */class?: string,
}
/**
 * "An artifact classification result facet is a grouping of characteristics unique to the results of an artifact classification analysis action."
 */
export interface ArtifactClassificationResultFacet  extends AnalyticResultFacet  {
    /**
     * "An asserted classification of an analyzed artifact resulting from the analysis."
     */classification?: ArtifactClassification[],
}

