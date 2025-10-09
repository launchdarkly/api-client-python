# GuardedReleaseConfig

Configuration for guarded releases

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_sample_size** | **int** | The minimum number of samples required to make a decision | [optional] 
**rollback_on_regression** | **bool** | Whether to roll back on regression | 

## Example

```python
from launchdarkly_api.models.guarded_release_config import GuardedReleaseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GuardedReleaseConfig from a JSON string
guarded_release_config_instance = GuardedReleaseConfig.from_json(json)
# print the JSON string representation of the object
print(GuardedReleaseConfig.to_json())

# convert the object into a dict
guarded_release_config_dict = guarded_release_config_instance.to_dict()
# create an instance of GuardedReleaseConfig from a dict
guarded_release_config_from_dict = GuardedReleaseConfig.from_dict(guarded_release_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


