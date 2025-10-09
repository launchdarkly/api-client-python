# ViewLinkRequestSegmentIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 
**segment_key** | **str** |  | 

## Example

```python
from launchdarkly_api.models.view_link_request_segment_identifier import ViewLinkRequestSegmentIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkRequestSegmentIdentifier from a JSON string
view_link_request_segment_identifier_instance = ViewLinkRequestSegmentIdentifier.from_json(json)
# print the JSON string representation of the object
print(ViewLinkRequestSegmentIdentifier.to_json())

# convert the object into a dict
view_link_request_segment_identifier_dict = view_link_request_segment_identifier_instance.to_dict()
# create an instance of ViewLinkRequestSegmentIdentifier from a dict
view_link_request_segment_identifier_from_dict = ViewLinkRequestSegmentIdentifier.from_dict(view_link_request_segment_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


