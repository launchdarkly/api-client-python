# RandomizationUnitRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**randomization_unit** | **str** | The unit of randomization. Defaults to user. | [optional] 
**default** | **bool** | Whether this randomization unit is the default for experiments | [optional] 
**hidden** | **bool** |  | [optional] 
**display_name** | **str** | The display name for the randomization unit, displayed in the LaunchDarkly user interface. | [optional] 

## Example

```python
from launchdarkly_api.models.randomization_unit_rep import RandomizationUnitRep

# TODO update the JSON string below
json = "{}"
# create an instance of RandomizationUnitRep from a JSON string
randomization_unit_rep_instance = RandomizationUnitRep.from_json(json)
# print the JSON string representation of the object
print(RandomizationUnitRep.to_json())

# convert the object into a dict
randomization_unit_rep_dict = randomization_unit_rep_instance.to_dict()
# create an instance of RandomizationUnitRep from a dict
randomization_unit_rep_from_dict = RandomizationUnitRep.from_dict(randomization_unit_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


