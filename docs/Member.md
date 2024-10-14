# Member


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | 
**id** | **str** | The member&#39;s ID | 
**role** | **str** | The member&#39;s built-in role. If the member has no custom roles, this role will be in effect. | 
**email** | **str** | The member&#39;s email address | 
**pending_invite** | **bool** | Whether the member has a pending invitation | 
**verified** | **bool** | Whether the member&#39;s email address has been verified | 
**custom_roles** | **[str]** | The set of custom roles (as keys) assigned to the member | 
**mfa** | **str** | Whether multi-factor authentication is enabled for this member | 
**last_seen** | **int** |  | 
**creation_date** | **int** |  | 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**pending_email** | **str** | The member&#39;s email address before it has been verified, for accounts where email verification is required | [optional] 
**excluded_dashboards** | **[str]** | Default dashboards that the member has chosen to ignore | [optional] 
**last_seen_metadata** | [**LastSeenMetadata**](LastSeenMetadata.md) |  | [optional] 
**integration_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**teams** | [**[MemberTeamSummaryRep]**](MemberTeamSummaryRep.md) | Details on the teams this member is assigned to | [optional] 
**permission_grants** | [**[MemberPermissionGrantSummaryRep]**](MemberPermissionGrantSummaryRep.md) | A list of permission grants. Permission grants allow a member to have access to a specific action, without having to create or update a custom role. | [optional] 
**oauth_providers** | **[str]** | A list of OAuth providers | [optional] 
**version** | **int** | Version of the current configuration | [optional] 
**role_attributes** | [**RoleAttributeMap**](RoleAttributeMap.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


