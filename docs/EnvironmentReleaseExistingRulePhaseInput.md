# EnvironmentReleaseExistingRulePhaseInput

A phase that releases on an existing rule. Allowed only on a single-phase release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Existing rule to release on. The rule must already include the &#x60;kind&#x60; clause for &#x60;randomizationUnit&#x60; described in &#x60;startEnvironmentRelease&#x60;.  | 
**steps** | [**List[EnvironmentReleaseStepInput]**](EnvironmentReleaseStepInput.md) |  | 

## Example

```python
from launchdarkly_api.models.environment_release_existing_rule_phase_input import EnvironmentReleaseExistingRulePhaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseExistingRulePhaseInput from a JSON string
environment_release_existing_rule_phase_input_instance = EnvironmentReleaseExistingRulePhaseInput.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseExistingRulePhaseInput.to_json())

# convert the object into a dict
environment_release_existing_rule_phase_input_dict = environment_release_existing_rule_phase_input_instance.to_dict()
# create an instance of EnvironmentReleaseExistingRulePhaseInput from a dict
environment_release_existing_rule_phase_input_from_dict = EnvironmentReleaseExistingRulePhaseInput.from_dict(environment_release_existing_rule_phase_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


