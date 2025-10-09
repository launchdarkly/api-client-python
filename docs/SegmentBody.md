# SegmentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the segment | 
**key** | **str** | A unique key used to reference the segment | 
**description** | **str** | A description of the segment&#39;s purpose | [optional] 
**tags** | **List[str]** | Tags for the segment | [optional] 
**unbounded** | **bool** | Whether to create a standard segment (&lt;code&gt;false&lt;/code&gt;) or a big segment (&lt;code&gt;true&lt;/code&gt;). Standard segments include rule-based and smaller list-based segments. Big segments include larger list-based segments and synced segments. Only use a big segment if you need to add more than 15,000 individual targets. | [optional] 
**unbounded_context_kind** | **str** | For big segments, the targeted context kind. | [optional] 

## Example

```python
from launchdarkly_api.models.segment_body import SegmentBody

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentBody from a JSON string
segment_body_instance = SegmentBody.from_json(json)
# print the JSON string representation of the object
print(SegmentBody.to_json())

# convert the object into a dict
segment_body_dict = segment_body_instance.to_dict()
# create an instance of SegmentBody from a dict
segment_body_from_dict = SegmentBody.from_dict(segment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


