# PatchFlagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the change | [optional] 
**instructions** | **List[Dict[str, object]]** | The instructions to perform when updating | 

## Example

```python
from launchdarkly_api.models.patch_flags_request import PatchFlagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFlagsRequest from a JSON string
patch_flags_request_instance = PatchFlagsRequest.from_json(json)
# print the JSON string representation of the object
print(PatchFlagsRequest.to_json())

# convert the object into a dict
patch_flags_request_dict = patch_flags_request_instance.to_dict()
# create an instance of PatchFlagsRequest from a dict
patch_flags_request_from_dict = PatchFlagsRequest.from_dict(patch_flags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


