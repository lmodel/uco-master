

CREATE TABLE "Account" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AccountAuthenticationFacet" (
	"passwordLastChanged" DATETIME, 
	password TEXT, 
	"passwordType" TEXT, 
	PRIMARY KEY ("passwordLastChanged", password, "passwordType")
);

CREATE TABLE "AccountFacet" (
	"accountIssuer" TEXT, 
	owner TEXT, 
	"isActive" BOOLEAN, 
	"expirationDate" DATETIME, 
	"modifiedTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	"accountIdentifier" TEXT, 
	"accountType" TEXT, 
	PRIMARY KEY ("accountIssuer", owner, "isActive", "expirationDate", "modifiedTime", "observableCreatedTime", "accountIdentifier", "accountType")
);

CREATE TABLE "Action" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "ActionArgumentFacet" (
	"argumentName" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("argumentName", value)
);

CREATE TABLE "ActionEstimationFacet" (
	"estimatedCost" TEXT, 
	"estimatedEfficacy" TEXT, 
	"estimatedImpact" TEXT, 
	objective TEXT, 
	PRIMARY KEY ("estimatedCost", "estimatedEfficacy", "estimatedImpact", objective)
);

CREATE TABLE "ActionFrequencyFacet" (
	rate FLOAT NOT NULL, 
	scale TEXT NOT NULL, 
	units TEXT NOT NULL, 
	trend VARCHAR(10) NOT NULL, 
	PRIMARY KEY (rate, scale, units, trend)
);

CREATE TABLE "ActionLifecycle" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	phase TEXT NOT NULL, 
	error TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, instrument, object, participant, result, location, phase, error, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "ActionPattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "Adaptor" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Address" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AddressFacet" (
	address TEXT, 
	PRIMARY KEY (address)
);

CREATE TABLE "AlternateDataStream" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AlternateDataStreamFacet" (
	hashes TEXT, 
	name TEXT, 
	size INTEGER, 
	PRIMARY KEY (hashes, name, size)
);

CREATE TABLE "Analysis" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "AnalyticResult" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	"originatingAnalysis" TEXT, 
	"resultContent" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement, "originatingAnalysis", "resultContent")
);

CREATE TABLE "AnalyticTool" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	_creator TEXT, 
	_references TEXT, 
	"servicePack" TEXT, 
	"toolType" TEXT, 
	_version TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, _creator, _references, "servicePack", "toolType", _version)
);

CREATE TABLE "AndroidDevice" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AndroidDeviceFacet" (
	"androidFingerprint" TEXT, 
	"androidVersion" TEXT, 
	"androidID" TEXT, 
	"isADBRootEnabled" BOOLEAN, 
	"isSURootEnabled" BOOLEAN, 
	PRIMARY KEY ("androidFingerprint", "androidVersion", "androidID", "isADBRootEnabled", "isSURootEnabled")
);

CREATE TABLE "AndroidPhone" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Annotation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement, object)
);

CREATE TABLE "AntennaFacet" (
	"antennaHeight" FLOAT, 
	azimuth FLOAT, 
	elevation FLOAT, 
	"horizontalBeamWidth" FLOAT, 
	"signalStrength" FLOAT, 
	skew FLOAT, 
	PRIMARY KEY ("antennaHeight", azimuth, elevation, "horizontalBeamWidth", "signalStrength", skew)
);

CREATE TABLE "API" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AppleDevice" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Appliance" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Application" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ApplicationAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ApplicationAccountFacet" (
	application TEXT, 
	PRIMARY KEY (application)
);

CREATE TABLE "ApplicationFacet" (
	"numberOfLaunches" INTEGER, 
	"applicationIdentifier" TEXT, 
	"installedVersionHistory" TEXT, 
	"operatingSystem" TEXT, 
	version TEXT, 
	PRIMARY KEY ("numberOfLaunches", "applicationIdentifier", "installedVersionHistory", "operatingSystem", version)
);

CREATE TABLE "ApplicationVersion" (
	"installDate" DATETIME, 
	"uninstallDate" DATETIME, 
	version TEXT, 
	PRIMARY KEY ("installDate", "uninstallDate", version)
);

CREATE TABLE "ArchiveFile" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ArchiveFileFacet" (
	"archiveType" TEXT, 
	comment TEXT, 
	version TEXT, 
	PRIMARY KEY ("archiveType", comment, version)
);

CREATE TABLE "ARPCache" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ARPCacheEntry" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ArrayOfAction" (
	action TEXT, 
	PRIMARY KEY (action)
);

CREATE TABLE "ArtifactClassification" (
	"classificationConfidence" FLOAT, 
	class TEXT, 
	PRIMARY KEY ("classificationConfidence", class)
);

CREATE TABLE "ArtifactClassificationResultFacet" (
	classification TEXT, 
	PRIMARY KEY (classification)
);

CREATE TABLE "Assertion" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	statement TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, statement)
);

CREATE TABLE "AttributedName" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"namingAuthority" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "namingAuthority")
);

CREATE TABLE "Audio" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AudioFacet" (
	"bitRate" INTEGER, 
	duration INTEGER, 
	"audioType" TEXT, 
	format TEXT, 
	PRIMARY KEY ("bitRate", duration, "audioType", format)
);

CREATE TABLE "AutonomousSystem" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "AutonomousSystemFacet" (
	number INTEGER, 
	"asHandle" TEXT, 
	"regionalInternetRegistry" TEXT, 
	PRIMARY KEY (number, "asHandle", "regionalInternetRegistry")
);

CREATE TABLE "Bag" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "BenevolentRole" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BirthInformationFacet" (
	birthdate DATETIME, 
	PRIMARY KEY (birthdate)
);

CREATE TABLE "BlackBerryPhone" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BlockDeviceNode" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BluetoothAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BluetoothAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "BotConfiguration" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BrowserBookmark" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BrowserBookmarkFacet" (
	application TEXT, 
	"accessedTime" DATETIME, 
	"modifiedTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	"urlTargeted" TEXT, 
	"visitCount" INTEGER, 
	"bookmarkPath" TEXT, 
	PRIMARY KEY (application, "accessedTime", "modifiedTime", "observableCreatedTime", "urlTargeted", "visitCount", "bookmarkPath")
);

CREATE TABLE "BrowserCookie" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "BrowserCookieFacet" (
	"accessedTime" DATETIME, 
	application TEXT, 
	"cookieDomain" TEXT, 
	"cookieName" TEXT, 
	"cookiePath" TEXT, 
	"expirationTime" DATETIME, 
	"isSecure" BOOLEAN, 
	"observableCreatedTime" DATETIME, 
	PRIMARY KEY ("accessedTime", application, "cookieDomain", "cookieName", "cookiePath", "expirationTime", "isSecure", "observableCreatedTime")
);

CREATE TABLE "BuildFacet" (
	"buildInformation" TEXT, 
	PRIMARY KEY ("buildInformation")
);

CREATE TABLE "BuildInformationType" (
	"buildConfiguration" TEXT, 
	"buildUtility" TEXT, 
	compilers TEXT, 
	libraries TEXT, 
	"compilationDate" DATETIME, 
	"buildID" TEXT, 
	"buildLabel" TEXT, 
	"buildOutputLog" TEXT, 
	"buildProject" TEXT, 
	"buildScript" TEXT, 
	"buildVersion" TEXT, 
	PRIMARY KEY ("buildConfiguration", "buildUtility", compilers, libraries, "compilationDate", "buildID", "buildLabel", "buildOutputLog", "buildProject", "buildScript", "buildVersion")
);

CREATE TABLE "BuildUtilityType" (
	"buildUtilityName" TEXT, 
	_cpeid TEXT, 
	_swid TEXT, 
	PRIMARY KEY ("buildUtilityName", _cpeid, _swid)
);

CREATE TABLE "Bundle" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "Calendar" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CalendarEntry" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CalendarEntryFacet" (
	application TEXT, 
	attendant TEXT, 
	"isPrivate" BOOLEAN, 
	"endTime" DATETIME, 
	location TEXT, 
	"modifiedTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	owner TEXT, 
	"remindTime" DATETIME, 
	"startTime" DATETIME, 
	duration INTEGER, 
	"eventStatus" TEXT, 
	"eventType" TEXT, 
	recurrence TEXT, 
	subject TEXT, 
	PRIMARY KEY (application, attendant, "isPrivate", "endTime", location, "modifiedTime", "observableCreatedTime", owner, "remindTime", "startTime", duration, "eventStatus", "eventType", recurrence, subject)
);

CREATE TABLE "CalendarFacet" (
	owner TEXT, 
	application TEXT, 
	PRIMARY KEY (owner, application)
);

