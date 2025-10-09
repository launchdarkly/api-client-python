# FeatureFlagStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Status of the flag | 
**last_requested** | **datetime** | Timestamp of last time flag was requested | [optional] 
**default** | **object** | Default value seen from code | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag_status import FeatureFlagStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagStatus from a JSON string
feature_flag_status_instance = FeatureFlagStatus.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagStatus.to_json())

# convert the object into a dict
feature_flag_status_dict = feature_flag_status_instance.to_dict()
# create an instance of FeatureFlagStatus from a dict
feature_flag_status_from_dict = FeatureFlagStatus.from_dict(feature_flag_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


