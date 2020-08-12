# Token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | [optional] 
**id** | [**Id**](Id.md) |  | [optional] 
**owner_id** | [**Id**](Id.md) |  | [optional] 
**member_id** | [**Id**](Id.md) |  | [optional] 
**member** | [**Member**](Member.md) |  | [optional] 
**creation_date** | **int** | A unix epoch time in milliseconds specifying the creation time of this access token. | [optional] 
**last_modified** | **int** | A unix epoch time in milliseconds specifying the last time this access token was modified. | [optional] 
**last_used** | **int** | A unix epoch time in milliseconds specifying the last time this access token was used to authorize access to the LaunchDarkly REST API. | [optional] 
**token** | **str** | The last 4 digits of the unique secret key for this access token. If creating or resetting the token, this will be the full token secret. | [optional] 
**name** | **str** | A human-friendly name for the access token | [optional] 
**role** | **str** | The name of a built-in role for the token | [optional] 
**custom_role_ids** | **list[str]** | A list of custom role IDs to use as access limits for the access token | [optional] 
**inline_role** | [**list[Statement]**](Statement.md) |  | [optional] 
**service_token** | **bool** | Whether the token will be a service token https://docs.launchdarkly.com/home/account-security/api-access-tokens#service-tokens | [optional] 
**default_api_version** | **int** | The default API version for this token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


