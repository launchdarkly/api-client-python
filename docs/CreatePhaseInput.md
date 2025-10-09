# CreatePhaseInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | [**List[AudiencePost]**](AudiencePost.md) | An ordered list of the audiences for this release phase. Each audience corresponds to a LaunchDarkly environment. | 
**name** | **str** | The release phase name | 
**configuration** | **object** |  | [optional] 

## Example

```python
from launchdarkly_api.models.create_phase_input import CreatePhaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePhaseInput from a JSON string
create_phase_input_instance = CreatePhaseInput.from_json(json)
# print the JSON string representation of the object
print(CreatePhaseInput.to_json())

# convert the object into a dict
create_phase_input_dict = create_phase_input_instance.to_dict()
# create an instance of CreatePhaseInput from a dict
create_phase_input_from_dict = CreatePhaseInput.from_dict(create_phase_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


