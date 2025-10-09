# InsightsRepositoryProjectMappings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mappings** | [**List[InsightsRepositoryProject]**](InsightsRepositoryProject.md) |  | 

## Example

```python
from launchdarkly_api.models.insights_repository_project_mappings import InsightsRepositoryProjectMappings

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsRepositoryProjectMappings from a JSON string
insights_repository_project_mappings_instance = InsightsRepositoryProjectMappings.from_json(json)
# print the JSON string representation of the object
print(InsightsRepositoryProjectMappings.to_json())

# convert the object into a dict
insights_repository_project_mappings_dict = insights_repository_project_mappings_instance.to_dict()
# create an instance of InsightsRepositoryProjectMappings from a dict
insights_repository_project_mappings_from_dict = InsightsRepositoryProjectMappings.from_dict(insights_repository_project_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


