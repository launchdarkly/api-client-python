# FlagDefaultsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**key** | **str** | A unique key for the flag default | [optional] 
**tags** | **List[str]** | A list of default tags for each flag | [optional] 
**temporary** | **bool** | Whether the flag should be temporary by default | [optional] 
**default_client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**boolean_defaults** | [**BooleanDefaults**](BooleanDefaults.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.flag_defaults_rep import FlagDefaultsRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagDefaultsRep from a JSON string
flag_defaults_rep_instance = FlagDefaultsRep.from_json(json)
# print the JSON string representation of the object
print(FlagDefaultsRep.to_json())

# convert the object into a dict
flag_defaults_rep_dict = flag_defaults_rep_instance.to_dict()
# create an instance of FlagDefaultsRep from a dict
flag_defaults_rep_from_dict = FlagDefaultsRep.from_dict(flag_defaults_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


