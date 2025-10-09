# InsightsRepositoryProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_key** | **str** | The repository key | 
**project_key** | **str** | The project key | 

## Example

```python
from launchdarkly_api.models.insights_repository_project import InsightsRepositoryProject

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsRepositoryProject from a JSON string
insights_repository_project_instance = InsightsRepositoryProject.from_json(json)
# print the JSON string representation of the object
print(InsightsRepositoryProject.to_json())

# convert the object into a dict
insights_repository_project_dict = insights_repository_project_instance.to_dict()
# create an instance of InsightsRepositoryProject from a dict
insights_repository_project_from_dict = InsightsRepositoryProject.from_dict(insights_repository_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