CREATE TABLE "Call" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CallFacet" (
	application TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	duration INTEGER, 
	participant TEXT, 
	"callType" TEXT, 
	"from" TEXT, 
	"to" TEXT, 
	PRIMARY KEY (application, "endTime", "startTime", duration, participant, "callType", "from", "to")
);

CREATE TABLE "CapturedTelecommunicationsInformation" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CapturedTelecommunicationsInformationFacet" (
	"captureCellSite" TEXT NOT NULL, 
	"startTime" DATETIME, 
	"endTime" DATETIME, 
	"interceptedCallState" TEXT, 
	PRIMARY KEY ("captureCellSite", "startTime", "endTime", "interceptedCallState")
);

CREATE TABLE "CellSite" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CellSiteFacet" (
	"cellSiteCountryCode" TEXT, 
	"cellSiteIdentifier" TEXT, 
	"cellSiteLocationAreaCode" TEXT, 
	"cellSiteNetworkCode" TEXT, 
	"cellSiteType" TEXT, 
	PRIMARY KEY ("cellSiteCountryCode", "cellSiteIdentifier", "cellSiteLocationAreaCode", "cellSiteNetworkCode", "cellSiteType")
);

CREATE TABLE "CharacterDeviceNode" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Code" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CoItem" (
	"itemOf" TEXT, 
	PRIMARY KEY ("itemOf")
);

CREATE TABLE "Collection" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "Compilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CompilerType" (
	"compilerInformalDescription" TEXT, 
	_cpeid TEXT, 
	_swid TEXT, 
	PRIMARY KEY ("compilerInformalDescription", _cpeid, _swid)
);

CREATE TABLE "CompressedStreamFacet" (
	"compressionRatio" FLOAT, 
	"compressionMethod" TEXT, 
	PRIMARY KEY ("compressionRatio", "compressionMethod")
);

CREATE TABLE "ComputerSpecification" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ComputerSpecificationFacet" (
	"biosDate" DATETIME, 
	"biosReleaseDate" DATETIME, 
	"currentSystemDate" DATETIME, 
	"localTime" DATETIME, 
	"systemTime" DATETIME, 
	"availableRam" INTEGER, 
	"totalRam" INTEGER, 
	"biosManufacturer" TEXT, 
	"biosSerialNumber" TEXT, 
	"biosVersion" TEXT, 
	cpu TEXT, 
	"cpuFamily" TEXT, 
	gpu TEXT, 
	"gpuFamily" TEXT, 
	hostname TEXT, 
	"networkInterface" TEXT, 
	"processorArchitecture" TEXT, 
	"timezoneDST" TEXT, 
	"timezoneStandard" TEXT, 
	uptime TEXT, 
	PRIMARY KEY ("biosDate", "biosReleaseDate", "currentSystemDate", "localTime", "systemTime", "availableRam", "totalRam", "biosManufacturer", "biosSerialNumber", "biosVersion", cpu, "cpuFamily", gpu, "gpuFamily", hostname, "networkInterface", "processorArchitecture", "timezoneDST", "timezoneStandard", uptime)
);

CREATE TABLE "ConfidenceFacet" (
	confidence INTEGER NOT NULL, 
	PRIMARY KEY (confidence)
);

CREATE TABLE "Configuration" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"configurationEntry" TEXT, 
	dependencies TEXT, 
	"usageContextAssumptions" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "configurationEntry", dependencies, "usageContextAssumptions")
);

CREATE TABLE "ConfigurationEntry" (
	"itemObject" TEXT, 
	"itemDescription" TEXT, 
	"itemName" TEXT, 
	"itemType" TEXT, 
	"itemValue" TEXT, 
	PRIMARY KEY ("itemObject", "itemDescription", "itemName", "itemType", "itemValue")
);

CREATE TABLE "ConfiguredSoftware" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"usesConfiguration" TEXT, 
	"isConfigurationOf" TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "usesConfiguration", "isConfigurationOf")
);

CREATE TABLE "ConfiguredTool" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	_creator TEXT, 
	_references TEXT, 
	"servicePack" TEXT, 
	"toolType" TEXT, 
	_version TEXT, 
	"usesConfiguration" TEXT, 
	"isConfigurationOf" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, _creator, _references, "servicePack", "toolType", _version, "usesConfiguration", "isConfigurationOf")
);

CREATE TABLE "Contact" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ContactAddress" (
	"geoLocationAddress" TEXT, 
	"contactAddressScope" TEXT, 
	PRIMARY KEY ("geoLocationAddress", "contactAddressScope")
);

CREATE TABLE "ContactAffiliation" (
	"contactOrganization" TEXT, 
	"organizationLocation" TEXT, 
	"contactEmail" TEXT, 
	"contactMessaging" TEXT, 
	"contactPhone" TEXT, 
	"contactProfile" TEXT, 
	"contactURL" TEXT, 
	"organizationDepartment" TEXT, 
	"organizationPosition" TEXT, 
	PRIMARY KEY ("contactOrganization", "organizationLocation", "contactEmail", "contactMessaging", "contactPhone", "contactProfile", "contactURL", "organizationDepartment", "organizationPosition")
);

CREATE TABLE "ContactEmail" (
	"emailAddress" TEXT, 
	"contactEmailScope" VARCHAR(6), 
	PRIMARY KEY ("emailAddress", "contactEmailScope")
);

CREATE TABLE "ContactFacet" (
	"contactAddress" TEXT, 
	"contactAffiliation" TEXT, 
	"contactEmail" TEXT, 
	"contactMessaging" TEXT, 
	"contactPhone" TEXT, 
	"contactProfile" TEXT, 
	"contactSIP" TEXT, 
	"contactURL" TEXT, 
	"sourceApplication" TEXT, 
	birthdate DATETIME, 
	"lastTimeContacted" DATETIME, 
	"numberTimesContacted" INTEGER, 
	"contactID" TEXT, 
	"displayName" TEXT, 
	"firstName" TEXT, 
	"lastName" TEXT, 
	"middleName" TEXT, 
	"namePhonetic" TEXT, 
	"namePrefix" TEXT, 
	"nameSuffix" TEXT, 
	"contactGroup" TEXT, 
	"contactNote" TEXT, 
	nickname TEXT, 
	PRIMARY KEY ("contactAddress", "contactAffiliation", "contactEmail", "contactMessaging", "contactPhone", "contactProfile", "contactSIP", "contactURL", "sourceApplication", birthdate, "lastTimeContacted", "numberTimesContacted", "contactID", "displayName", "firstName", "lastName", "middleName", "namePhonetic", "namePrefix", "nameSuffix", "contactGroup", "contactNote", nickname)
);

CREATE TABLE "ContactList" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ContactListFacet" (
	"sourceApplication" TEXT, 
	contact TEXT, 
	PRIMARY KEY ("sourceApplication", contact)
);

CREATE TABLE "ContactMessaging" (
	"contactMessagingPlatform" TEXT, 
	"messagingAddress" TEXT, 
	PRIMARY KEY ("contactMessagingPlatform", "messagingAddress")
);

CREATE TABLE "ContactPhone" (
	"contactPhoneNumber" TEXT, 
	"contactPhoneScope" TEXT, 
	PRIMARY KEY ("contactPhoneNumber", "contactPhoneScope")
);

CREATE TABLE "ContactProfile" (
	"contactProfilePlatform" TEXT, 
	profile TEXT, 
	PRIMARY KEY ("contactProfilePlatform", profile)
);

CREATE TABLE "ContactSIP" (
	"sipAddress" TEXT, 
	"contactSIPScope" TEXT, 
	PRIMARY KEY ("sipAddress", "contactSIPScope")
);

CREATE TABLE "ContactURL" (
	"contactURLScope" TEXT, 
	url TEXT, 
	PRIMARY KEY ("contactURLScope", url)
);

CREATE TABLE "ContentData" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ContentDataFacet" (
	"dataPayloadReferenceURL" TEXT, 
	hash TEXT, 
	"isEncrypted" BOOLEAN, 
	entropy FLOAT, 
	"sizeInBytes" INTEGER, 
	"dataPayload" TEXT, 
	"magicNumber" TEXT, 
	"mimeClass" TEXT, 
	"mimeType" TEXT, 
	"byteOrder" TEXT, 
	PRIMARY KEY ("dataPayloadReferenceURL", hash, "isEncrypted", entropy, "sizeInBytes", "dataPayload", "magicNumber", "mimeClass", "mimeType", "byteOrder")
);

CREATE TABLE "ContextualCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "ControlledDictionary" (
	entry TEXT, 
	PRIMARY KEY (entry)
);

CREATE TABLE "ControlledDictionaryEntry" (
	"key" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("key", value)
);

