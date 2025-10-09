# MigrationSafetyIssueRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**causing_rule_id** | **str** | The ID of the rule which caused this issue | [optional] 
**affected_rule_ids** | **List[str]** | A list of the IDs of the rules which are affected by this issue. &lt;code&gt;fallthrough&lt;/code&gt; is a sentinel value for the default rule. | [optional] 
**issue** | **str** | A description of the issue that &lt;code&gt;causingRuleId&lt;/code&gt; has caused for &lt;code&gt;affectedRuleIds&lt;/code&gt;. | [optional] 
**old_system_affected** | **bool** | Whether the changes caused by &lt;code&gt;causingRuleId&lt;/code&gt; bring inconsistency to the old system | [optional] 

## Example

```python
from launchdarkly_api.models.migration_safety_issue_rep import MigrationSafetyIssueRep

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationSafetyIssueRep from a JSON string
migration_safety_issue_rep_instance = MigrationSafetyIssueRep.from_json(json)
# print the JSON string representation of the object
print(MigrationSafetyIssueRep.to_json())

# convert the object into a dict
migration_safety_issue_rep_dict = migration_safety_issue_rep_instance.to_dict()
# create an instance of MigrationSafetyIssueRep from a dict
migration_safety_issue_rep_from_dict = MigrationSafetyIssueRep.from_dict(migration_safety_issue_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


