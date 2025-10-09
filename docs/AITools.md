# AITools


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[AITool]**](AITool.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ai_tools import AITools

# TODO update the JSON string below
json = "{}"
# create an instance of AITools from a JSON string
ai_tools_instance = AITools.from_json(json)
# print the JSON string representation of the object
print(AITools.to_json())

# convert the object into a dict
ai_tools_dict = ai_tools_instance.to_dict()
# create an instance of AITools from a dict
ai_tools_from_dict = AITools.from_dict(ai_tools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


