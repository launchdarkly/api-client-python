# FlagRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targeting_rule** | **str** | The targeting rule | [optional] 
**targeting_rule_description** | **str** | The rule description | [optional] 
**targeting_rule_clauses** | **List[object]** | An array of clauses used for individual targeting based on attributes | [optional] 
**flag_config_version** | **int** | The flag version | [optional] 
**not_in_experiment_variation_id** | **str** | The ID of the variation to route traffic not part of the experiment analysis to | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.flag_rep import FlagRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagRep from a JSON string
flag_rep_instance = FlagRep.from_json(json)
# print the JSON string representation of the object
print(FlagRep.to_json())

# convert the object into a dict
flag_rep_dict = flag_rep_instance.to_dict()
# create an instance of FlagRep from a dict
flag_rep_from_dict = FlagRep.from_dict(flag_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


