# AnnouncementResponse

Announcement response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the announcement | 
**is_dismissible** | **bool** | true if the announcement is dismissible | 
**title** | **str** | The title of the announcement | 
**message** | **str** | The message of the announcement | 
**start_time** | **int** | The start time of the announcement. This is a Unix timestamp in milliseconds. | 
**end_time** | **int** | The end time of the announcement. This is a Unix timestamp in milliseconds. | [optional] 
**severity** | **str** | The severity of the announcement | 
**status** | **str** | The status of the announcement | 
**access** | [**AnnouncementAccessRep**](AnnouncementAccessRep.md) |  | [optional] 
**links** | [**AnnouncementResponseLinks**](AnnouncementResponseLinks.md) |  | 

## Example

```python
from launchdarkly_api.models.announcement_response import AnnouncementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementResponse from a JSON string
announcement_response_instance = AnnouncementResponse.from_json(json)
# print the JSON string representation of the object
print(AnnouncementResponse.to_json())

# convert the object into a dict
announcement_response_dict = announcement_response_instance.to_dict()
# create an instance of AnnouncementResponse from a dict
announcement_response_from_dict = AnnouncementResponse.from_dict(announcement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


