# PromptSnippets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginatedLinks**](PaginatedLinks.md) |  | [optional] 
**items** | [**List[PromptSnippet]**](PromptSnippet.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from launchdarkly_api.models.prompt_snippets import PromptSnippets

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSnippets from a JSON string
prompt_snippets_instance = PromptSnippets.from_json(json)
# print the JSON string representation of the object
print(PromptSnippets.to_json())

# convert the object into a dict
prompt_snippets_dict = prompt_snippets_instance.to_dict()
# create an instance of PromptSnippets from a dict
prompt_snippets_from_dict = PromptSnippets.from_dict(prompt_snippets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


