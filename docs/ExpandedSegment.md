# ExpandedSegment

Segment representation for Views API - contains only fields actually used by the Views service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key used to reference the segment | 
**name** | **str** | A human-friendly name for the segment | 
**environment_id** | **str** | Environment ID of the segment | [optional] 
**environment_key** | **str** | Environment key of the segment | [optional] 
**description** | **str** | Description of the segment | [optional] 
**creation_date** | **int** | Creation date in milliseconds | [optional] 
**last_modified_date** | **int** | Last modification date in milliseconds | [optional] 
**deleted** | **bool** | Whether the segment is deleted | [optional] 
**tags** | **List[str]** | Tags for the segment | [optional] 
**unbounded** | **bool** | Whether the segment is unbounded | [optional] 
**version** | **int** | Version of the segment | [optional] 
**generation** | **int** | Generation of the segment | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.expanded_segment import ExpandedSegment

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandedSegment from a JSON string
expanded_segment_instance = ExpandedSegment.from_json(json)
# print the JSON string representation of the object
print(ExpandedSegment.to_json())

# convert the object into a dict
expanded_segment_dict = expanded_segment_instance.to_dict()
# create an instance of ExpandedSegment from a dict
expanded_segment_from_dict = ExpandedSegment.from_dict(expanded_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


