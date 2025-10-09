# InsightGroupsCountByIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excellent** | **int** | The number of insight groups with an excellent indicator | 
**good** | **int** | The number of insight groups with a good indicator | 
**fair** | **int** | The number of insight groups with a fair indicator | 
**needs_attention** | **int** | The number of insight groups with a needs attention indicator | 
**not_calculated** | **int** | The number of insight groups with a not calculated indicator | 
**unknown** | **int** | The number of insight groups with an unknown indicator | 
**total** | **int** | The total number of insight groups | 

## Example

```python
from launchdarkly_api.models.insight_groups_count_by_indicator import InsightGroupsCountByIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroupsCountByIndicator from a JSON string
insight_groups_count_by_indicator_instance = InsightGroupsCountByIndicator.from_json(json)
# print the JSON string representation of the object
print(InsightGroupsCountByIndicator.to_json())

# convert the object into a dict
insight_groups_count_by_indicator_dict = insight_groups_count_by_indicator_instance.to_dict()
# create an instance of InsightGroupsCountByIndicator from a dict
insight_groups_count_by_indicator_from_dict = InsightGroupsCountByIndicator.from_dict(insight_groups_count_by_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


