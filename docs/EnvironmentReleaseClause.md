# EnvironmentReleaseClause

One targeting clause of a rule created for the release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_kind** | **str** | Context kind the clause applies to. Omit for &#x60;segmentMatch&#x60;. | [optional] 
**attribute** | **str** |  | 
**op** | **str** | One of &#x60;in&#x60;, &#x60;endsWith&#x60;, &#x60;startsWith&#x60;, &#x60;matches&#x60;, &#x60;contains&#x60;, &#x60;lessThan&#x60;, &#x60;lessThanOrEqual&#x60;, &#x60;greaterThan&#x60;, &#x60;greaterThanOrEqual&#x60;, &#x60;before&#x60;, &#x60;after&#x60;, &#x60;segmentMatch&#x60;, &#x60;semVerEqual&#x60;, &#x60;semVerLessThan&#x60;, &#x60;semVerGreaterThan&#x60;.  | 
**values** | **List[object]** | JSON primitives only (strings, numbers, booleans); objects, arrays, and null are rejected. | 
**negate** | **bool** |  | [optional] [default to False]

## Example

```python
from launchdarkly_api.models.environment_release_clause import EnvironmentReleaseClause

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseClause from a JSON string
environment_release_clause_instance = EnvironmentReleaseClause.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseClause.to_json())

# convert the object into a dict
environment_release_clause_dict = environment_release_clause_instance.to_dict()
# create an instance of EnvironmentReleaseClause from a dict
environment_release_clause_from_dict = EnvironmentReleaseClause.from_dict(environment_release_clause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


