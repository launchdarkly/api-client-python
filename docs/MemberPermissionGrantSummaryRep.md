# MemberPermissionGrantSummaryRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_set** | **str** | The name of the group of related actions to allow. A permission grant may have either an &lt;code&gt;actionSet&lt;/code&gt; or a list of &lt;code&gt;actions&lt;/code&gt; but not both at the same time. | [optional] 
**actions** | **List[str]** | A list of actions to allow. A permission grant may have either an &lt;code&gt;actionSet&lt;/code&gt; or a list of &lt;code&gt;actions&lt;/code&gt; but not both at the same time. | [optional] 
**resource** | **str** | The resource for which the actions are allowed | 

## Example

```python
from launchdarkly_api.models.member_permission_grant_summary_rep import MemberPermissionGrantSummaryRep

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPermissionGrantSummaryRep from a JSON string
member_permission_grant_summary_rep_instance = MemberPermissionGrantSummaryRep.from_json(json)
# print the JSON string representation of the object
print(MemberPermissionGrantSummaryRep.to_json())

# convert the object into a dict
member_permission_grant_summary_rep_dict = member_permission_grant_summary_rep_instance.to_dict()
# create an instance of MemberPermissionGrantSummaryRep from a dict
member_permission_grant_summary_rep_from_dict = MemberPermissionGrantSummaryRep.from_dict(member_permission_grant_summary_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


