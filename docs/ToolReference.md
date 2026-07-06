# ToolReference

A usage of an AI tool in a specific AgentControl config variation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_config_key** | **str** | The key of the AgentControl config with a variation that references this tool. | 
**ai_config_name** | **str** | The name of the AgentControl config with a variation that references this tool. | 
**variation_id** | **str** | The ID of the variation that references this tool. | 
**variation_key** | **str** | The key of the AgentControl config variation that references this tool. | 
**variation_name** | **str** | The name of the variation that references this tool. | 
**tool_version** | **int** | The version of the tool being referenced. | 

## Example

```python
from launchdarkly_api.models.tool_reference import ToolReference

# TODO update the JSON string below
json = "{}"
# create an instance of ToolReference from a JSON string
tool_reference_instance = ToolReference.from_json(json)
# print the JSON string representation of the object
print(ToolReference.to_json())

# convert the object into a dict
tool_reference_dict = tool_reference_instance.to_dict()
# create an instance of ToolReference from a dict
tool_reference_from_dict = ToolReference.from_dict(tool_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


