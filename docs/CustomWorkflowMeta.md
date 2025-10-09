# CustomWorkflowMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workflow stage that required this approval request | [optional] 
**stage** | [**CustomWorkflowStageMeta**](CustomWorkflowStageMeta.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.custom_workflow_meta import CustomWorkflowMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWorkflowMeta from a JSON string
custom_workflow_meta_instance = CustomWorkflowMeta.from_json(json)
# print the JSON string representation of the object
print(CustomWorkflowMeta.to_json())

# convert the object into a dict
custom_workflow_meta_dict = custom_workflow_meta_instance.to_dict()
# create an instance of CustomWorkflowMeta from a dict
custom_workflow_meta_from_dict = CustomWorkflowMeta.from_dict(custom_workflow_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


