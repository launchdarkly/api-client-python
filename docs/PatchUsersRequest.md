# PatchUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the change | [optional] 
**instructions** | [**List[InstructionUserRequest]**](InstructionUserRequest.md) | The instructions to perform when updating | 

## Example

```python
from launchdarkly_api.models.patch_users_request import PatchUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUsersRequest from a JSON string
patch_users_request_instance = PatchUsersRequest.from_json(json)
# print the JSON string representation of the object
print(PatchUsersRequest.to_json())

# convert the object into a dict
patch_users_request_dict = patch_users_request_instance.to_dict()
# create an instance of PatchUsersRequest from a dict
patch_users_request_from_dict = PatchUsersRequest.from_dict(patch_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


