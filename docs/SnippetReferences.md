# SnippetReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**resource_key** | **str** | The key of the prompt snippet. | 
**resource_type** | **str** | The type of the resource being referenced. | 
**items** | [**List[SnippetReference]**](SnippetReference.md) |  | 
**total_count** | **int** | The total number of references. | 

## Example

```python
from launchdarkly_api.models.snippet_references import SnippetReferences

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetReferences from a JSON string
snippet_references_instance = SnippetReferences.from_json(json)
# print the JSON string representation of the object
print(SnippetReferences.to_json())

# convert the object into a dict
snippet_references_dict = snippet_references_instance.to_dict()
# create an instance of SnippetReferences from a dict
snippet_references_from_dict = SnippetReferences.from_dict(snippet_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


