# AnnouncementResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**AnnouncementLink**](AnnouncementLink.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_response_links import AnnouncementResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementResponseLinks from a JSON string
announcement_response_links_instance = AnnouncementResponseLinks.from_json(json)
# print the JSON string representation of the object
print(AnnouncementResponseLinks.to_json())

# convert the object into a dict
announcement_response_links_dict = announcement_response_links_instance.to_dict()
# create an instance of AnnouncementResponseLinks from a dict
announcement_response_links_from_dict = AnnouncementResponseLinks.from_dict(announcement_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


