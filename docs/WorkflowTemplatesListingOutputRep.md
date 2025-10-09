# WorkflowTemplatesListingOutputRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WorkflowTemplateOutput]**](WorkflowTemplateOutput.md) |  | 

## Example

```python
from launchdarkly_api.models.workflow_templates_listing_output_rep import WorkflowTemplatesListingOutputRep

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplatesListingOutputRep from a JSON string
workflow_templates_listing_output_rep_instance = WorkflowTemplatesListingOutputRep.from_json(json)
# print the JSON string representation of the object
print(WorkflowTemplatesListingOutputRep.to_json())

# convert the object into a dict
workflow_templates_listing_output_rep_dict = workflow_templates_listing_output_rep_instance.to_dict()
# create an instance of WorkflowTemplatesListingOutputRep from a dict
workflow_templates_listing_output_rep_from_dict = WorkflowTemplatesListingOutputRep.from_dict(workflow_templates_listing_output_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


