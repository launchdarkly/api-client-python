# FlagFollowersByProjEnvGetRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**items** | [**List[FollowersPerFlag]**](FollowersPerFlag.md) | An array of flags and their followers | [optional] 

## Example

```python
from launchdarkly_api.models.flag_followers_by_proj_env_get_rep import FlagFollowersByProjEnvGetRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagFollowersByProjEnvGetRep from a JSON string
flag_followers_by_proj_env_get_rep_instance = FlagFollowersByProjEnvGetRep.from_json(json)
# print the JSON string representation of the object
print(FlagFollowersByProjEnvGetRep.to_json())

# convert the object into a dict
flag_followers_by_proj_env_get_rep_dict = flag_followers_by_proj_env_get_rep_instance.to_dict()
# create an instance of FlagFollowersByProjEnvGetRep from a dict
flag_followers_by_proj_env_get_rep_from_dict = FlagFollowersByProjEnvGetRep.from_dict(flag_followers_by_proj_env_get_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


