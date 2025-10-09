# PostReleasePolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**ReleasePolicyScope**](ReleasePolicyScope.md) |  | [optional] 
**release_method** | [**ReleaseMethod**](ReleaseMethod.md) |  | 
**guarded_release_config** | [**GuardedReleaseConfig**](GuardedReleaseConfig.md) |  | [optional] 
**progressive_release_config** | **object** | Configuration for progressive releases | [optional] 
**name** | **str** | The name of the release policy | 
**key** | **str** | The human-readable key of the release policy | 

## Example

```python
from launchdarkly_api.models.post_release_policy_request import PostReleasePolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostReleasePolicyRequest from a JSON string
post_release_policy_request_instance = PostReleasePolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PostReleasePolicyRequest.to_json())

# convert the object into a dict
post_release_policy_request_dict = post_release_policy_request_instance.to_dict()
# create an instance of PostReleasePolicyRequest from a dict
post_release_policy_request_from_dict = PostReleasePolicyRequest.from_dict(post_release_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


