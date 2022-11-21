# Token


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owner_id** | **str** |  | 
**member_id** | **str** |  | 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**member** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**name** | **str** | A human-friendly name for the access token | [optional] 
**description** | **str** | A description for the access token | [optional] 
**custom_role_ids** | **[str]** | A list of custom role IDs to use as access limits for the access token | [optional] 
**inline_role** | [**[Statement]**](Statement.md) | An array of policy statements, with three attributes: effect, resources, actions. May be used in place of a built-in or custom role. | [optional] 
**role** | **str** | Built-in role for the token | [optional] 
**token** | **str** | Last four characters of the token value | [optional] 
**service_token** | **bool** | Whether this is a service token or a personal token | [optional] 
**default_api_version** | **int** | The default API version for this token | [optional] 
**last_used** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


