# PromptSnippetPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**text** | **str** | The text content of the prompt snippet | [optional] 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.prompt_snippet_patch import PromptSnippetPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSnippetPatch from a JSON string
prompt_snippet_patch_instance = PromptSnippetPatch.from_json(json)
# print the JSON string representation of the object
print(PromptSnippetPatch.to_json())

# convert the object into a dict
prompt_snippet_patch_dict = prompt_snippet_patch_instance.to_dict()
# create an instance of PromptSnippetPatch from a dict
prompt_snippet_patch_from_dict = PromptSnippetPatch.from_dict(prompt_snippet_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


