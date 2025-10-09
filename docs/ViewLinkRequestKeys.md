# ViewLinkRequestKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | Keys of the resources (flags, segments, AI configs) to link/unlink | 
**comment** | **str** | Optional comment for the link/unlink operation | [optional] [default to '']

## Example

```python
from launchdarkly_api.models.view_link_request_keys import ViewLinkRequestKeys

# TODO update the JSON string below
json = "{}"
# create an instance of ViewLinkRequestKeys from a JSON string
view_link_request_keys_instance = ViewLinkRequestKeys.from_json(json)
# print the JSON string representation of the object
print(ViewLinkRequestKeys.to_json())

# convert the object into a dict
view_link_request_keys_dict = view_link_request_keys_instance.to_dict()
# create an instance of ViewLinkRequestKeys from a dict
view_link_request_keys_from_dict = ViewLinkRequestKeys.from_dict(view_link_request_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


