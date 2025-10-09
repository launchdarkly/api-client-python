# AITool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**description** | **str** |  | [optional] 
**var_schema** | **object** |  | 
**version** | **int** |  | 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.ai_tool import AITool

# TODO update the JSON string below
json = "{}"
# create an instance of AITool from a JSON string
ai_tool_instance = AITool.from_json(json)
# print the JSON string representation of the object
print(AITool.to_json())

# convert the object into a dict
ai_tool_dict = ai_tool_instance.to_dict()
# create an instance of AITool from a dict
ai_tool_from_dict = AITool.from_dict(ai_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


