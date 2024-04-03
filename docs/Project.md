# Project


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**id** | **str** | The ID of this project | 
**key** | **str** | The key of this project | 
**include_in_snippet_by_default** | **bool** | Whether or not flags created in this project are made available to the client-side JavaScript SDK by default | 
**name** | **str** | A human-friendly name for the project | 
**tags** | **[str]** | A list of tags for the project | 
**default_client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**default_release_pipeline_key** | **str** | The key of the default release pipeline for this project | [optional] 
**environments** | [**Environments**](Environments.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


