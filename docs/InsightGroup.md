# InsightGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**Environment**](Environment.md) |  | [optional] 
**scores** | [**InsightGroupScores**](InsightGroupScores.md) |  | [optional] 
**score_metadata** | [**InsightGroupCollectionScoreMetadata**](InsightGroupCollectionScoreMetadata.md) |  | [optional] 
**key** | **str** | The insight group key | 
**name** | **str** | The insight group name | 
**project_key** | **str** | The project key | 
**environment_key** | **str** | The environment key | 
**application_keys** | **List[str]** | The application keys | [optional] 
**created_at** | **int** |  | 

## Example

```python
from launchdarkly_api.models.insight_group import InsightGroup

# TODO update the JSON string below
json = "{}"
# create an instance of InsightGroup from a JSON string
insight_group_instance = InsightGroup.from_json(json)
# print the JSON string representation of the object
print(InsightGroup.to_json())

# convert the object into a dict
insight_group_dict = insight_group_instance.to_dict()
# create an instance of InsightGroup from a dict
insight_group_from_dict = InsightGroup.from_dict(insight_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


