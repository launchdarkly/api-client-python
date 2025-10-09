# Defaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_variation** | **int** | The index, from the array of variations for this flag, of the variation to serve by default when targeting is on. | 
**off_variation** | **int** | The index, from the array of variations for this flag, of the variation to serve by default when targeting is off. | 

## Example

```python
from launchdarkly_api.models.defaults import Defaults

# TODO update the JSON string below
json = "{}"
# create an instance of Defaults from a JSON string
defaults_instance = Defaults.from_json(json)
# print the JSON string representation of the object
print(Defaults.to_json())

# convert the object into a dict
defaults_dict = defaults_instance.to_dict()
# create an instance of Defaults from a dict
defaults_from_dict = Defaults.from_dict(defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


