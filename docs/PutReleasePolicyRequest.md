# PutReleasePolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ReleasePolicyScope**](ReleasePolicyScope.md) |  | [optional] 
**release_method** | [**ReleaseMethod**](ReleaseMethod.md) |  | 
**guarded_release_config** | [**GuardedReleaseConfig**](GuardedReleaseConfig.md) |  | [optional] 
**progressive_release_config** | [**ProgressiveReleaseConfig**](ProgressiveReleaseConfig.md) |  | [optional] 
**name** | **str** | The name of the release policy | 

## Example

```python
from launchdarkly_api.models.put_release_policy_request import PutReleasePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutReleasePolicyRequest from a JSON string
put_release_policy_request_instance = PutReleasePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PutReleasePolicyRequest.to_json())

# convert the object into a dict
put_release_policy_request_dict = put_release_policy_request_instance.to_dict()
# create an instance of PutReleasePolicyRequest from a dict
put_release_policy_request_from_dict = PutReleasePolicyRequest.from_dict(put_release_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


