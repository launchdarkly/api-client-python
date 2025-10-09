# FlagFollowersGetRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**items** | [**List[FollowFlagMember]**](FollowFlagMember.md) | An array of members who are following this flag | 

## Example

```python
from launchdarkly_api.models.flag_followers_get_rep import FlagFollowersGetRep

# TODO update the JSON string below
json = "{}"
# create an instance of FlagFollowersGetRep from a JSON string
flag_followers_get_rep_instance = FlagFollowersGetRep.from_json(json)
# print the JSON string representation of the object
print(FlagFollowersGetRep.to_json())

# convert the object into a dict
flag_followers_get_rep_dict = flag_followers_get_rep_instance.to_dict()
# create an instance of FlagFollowersGetRep from a dict
flag_followers_get_rep_from_dict = FlagFollowersGetRep.from_dict(flag_followers_get_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


