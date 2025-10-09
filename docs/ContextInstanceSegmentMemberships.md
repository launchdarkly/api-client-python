# ContextInstanceSegmentMemberships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContextInstanceSegmentMembership]**](ContextInstanceSegmentMembership.md) |  | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.context_instance_segment_memberships import ContextInstanceSegmentMemberships

# TODO update the JSON string below
json = "{}"
# create an instance of ContextInstanceSegmentMemberships from a JSON string
context_instance_segment_memberships_instance = ContextInstanceSegmentMemberships.from_json(json)
# print the JSON string representation of the object
print(ContextInstanceSegmentMemberships.to_json())

# convert the object into a dict
context_instance_segment_memberships_dict = context_instance_segment_memberships_instance.to_dict()
# create an instance of ContextInstanceSegmentMemberships from a dict
context_instance_segment_memberships_from_dict = ContextInstanceSegmentMemberships.from_dict(context_instance_segment_memberships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


