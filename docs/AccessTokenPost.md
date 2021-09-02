# AccessTokenPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the access token | [optional] 
**description** | **str** | A description for the access token | [optional] 
**role** | **str** | Built-in role for the token | [optional] 
**custom_role_ids** | **[str]** | A list of custom role IDs to use as access limits for the access token | [optional] 
**inline_role** | [**[StatementPost]**](StatementPost.md) | A JSON array of statements represented as JSON objects with three attributes: effect, resources, actions. May be used in place of a built-in or custom role. | [optional] 
**service_token** | **bool** | Whether the token is a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens | [optional] 
**default_api_version** | **int** | The default API version for this token | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


