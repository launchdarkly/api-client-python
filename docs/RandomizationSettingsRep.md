# RandomizationSettingsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | The project ID | [optional] 
**project_key** | **str** | The project key | [optional] 
**randomization_units** | [**List[RandomizationUnitRep]**](RandomizationUnitRep.md) | An array of the randomization units in this project | [optional] 
**creation_date** | **int** |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.randomization_settings_rep import RandomizationSettingsRep

# TODO update the JSON string below
json = "{}"
# create an instance of RandomizationSettingsRep from a JSON string
randomization_settings_rep_instance = RandomizationSettingsRep.from_json(json)
# print the JSON string representation of the object
print(RandomizationSettingsRep.to_json())

# convert the object into a dict
randomization_settings_rep_dict = randomization_settings_rep_instance.to_dict()
# create an instance of RandomizationSettingsRep from a dict
randomization_settings_rep_from_dict = RandomizationSettingsRep.from_dict(randomization_settings_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