CREATE TABLE "ControlledVocabulary" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"constrainingVocabularyReference" TEXT, 
	"constrainingVocabularyName" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "constrainingVocabularyReference", "constrainingVocabularyName", value)
);

CREATE TABLE "CookieHistory" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Credential" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "CredentialDump" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DataRangeFacet" (
	"rangeOffset" INTEGER, 
	"rangeSize" INTEGER, 
	"rangeOffsetType" TEXT, 
	PRIMARY KEY ("rangeOffset", "rangeSize", "rangeOffsetType")
);

CREATE TABLE "DefensiveTool" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	_creator TEXT, 
	_references TEXT, 
	"servicePack" TEXT, 
	"toolType" TEXT, 
	_version TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, _creator, _references, "servicePack", "toolType", _version)
);

CREATE TABLE "Dependency" (
	"dependencyDescription" TEXT, 
	"dependencyType" TEXT, 
	PRIMARY KEY ("dependencyDescription", "dependencyType")
);

CREATE TABLE "Device" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DeviceFacet" (
	manufacturer TEXT, 
	"deviceType" TEXT, 
	model TEXT, 
	"serialNumber" TEXT, 
	PRIMARY KEY (manufacturer, "deviceType", model, "serialNumber")
);

CREATE TABLE "Dictionary" (
	entry TEXT NOT NULL, 
	PRIMARY KEY (entry)
);

CREATE TABLE "DictionaryEntry" (
	"key" TEXT NOT NULL, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("key", value)
);

CREATE TABLE "DigitalAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DigitalAccountFacet" (
	"isDisabled" BOOLEAN, 
	"firstLoginTime" DATETIME, 
	"lastLoginTime" DATETIME, 
	"displayName" TEXT, 
	"accountLogin" TEXT, 
	PRIMARY KEY ("isDisabled", "firstLoginTime", "lastLoginTime", "displayName", "accountLogin")
);

CREATE TABLE "DigitalAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DigitalAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "DigitalCamera" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DigitalSignatureInfo" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DigitalSignatureInfoFacet" (
	"certificateSubject" TEXT, 
	"certificateIssuer" TEXT, 
	"signatureExists" BOOLEAN, 
	"signatureVerified" BOOLEAN, 
	"signatureDescription" TEXT, 
	PRIMARY KEY ("certificateSubject", "certificateIssuer", "signatureExists", "signatureVerified", "signatureDescription")
);

CREATE TABLE "Directory" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Disk" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DiskFacet" (
	partition TEXT, 
	"diskSize" INTEGER, 
	"freeSpace" INTEGER, 
	"diskType" TEXT, 
	PRIMARY KEY (partition, "diskSize", "freeSpace", "diskType")
);

CREATE TABLE "DiskPartition" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DiskPartitionFacet" (
	"observableCreatedTime" DATETIME, 
	"partitionLength" INTEGER, 
	"partitionOffset" INTEGER, 
	"spaceLeft" INTEGER, 
	"spaceUsed" INTEGER, 
	"totalSpace" INTEGER, 
	"diskPartitionType" TEXT, 
	"mountPoint" TEXT, 
	"partitionID" TEXT, 
	PRIMARY KEY ("observableCreatedTime", "partitionLength", "partitionOffset", "spaceLeft", "spaceUsed", "totalSpace", "diskPartitionType", "mountPoint", "partitionID")
);

CREATE TABLE "DNSCache" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DNSRecord" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DomainName" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "DomainNameFacet" (
	"isTLD" BOOLEAN, 
	value TEXT, 
	PRIMARY KEY ("isTLD", value)
);

CREATE TABLE "Drone" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EmailAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EmailAccountFacet" (
	"emailAddress" TEXT, 
	PRIMARY KEY ("emailAddress")
);

CREATE TABLE "EmailAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EmailAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "EmailMessage" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EmailMessageFacet" (
	"bodyMultipart" TEXT, 
	application TEXT, 
	"bodyRaw" TEXT, 
	"from" TEXT, 
	"headerRaw" TEXT, 
	sender TEXT, 
	"xOriginatingIP" TEXT, 
	bcc TEXT, 
	cc TEXT, 
	"references" TEXT, 
	"to" TEXT, 
	"otherHeaders" TEXT, 
	"isMimeEncoded" BOOLEAN, 
	"isMultipart" BOOLEAN, 
	"isRead" BOOLEAN, 
	"modifiedTime" DATETIME, 
	"receivedTime" DATETIME, 
	"sentTime" DATETIME, 
	body TEXT, 
	"contentDisposition" TEXT, 
	"contentType" TEXT, 
	"inReplyTo" TEXT, 
	"messageID" TEXT, 
	priority TEXT, 
	subject TEXT, 
	"xMailer" TEXT, 
	categories TEXT, 
	labels TEXT, 
	"receivedLines" TEXT, 
	PRIMARY KEY ("bodyMultipart", application, "bodyRaw", "from", "headerRaw", sender, "xOriginatingIP", bcc, cc, "references", "to", "otherHeaders", "isMimeEncoded", "isMultipart", "isRead", "modifiedTime", "receivedTime", "sentTime", body, "contentDisposition", "contentType", "inReplyTo", "messageID", priority, subject, "xMailer", categories, labels, "receivedLines")
);

CREATE TABLE "EmbeddedDevice" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EnclosingCompilation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object)
);

CREATE TABLE "EncodedStreamFacet" (
	"encodingMethod" TEXT, 
	PRIMARY KEY ("encodingMethod")
);

CREATE TABLE "EncryptedStreamFacet" (
	"encryptionMethod" TEXT, 
	"encryptionMode" TEXT, 
	"encryptionIV" TEXT, 
	"encryptionKey" TEXT, 
	PRIMARY KEY ("encryptionMethod", "encryptionMode", "encryptionIV", "encryptionKey")
);

CREATE TABLE "EnvironmentVariable" (
	name TEXT, 
	value TEXT, 
	PRIMARY KEY (name, value)
);

CREATE TABLE "EventLog" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EventRecord" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "EventRecordFacet" (
	"cyberAction" TEXT, 
	account TEXT, 
	application TEXT, 
	"eventRecordDevice" TEXT, 
	"observableCreatedTime" DATETIME, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"eventID" TEXT, 
	"eventRecordID" TEXT, 
	"eventRecordRaw" TEXT, 
	"eventRecordServiceName" TEXT, 
	"eventRecordText" TEXT, 
	"eventType" TEXT, 
	PRIMARY KEY ("cyberAction", account, application, "eventRecordDevice", "observableCreatedTime", "endTime", "startTime", "eventID", "eventRecordID", "eventRecordRaw", "eventRecordServiceName", "eventRecordText", "eventType")
);

CREATE TABLE "EXIFFacet" (
	"exifData" TEXT, 
	PRIMARY KEY ("exifData")
);

CREATE TABLE "ExternalReference" (
	"referenceURL" TEXT, 
	"definingContext" TEXT, 
	"externalIdentifier" TEXT, 
	PRIMARY KEY ("referenceURL", "definingContext", "externalIdentifier")
);

CREATE TABLE "ExtInodeFacet" (
	"extDeletionTime" DATETIME, 
	"extInodeChangeTime" DATETIME, 
	"extFileType" INTEGER, 
	"extFlags" INTEGER, 
	"extHardLinkCount" INTEGER, 
	"extInodeID" INTEGER, 
	"extPermissions" INTEGER, 
	"extSGID" INTEGER, 
	"extSUID" INTEGER, 
	PRIMARY KEY ("extDeletionTime", "extInodeChangeTime", "extFileType", "extFlags", "extHardLinkCount", "extInodeID", "extPermissions", "extSGID", "extSUID")
);

CREATE TABLE "ExtractedString" (
	length INTEGER, 
	"byteStringValue" TEXT, 
	encoding TEXT, 
	"englishTranslation" TEXT, 
	language TEXT, 
	"stringValue" TEXT, 
	PRIMARY KEY (length, "byteStringValue", encoding, "englishTranslation", language, "stringValue")
);

CREATE TABLE "ExtractedStringsFacet" (
	strings TEXT, 
	PRIMARY KEY (strings)
);

CREATE TABLE "File" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "FileFacet" (
	"isDirectory" BOOLEAN, 
	"accessedTime" DATETIME, 
	"metadataChangeTime" DATETIME, 
	"modifiedTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	"sizeInBytes" INTEGER, 
	"allocationStatus" TEXT, 
	extension TEXT, 
	"fileName" TEXT, 
	"filePath" TEXT, 
	PRIMARY KEY ("isDirectory", "accessedTime", "metadataChangeTime", "modifiedTime", "observableCreatedTime", "sizeInBytes", "allocationStatus", extension, "fileName", "filePath")
);

