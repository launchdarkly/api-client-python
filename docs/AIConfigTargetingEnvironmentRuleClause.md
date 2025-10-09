# AIConfigTargetingEnvironmentRuleClause


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** |  | 
**id** | **str** |  | 
**negate** | **bool** |  | 
**op** | **str** |  | 
**values** | **List[object]** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_environment_rule_clause import AIConfigTargetingEnvironmentRuleClause

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingEnvironmentRuleClause from a JSON string
ai_config_targeting_environment_rule_clause_instance = AIConfigTargetingEnvironmentRuleClause.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingEnvironmentRuleClause.to_json())

# convert the object into a dict
ai_config_targeting_environment_rule_clause_dict = ai_config_targeting_environment_rule_clause_instance.to_dict()
# create an instance of AIConfigTargetingEnvironmentRuleClause from a dict
ai_config_targeting_environment_rule_clause_from_dict = AIConfigTargetingEnvironmentRuleClause.from_dict(ai_config_targeting_environment_rule_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


