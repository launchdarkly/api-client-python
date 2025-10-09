# ExperimentPatchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Optional comment describing the update | [optional] 
**instructions** | **List[Dict[str, object]]** |  | 

## Example

```python
from launchdarkly_api.models.experiment_patch_input import ExperimentPatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentPatchInput from a JSON string
experiment_patch_input_instance = ExperimentPatchInput.from_json(json)
# print the JSON string representation of the object
print(ExperimentPatchInput.to_json())

# convert the object into a dict
experiment_patch_input_dict = experiment_patch_input_instance.to_dict()
# create an instance of ExperimentPatchInput from a dict
experiment_patch_input_from_dict = ExperimentPatchInput.from_dict(experiment_patch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


