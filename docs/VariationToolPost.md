# VariationToolPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the tool to use. | 
**version** | **int** | The version of the tool. | 

## Example

```python
from launchdarkly_api.models.variation_tool_post import VariationToolPost

# TODO update the JSON string below
json = "{}"
# create an instance of VariationToolPost from a JSON string
variation_tool_post_instance = VariationToolPost.from_json(json)
# print the JSON string representation of the object
print(VariationToolPost.to_json())

# convert the object into a dict
variation_tool_post_dict = variation_tool_post_instance.to_dict()
# create an instance of VariationToolPost from a dict
variation_tool_post_from_dict = VariationToolPost.from_dict(variation_tool_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


