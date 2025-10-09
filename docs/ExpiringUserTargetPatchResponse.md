# ExpiringUserTargetPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpiringUserTargetItem]**](ExpiringUserTargetItem.md) | An array of expiring user targets | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_instructions** | **int** | The total count of instructions sent in the PATCH request | [optional] 
**successful_instructions** | **int** | The total count of successful instructions sent in the PATCH request | [optional] 
**failed_instructions** | **int** | The total count of the failed instructions sent in the PATCH request | [optional] 
**errors** | [**List[ExpiringTargetError]**](ExpiringTargetError.md) | An array of error messages for the failed instructions | [optional] 

## Example

```python
from launchdarkly_api.models.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringUserTargetPatchResponse from a JSON string
expiring_user_target_patch_response_instance = ExpiringUserTargetPatchResponse.from_json(json)
# print the JSON string representation of the object
print(ExpiringUserTargetPatchResponse.to_json())

# convert the object into a dict
expiring_user_target_patch_response_dict = expiring_user_target_patch_response_instance.to_dict()
# create an instance of ExpiringUserTargetPatchResponse from a dict
expiring_user_target_patch_response_from_dict = ExpiringUserTargetPatchResponse.from_dict(expiring_user_target_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


