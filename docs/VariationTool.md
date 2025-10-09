# VariationTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the tool to use. | 
**version** | **int** | The version of the tool. | 

## Example

```python
from launchdarkly_api.models.variation_tool import VariationTool

# TODO update the JSON string below
json = "{}"
# create an instance of VariationTool from a JSON string
variation_tool_instance = VariationTool.from_json(json)
# print the JSON string representation of the object
print(VariationTool.to_json())

# convert the object into a dict
variation_tool_dict = variation_tool_instance.to_dict()
# create an instance of VariationTool from a dict
variation_tool_from_dict = VariationTool.from_dict(variation_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


