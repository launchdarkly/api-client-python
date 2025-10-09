# OptionsArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.options_array import OptionsArray

# TODO update the JSON string below
json = "{}"
# create an instance of OptionsArray from a JSON string
options_array_instance = OptionsArray.from_json(json)
# print the JSON string representation of the object
print(OptionsArray.to_json())

# convert the object into a dict
options_array_dict = options_array_instance.to_dict()
# create an instance of OptionsArray from a dict
options_array_from_dict = OptionsArray.from_dict(options_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


