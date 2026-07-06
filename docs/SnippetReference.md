# SnippetReference

A usage of a prompt snippet in a specific config variation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_config_key** | **str** | The key of the config with a variation that references this snippet. | 
**ai_config_name** | **str** | The name of the config with a variation that references this snippet. | 
**variation_id** | **str** | The ID of the variation that references this snippet. | 
**variation_key** | **str** | The key of the config variation that references this snippet. | 
**variation_name** | **str** | The name of the variation that references this snippet. | 
**resource_version** | **int** | The version of the snippet being referenced. | 

## Example

```python
from launchdarkly_api.models.snippet_reference import SnippetReference

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetReference from a JSON string
snippet_reference_instance = SnippetReference.from_json(json)
# print the JSON string representation of the object
print(SnippetReference.to_json())

# convert the object into a dict
snippet_reference_dict = snippet_reference_instance.to_dict()
# create an instance of SnippetReference from a dict
snippet_reference_from_dict = SnippetReference.from_dict(snippet_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


