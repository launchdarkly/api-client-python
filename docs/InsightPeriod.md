# InsightPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **int** |  | 
**end_time** | **int** |  | 

## Example

```python
from launchdarkly_api.models.insight_period import InsightPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of InsightPeriod from a JSON string
insight_period_instance = InsightPeriod.from_json(json)
# print the JSON string representation of the object
print(InsightPeriod.to_json())

# convert the object into a dict
insight_period_dict = insight_period_instance.to_dict()
# create an instance of InsightPeriod from a dict
insight_period_from_dict = InsightPeriod.from_dict(insight_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


