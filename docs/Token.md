# Token


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owner_id** | **str** |  | 
**member_id** | **str** |  | 
**member** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**name** | **str** | A human-friendly name for the access token | [optional] 
**description** | **str** | A description for the access token | [optional] 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 
**custom_role_ids** | **List[str]** | A list of custom role IDs to use as access limits for the access token | [optional] 
**inline_role** | [**List[Statement]**](Statement.md) | An array of policy statements, with three attributes: effect, resources, actions. May be used in place of a role. | [optional] 
**role** | **str** | Base role for the token | [optional] 
**token** | **str** | The token value. When creating or resetting, contains the entire token value. Otherwise, contains the last four characters. | [optional] 
**service_token** | **bool** | Whether this is a service token or a personal token | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**default_api_version** | **int** | The default API version for this token | [optional] 
**last_used** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.token import Token

# TODO update the JSON string below
json = "{}"
# create an instance of Token from a JSON string
token_instance = Token.from_json(json)
# print the JSON string representation of the object
print(Token.to_json())

# convert the object into a dict
token_dict = token_instance.to_dict()
# create an instance of Token from a dict
token_from_dict = Token.from_dict(token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


