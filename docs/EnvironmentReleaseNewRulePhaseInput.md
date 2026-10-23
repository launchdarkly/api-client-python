# EnvironmentReleaseNewRulePhaseInput

A phase that creates a new rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clauses** | [**List[EnvironmentReleaseClause]**](EnvironmentReleaseClause.md) | Clauses for a new rule. Must include the &#x60;kind&#x60; clause for &#x60;randomizationUnit&#x60; described in &#x60;startEnvironmentRelease&#x60;. A new rule that exactly duplicates an existing rule on the flag returns &#x60;400&#x60; with &#x60;new rule is exact duplicate of an existing rule at index &lt;n&gt;&#x60;.  | 
**description** | **str** | Description for a new rule. Must differ from the description of every other rule on the flag, including rules an earlier release left in place, or the request returns &#x60;400&#x60; with &#x60;duplicate rule description not allowed&#x60;.  | [optional] 
**steps** | [**List[EnvironmentReleaseStepInput]**](EnvironmentReleaseStepInput.md) |  | 

## Example

```python
from launchdarkly_api.models.environment_release_new_rule_phase_input import EnvironmentReleaseNewRulePhaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseNewRulePhaseInput from a JSON string
environment_release_new_rule_phase_input_instance = EnvironmentReleaseNewRulePhaseInput.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseNewRulePhaseInput.to_json())

# convert the object into a dict
environment_release_new_rule_phase_input_dict = environment_release_new_rule_phase_input_instance.to_dict()
# create an instance of EnvironmentReleaseNewRulePhaseInput from a dict
environment_release_new_rule_phase_input_from_dict = EnvironmentReleaseNewRulePhaseInput.from_dict(environment_release_new_rule_phase_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