CREATE TABLE "FilePermissionsFacet" (
	owner TEXT, 
	PRIMARY KEY (owner)
);

CREATE TABLE "FileSystem" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "FileSystemFacet" (
	"clusterSize" INTEGER, 
	"fileSystemType" TEXT, 
	PRIMARY KEY ("clusterSize", "fileSystemType")
);

CREATE TABLE "FileSystemObject" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ForumPost" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ForumPrivateMessage" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "FragmentFacet" (
	"fragmentIndex" INTEGER, 
	"totalFragments" INTEGER, 
	PRIMARY KEY ("fragmentIndex", "totalFragments")
);

CREATE TABLE "GamingConsole" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "GenericObservableObject" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "GeoLocationEntry" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "GeoLocationEntryFacet" (
	location TEXT, 
	application TEXT, 
	"observableCreatedTime" DATETIME, 
	PRIMARY KEY (location, application, "observableCreatedTime")
);

CREATE TABLE "GeoLocationLog" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "GeoLocationLogFacet" (
	application TEXT, 
	"observableCreatedTime" DATETIME, 
	PRIMARY KEY (application, "observableCreatedTime")
);

CREATE TABLE "GeoLocationTrack" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "GeoLocationTrackFacet" (
	application TEXT, 
	"geoLocationEntry" TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	PRIMARY KEY (application, "geoLocationEntry", "endTime", "startTime")
);

CREATE TABLE "GlobalFlagType" (
	"hexadecimalValue" TEXT, 
	abbreviation TEXT, 
	destination TEXT, 
	"symbolicName" TEXT, 
	PRIMARY KEY ("hexadecimalValue", abbreviation, destination, "symbolicName")
);

CREATE TABLE "GPSCoordinatesFacet" (
	hdop FLOAT, 
	pdop FLOAT, 
	tdop FLOAT, 
	vdop FLOAT, 
	PRIMARY KEY (hdop, pdop, tdop, vdop)
);

CREATE TABLE "GranularMarking" (
	marking TEXT, 
	"contentSelectors" TEXT, 
	PRIMARY KEY (marking, "contentSelectors")
);

CREATE TABLE "Grouping" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	object TEXT NOT NULL, 
	context TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, object, context)
);

CREATE TABLE "GUI" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Hash" (
	"hashValue" TEXT NOT NULL, 
	"hashMethod" TEXT NOT NULL, 
	PRIMARY KEY ("hashValue", "hashMethod")
);

CREATE TABLE "Hostname" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "HTTPConnection" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "HTTPConnectionFacet" (
	"httpMessageBodyData" TEXT, 
	"httpMessageBodyLength" INTEGER, 
	"httpRequestHeader" TEXT, 
	"requestMethod" TEXT, 
	"requestValue" TEXT, 
	"requestVersion" TEXT, 
	PRIMARY KEY ("httpMessageBodyData", "httpMessageBodyLength", "httpRequestHeader", "requestMethod", "requestValue", "requestVersion")
);

CREATE TABLE "ICMPConnection" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ICMPConnectionFacet" (
	"icmpCode" TEXT, 
	"icmpType" TEXT, 
	PRIMARY KEY ("icmpCode", "icmpType")
);

CREATE TABLE "IComHandlerActionType" (
	"comClassID" TEXT, 
	"comData" TEXT, 
	PRIMARY KEY ("comClassID", "comData")
);

CREATE TABLE "Identity" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IdentityAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IExecActionType" (
	"execProgramHashes" TEXT, 
	"execArguments" TEXT, 
	"execProgramPath" TEXT, 
	"execWorkingDirectory" TEXT, 
	PRIMARY KEY ("execProgramHashes", "execArguments", "execProgramPath", "execWorkingDirectory")
);

CREATE TABLE "Image" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ImageFacet" (
	"imageType" TEXT, 
	PRIMARY KEY ("imageType")
);

CREATE TABLE "InstantMessagingAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "InstantMessagingAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "IPAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IPAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "IPhone" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IPNetmask" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IPv4Address" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IPv4AddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "IPv6Address" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "IPv6AddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "IShowMessageActionType" (
	"showMessageBody" TEXT, 
	"showMessageTitle" TEXT, 
	PRIMARY KEY ("showMessageBody", "showMessageTitle")
);

CREATE TABLE "Item" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Junction" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Laptop" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "LatLongCoordinatesFacet" (
	altitude FLOAT, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (altitude, latitude, longitude)
);

CREATE TABLE "Library" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "LibraryFacet" (
	"libraryType" TEXT, 
	PRIMARY KEY ("libraryType")
);

CREATE TABLE "LibraryType" (
	"libraryName" TEXT, 
	"libraryVersion" TEXT, 
	PRIMARY KEY ("libraryName", "libraryVersion")
);

CREATE TABLE "LicenseMarking" (
	"definitionType" TEXT, 
	license TEXT NOT NULL, 
	PRIMARY KEY ("definitionType", license)
);

CREATE TABLE "List" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	"lastItem" TEXT, 
	"firstItem" TEXT, 
	PRIMARY KEY (element, size, item, "lastItem", "firstItem")
);

CREATE TABLE "ListItem" (
	"itemOf" TEXT, 
	_index INTEGER NOT NULL, 
	PRIMARY KEY ("itemOf", _index)
);

CREATE TABLE "Location" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "LogicalPattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"patternExpression" TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "patternExpression")
);

CREATE TABLE "MACAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MACAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "MaliciousRole" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MaliciousTool" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	_creator TEXT, 
	_references TEXT, 
	"servicePack" TEXT, 
	"toolType" TEXT, 
	_version TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, _creator, _references, "servicePack", "toolType", _version)
);

CREATE TABLE "MarkingDefinition" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	definition TEXT, 
	"definitionType" TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, definition, "definitionType")
);

CREATE TABLE "MarkingDefinitionAbstraction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Memory" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MemoryFacet" (
	"isInjected" BOOLEAN, 
	"isMapped" BOOLEAN, 
	"isProtected" BOOLEAN, 
	"isVolatile" BOOLEAN, 
	"regionEndAddress" TEXT, 
	"regionStartAddress" TEXT, 
	"regionSize" INTEGER, 
	"blockType" VARCHAR(13), 
	PRIMARY KEY ("isInjected", "isMapped", "isProtected", "isVolatile", "regionEndAddress", "regionStartAddress", "regionSize", "blockType")
);

CREATE TABLE "Message" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MessageFacet" (
	application TEXT, 
	"from" TEXT, 
	"to" TEXT, 
	"sentTime" DATETIME, 
	"messageID" TEXT, 
	"messageText" TEXT, 
	"messageType" TEXT, 
	"sessionID" TEXT, 
	PRIMARY KEY (application, "from", "to", "sentTime", "messageID", "messageText", "messageType", "sessionID")
);

CREATE TABLE "MessageThreadFacet" (
	"messageThreadOrderedItems" TEXT, 
	"messageThreadOriginItems" TEXT, 
	"messageThreadTerminalItems" TEXT, 
	"messageThreadUnorderedItems" TEXT, 
	participant TEXT, 
	"messageThread" TEXT, 
	visibility BOOLEAN, 
	PRIMARY KEY ("messageThreadOrderedItems", "messageThreadOriginItems", "messageThreadTerminalItems", "messageThreadUnorderedItems", participant, "messageThread", visibility)
);

CREATE TABLE "MftRecordFacet" (
	"mftFileNameAccessedTime" DATETIME, 
	"mftFileNameCreatedTime" DATETIME, 
	"mftFileNameModifiedTime" DATETIME, 
	"mftFileNameRecordChangeTme" DATETIME, 
	"mftRecordChangeTime" DATETIME, 
	"mftFileID" INTEGER, 
	"mftFileNameLength" INTEGER, 
	"mftFlags" INTEGER, 
	"mftParentID" INTEGER, 
	"ntfsHardLinkCount" INTEGER, 
	"ntfsOwnerID" TEXT, 
	"ntfsOwnerSID" TEXT, 
	PRIMARY KEY ("mftFileNameAccessedTime", "mftFileNameCreatedTime", "mftFileNameModifiedTime", "mftFileNameRecordChangeTme", "mftRecordChangeTime", "mftFileID", "mftFileNameLength", "mftFlags", "mftParentID", "ntfsHardLinkCount", "ntfsOwnerID", "ntfsOwnerSID")
);

CREATE TABLE "MimePartType" (
	"bodyRaw" TEXT, 
	body TEXT, 
	"contentDisposition" TEXT, 
	"contentType" TEXT, 
	PRIMARY KEY ("bodyRaw", body, "contentDisposition", "contentType")
);

