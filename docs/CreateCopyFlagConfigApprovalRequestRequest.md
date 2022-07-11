# CreateCopyFlagConfigApprovalRequestRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A brief description of your changes | 
**source** | [**SourceFlag**](SourceFlag.md) |  | 
**comment** | **str** | Optional comment describing the approval request | [optional] 
**notify_member_ids** | **[str]** | An array of member IDs. These members are notified to review the approval request. | [optional] 
**notify_team_keys** | **[str]** | An array of team keys. The members of these teams are notified to review the approval request. | [optional] 
**included_actions** | **[str]** | Optional list of the flag changes to copy from the source environment to the target environment. You may include either &lt;code&gt;includedActions&lt;/code&gt; or &lt;code&gt;excludedActions&lt;/code&gt;, but not both. If neither are included, then all flag changes will be copied. | [optional] 
**excluded_actions** | **[str]** | Optional list of the flag changes NOT to copy from the source environment to the target environment. You may include either &lt;code&gt;includedActions&lt;/code&gt; or &lt;code&gt;excludedActions&lt;/code&gt;, but not both. If neither are included, then all flag changes will be copied. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


