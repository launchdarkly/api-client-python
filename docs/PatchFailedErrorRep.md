# PatchFailedErrorRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Specific error code encountered | 
**message** | **str** | Description of the error | 

## Example

```python
from launchdarkly_api.models.patch_failed_error_rep import PatchFailedErrorRep

# TODO update the JSON string below
json = "{}"
# create an instance of PatchFailedErrorRep from a JSON string
patch_failed_error_rep_instance = PatchFailedErrorRep.from_json(json)
# print the JSON string representation of the object
print(PatchFailedErrorRep.to_json())

# convert the object into a dict
patch_failed_error_rep_dict = patch_failed_error_rep_instance.to_dict()
# create an instance of PatchFailedErrorRep from a dict
patch_failed_error_rep_from_dict = PatchFailedErrorRep.from_dict(patch_failed_error_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


