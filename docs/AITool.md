# AITool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The tool key | 
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**site** | [**CoreLink**](CoreLink.md) |  | [optional] 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**description** | **str** | A description of the tool | [optional] 
**var_schema** | **object** | JSON Schema defining the tool&#39;s parameters for LLM consumption | 
**custom_parameters** | **object** | Custom metadata and configuration for application-level use (not sent to LLM) | [optional] 
**tags** | **List[str]** | Tags for the tool. Tags can be used in custom role policies. | [optional] 
**version** | **int** | Version of the tool. Starts at 1, and each update that changes the description, schema, custom parameters, or tags creates a new version. Pass this value with &#x60;key&#x60; in a variation&#39;s &#x60;tools: [{key, version}]&#x60;. | 
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


