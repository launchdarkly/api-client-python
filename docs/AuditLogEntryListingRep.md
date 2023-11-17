# AuditLogEntryListingRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**id** | **str** | The ID of the audit log entry | 
**account_id** | **str** | The ID of the account to which this audit log entry belongs | 
**date** | **int** |  | 
**accesses** | [**[ResourceAccess]**](ResourceAccess.md) | Details on the actions performed and resources acted on in this audit log entry | 
**kind** | **str** |  | 
**name** | **str** | The name of the resource this audit log entry refers to | 
**description** | **str** | Description of the change recorded in the audit log entry | 
**short_description** | **str** | Shorter version of the change recorded in the audit log entry | 
**comment** | **str** | Optional comment for the audit log entry | [optional] 
**subject** | [**SubjectDataRep**](SubjectDataRep.md) |  | [optional] 
**member** | [**MemberDataRep**](MemberDataRep.md) |  | [optional] 
**token** | [**TokenSummary**](TokenSummary.md) |  | [optional] 
**app** | [**AuthorizedAppDataRep**](AuthorizedAppDataRep.md) |  | [optional] 
**title_verb** | **str** | The action and resource recorded in this audit log entry | [optional] 
**title** | **str** | A description of what occurred, in the format &lt;code&gt;member&lt;/code&gt; &lt;code&gt;titleVerb&lt;/code&gt; &lt;code&gt;target&lt;/code&gt; | [optional] 
**target** | [**TargetResourceRep**](TargetResourceRep.md) |  | [optional] 
**parent** | [**ParentResourceRep**](ParentResourceRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


