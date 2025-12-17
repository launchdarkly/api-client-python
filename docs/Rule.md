# Rule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The flag rule ID | [optional] 
**disabled** | **bool** | Whether the rule is disabled | [optional] 
**variation** | **int** | The index of the variation, from the array of variations for this flag | [optional] 
**rollout** | [**Rollout**](Rollout.md) |  | [optional] 
**clauses** | [**List[Clause]**](Clause.md) | An array of clauses used for individual targeting based on attributes | 
**track_events** | **bool** | Whether LaunchDarkly tracks events for this rule | 
**description** | **str** | The rule description | [optional] 
**ref** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print(Rule.to_json())

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_from_dict = Rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


