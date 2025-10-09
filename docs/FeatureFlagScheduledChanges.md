# FeatureFlagScheduledChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[FeatureFlagScheduledChange]**](FeatureFlagScheduledChange.md) | Array of scheduled changes | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag_scheduled_changes import FeatureFlagScheduledChanges

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagScheduledChanges from a JSON string
feature_flag_scheduled_changes_instance = FeatureFlagScheduledChanges.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagScheduledChanges.to_json())

# convert the object into a dict
feature_flag_scheduled_changes_dict = feature_flag_scheduled_changes_instance.to_dict()
# create an instance of FeatureFlagScheduledChanges from a dict
feature_flag_scheduled_changes_from_dict = FeatureFlagScheduledChanges.from_dict(feature_flag_scheduled_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


