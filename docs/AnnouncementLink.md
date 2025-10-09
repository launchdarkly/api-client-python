# AnnouncementLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.announcement_link import AnnouncementLink

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementLink from a JSON string
announcement_link_instance = AnnouncementLink.from_json(json)
# print the JSON string representation of the object
print(AnnouncementLink.to_json())

# convert the object into a dict
announcement_link_dict = announcement_link_instance.to_dict()
# create an instance of AnnouncementLink from a dict
announcement_link_from_dict = AnnouncementLink.from_dict(announcement_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


