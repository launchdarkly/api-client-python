# ViewPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the view | [optional] 
**description** | **str** | Optional detailed description of the view | [optional] 
**generate_sdk_keys** | **bool** | Whether to generate SDK keys for this view | [optional] 
**maintainer_id** | **str** | Member ID of the maintainer for this view. Only one of &#x60;maintainerId&#x60; or &#x60;maintainerTeamKey&#x60; can be specified. | [optional] 
**maintainer_team_key** | **str** | Key of the maintainer team for this view. Only one of &#x60;maintainerId&#x60; or &#x60;maintainerTeamKey&#x60; can be specified. | [optional] 
**tags** | **List[str]** | Tags associated with this view | [optional] 
**archived** | **bool** | Whether or not the view is archived | [optional] 

## Example

```python
from launchdarkly_api.models.view_patch import ViewPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ViewPatch from a JSON string
view_patch_instance = ViewPatch.from_json(json)
# print the JSON string representation of the object
print(ViewPatch.to_json())

# convert the object into a dict
view_patch_dict = view_patch_instance.to_dict()
# create an instance of ViewPatch from a dict
view_patch_from_dict = ViewPatch.from_dict(view_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


