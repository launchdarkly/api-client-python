# ProgressiveReleaseConfig

Configuration for progressive releases

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollout_context_kind_key** | **str** | Context kind key to use as the randomization unit for the rollout | [optional] 
**stages** | [**List[ReleasePolicyStage]**](ReleasePolicyStage.md) | List of stages | [optional] 

## Example

```python
from launchdarkly_api.models.progressive_release_config import ProgressiveReleaseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressiveReleaseConfig from a JSON string
progressive_release_config_instance = ProgressiveReleaseConfig.from_json(json)
# print the JSON string representation of the object
print(ProgressiveReleaseConfig.to_json())

# convert the object into a dict
progressive_release_config_dict = progressive_release_config_instance.to_dict()
# create an instance of ProgressiveReleaseConfig from a dict
progressive_release_config_from_dict = ProgressiveReleaseConfig.from_dict(progressive_release_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


