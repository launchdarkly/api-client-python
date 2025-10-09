# LastSeenMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the token used in the member&#39;s last session | [optional] 

## Example

```python
from launchdarkly_api.models.last_seen_metadata import LastSeenMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LastSeenMetadata from a JSON string
last_seen_metadata_instance = LastSeenMetadata.from_json(json)
# print the JSON string representation of the object
print(LastSeenMetadata.to_json())

# convert the object into a dict
last_seen_metadata_dict = last_seen_metadata_instance.to_dict()
# create an instance of LastSeenMetadata from a dict
last_seen_metadata_from_dict = LastSeenMetadata.from_dict(last_seen_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


