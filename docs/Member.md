# Member


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{str: (Link,)}**](Link.md) |  | 
**id** | **str** | The member&#39;s ID | 
**role** | **str** | The member&#39;s built-in role. If the member has no custom roles, this role will be in effect. | 
**email** | **str** | The member&#39;s email address | 
**pending_invite** | **bool** | Whether or not the member has a pending invitation | 
**verified** | **bool** | Whether or not the member&#39;s email address has been verified | 
**custom_roles** | **[str]** | The set of custom roles (as keys) assigned to the member | 
**mfa** | **str** | Whether or not multi-factor authentication is enabled for this member | 
**excluded_dashboards** | **[str]** | Default dashboards that the member has chosen to ignore | 
**last_seen** | **int** |  | 
**creation_date** | **int** |  | 
**first_name** | **str** | The member&#39;s first name | [optional] 
**last_name** | **str** | The member&#39;s last name | [optional] 
**pending_email** | **str** |  | [optional] 
**last_seen_metadata** | [**LastSeenMetadata**](LastSeenMetadata.md) |  | [optional] 
**integration_metadata** | [**IntegrationMetadata**](IntegrationMetadata.md) |  | [optional] 
**teams** | [**[MemberTeamSummaryRep]**](MemberTeamSummaryRep.md) |  | [optional] 
**permission_grants** | [**[MemberPermissionGrantSummaryRep]**](MemberPermissionGrantSummaryRep.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


