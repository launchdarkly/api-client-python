# FeatureFlagStatusAcrossEnvironments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**Dict[str, FeatureFlagStatus]**](FeatureFlagStatus.md) | Flag status for environment. | 
**key** | **str** | feature flag key | 
**links** | [**Dict[str, Link]**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.feature_flag_status_across_environments import FeatureFlagStatusAcrossEnvironments

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagStatusAcrossEnvironments from a JSON string
feature_flag_status_across_environments_instance = FeatureFlagStatusAcrossEnvironments.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagStatusAcrossEnvironments.to_json())

# convert the object into a dict
feature_flag_status_across_environments_dict = feature_flag_status_across_environments_instance.to_dict()
# create an instance of FeatureFlagStatusAcrossEnvironments from a dict
feature_flag_status_across_environments_from_dict = FeatureFlagStatusAcrossEnvironments.from_dict(feature_flag_status_across_environments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


