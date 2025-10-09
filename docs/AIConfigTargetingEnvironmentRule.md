# AIConfigTargetingEnvironmentRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clauses** | [**List[AIConfigTargetingEnvironmentRuleClause]**](AIConfigTargetingEnvironmentRuleClause.md) |  | 
**track_events** | **bool** |  | 

## Example

```python
from launchdarkly_api.models.ai_config_targeting_environment_rule import AIConfigTargetingEnvironmentRule

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfigTargetingEnvironmentRule from a JSON string
ai_config_targeting_environment_rule_instance = AIConfigTargetingEnvironmentRule.from_json(json)
# print the JSON string representation of the object
print(AIConfigTargetingEnvironmentRule.to_json())

# convert the object into a dict
ai_config_targeting_environment_rule_dict = ai_config_targeting_environment_rule_instance.to_dict()
# create an instance of AIConfigTargetingEnvironmentRule from a dict
ai_config_targeting_environment_rule_from_dict = AIConfigTargetingEnvironmentRule.from_dict(ai_config_targeting_environment_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


