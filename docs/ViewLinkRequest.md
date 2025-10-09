# ViewLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | Keys of the resources (flags, segments, AI configs) to link/unlink | 
**comment** | **str** | Optional comment for the link/unlink operation | [optional] [default to '']
**segment_identifiers** | [**List[ViewLinkRequestSegmentIdentifier]**](ViewLinkRequestSegmentIdentifier.md) | Identifiers of the segments to link/unlink (environmentId and segmentKey) | 

## Example

```python
from launchdarkly_api.models.view_link_request import ViewLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkRequest from a JSON string
view_link_request_instance = ViewLinkRequest.from_json(json)
# print the JSON string representation of the object
print(ViewLinkRequest.to_json())

# convert the object into a dict
view_link_request_dict = view_link_request_instance.to_dict()
# create an instance of ViewLinkRequest from a dict
view_link_request_from_dict = ViewLinkRequest.from_dict(view_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


