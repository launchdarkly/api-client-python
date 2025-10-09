# ExpiringTargetPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ExpiringTarget]**](ExpiringTarget.md) | A list of the results from each instruction | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_instructions** | **int** |  | [optional] 
**successful_instructions** | **int** |  | [optional] 
**failed_instructions** | **int** |  | [optional] 
**errors** | [**List[ExpiringTargetError]**](ExpiringTargetError.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expiring_target_patch_response import ExpiringTargetPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiringTargetPatchResponse from a JSON string
expiring_target_patch_response_instance = ExpiringTargetPatchResponse.from_json(json)
# print the JSON string representation of the object
print(ExpiringTargetPatchResponse.to_json())

# convert the object into a dict
expiring_target_patch_response_dict = expiring_target_patch_response_instance.to_dict()
# create an instance of ExpiringTargetPatchResponse from a dict
expiring_target_patch_response_from_dict = ExpiringTargetPatchResponse.from_dict(expiring_target_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


