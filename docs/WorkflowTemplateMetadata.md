# WorkflowTemplateMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[WorkflowTemplateParameter]**](WorkflowTemplateParameter.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.workflow_template_metadata import WorkflowTemplateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateMetadata from a JSON string
workflow_template_metadata_instance = WorkflowTemplateMetadata.from_json(json)
# print the JSON string representation of the object
print(WorkflowTemplateMetadata.to_json())

# convert the object into a dict
workflow_template_metadata_dict = workflow_template_metadata_instance.to_dict()
# create an instance of WorkflowTemplateMetadata from a dict
workflow_template_metadata_from_dict = WorkflowTemplateMetadata.from_dict(workflow_template_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


