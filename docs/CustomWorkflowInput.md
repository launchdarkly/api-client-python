# CustomWorkflowInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintainer_id** | **str** |  | [optional] 
**name** | **str** | The workflow name | 
**description** | **str** | The workflow description | [optional] 
**stages** | [**List[StageInput]**](StageInput.md) | A list of the workflow stages | [optional] 
**template_key** | **str** | The template key | [optional] 

## Example

```python
from launchdarkly_api.models.custom_workflow_input import CustomWorkflowInput

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWorkflowInput from a JSON string
custom_workflow_input_instance = CustomWorkflowInput.from_json(json)
# print the JSON string representation of the object
print(CustomWorkflowInput.to_json())

# convert the object into a dict
custom_workflow_input_dict = custom_workflow_input_instance.to_dict()
# create an instance of CustomWorkflowInput from a dict
custom_workflow_input_from_dict = CustomWorkflowInput.from_dict(custom_workflow_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


