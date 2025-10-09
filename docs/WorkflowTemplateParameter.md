# WorkflowTemplateParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** | The path of the property to parameterize, relative to its parent condition or instruction | [optional] 
**default** | [**ParameterDefault**](ParameterDefault.md) |  | [optional] 
**valid** | **bool** | Whether the default value is valid for the target flag and environment | [optional] 

## Example

```python
from launchdarkly_api.models.workflow_template_parameter import WorkflowTemplateParameter

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateParameter from a JSON string
workflow_template_parameter_instance = WorkflowTemplateParameter.from_json(json)
# print the JSON string representation of the object
print(WorkflowTemplateParameter.to_json())

# convert the object into a dict
workflow_template_parameter_dict = workflow_template_parameter_instance.to_dict()
# create an instance of WorkflowTemplateParameter from a dict
workflow_template_parameter_from_dict = WorkflowTemplateParameter.from_dict(workflow_template_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


