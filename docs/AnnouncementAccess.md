# AnnouncementAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[AnnouncementAccessDenied]**](AnnouncementAccessDenied.md) |  | 
**allowed** | [**List[AnnouncementAccessAllowedRep]**](AnnouncementAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_access import AnnouncementAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementAccess from a JSON string
announcement_access_instance = AnnouncementAccess.from_json(json)
# print the JSON string representation of the object
print(AnnouncementAccess.to_json())

# convert the object into a dict
announcement_access_dict = announcement_access_instance.to_dict()
# create an instance of AnnouncementAccess from a dict
announcement_access_from_dict = AnnouncementAccess.from_dict(announcement_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


