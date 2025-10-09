# ExpiringTargetError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruction_index** | **int** | The index of the PATCH instruction where the error occurred | 
**message** | **str** | The error message related to a failed PATCH instruction | 

## Example

```python
from launchdarkly_api.models.expiring_target_error import ExpiringTargetError

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringTargetError from a JSON string
expiring_target_error_instance = ExpiringTargetError.from_json(json)
# print the JSON string representation of the object
print(ExpiringTargetError.to_json())

# convert the object into a dict
expiring_target_error_dict = expiring_target_error_instance.to_dict()
# create an instance of ExpiringTargetError from a dict
expiring_target_error_from_dict = ExpiringTargetError.from_dict(expiring_target_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


