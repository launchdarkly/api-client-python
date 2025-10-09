# PatchWithComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch** | [**List[PatchOperation]**](PatchOperation.md) |  | 
**comment** | **str** | Optional comment | [optional] 

## Example

```python
from launchdarkly_api.models.patch_with_comment import PatchWithComment

# TODO update the JSON string below
json = "{}"
# create an instance of PatchWithComment from a JSON string
patch_with_comment_instance = PatchWithComment.from_json(json)
# print the JSON string representation of the object
print(PatchWithComment.to_json())

# convert the object into a dict
patch_with_comment_dict = patch_with_comment_instance.to_dict()
# create an instance of PatchWithComment from a dict
patch_with_comment_from_dict = PatchWithComment.from_dict(patch_with_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


