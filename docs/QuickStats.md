# QuickStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_configs** | **int** |  | 
**active_experiments** | **int** |  | 
**average_satisfaction7_d** | **float** |  | [optional] 
**spend_month_to_date** | **float** |  | [optional] 

## Example

```python
from launchdarkly_api.models.quick_stats import QuickStats

# TODO update the JSON string below
json = "{}"
# create an instance of QuickStats from a JSON string
quick_stats_instance = QuickStats.from_json(json)
# print the JSON string representation of the object
print(QuickStats.to_json())

# convert the object into a dict
quick_stats_dict = quick_stats_instance.to_dict()
# create an instance of QuickStats from a dict
quick_stats_from_dict = QuickStats.from_dict(quick_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


