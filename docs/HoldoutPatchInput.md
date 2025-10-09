# HoldoutPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.holdout_patch_input import HoldoutPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of HoldoutPatchInput from a JSON string
holdout_patch_input_instance = HoldoutPatchInput.from_json(json)
# print the JSON string representation of the object
print(HoldoutPatchInput.to_json())

# convert the object into a dict
holdout_patch_input_dict = holdout_patch_input_instance.to_dict()
# create an instance of HoldoutPatchInput from a dict
holdout_patch_input_from_dict = HoldoutPatchInput.from_dict(holdout_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


