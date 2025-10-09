# CreateAnnouncementBody

Create announcement request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dismissible** | **bool** | true if the announcement is dismissible | 
**title** | **str** | The title of the announcement | 
**message** | **str** | The message of the announcement | 
**start_time** | **int** | The start time of the announcement. This is a Unix timestamp in milliseconds. | 
**end_time** | **int** | The end time of the announcement. This is a Unix timestamp in milliseconds. | [optional] 
**severity** | **str** | The severity of the announcement | 

## Example

```python
from launchdarkly_api.models.create_announcement_body import CreateAnnouncementBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnnouncementBody from a JSON string
create_announcement_body_instance = CreateAnnouncementBody.from_json(json)
# print the JSON string representation of the object
print(CreateAnnouncementBody.to_json())

# convert the object into a dict
create_announcement_body_dict = create_announcement_body_instance.to_dict()
# create an instance of CreateAnnouncementBody from a dict
create_announcement_body_from_dict = CreateAnnouncementBody.from_dict(create_announcement_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


