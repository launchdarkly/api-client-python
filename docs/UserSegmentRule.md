# UserSegmentRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**clauses** | [**List[Clause]**](Clause.md) |  | 
**weight** | **int** |  | [optional] 
**rollout_context_kind** | **str** |  | [optional] 
**bucket_by** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.user_segment_rule import UserSegmentRule

# TODO update the JSON string below
json = "{}"
# create an instance of UserSegmentRule from a JSON string
user_segment_rule_instance = UserSegmentRule.from_json(json)
# print the JSON string representation of the object
print(UserSegmentRule.to_json())

# convert the object into a dict
user_segment_rule_dict = user_segment_rule_instance.to_dict()
# create an instance of UserSegmentRule from a dict
user_segment_rule_from_dict = UserSegmentRule.from_dict(user_segment_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


