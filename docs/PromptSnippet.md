# PromptSnippet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The prompt snippet key | 
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**links** | [**ParentAndSelfLinks**](ParentAndSelfLinks.md) |  | [optional] 
**site** | [**CoreLink**](CoreLink.md) |  | [optional] 
**maintainer** | [**AIConfigMaintainer**](AIConfigMaintainer.md) |  | [optional] 
**name** | **str** | The prompt snippet name | 
**description** | **str** | A description of the prompt snippet | [optional] 
**text** | **str** | The text content of the prompt snippet | 
**tags** | **List[str]** | Tags for this resource | 
**version** | **int** | The version number of this resource | 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.prompt_snippet import PromptSnippet

# TODO update the JSON string below
json = "{}"
# create an instance of PromptSnippet from a JSON string
prompt_snippet_instance = PromptSnippet.from_json(json)
# print the JSON string representation of the object
print(PromptSnippet.to_json())

# convert the object into a dict
prompt_snippet_dict = prompt_snippet_instance.to_dict()
# create an instance of PromptSnippet from a dict
prompt_snippet_from_dict = PromptSnippet.from_dict(prompt_snippet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


