# TriggerWorkflowCollectionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TriggerWorkflowRep]**](TriggerWorkflowRep.md) | An array of flag triggers | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.trigger_workflow_collection_rep import TriggerWorkflowCollectionRep

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerWorkflowCollectionRep from a JSON string
trigger_workflow_collection_rep_instance = TriggerWorkflowCollectionRep.from_json(json)
# print the JSON string representation of the object
print(TriggerWorkflowCollectionRep.to_json())

# convert the object into a dict
trigger_workflow_collection_rep_dict = trigger_workflow_collection_rep_instance.to_dict()
# create an instance of TriggerWorkflowCollectionRep from a dict
trigger_workflow_collection_rep_from_dict = TriggerWorkflowCollectionRep.from_dict(trigger_workflow_collection_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


