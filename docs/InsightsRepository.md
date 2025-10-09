# InsightsRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The repository ID | 
**version** | **int** | The repository version | 
**key** | **str** | The repository key | 
**type** | **str** | The repository type | 
**url** | **str** | The repository URL | 
**main_branch** | **str** | The repository main branch | 
**projects** | [**ProjectSummaryCollection**](ProjectSummaryCollection.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.insights_repository import InsightsRepository

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsRepository from a JSON string
insights_repository_instance = InsightsRepository.from_json(json)
# print the JSON string representation of the object
print(InsightsRepository.to_json())

# convert the object into a dict
insights_repository_dict = insights_repository_instance.to_dict()
# create an instance of InsightsRepository from a dict
insights_repository_from_dict = InsightsRepository.from_dict(insights_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


