# DynamicOptionsSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.dynamic_options_source import DynamicOptionsSource

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicOptionsSource from a JSON string
dynamic_options_source_instance = DynamicOptionsSource.from_json(json)
# print the JSON string representation of the object
print(DynamicOptionsSource.to_json())

# convert the object into a dict
dynamic_options_source_dict = dynamic_options_source_instance.to_dict()
# create an instance of DynamicOptionsSource from a dict
dynamic_options_source_from_dict = DynamicOptionsSource.from_dict(dynamic_options_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


