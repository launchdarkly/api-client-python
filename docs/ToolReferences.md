# ToolReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**resource_key** | **str** | The key of the AI tool. | 
**resource_type** | **str** | The type of the resource being referenced. | 
**items** | [**List[ToolReference]**](ToolReference.md) |  | 
**total_count** | **int** | The total number of references. | 

## Example

```python
from launchdarkly_api.models.tool_references import ToolReferences

# TODO update the JSON string below
json = "{}"
# create an instance of ToolReferences from a JSON string
tool_references_instance = ToolReferences.from_json(json)
# print the JSON string representation of the object
print(ToolReferences.to_json())

# convert the object into a dict
tool_references_dict = tool_references_instance.to_dict()
# create an instance of ToolReferences from a dict
tool_references_from_dict = ToolReferences.from_dict(tool_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


