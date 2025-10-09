# AccessTokenPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the access token | [optional] 
**description** | **str** | A description for the access token | [optional] 
**role** | **str** | Base role for the token | [optional] 
**custom_role_ids** | **List[str]** | A list of custom role IDs to use as access limits for the access token | [optional] 
**inline_role** | [**List[StatementPost]**](StatementPost.md) | A JSON array of statements represented as JSON objects with three attributes: effect, resources, actions. May be used in place of a role. | [optional] 
**service_token** | **bool** | Whether the token is a service token | [optional] 
**default_api_version** | **int** | The default API version for this token | [optional] 

## Example

```python
from launchdarkly_api.models.access_token_post import AccessTokenPost

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokenPost from a JSON string
access_token_post_instance = AccessTokenPost.from_json(json)
# print the JSON string representation of the object
print(AccessTokenPost.to_json())

# convert the object into a dict
access_token_post_dict = access_token_post_instance.to_dict()
# create an instance of AccessTokenPost from a dict
access_token_post_from_dict = AccessTokenPost.from_dict(access_token_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


