# WorkflowTemplateOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | [optional] 
**creation_date** | **int** |  | 
**owner_id** | **str** |  | 
**maintainer_id** | **str** |  | 
**links** | [**Dict[str, Link]**](Link.md) |  | 
**description** | **str** |  | [optional] 
**stages** | [**List[StageOutput]**](StageOutput.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.workflow_template_output import WorkflowTemplateOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateOutput from a JSON string
workflow_template_output_instance = WorkflowTemplateOutput.from_json(json)
# print the JSON string representation of the object
print(WorkflowTemplateOutput.to_json())

# convert the object into a dict
workflow_template_output_dict = workflow_template_output_instance.to_dict()
# create an instance of WorkflowTemplateOutput from a dict
workflow_template_output_from_dict = WorkflowTemplateOutput.from_dict(workflow_template_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


