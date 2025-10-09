# AnnouncementAccessRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denied** | [**List[AnnouncementAccessDenied]**](AnnouncementAccessDenied.md) |  | 
**allowed** | [**List[AnnouncementAccessAllowedRep]**](AnnouncementAccessAllowedRep.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_access_rep import AnnouncementAccessRep

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementAccessRep from a JSON string
announcement_access_rep_instance = AnnouncementAccessRep.from_json(json)
# print the JSON string representation of the object
print(AnnouncementAccessRep.to_json())

# convert the object into a dict
announcement_access_rep_dict = announcement_access_rep_instance.to_dict()
# create an instance of AnnouncementAccessRep from a dict
announcement_access_rep_from_dict = AnnouncementAccessRep.from_dict(announcement_access_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


