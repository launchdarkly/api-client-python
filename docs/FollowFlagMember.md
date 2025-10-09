# FollowFlagMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The member&#39;s ID | 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**role** | **str** | The member&#39;s base role. If the member has no additional roles, this role will be in effect. | 
**email** | **str** | The member&#39;s email address | 

## Example

```python
from launchdarkly_api.models.follow_flag_member import FollowFlagMember

# TODO update the JSON string below
json = "{}"
# create an instance of FollowFlagMember from a JSON string
follow_flag_member_instance = FollowFlagMember.from_json(json)
# print the JSON string representation of the object
print(FollowFlagMember.to_json())

# convert the object into a dict
follow_flag_member_dict = follow_flag_member_instance.to_dict()
# create an instance of FollowFlagMember from a dict
follow_flag_member_from_dict = FollowFlagMember.from_dict(follow_flag_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


