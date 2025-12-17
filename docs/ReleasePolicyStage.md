# ReleasePolicyStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | **int** |  | 
**duration_millis** | **int** |  | 

## Example

```python
from launchdarkly_api.models.release_policy_stage import ReleasePolicyStage

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePolicyStage from a JSON string
release_policy_stage_instance = ReleasePolicyStage.from_json(json)
# print the JSON string representation of the object
print(ReleasePolicyStage.to_json())

# convert the object into a dict
release_policy_stage_dict = release_policy_stage_instance.to_dict()
# create an instance of ReleasePolicyStage from a dict
release_policy_stage_from_dict = ReleasePolicyStage.from_dict(release_policy_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


