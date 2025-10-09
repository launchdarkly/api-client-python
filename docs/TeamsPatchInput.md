# TeamsPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.teams_patch_input import TeamsPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsPatchInput from a JSON string
teams_patch_input_instance = TeamsPatchInput.from_json(json)
# print the JSON string representation of the object
print(TeamsPatchInput.to_json())

# convert the object into a dict
teams_patch_input_dict = teams_patch_input_instance.to_dict()
# create an instance of TeamsPatchInput from a dict
teams_patch_input_from_dict = TeamsPatchInput.from_dict(teams_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


