# RuleClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The attribute the rule applies to, for example, last name or email address | [optional] 
**op** | **str** | The operator to apply to the given attribute | [optional] 
**negate** | **bool** | Whether the operator should be negated | [optional] 

## Example

```python
from launchdarkly_api.models.rule_clause import RuleClause

# TODO update the JSON string below
json = "{}"
# create an instance of RuleClause from a JSON string
rule_clause_instance = RuleClause.from_json(json)
# print the JSON string representation of the object
print(RuleClause.to_json())

# convert the object into a dict
rule_clause_dict = rule_clause_instance.to_dict()
# create an instance of RuleClause from a dict
rule_clause_from_dict = RuleClause.from_dict(rule_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


