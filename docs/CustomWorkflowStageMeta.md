# CustomWorkflowStageMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The zero-based index of the workflow stage | [optional] 
**name** | **str** | The name of the workflow stage | [optional] 

## Example

```python
from launchdarkly_api.models.custom_workflow_stage_meta import CustomWorkflowStageMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWorkflowStageMeta from a JSON string
custom_workflow_stage_meta_instance = CustomWorkflowStageMeta.from_json(json)
# print the JSON string representation of the object
print(CustomWorkflowStageMeta.to_json())

# convert the object into a dict
custom_workflow_stage_meta_dict = custom_workflow_stage_meta_instance.to_dict()
# create an instance of CustomWorkflowStageMeta from a dict
custom_workflow_stage_meta_from_dict = CustomWorkflowStageMeta.from_dict(custom_workflow_stage_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


