# CreateWorkflowTemplateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**stages** | [**List[StageInput]**](StageInput.md) |  | [optional] 
**project_key** | **str** |  | [optional] 
**environment_key** | **str** |  | [optional] 
**flag_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.create_workflow_template_input import CreateWorkflowTemplateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkflowTemplateInput from a JSON string
create_workflow_template_input_instance = CreateWorkflowTemplateInput.from_json(json)
# print the JSON string representation of the object
print(CreateWorkflowTemplateInput.to_json())

# convert the object into a dict
create_workflow_template_input_dict = create_workflow_template_input_instance.to_dict()
# create an instance of CreateWorkflowTemplateInput from a dict
create_workflow_template_input_from_dict = CreateWorkflowTemplateInput.from_dict(create_workflow_template_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


