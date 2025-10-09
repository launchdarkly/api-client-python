# FeatureFlagStatuses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | 
**items** | [**List[FlagStatusRep]**](FlagStatusRep.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag_statuses import FeatureFlagStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagStatuses from a JSON string
feature_flag_statuses_instance = FeatureFlagStatuses.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagStatuses.to_json())

# convert the object into a dict
feature_flag_statuses_dict = feature_flag_statuses_instance.to_dict()
# create an instance of FeatureFlagStatuses from a dict
feature_flag_statuses_from_dict = FeatureFlagStatuses.from_dict(feature_flag_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