CREATE TABLE "MobileAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MobileAccountFacet" (
	"IMSI" TEXT, 
	"MSISDN" TEXT, 
	"MSISDNType" TEXT, 
	PRIMARY KEY ("IMSI", "MSISDN", "MSISDNType")
);

CREATE TABLE "MobileDevice" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MobileDeviceFacet" (
	"mockLocationsAllowed" BOOLEAN, 
	"clockSetting" DATETIME, 
	"phoneActivationTime" DATETIME, 
	"storageCapacityInBytes" INTEGER, 
	"ESN" TEXT, 
	"IMEI" TEXT, 
	"bluetoothDeviceName" TEXT, 
	"keypadUnlockCode" TEXT, 
	network TEXT, 
	PRIMARY KEY ("mockLocationsAllowed", "clockSetting", "phoneActivationTime", "storageCapacityInBytes", "ESN", "IMEI", "bluetoothDeviceName", "keypadUnlockCode", network)
);

CREATE TABLE "ModusOperandi" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Mutex" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "MutexFacet" (
	"isNamed" BOOLEAN, 
	"mutexName" TEXT, 
	PRIMARY KEY ("isNamed", "mutexName")
);

CREATE TABLE "NamedPipe" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkAppliance" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkConnection" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkConnectionFacet" (
	src TEXT, 
	dst TEXT, 
	protocols TEXT, 
	"isActive" BOOLEAN, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"destinationPort" INTEGER, 
	"sourcePort" INTEGER, 
	PRIMARY KEY (src, dst, protocols, "isActive", "endTime", "startTime", "destinationPort", "sourcePort")
);

CREATE TABLE "NetworkFlow" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkFlowFacet" (
	"dstPayload" TEXT, 
	"srcPayload" TEXT, 
	ipfix TEXT, 
	"dstBytes" INTEGER, 
	"dstPackets" INTEGER, 
	"srcBytes" INTEGER, 
	"srcPackets" INTEGER, 
	PRIMARY KEY ("dstPayload", "srcPayload", ipfix, "dstBytes", "dstPackets", "srcBytes", "srcPackets")
);

CREATE TABLE "NetworkInterface" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkInterfaceFacet" (
	"macAddress" TEXT, 
	"dhcpServer" TEXT, 
	ip TEXT, 
	"ipGateway" TEXT, 
	"dhcpLeaseExpires" DATETIME, 
	"dhcpLeaseObtained" DATETIME, 
	"adapterName" TEXT, 
	PRIMARY KEY ("macAddress", "dhcpServer", ip, "ipGateway", "dhcpLeaseExpires", "dhcpLeaseObtained", "adapterName")
);

CREATE TABLE "NetworkProtocol" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkRoute" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NetworkSubnet" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NeutralRole" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Note" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NoteFacet" (
	application TEXT, 
	"modifiedTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	text TEXT, 
	PRIMARY KEY (application, "modifiedTime", "observableCreatedTime", text)
);

CREATE TABLE "NTFSFile" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "NTFSFileFacet" (
	"alternateDataStreams" TEXT, 
	"entryID" INTEGER, 
	sid TEXT, 
	PRIMARY KEY ("alternateDataStreams", "entryID", sid)
);

CREATE TABLE "ObservableAction" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus")
);

CREATE TABLE "ObservableObject" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ObservablePattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ObservableRelationship" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"endTime" DATETIME, 
	"isDirectional" BOOLEAN NOT NULL, 
	"kindOfRelationship" TEXT, 
	source TEXT NOT NULL, 
	"startTime" DATETIME, 
	target TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "endTime", "isDirectional", "kindOfRelationship", source, "startTime", target)
);

CREATE TABLE "Observation" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	subaction TEXT, 
	environment TEXT, 
	performer TEXT, 
	error TEXT, 
	instrument TEXT, 
	object TEXT, 
	participant TEXT, 
	result TEXT, 
	location TEXT, 
	"endTime" DATETIME, 
	"startTime" DATETIME, 
	"actionCount" INTEGER, 
	"actionStatus" VARCHAR(15), 
	name TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", "objectMarking", "objectCreatedTime", "specVersion", tag, subaction, environment, performer, error, instrument, object, participant, result, location, "endTime", "startTime", "actionCount", "actionStatus", name)
);

CREATE TABLE "OnlineService" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "OnlineServiceFacet" (
	location TEXT, 
	"inetLocation" TEXT, 
	name TEXT, 
	PRIMARY KEY (location, "inetLocation", name)
);

CREATE TABLE "OperatingSystem" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "OperatingSystemFacet" (
	manufacturer TEXT, 
	"environmentVariables" TEXT, 
	"isLimitAdTrackingEnabled" BOOLEAN, 
	"installDate" DATETIME, 
	bitness TEXT, 
	version TEXT, 
	"advertisingID" TEXT, 
	PRIMARY KEY (manufacturer, "environmentVariables", "isLimitAdTrackingEnabled", "installDate", bitness, version, "advertisingID")
);

CREATE TABLE "Organization" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "PathRelationFacet" (
	path TEXT, 
	PRIMARY KEY (path)
);

CREATE TABLE "Pattern" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "PaymentCard" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "PDFFile" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "PDFFileFacet" (
	"documentInformationDictionary" TEXT, 
	"isOptimized" BOOLEAN, 
	"pdfCreationDate" DATETIME, 
	"pdfModDate" DATETIME, 
	"pdfId1" TEXT, 
	version TEXT, 
	"pdfId0" TEXT, 
	PRIMARY KEY ("documentInformationDictionary", "isOptimized", "pdfCreationDate", "pdfModDate", "pdfId1", version, "pdfId0")
);

CREATE TABLE "Person" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "PhoneAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "PhoneAccountFacet" (
	"phoneNumber" TEXT, 
	PRIMARY KEY ("phoneNumber")
);

CREATE TABLE "Pipe" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Post" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Process" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ProcessFacet" (
	binary TEXT, 
	"creatorUser" TEXT, 
	parent TEXT, 
	"environmentVariables" TEXT, 
	"isHidden" BOOLEAN, 
	"exitTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	"exitStatus" INTEGER, 
	pid INTEGER, 
	"currentWorkingDirectory" TEXT, 
	status TEXT, 
	arguments TEXT, 
	PRIMARY KEY (binary, "creatorUser", parent, "environmentVariables", "isHidden", "exitTime", "observableCreatedTime", "exitStatus", pid, "currentWorkingDirectory", status, arguments)
);

CREATE TABLE "ProcessThread" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Profile" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "ProfileFacet" (
	"profileIdentity" TEXT, 
	"contactAddress" TEXT, 
	"contactEmail" TEXT, 
	"contactMessaging" TEXT, 
	"contactPhone" TEXT, 
	"contactURL" TEXT, 
	"profileAccount" TEXT, 
	"profileService" TEXT, 
	"profileWebsite" TEXT, 
	"profileCreated" DATETIME, 
	name TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("profileIdentity", "contactAddress", "contactEmail", "contactMessaging", "contactPhone", "contactURL", "profileAccount", "profileService", "profileWebsite", "profileCreated", name, "displayName")
);

CREATE TABLE "PropertiesEnumeratedEffectFacet" (
	properties TEXT, 
	PRIMARY KEY (properties)
);

CREATE TABLE "PropertyReadEffectFacet" (
	"propertyName" TEXT, 
	value TEXT, 
	PRIMARY KEY ("propertyName", value)
);

CREATE TABLE "ProtocolConverter" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "RasterPicture" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "RasterPictureFacet" (
	camera TEXT, 
	"bitsPerPixel" INTEGER, 
	"pictureHeight" INTEGER, 
	"pictureWidth" INTEGER, 
	"imageCompressionMethod" TEXT, 
	"pictureType" TEXT, 
	PRIMARY KEY (camera, "bitsPerPixel", "pictureHeight", "pictureWidth", "imageCompressionMethod", "pictureType")
);

CREATE TABLE "RecoveredObject" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "RecoveredObjectFacet" (
	"contentRecoveredStatus" VARCHAR(19), 
	"metadataRecoveredStatus" VARCHAR(19), 
	"nameRecoveredStatus" VARCHAR(19), 
	PRIMARY KEY ("contentRecoveredStatus", "metadataRecoveredStatus", "nameRecoveredStatus")
);

CREATE TABLE "Relationship" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	"endTime" DATETIME, 
	"isDirectional" BOOLEAN NOT NULL, 
	"kindOfRelationship" TEXT, 
	source TEXT NOT NULL, 
	"startTime" DATETIME, 
	target TEXT NOT NULL, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, "endTime", "isDirectional", "kindOfRelationship", source, "startTime", target)
);

