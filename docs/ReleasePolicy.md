# ReleasePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**ReleasePoliciesAccessRep**](ReleasePoliciesAccessRep.md) |  | [optional] 
**id** | **str** | The unique identifier of the release policy | 
**scope** | [**ReleasePolicyScope**](ReleasePolicyScope.md) |  | [optional] 
**rank** | **int** | The rank/priority of the release policy | 
**release_method** | [**ReleaseMethod**](ReleaseMethod.md) |  | 
**guarded_release_config** | [**GuardedReleaseConfig**](GuardedReleaseConfig.md) |  | [optional] 
**progressive_release_config** | **object** | Configuration for progressive releases | [optional] 
**name** | **str** | The name of the release policy | 
**key** | **str** | The human-readable key of the release policy | 

## Example

```python
from launchdarkly_api.models.release_policy import ReleasePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePolicy from a JSON string
release_policy_instance = ReleasePolicy.from_json(json)
# print the JSON string representation of the object
print(ReleasePolicy.to_json())

# convert the object into a dict
release_policy_dict = release_policy_instance.to_dict()
# create an instance of ReleasePolicy from a dict
release_policy_from_dict = ReleasePolicy.from_dict(release_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


