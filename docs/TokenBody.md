# TokenBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the access token | [optional] 
**role** | **str** | The name of a built-in role for the token | [optional] 
**custom_role_ids** | **list[str]** | A list of custom role IDs to use as access limits for the access token | [optional] 
**inline_role** | [**list[Statement]**](Statement.md) |  | [optional] 
**service_token** | **bool** | Whether the token will be a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens | [optional] 
**default_api_version** | **int** | The default API version for this token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


