# AuditLogEntryRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) |  | 
**id** | **str** |  | 
**account_id** | **str** |  | 
**date** | **int** |  | 
**accesses** | [**[ResourceAccess]**](ResourceAccess.md) |  | 
**kind** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**short_description** | **str** |  | 
**comment** | **str** |  | [optional] 
**subject** | [**SubjectDataRep**](SubjectDataRep.md) |  | [optional] 
**member** | [**MemberDataRep**](MemberDataRep.md) |  | [optional] 
**token** | [**TokenDataRep**](TokenDataRep.md) |  | [optional] 
**app** | [**AuthorizedAppDataRep**](AuthorizedAppDataRep.md) |  | [optional] 
**title_verb** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**target** | [**TargetResourceRep**](TargetResourceRep.md) |  | [optional] 
**parent** | [**ParentResourceRep**](ParentResourceRep.md) |  | [optional] 
**delta** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**trigger_body** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**merge** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**previous_version** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**current_version** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**subentries** | [**[AuditLogEntryListingRep]**](AuditLogEntryListingRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


