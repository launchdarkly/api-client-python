# CustomWorkflowOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the workflow | 
**version** | **int** | The version of the workflow | 
**conflicts** | [**List[ConflictOutput]**](ConflictOutput.md) | Any conflicts that are present in the workflow stages | 
**creation_date** | **int** |  | 
**maintainer_id** | **str** | The member ID of the maintainer of the workflow. Defaults to the workflow creator. | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**name** | **str** | The name of the workflow | 
**description** | **str** | A brief description of the workflow | [optional] 
**kind** | **str** | The kind of workflow | [optional] 
**stages** | [**List[StageOutput]**](StageOutput.md) | The stages that make up the workflow. Each stage contains conditions and actions. | [optional] 
**execution** | [**ExecutionOutput**](ExecutionOutput.md) |  | 
**meta** | [**WorkflowTemplateMetadata**](WorkflowTemplateMetadata.md) |  | [optional] 
**template_key** | **str** | For workflows being created from a workflow template, this value is the template&#39;s key | [optional] 

## Example

```python
from launchdarkly_api.models.custom_workflow_output import CustomWorkflowOutput

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWorkflowOutput from a JSON string
custom_workflow_output_instance = CustomWorkflowOutput.from_json(json)
# print the JSON string representation of the object
print(CustomWorkflowOutput.to_json())

# convert the object into a dict
custom_workflow_output_dict = custom_workflow_output_instance.to_dict()
# create an instance of CustomWorkflowOutput from a dict
custom_workflow_output_from_dict = CustomWorkflowOutput.from_dict(custom_workflow_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


