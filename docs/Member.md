# Member


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The member&#39;s ID | 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**role** | **str** | The member&#39;s base role. If the member has no additional roles, this role will be in effect. | 
**email** | **str** | The member&#39;s email address | 
**pending_invite** | **bool** | Whether the member has a pending invitation | 
**verified** | **bool** | Whether the member&#39;s email address has been verified | 
**pending_email** | **str** | The member&#39;s email address before it has been verified, for accounts where email verification is required | [optional] 
**custom_roles** | **List[str]** | The set of additional roles, besides the base role, assigned to the member | 
**mfa** | **str** | Whether multi-factor authentication is enabled for this member | 
**excluded_dashboards** | **List[str]** | Default dashboards that the member has chosen to ignore | [optional] 
**last_seen** | **int** |  | 
**last_seen_metadata** | [**LastSeenMetadata**](LastSeenMetadata.md) |  | [optional] 
**integration_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**teams** | [**List[MemberTeamSummaryRep]**](MemberTeamSummaryRep.md) | Details on the teams this member is assigned to | [optional] 
**permission_grants** | [**List[MemberPermissionGrantSummaryRep]**](MemberPermissionGrantSummaryRep.md) | A list of permission grants. Permission grants allow a member to have access to a specific action, without having to create or update a custom role. | [optional] 
**creation_date** | **int** |  | 
**oauth_providers** | **List[str]** | A list of OAuth providers | [optional] 
**version** | **int** | Version of the current configuration | [optional] 
**role_attributes** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from launchdarkly_api.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print(Member.to_json())

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_from_dict = Member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