CREATE TABLE "ReleaseToMarking" (
	"authorizedIdentities" TEXT NOT NULL, 
	"definitionType" TEXT, 
	PRIMARY KEY ("authorizedIdentities", "definitionType")
);

CREATE TABLE "ReparsePoint" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Role" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SecurityAppliance" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Semaphore" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SendControlCodeEffectFacet" (
	"controlCode" TEXT, 
	PRIMARY KEY ("controlCode")
);

CREATE TABLE "Server" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Set" (
	element TEXT, 
	size INTEGER, 
	PRIMARY KEY (element, size)
);

CREATE TABLE "ShopListing" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SIMCard" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SIMCardFacet" (
	carrier TEXT, 
	"storageCapacityInBytes" INTEGER, 
	"ICCID" TEXT, 
	"IMSI" TEXT, 
	"PIN" TEXT, 
	"PUK" TEXT, 
	"SIMForm" TEXT, 
	"SIMType" TEXT, 
	PRIMARY KEY (carrier, "storageCapacityInBytes", "ICCID", "IMSI", "PIN", "PUK", "SIMForm", "SIMType")
);

CREATE TABLE "SimpleAddressFacet" (
	"addressType" TEXT, 
	country TEXT, 
	locality TEXT, 
	"postalCode" TEXT, 
	region TEXT, 
	street TEXT, 
	PRIMARY KEY ("addressType", country, locality, "postalCode", region, street)
);

CREATE TABLE "SimpleNameFacet" (
	"familyName" TEXT, 
	"givenName" TEXT, 
	"honorificPrefix" TEXT, 
	"honorificSuffix" TEXT, 
	PRIMARY KEY ("familyName", "givenName", "honorificPrefix", "honorificSuffix")
);

CREATE TABLE "SIPAaddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SIPAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "SmartPhone" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SMSMessage" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SMSMessageFacet" (
	"isRead" BOOLEAN, 
	PRIMARY KEY ("isRead")
);

CREATE TABLE "Snapshot" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Socket" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SocketAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Software" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SoftwareFacet" (
	manufacturer TEXT, 
	cpeid TEXT, 
	language TEXT, 
	swid TEXT, 
	version TEXT, 
	PRIMARY KEY (manufacturer, cpeid, language, swid, version)
);

CREATE TABLE "SQLiteBlob" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SQLiteBlobFacet" (
	"rowIndex" INTEGER, 
	"columnName" TEXT, 
	"rowCondition" TEXT, 
	"tableName" TEXT, 
	PRIMARY KEY ("rowIndex", "columnName", "rowCondition", "tableName")
);

CREATE TABLE "StateChangeEffectFacet" (
	"newObject" TEXT, 
	"oldObject" TEXT, 
	PRIMARY KEY ("newObject", "oldObject")
);

CREATE TABLE "StatementMarking" (
	"definitionType" TEXT, 
	statement TEXT NOT NULL, 
	PRIMARY KEY ("definitionType", statement)
);

CREATE TABLE "StorageMedium" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SymbolicLink" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "SymbolicLinkFacet" (
	"targetFile" TEXT, 
	PRIMARY KEY ("targetFile")
);

CREATE TABLE "TableField" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "TableFieldFacet" (
	"recordFieldIsNull" BOOLEAN, 
	"recordFieldName" TEXT, 
	"tableName" TEXT, 
	"tableSchema" TEXT, 
	"recordFieldValue" TEXT, 
	"recordRowID" TEXT, 
	PRIMARY KEY ("recordFieldIsNull", "recordFieldName", "tableName", "tableSchema", "recordFieldValue", "recordRowID")
);

CREATE TABLE "Tablet" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "TaskActionType" (
	"iComHandlerAction" TEXT, 
	"iExecAction" TEXT, 
	"iShowMessageAction" TEXT, 
	"iEmailAction" TEXT, 
	"actionID" TEXT, 
	"actionType" VARCHAR(24), 
	PRIMARY KEY ("iComHandlerAction", "iExecAction", "iShowMessageAction", "iEmailAction", "actionID", "actionType")
);

CREATE TABLE "TCPConnection" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "TCPConnectionFacet" (
	"sourceFlags" TEXT, 
	"destinationFlags" TEXT, 
	PRIMARY KEY ("sourceFlags", "destinationFlags")
);

CREATE TABLE "TermsOfUseMarking" (
	"definitionType" TEXT, 
	"termsOfUse" TEXT NOT NULL, 
	PRIMARY KEY ("definitionType", "termsOfUse")
);

CREATE TABLE "Thread" (
	element TEXT, 
	size INTEGER, 
	item TEXT, 
	PRIMARY KEY (element, size, item)
);

CREATE TABLE "ThreadItem" (
	"itemContent" TEXT, 
	PRIMARY KEY ("itemContent")
);

CREATE TABLE "Tool" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	_creator TEXT, 
	_references TEXT, 
	"servicePack" TEXT, 
	"toolType" TEXT, 
	_version TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag, _creator, _references, "servicePack", "toolType", _version)
);

CREATE TABLE "TriggerType" (
	"isEnabled" BOOLEAN, 
	"triggerBeginTime" DATETIME, 
	"triggerEndTime" DATETIME, 
	"triggerDelay" TEXT, 
	"triggerMaxRunTime" TEXT, 
	"triggerSessionChangeType" TEXT, 
	"triggerFrequency" VARCHAR(33), 
	"triggerType" VARCHAR(33), 
	PRIMARY KEY ("isEnabled", "triggerBeginTime", "triggerEndTime", "triggerDelay", "triggerMaxRunTime", "triggerSessionChangeType", "triggerFrequency", "triggerType")
);

CREATE TABLE "Tweet" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "TwitterProfileFacet" (
	"profileBackgroundLocation" TEXT, 
	"profileBannerLocation" TEXT, 
	"profileImageLocation" TEXT, 
	"profileBackgroundHash" TEXT, 
	"profileBannerHash" TEXT, 
	"profileImageHash" TEXT, 
	"profileIsProtected" BOOLEAN, 
	"profileIsVerified" BOOLEAN, 
	"listedCount" INTEGER, 
	"favoritesCount" INTEGER, 
	"followersCount" INTEGER, 
	"friendsCount" INTEGER, 
	"statusesCount" INTEGER, 
	"twitterHandle" TEXT, 
	"twitterId" TEXT, 
	"userLocationString" TEXT, 
	PRIMARY KEY ("profileBackgroundLocation", "profileBannerLocation", "profileImageLocation", "profileBackgroundHash", "profileBannerHash", "profileImageHash", "profileIsProtected", "profileIsVerified", "listedCount", "favoritesCount", "followersCount", "friendsCount", "statusesCount", "twitterHandle", "twitterId", "userLocationString")
);

CREATE TABLE "UcoObject" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "UNIXAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "UNIXAccountFacet" (
	gid INTEGER, 
	shell TEXT, 
	PRIMARY KEY (gid, shell)
);

CREATE TABLE "UNIXFile" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "UNIXProcess" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "UNIXProcessFacet" (
	"openFileDescriptor" INTEGER, 
	ruid INTEGER, 
	PRIMARY KEY ("openFileDescriptor", ruid)
);

CREATE TABLE "UNIXVolumeFacet" (
	"mountPoint" TEXT, 
	options TEXT, 
	PRIMARY KEY ("mountPoint", options)
);

CREATE TABLE "URL" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "URLFacet" (
	host TEXT, 
	port INTEGER, 
	fragment TEXT, 
	"fullValue" TEXT, 
	password TEXT, 
	path TEXT, 
	"query" TEXT, 
	scheme TEXT, 
	"userName" TEXT, 
	PRIMARY KEY (host, port, fragment, "fullValue", password, path, "query", scheme, "userName")
);

CREATE TABLE "URLHistory" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "URLHistoryEntry" (
	url TEXT, 
	"referrerURL" TEXT, 
	"expirationTime" DATETIME, 
	"firstVisit" DATETIME, 
	"lastVisit" DATETIME, 
	"visitCount" INTEGER, 
	"manuallyEnteredCount" INTEGER, 
	"browserUserProfile" TEXT, 
	hostname TEXT, 
	"pageTitle" TEXT, 
	"keywordSearchTerm" TEXT, 
	PRIMARY KEY (url, "referrerURL", "expirationTime", "firstVisit", "lastVisit", "visitCount", "manuallyEnteredCount", "browserUserProfile", hostname, "pageTitle", "keywordSearchTerm")
);

CREATE TABLE "URLHistoryFacet" (
	"browserInformation" TEXT, 
	"urlHistoryEntry" TEXT, 
	PRIMARY KEY ("browserInformation", "urlHistoryEntry")
);

