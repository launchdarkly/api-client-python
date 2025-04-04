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
**severity** | **str** | The severity of the announcement | 
**status** | **str** | The status of the announcement | 
**links** | [**AnnouncementResponseLinks**](AnnouncementResponseLinks.md) |  | 
**end_time** | **int** | The end time of the announcement. This is a Unix timestamp in milliseconds. | [optional] 
**access** | [**AnnouncementAccessRep**](AnnouncementAccessRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


