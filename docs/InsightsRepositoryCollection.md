# InsightsRepositoryCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Total number of repositories | 
**items** | [**List[InsightsRepository]**](InsightsRepository.md) | List of repositories | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.insights_repository_collection import InsightsRepositoryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsRepositoryCollection from a JSON string
insights_repository_collection_instance = InsightsRepositoryCollection.from_json(json)
# print the JSON string representation of the object
print(InsightsRepositoryCollection.to_json())

# convert the object into a dict
insights_repository_collection_dict = insights_repository_collection_instance.to_dict()
# create an instance of InsightsRepositoryCollection from a dict
insights_repository_collection_from_dict = InsightsRepositoryCollection.from_dict(insights_repository_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


