# AnnouncementAccessDenied


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AnnouncementAccessDeniedReason**](AnnouncementAccessDeniedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_access_denied import AnnouncementAccessDenied

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementAccessDenied from a JSON string
announcement_access_denied_instance = AnnouncementAccessDenied.from_json(json)
# print the JSON string representation of the object
print(AnnouncementAccessDenied.to_json())

# convert the object into a dict
announcement_access_denied_dict = announcement_access_denied_instance.to_dict()
# create an instance of AnnouncementAccessDenied from a dict
announcement_access_denied_from_dict = AnnouncementAccessDenied.from_dict(announcement_access_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


