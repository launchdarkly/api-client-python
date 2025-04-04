# PermissionGrantInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_set** | **str** | A group of related actions to allow. Specify either &lt;code&gt;actionSet&lt;/code&gt; or &lt;code&gt;actions&lt;/code&gt;. Use &lt;code&gt;maintainTeam&lt;/code&gt; to add team maintainers. | [optional]  if omitted the server will use the default value of "maintainTeam"
**actions** | **[str]** | A list of actions to allow. Specify either &lt;code&gt;actionSet&lt;/code&gt; or &lt;code&gt;actions&lt;/code&gt;. To learn more, read [Role actions](https://launchdarkly.com/docs/ld-docs/home/account/role-actions). | [optional] 
**member_ids** | **[str]** | A list of member IDs who receive the permission grant. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


