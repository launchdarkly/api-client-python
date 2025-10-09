# InsightScores


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**InsightPeriod**](InsightPeriod.md) |  | 
**last_period** | [**InsightPeriod**](InsightPeriod.md) |  | 
**scores** | [**InsightGroupScores**](InsightGroupScores.md) |  | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.insight_scores import InsightScores

# TODO update the JSON string below
json = "{}"
# create an instance of InsightScores from a JSON string
insight_scores_instance = InsightScores.from_json(json)
# print the JSON string representation of the object
print(InsightScores.to_json())

# convert the object into a dict
insight_scores_dict = insight_scores_instance.to_dict()
# create an instance of InsightScores from a dict
insight_scores_from_dict = InsightScores.from_dict(insight_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


