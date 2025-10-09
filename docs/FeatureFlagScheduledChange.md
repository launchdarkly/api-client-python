# FeatureFlagScheduledChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**creation_date** | **int** |  | 
**maintainer_id** | **str** | The ID of the scheduled change maintainer | 
**version** | **int** | Version of the scheduled change | 
**execution_date** | **int** |  | 
**instructions** | **List[Dict[str, object]]** |  | 
**conflicts** | **object** | Details on any conflicting scheduled changes | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.feature_flag_scheduled_change import FeatureFlagScheduledChange

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagScheduledChange from a JSON string
feature_flag_scheduled_change_instance = FeatureFlagScheduledChange.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagScheduledChange.to_json())

# convert the object into a dict
feature_flag_scheduled_change_dict = feature_flag_scheduled_change_instance.to_dict()
# create an instance of FeatureFlagScheduledChange from a dict
feature_flag_scheduled_change_from_dict = FeatureFlagScheduledChange.from_dict(feature_flag_scheduled_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


