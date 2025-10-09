# NamingConvention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case** | **str** | The casing convention to enforce for new flag keys in this project | [optional] 
**prefix** | **str** | The prefix to enforce for new flag keys in this project | [optional] 

## Example

```python
from launchdarkly_api.models.naming_convention import NamingConvention

# TODO update the JSON string below
json = "{}"
# create an instance of NamingConvention from a JSON string
naming_convention_instance = NamingConvention.from_json(json)
# print the JSON string representation of the object
print(NamingConvention.to_json())

# convert the object into a dict
naming_convention_dict = naming_convention_instance.to_dict()
# create an instance of NamingConvention from a dict
naming_convention_from_dict = NamingConvention.from_dict(naming_convention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


