# EnvironmentReleasesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Filter type. One of [contextAttribute, eventProperty, group] | 
**attribute** | **str** | If not a group node, the context attribute name or event property name to filter on | [optional] 
**op** | **str** |  | 
**values** | **List[object]** | The context attribute / event property values or group member nodes | 
**context_kind** | **str** | For context attribute filters, the context kind. | [optional] 
**negate** | **bool** | If set, then take the inverse of the operator. &#39;in&#39; becomes &#39;not in&#39;. | 

## Example

```python
from launchdarkly_api.models.environment_releases_filter import EnvironmentReleasesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleasesFilter from a JSON string
environment_releases_filter_instance = EnvironmentReleasesFilter.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleasesFilter.to_json())

# convert the object into a dict
environment_releases_filter_dict = environment_releases_filter_instance.to_dict()
# create an instance of EnvironmentReleasesFilter from a dict
environment_releases_filter_from_dict = EnvironmentReleasesFilter.from_dict(environment_releases_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


