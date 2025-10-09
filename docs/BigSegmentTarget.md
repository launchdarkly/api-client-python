# BigSegmentTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_key** | **str** | The target key | 
**included** | **bool** | Indicates whether the target is included.&lt;br /&gt;Included targets are always segment members, regardless of segment rules. | 
**excluded** | **bool** | Indicates whether the target is excluded.&lt;br /&gt;Segment rules bypass excluded targets, so they will never be included based on rules. Excluded targets may still be included explicitly. | 

## Example

```python
from launchdarkly_api.models.big_segment_target import BigSegmentTarget

# TODO update the JSON string below
json = "{}"
# create an instance of BigSegmentTarget from a JSON string
big_segment_target_instance = BigSegmentTarget.from_json(json)
# print the JSON string representation of the object
print(BigSegmentTarget.to_json())

# convert the object into a dict
big_segment_target_dict = big_segment_target_instance.to_dict()
# create an instance of BigSegmentTarget from a dict
big_segment_target_from_dict = BigSegmentTarget.from_dict(big_segment_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


