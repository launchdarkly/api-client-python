# SegmentTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[str]** |  | [optional] 
**context_kind** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.segment_target import SegmentTarget

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentTarget from a JSON string
segment_target_instance = SegmentTarget.from_json(json)
# print the JSON string representation of the object
print(SegmentTarget.to_json())

# convert the object into a dict
segment_target_dict = segment_target_instance.to_dict()
# create an instance of SegmentTarget from a dict
segment_target_from_dict = SegmentTarget.from_dict(segment_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