CREATE TABLE "URLVisit" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "URLVisitFacet" (
	"browserInformation" TEXT, 
	"fromURLVisit" TEXT, 
	url TEXT, 
	"visitTime" DATETIME, 
	"visitDuration" INTEGER, 
	"urlTransitionType" VARCHAR(17), 
	PRIMARY KEY ("browserInformation", "fromURLVisit", url, "visitTime", "visitDuration", "urlTransitionType")
);

CREATE TABLE "UserAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "UserAccountFacet" (
	"canEscalatePrivs" BOOLEAN, 
	"isPrivileged" BOOLEAN, 
	"isServiceAccount" BOOLEAN, 
	"homeDirectory" TEXT, 
	PRIMARY KEY ("canEscalatePrivs", "isPrivileged", "isServiceAccount", "homeDirectory")
);

CREATE TABLE "UserSession" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "UserSessionFacet" (
	"effectiveUser" TEXT, 
	"loginTime" DATETIME, 
	"logoutTime" DATETIME, 
	"effectiveGroup" TEXT, 
	"effectiveGroupID" TEXT, 
	PRIMARY KEY ("effectiveUser", "loginTime", "logoutTime", "effectiveGroup", "effectiveGroupID")
);

CREATE TABLE "ValuesEnumeratedEffectFacet" (
	"values" TEXT, 
	PRIMARY KEY ("values")
);

CREATE TABLE "Victim" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "VictimTargeting" (
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Volume" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "VolumeFacet" (
	"sectorSize" INTEGER, 
	"volumeID" TEXT, 
	PRIMARY KEY ("sectorSize", "volumeID")
);

CREATE TABLE "WearableDevice" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WebPage" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "Whois" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WhoisContactFacet" (
	"contactAddress" TEXT, 
	"contactAffiliation" TEXT, 
	"contactEmail" TEXT, 
	"contactMessaging" TEXT, 
	"contactPhone" TEXT, 
	"contactProfile" TEXT, 
	"contactSIP" TEXT, 
	"contactURL" TEXT, 
	"sourceApplication" TEXT, 
	birthdate DATETIME, 
	"lastTimeContacted" DATETIME, 
	"numberTimesContacted" INTEGER, 
	"contactID" TEXT, 
	"displayName" TEXT, 
	"firstName" TEXT, 
	"lastName" TEXT, 
	"middleName" TEXT, 
	"namePhonetic" TEXT, 
	"namePrefix" TEXT, 
	"nameSuffix" TEXT, 
	"contactGroup" TEXT, 
	"contactNote" TEXT, 
	nickname TEXT, 
	"whoisContactType" VARCHAR(9), 
	PRIMARY KEY ("contactAddress", "contactAffiliation", "contactEmail", "contactMessaging", "contactPhone", "contactProfile", "contactSIP", "contactURL", "sourceApplication", birthdate, "lastTimeContacted", "numberTimesContacted", "contactID", "displayName", "firstName", "lastName", "middleName", "namePhonetic", "namePrefix", "nameSuffix", "contactGroup", "contactNote", nickname, "whoisContactType")
);

CREATE TABLE "WhoisFacet" (
	"domainName" TEXT, 
	"ipAddress" TEXT, 
	"registrantContactInfo" TEXT, 
	"serverName" TEXT, 
	"nameServer" TEXT, 
	"registrarInfo" TEXT, 
	"creationDate" DATETIME, 
	"expirationDate" DATETIME, 
	"lookupDate" DATETIME, 
	"updatedDate" DATETIME, 
	"domainID" TEXT, 
	remarks TEXT, 
	"sponsoringRegistrar" TEXT, 
	"registrantIDs" TEXT, 
	dnssec TEXT, 
	status VARCHAR(36), 
	"regionalInternetRegistry" TEXT, 
	PRIMARY KEY ("domainName", "ipAddress", "registrantContactInfo", "serverName", "nameServer", "registrarInfo", "creationDate", "expirationDate", "lookupDate", "updatedDate", "domainID", remarks, "sponsoringRegistrar", "registrantIDs", dnssec, status, "regionalInternetRegistry")
);

CREATE TABLE "WhoisRegistrarInfoType" (
	"geoLocationAddress" TEXT, 
	"contactPhoneNumber" TEXT, 
	"emailAddress" TEXT, 
	"referralURL" TEXT, 
	"whoisServer" TEXT, 
	"registrarGUID" TEXT, 
	"registrarID" TEXT, 
	"registrarName" TEXT, 
	PRIMARY KEY ("geoLocationAddress", "contactPhoneNumber", "emailAddress", "referralURL", "whoisServer", "registrarGUID", "registrarID", "registrarName")
);

CREATE TABLE "WifiAddress" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WifiAddressFacet" (
	"addressValue" TEXT, 
	"displayName" TEXT, 
	PRIMARY KEY ("addressValue", "displayName")
);

CREATE TABLE "Wiki" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WikiArticle" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsAccountFacet" (
	groups TEXT, 
	PRIMARY KEY (groups)
);

CREATE TABLE "WindowsActiveDirectoryAccount" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsActiveDirectoryAccountFacet" (
	"objectGUID" TEXT, 
	"activeDirectoryGroups" TEXT, 
	PRIMARY KEY ("objectGUID", "activeDirectoryGroups")
);

CREATE TABLE "WindowsComputerSpecification" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsComputerSpecificationFacet" (
	"registeredOrganization" TEXT, 
	"registeredOwner" TEXT, 
	"globalFlagList" TEXT, 
	"windowsDirectory" TEXT, 
	"windowsSystemDirectory" TEXT, 
	"windowsTempDirectory" TEXT, 
	"lastShutdownDate" DATETIME, 
	"osInstallDate" DATETIME, 
	"osLastUpgradeDate" DATETIME, 
	"msProductID" TEXT, 
	"msProductName" TEXT, 
	"netBIOSName" TEXT, 
	domain TEXT, 
	PRIMARY KEY ("registeredOrganization", "registeredOwner", "globalFlagList", "windowsDirectory", "windowsSystemDirectory", "windowsTempDirectory", "lastShutdownDate", "osInstallDate", "osLastUpgradeDate", "msProductID", "msProductName", "netBIOSName", domain)
);

CREATE TABLE "WindowsCriticalSection" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsEvent" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsFileMapping" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsHandle" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsHook" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsMailSlot" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsNetworkShare" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsPEBinaryFile" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsPEBinaryFileFacet" (
	"optionalHeader" TEXT, 
	sections TEXT, 
	"fileHeaderHashes" TEXT, 
	"timeDateStamp" DATETIME, 
	"pointerToSymbolTable" TEXT, 
	"numberOfSections" INTEGER, 
	"numberOfSymbols" INTEGER, 
	"sizeOfOptionalHeader" INTEGER, 
	"impHash" TEXT, 
	"peType" TEXT, 
	machine TEXT, 
	characteristics INTEGER, 
	PRIMARY KEY ("optionalHeader", sections, "fileHeaderHashes", "timeDateStamp", "pointerToSymbolTable", "numberOfSections", "numberOfSymbols", "sizeOfOptionalHeader", "impHash", "peType", machine, characteristics)
);

CREATE TABLE "WindowsPEFileHheader" (
	"timeDateStamp" DATETIME, 
	PRIMARY KEY ("timeDateStamp")
);

CREATE TABLE "WindowsPEOptionalHeader" (
	"majorLinkerVersion" INTEGER, 
	"minorLinkerVersion" INTEGER, 
	"addressOfEntryPoint" INTEGER, 
	"baseOfCode" INTEGER, 
	checksum INTEGER, 
	"fileAlignment" INTEGER, 
	"imageBase" INTEGER, 
	"loaderFlags" INTEGER, 
	"numberOfRVAAndSizes" INTEGER, 
	"sectionAlignment" INTEGER, 
	"sizeOfCode" INTEGER, 
	"sizeOfHeaders" INTEGER, 
	"sizeOfHeapCommit" INTEGER, 
	"sizeOfHeapReserve" INTEGER, 
	"sizeOfImage" INTEGER, 
	"sizeOfInitializedData" INTEGER, 
	"sizeOfStackCommit" INTEGER, 
	"sizeOfStackReserve" INTEGER, 
	"sizeOfUninitializedData" INTEGER, 
	"win32VersionValue" INTEGER, 
	"dllCharacteristics" INTEGER, 
	magic INTEGER, 
	"majorImageVersion" INTEGER, 
	"majorOSVersion" INTEGER, 
	"majorSubsystemVersion" INTEGER, 
	"minorImageVersion" INTEGER, 
	"minorOSVersion" INTEGER, 
	"minorSubsystemVersion" INTEGER, 
	subsystem INTEGER, 
	PRIMARY KEY ("majorLinkerVersion", "minorLinkerVersion", "addressOfEntryPoint", "baseOfCode", checksum, "fileAlignment", "imageBase", "loaderFlags", "numberOfRVAAndSizes", "sectionAlignment", "sizeOfCode", "sizeOfHeaders", "sizeOfHeapCommit", "sizeOfHeapReserve", "sizeOfImage", "sizeOfInitializedData", "sizeOfStackCommit", "sizeOfStackReserve", "sizeOfUninitializedData", "win32VersionValue", "dllCharacteristics", magic, "majorImageVersion", "majorOSVersion", "majorSubsystemVersion", "minorImageVersion", "minorOSVersion", "minorSubsystemVersion", subsystem)
);

