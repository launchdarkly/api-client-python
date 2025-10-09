# InsightsRepositoryProjectCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Total number of repository project associations | 
**items** | [**List[InsightsRepositoryProject]**](InsightsRepositoryProject.md) | List of repository project associations | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 

## Example

```python
from launchdarkly_api.models.insights_repository_project_collection import InsightsRepositoryProjectCollection

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsRepositoryProjectCollection from a JSON string
insights_repository_project_collection_instance = InsightsRepositoryProjectCollection.from_json(json)
# print the JSON string representation of the object
print(InsightsRepositoryProjectCollection.to_json())

# convert the object into a dict
insights_repository_project_collection_dict = insights_repository_project_collection_instance.to_dict()
# create an instance of InsightsRepositoryProjectCollection from a dict
insights_repository_project_collection_from_dict = InsightsRepositoryProjectCollection.from_dict(insights_repository_project_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


