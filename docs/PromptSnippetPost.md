# PromptSnippetPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**text** | **str** | The text content of the prompt snippet | 
**maintainer_id** | **str** |  | [optional] 
**maintainer_team_key** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.prompt_snippet_post import PromptSnippetPost

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSnippetPost from a JSON string
prompt_snippet_post_instance = PromptSnippetPost.from_json(json)
# print the JSON string representation of the object
print(PromptSnippetPost.to_json())

# convert the object into a dict
prompt_snippet_post_dict = prompt_snippet_post_instance.to_dict()
# create an instance of PromptSnippetPost from a dict
prompt_snippet_post_from_dict = PromptSnippetPost.from_dict(prompt_snippet_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


