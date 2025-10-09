# CustomRolePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the custom role | 
**key** | **str** | The custom role key | 
**description** | **str** | Description of custom role | [optional] 
**policy** | [**List[StatementPost]**](StatementPost.md) |  | 
**base_permissions** | **str** |  | [optional] 
**resource_category** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.custom_role_post import CustomRolePost

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRolePost from a JSON string
custom_role_post_instance = CustomRolePost.from_json(json)
# print the JSON string representation of the object
print(CustomRolePost.to_json())

# convert the object into a dict
custom_role_post_dict = custom_role_post_instance.to_dict()
# create an instance of CustomRolePost from a dict
custom_role_post_from_dict = CustomRolePost.from_dict(custom_role_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


