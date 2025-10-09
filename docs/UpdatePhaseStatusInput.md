# UpdatePhaseStatusInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**audiences** | [**List[ReleaserAudienceConfigInput]**](ReleaserAudienceConfigInput.md) | Extra configuration for audiences required upon phase initialization. | [optional] 

## Example

```python
from launchdarkly_api.models.update_phase_status_input import UpdatePhaseStatusInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePhaseStatusInput from a JSON string
update_phase_status_input_instance = UpdatePhaseStatusInput.from_json(json)
# print the JSON string representation of the object
print(UpdatePhaseStatusInput.to_json())

# convert the object into a dict
update_phase_status_input_dict = update_phase_status_input_instance.to_dict()
# create an instance of UpdatePhaseStatusInput from a dict
update_phase_status_input_from_dict = UpdatePhaseStatusInput.from_dict(update_phase_status_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


