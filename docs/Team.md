# Team


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the team | [optional] 
**key** | **str** | The team key | [optional] 
**name** | **str** | A human-friendly name for the team | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**creation_date** | **int** |  | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**last_modified** | **int** |  | [optional] 
**version** | **int** | The team version | [optional] 
**idp_synced** | **bool** | Whether the team has been synced with an external identity provider (IdP). Team sync is available to customers on an Enterprise plan. | [optional] 
**role_attributes** | [**RoleAttributeMap**](RoleAttributeMap.md) |  | [optional] 
**roles** | [**TeamCustomRoles**](TeamCustomRoles.md) |  | [optional] 
**members** | [**TeamMembers**](TeamMembers.md) |  | [optional] 
**projects** | [**TeamProjects**](TeamProjects.md) |  | [optional] 
**maintainers** | [**TeamMaintainers**](TeamMaintainers.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


