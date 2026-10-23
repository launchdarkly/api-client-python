# DynamicOptionFiltersItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | [optional] 
**variable_key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.dynamic_option_filters_items import DynamicOptionFiltersItems

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicOptionFiltersItems from a JSON string
dynamic_option_filters_items_instance = DynamicOptionFiltersItems.from_json(json)
# print the JSON string representation of the object
print(DynamicOptionFiltersItems.to_json())

# convert the object into a dict
dynamic_option_filters_items_dict = dynamic_option_filters_items_instance.to_dict()
# create an instance of DynamicOptionFiltersItems from a dict
dynamic_option_filters_items_from_dict = DynamicOptionFiltersItems.from_dict(dynamic_option_filters_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


