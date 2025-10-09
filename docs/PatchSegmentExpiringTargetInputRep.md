# PatchSegmentExpiringTargetInputRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional description of changes | [optional] 
**instructions** | [**List[PatchSegmentExpiringTargetInstruction]**](PatchSegmentExpiringTargetInstruction.md) | Semantic patch instructions for the desired changes to the resource | 

## Example

```python
from launchdarkly_api.models.patch_segment_expiring_target_input_rep import PatchSegmentExpiringTargetInputRep

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSegmentExpiringTargetInputRep from a JSON string
patch_segment_expiring_target_input_rep_instance = PatchSegmentExpiringTargetInputRep.from_json(json)
# print the JSON string representation of the object
print(PatchSegmentExpiringTargetInputRep.to_json())

# convert the object into a dict
patch_segment_expiring_target_input_rep_dict = patch_segment_expiring_target_input_rep_instance.to_dict()
# create an instance of PatchSegmentExpiringTargetInputRep from a dict
patch_segment_expiring_target_input_rep_from_dict = PatchSegmentExpiringTargetInputRep.from_dict(patch_segment_expiring_target_input_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


