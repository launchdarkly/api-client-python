# PhaseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The phase ID | 
**name** | **str** | The release phase name | 
**release_count** | **int** | The number of active releases in this phase | 

## Example

```python
from launchdarkly_api.models.phase_info import PhaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PhaseInfo from a JSON string
phase_info_instance = PhaseInfo.from_json(json)
# print the JSON string representation of the object
print(PhaseInfo.to_json())

# convert the object into a dict
phase_info_dict = phase_info_instance.to_dict()
# create an instance of PhaseInfo from a dict
phase_info_from_dict = PhaseInfo.from_dict(phase_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


