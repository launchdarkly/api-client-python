# DynamicOptionsParser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options_items** | [**OptionsArray**](OptionsArray.md) |  | [optional] 
**options_path** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.dynamic_options_parser import DynamicOptionsParser

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicOptionsParser from a JSON string
dynamic_options_parser_instance = DynamicOptionsParser.from_json(json)
# print the JSON string representation of the object
print(DynamicOptionsParser.to_json())

# convert the object into a dict
dynamic_options_parser_dict = dynamic_options_parser_instance.to_dict()
# create an instance of DynamicOptionsParser from a dict
dynamic_options_parser_from_dict = DynamicOptionsParser.from_dict(dynamic_options_parser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


