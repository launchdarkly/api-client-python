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
**instructions** | **List[Dict[str, object]]** |  | [optional] 
**last_triggered_at** | **int** |  | [optional] 
**recent_trigger_bodies** | [**List[RecentTriggerBody]**](RecentTriggerBody.md) | Details on recent flag trigger requests. | [optional] 
**trigger_count** | **int** | Number of times the trigger has been executed | [optional] 
**trigger_url** | **str** | The unguessable URL for this flag trigger | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.trigger_workflow_rep import TriggerWorkflowRep

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerWorkflowRep from a JSON string
trigger_workflow_rep_instance = TriggerWorkflowRep.from_json(json)
# print the JSON string representation of the object
print(TriggerWorkflowRep.to_json())

# convert the object into a dict
trigger_workflow_rep_dict = trigger_workflow_rep_instance.to_dict()
# create an instance of TriggerWorkflowRep from a dict
trigger_workflow_rep_from_dict = TriggerWorkflowRep.from_dict(trigger_workflow_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


