# PatchSegmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional description of changes | [optional] 
**instructions** | [**List[PatchSegmentInstruction]**](PatchSegmentInstruction.md) | Semantic patch instructions for the desired changes to the resource | 

## Example

```python
from launchdarkly_api.models.patch_segment_request import PatchSegmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSegmentRequest from a JSON string
patch_segment_request_instance = PatchSegmentRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSegmentRequest.to_json())

# convert the object into a dict
patch_segment_request_dict = patch_segment_request_instance.to_dict()
# create an instance of PatchSegmentRequest from a dict
patch_segment_request_from_dict = PatchSegmentRequest.from_dict(patch_segment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


