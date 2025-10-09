# TeamPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.team_patch_input import TeamPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPatchInput from a JSON string
team_patch_input_instance = TeamPatchInput.from_json(json)
# print the JSON string representation of the object
print(TeamPatchInput.to_json())

# convert the object into a dict
team_patch_input_dict = team_patch_input_instance.to_dict()
# create an instance of TeamPatchInput from a dict
team_patch_input_from_dict = TeamPatchInput.from_dict(team_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


