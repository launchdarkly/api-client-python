# GetAnnouncementsPublic200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnnouncementResponse]**](AnnouncementResponse.md) |  | 
**links** | [**AnnouncementPaginatedLinks**](AnnouncementPaginatedLinks.md) |  | 

## Example

```python
from launchdarkly_api.models.get_announcements_public200_response import GetAnnouncementsPublic200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnnouncementsPublic200Response from a JSON string
get_announcements_public200_response_instance = GetAnnouncementsPublic200Response.from_json(json)
# print the JSON string representation of the object
print(GetAnnouncementsPublic200Response.to_json())

# convert the object into a dict
get_announcements_public200_response_dict = get_announcements_public200_response_instance.to_dict()
# create an instance of GetAnnouncementsPublic200Response from a dict
get_announcements_public200_response_from_dict = GetAnnouncementsPublic200Response.from_dict(get_announcements_public200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


