# DynamicOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_unknown_value** | **bool** |  | [optional] 
**endpoint** | [**Endpoint**](Endpoint.md) |  | [optional] 
**filters** | [**List[DynamicOptionFiltersItems]**](DynamicOptionFiltersItems.md) |  | [optional] 
**parser** | [**DynamicOptionsParser**](DynamicOptionsParser.md) |  | [optional] 
**source** | [**DynamicOptionsSource**](DynamicOptionsSource.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.dynamic_options import DynamicOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicOptions from a JSON string
dynamic_options_instance = DynamicOptions.from_json(json)
# print the JSON string representation of the object
print(DynamicOptions.to_json())

# convert the object into a dict
dynamic_options_dict = dynamic_options_instance.to_dict()
# create an instance of DynamicOptions from a dict
dynamic_options_from_dict = DynamicOptions.from_dict(dynamic_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


