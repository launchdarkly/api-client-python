# FollowersPerFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag_key** | **str** | The flag key | [optional] 
**followers** | [**List[FollowFlagMember]**](FollowFlagMember.md) | A list of members who are following this flag | [optional] 

## Example

```python
from launchdarkly_api.models.followers_per_flag import FollowersPerFlag

# TODO update the JSON string below
json = "{}"
# create an instance of FollowersPerFlag from a JSON string
followers_per_flag_instance = FollowersPerFlag.from_json(json)
# print the JSON string representation of the object
print(FollowersPerFlag.to_json())

# convert the object into a dict
followers_per_flag_dict = followers_per_flag_instance.to_dict()
# create an instance of FollowersPerFlag from a dict
followers_per_flag_from_dict = FollowersPerFlag.from_dict(followers_per_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


