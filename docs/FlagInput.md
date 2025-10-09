# FlagInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The ID of the variation or rollout of the flag to use. Use \&quot;fallthrough\&quot; for the default targeting behavior when the flag is on. | 
**flag_config_version** | **int** | The flag version | 
**not_in_experiment_variation_id** | **str** | The ID of the variation to route traffic not part of the experiment analysis to. Defaults to variation ID of baseline treatment, if set. | [optional] 

## Example

```python
from launchdarkly_api.models.flag_input import FlagInput

# TODO update the JSON string below
json = "{}"
# create an instance of FlagInput from a JSON string
flag_input_instance = FlagInput.from_json(json)
# print the JSON string representation of the object
print(FlagInput.to_json())

# convert the object into a dict
flag_input_dict = flag_input_instance.to_dict()
# create an instance of FlagInput from a dict
flag_input_from_dict = FlagInput.from_dict(flag_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


