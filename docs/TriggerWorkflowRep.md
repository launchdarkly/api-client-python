# TriggerWorkflowRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**version** | **int** | The flag trigger version | [optional] 
**creation_date** | **int** |  | [optional] 
**maintainer_id** | **str** | The ID of the flag trigger maintainer | [optional] 
**maintainer** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**enabled** | **bool** | Whether the flag trigger is currently enabled | [optional] 
**integration_key** | **str** | The unique identifier of the integration for your trigger | [optional] 
**instructions** | [**Instructions**](Instructions.md) |  | [optional] 
**last_triggered_at** | **int** |  | [optional] 
**recent_trigger_bodies** | [**[RecentTriggerBody]**](RecentTriggerBody.md) | Details on recent flag trigger requests. | [optional] 
**trigger_count** | **int** | Number of times the trigger has been executed | [optional] 
**trigger_url** | **str** | The unguessable URL for this flag trigger | [optional] 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


