# ViewLinkRequestSegmentIdentifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_identifiers** | [**List[ViewLinkRequestSegmentIdentifier]**](ViewLinkRequestSegmentIdentifier.md) | Identifiers of the segments to link/unlink (environmentId and segmentKey) | 
**filter** | **str** | Optional filter string to determine which resources should be linked. Resources only need to match either the filter or explicitly-listed keys to be linked (union). Uses the same queryfilter syntax as the segments list endpoint.  Supported filters for segments: query, tags, keys, excludedKeys, unbounded, external, view, type  | [optional] 
**environment_id** | **str** | Required when using filter for segment resources. Specifies which environment to query for segments matching the filter. Ignored when only using explicit segmentIdentifiers (since each identifier contains its own environmentId).  | [optional] 
**comment** | **str** | Optional comment for the link/unlink operation | [optional] [default to '']

## Example

```python
from launchdarkly_api.models.view_link_request_segment_identifiers import ViewLinkRequestSegmentIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkRequestSegmentIdentifiers from a JSON string
view_link_request_segment_identifiers_instance = ViewLinkRequestSegmentIdentifiers.from_json(json)
# print the JSON string representation of the object
print(ViewLinkRequestSegmentIdentifiers.to_json())

# convert the object into a dict
view_link_request_segment_identifiers_dict = view_link_request_segment_identifiers_instance.to_dict()
# create an instance of ViewLinkRequestSegmentIdentifiers from a dict
view_link_request_segment_identifiers_from_dict = ViewLinkRequestSegmentIdentifiers.from_dict(view_link_request_segment_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


