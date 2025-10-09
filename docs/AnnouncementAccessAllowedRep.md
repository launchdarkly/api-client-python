# AnnouncementAccessAllowedRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**reason** | [**AnnouncementAccessAllowedReason**](AnnouncementAccessAllowedReason.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_access_allowed_rep import AnnouncementAccessAllowedRep

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementAccessAllowedRep from a JSON string
announcement_access_allowed_rep_instance = AnnouncementAccessAllowedRep.from_json(json)
# print the JSON string representation of the object
print(AnnouncementAccessAllowedRep.to_json())

# convert the object into a dict
announcement_access_allowed_rep_dict = announcement_access_allowed_rep_instance.to_dict()
# create an instance of AnnouncementAccessAllowedRep from a dict
announcement_access_allowed_rep_from_dict = AnnouncementAccessAllowedRep.from_dict(announcement_access_allowed_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


