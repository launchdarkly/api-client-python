# ReleasePolicyScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_keys** | **List[str]** | List of environment keys this policy applies to | [optional] 
**flag_tag_keys** | **List[str]** | List of flag tag keys this policy applies to | [optional] 

## Example

```python
from launchdarkly_api.models.release_policy_scope import ReleasePolicyScope

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePolicyScope from a JSON string
release_policy_scope_instance = ReleasePolicyScope.from_json(json)
# print the JSON string representation of the object
print(ReleasePolicyScope.to_json())

# convert the object into a dict
release_policy_scope_dict = release_policy_scope_instance.to_dict()
# create an instance of ReleasePolicyScope from a dict
release_policy_scope_from_dict = ReleasePolicyScope.from_dict(release_policy_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


