# PermissionGrantInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_set** | **str** | A group of related actions to allow. Specify either &lt;code&gt;actionSet&lt;/code&gt; or &lt;code&gt;actions&lt;/code&gt;. Use &lt;code&gt;maintainTeam&lt;/code&gt; to add team maintainers. | [optional] 
**actions** | **List[str]** | A list of actions to allow. Specify either &lt;code&gt;actionSet&lt;/code&gt; or &lt;code&gt;actions&lt;/code&gt;. To learn more, read [Role actions](https://launchdarkly.com/docs/ld-docs/home/account/role-actions). | [optional] 
**member_ids** | **List[str]** | A list of member IDs who receive the permission grant. | [optional] 

## Example

```python
from launchdarkly_api.models.permission_grant_input import PermissionGrantInput

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionGrantInput from a JSON string
permission_grant_input_instance = PermissionGrantInput.from_json(json)
# print the JSON string representation of the object
print(PermissionGrantInput.to_json())

# convert the object into a dict
permission_grant_input_dict = permission_grant_input_instance.to_dict()
# create an instance of PermissionGrantInput from a dict
permission_grant_input_from_dict = PermissionGrantInput.from_dict(permission_grant_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


