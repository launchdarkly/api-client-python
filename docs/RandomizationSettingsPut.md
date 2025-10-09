# RandomizationSettingsPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**randomization_units** | [**List[RandomizationUnitInput]**](RandomizationUnitInput.md) | An array of randomization units allowed for this project. | 

## Example

```python
from launchdarkly_api.models.randomization_settings_put import RandomizationSettingsPut

# TODO update the JSON string below
json = "{}"
# create an instance of RandomizationSettingsPut from a JSON string
randomization_settings_put_instance = RandomizationSettingsPut.from_json(json)
# print the JSON string representation of the object
print(RandomizationSettingsPut.to_json())

# convert the object into a dict
randomization_settings_put_dict = randomization_settings_put_instance.to_dict()
# create an instance of RandomizationSettingsPut from a dict
randomization_settings_put_from_dict = RandomizationSettingsPut.from_dict(randomization_settings_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