CREATE TABLE "WindowsPESection" (
	hashes TEXT, 
	entropy FLOAT, 
	size INTEGER, 
	name TEXT, 
	PRIMARY KEY (hashes, entropy, size, name)
);

CREATE TABLE "WindowsPrefetch" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsPrefetchFacet" (
	volume TEXT, 
	"accessedDirectory" TEXT, 
	"accessedFile" TEXT, 
	"firstRun" DATETIME, 
	"lastRun" DATETIME, 
	"timesExecuted" INTEGER, 
	"applicationFileName" TEXT, 
	"prefetchHash" TEXT, 
	PRIMARY KEY (volume, "accessedDirectory", "accessedFile", "firstRun", "lastRun", "timesExecuted", "applicationFileName", "prefetchHash")
);

CREATE TABLE "WindowsProcess" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsProcessFacet" (
	"startupInfo" TEXT, 
	"aslrEnabled" BOOLEAN, 
	"depEnabled" BOOLEAN, 
	"ownerSID" TEXT, 
	priority TEXT, 
	"windowTitle" TEXT, 
	PRIMARY KEY ("startupInfo", "aslrEnabled", "depEnabled", "ownerSID", priority, "windowTitle")
);

CREATE TABLE "WindowsRegistryHive" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsRegistryHiveFacet" (
	"hiveType" TEXT, 
	PRIMARY KEY ("hiveType")
);

CREATE TABLE "WindowsRegistryKey" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsRegistrykeyFacet" (
	creator TEXT, 
	"registryValues" TEXT, 
	"modifiedTime" DATETIME, 
	"numberOfSubkeys" INTEGER, 
	"key" TEXT, 
	PRIMARY KEY (creator, "registryValues", "modifiedTime", "numberOfSubkeys", "key")
);

CREATE TABLE "WindowsRegistryValue" (
	name TEXT, 
	data TEXT, 
	"dataType" TEXT, 
	PRIMARY KEY (name, data, "dataType")
);

CREATE TABLE "WindowsService" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsServiceFacet" (
	"displayName" TEXT, 
	"groupName" TEXT, 
	"serviceName" TEXT, 
	"servicStatus" TEXT, 
	"serviceType" TEXT, 
	"startCommandLine" TEXT, 
	"startType" TEXT, 
	descriptions TEXT, 
	PRIMARY KEY ("displayName", "groupName", "serviceName", "servicStatus", "serviceType", "startCommandLine", "startType", descriptions)
);

CREATE TABLE "WindowsSystemRestore" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsTask" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsTaskFacet" (
	account TEXT, 
	application TEXT, 
	"workItemData" TEXT, 
	"workingDirectory" TEXT, 
	"actionList" TEXT, 
	"triggerList" TEXT, 
	"mostRecentRunTime" DATETIME, 
	"nextRunTime" DATETIME, 
	"observableCreatedTime" DATETIME, 
	"exitCode" INTEGER, 
	"maxRunTime" INTEGER, 
	"accountLogonType" TEXT, 
	"accountRunLevel" TEXT, 
	"imageName" TEXT, 
	parameters TEXT, 
	"taskComment" TEXT, 
	"taskCreator" TEXT, 
	flags VARCHAR(38), 
	priority VARCHAR(27), 
	status VARCHAR(35), 
	PRIMARY KEY (account, application, "workItemData", "workingDirectory", "actionList", "triggerList", "mostRecentRunTime", "nextRunTime", "observableCreatedTime", "exitCode", "maxRunTime", "accountLogonType", "accountRunLevel", "imageName", parameters, "taskComment", "taskCreator", flags, priority, status)
);

CREATE TABLE "WindowsThread" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WindowsThreadFacet" (
	"creationTime" DATETIME, 
	"parameterAddress" TEXT, 
	"startAddress" TEXT, 
	priority TEXT, 
	"stackSize" INTEGER, 
	"threadID" INTEGER, 
	context TEXT, 
	"runningStatus" TEXT, 
	"securityAttributes" TEXT, 
	"creationFlags" INTEGER, 
	PRIMARY KEY ("creationTime", "parameterAddress", "startAddress", priority, "stackSize", "threadID", context, "runningStatus", "securityAttributes", "creationFlags")
);

CREATE TABLE "WindowsVolumeFacet" (
	"driveLetter" TEXT, 
	"driveType" VARCHAR(17), 
	"windowsVolumeAttributes" TEXT, 
	PRIMARY KEY ("driveLetter", "driveType", "windowsVolumeAttributes")
);

CREATE TABLE "WindowsWaitableTime" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "wirelessNetworkConnection" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "WirelessNetworkConnectionFacet" (
	"baseStation" TEXT, 
	password TEXT, 
	ssid TEXT, 
	"wirelessNetworkSecurityMode" VARCHAR(15), 
	PRIMARY KEY ("baseStation", password, ssid, "wirelessNetworkSecurityMode")
);

CREATE TABLE "WriteBlocker" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "X509Certificate" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "X509CertificateFacet" (
	x509v3extensions TEXT, 
	"issuerHash" TEXT, 
	"subjectHash" TEXT, 
	"thumbprintHash" TEXT, 
	"isSelfSigned" BOOLEAN, 
	"validityNotAfter" DATETIME, 
	"validityNotBefore" DATETIME, 
	"subjectPublicKeyExponent" INTEGER, 
	issuer TEXT, 
	"serialNumber" TEXT, 
	signature TEXT, 
	"signatureAlgorithm" TEXT, 
	subject TEXT, 
	"subjectPublicKeyAlgorithm" TEXT, 
	"subjectPublicKeyModulus" TEXT, 
	version TEXT, 
	PRIMARY KEY (x509v3extensions, "issuerHash", "subjectHash", "thumbprintHash", "isSelfSigned", "validityNotAfter", "validityNotBefore", "subjectPublicKeyExponent", issuer, "serialNumber", signature, "signatureAlgorithm", subject, "subjectPublicKeyAlgorithm", "subjectPublicKeyModulus", version)
);

CREATE TABLE "X509V3Certificate" (
	"itemOf" TEXT, 
	"hasChanged" BOOLEAN, 
	state TEXT, 
	"createdBy" TEXT, 
	description TEXT, 
	"externalReference" TEXT, 
	"hasFacet" TEXT, 
	"modifiedTime" DATETIME, 
	name TEXT, 
	"objectMarking" TEXT, 
	"objectCreatedTime" DATETIME, 
	"specVersion" TEXT, 
	tag TEXT, 
	PRIMARY KEY ("itemOf", "hasChanged", state, "createdBy", description, "externalReference", "hasFacet", "modifiedTime", name, "objectMarking", "objectCreatedTime", "specVersion", tag)
);

CREATE TABLE "X509V3ExtensionsFacet" (
	"privateKeyUsagePeriodNotAfter" DATETIME, 
	"privateKeyUsagePeriodNotBefore" DATETIME, 
	"authorityKeyIdentifier" TEXT, 
	"basicConstraints" TEXT, 
	"certificatePolicies" TEXT, 
	"crlDistributionPoints" TEXT, 
	"extendedKeyUsage" TEXT, 
	"inhibitAnyPolicy" TEXT, 
	"issuerAlternativeName" TEXT, 
	"keyUsage" TEXT, 
	"nameConstraints" TEXT, 
	"policyConstraints" TEXT, 
	"policyMappings" TEXT, 
	"subjectAlternativeName" TEXT, 
	"subjectDirectoryAttributes" TEXT, 
	"subjectKeyIdentifier" TEXT, 
	PRIMARY KEY ("privateKeyUsagePeriodNotAfter", "privateKeyUsagePeriodNotBefore", "authorityKeyIdentifier", "basicConstraints", "certificatePolicies", "crlDistributionPoints", "extendedKeyUsage", "inhibitAnyPolicy", "issuerAlternativeName", "keyUsage", "nameConstraints", "policyConstraints", "policyMappings", "subjectAlternativeName", "subjectDirectoryAttributes", "subjectKeyIdentifier")
);
