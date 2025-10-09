# ProjectSummaryCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**items** | [**List[ProjectSummary]**](ProjectSummary.md) |  | 
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.project_summary_collection import ProjectSummaryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSummaryCollection from a JSON string
project_summary_collection_instance = ProjectSummaryCollection.from_json(json)
# print the JSON string representation of the object
print(ProjectSummaryCollection.to_json())

# convert the object into a dict
project_summary_collection_dict = project_summary_collection_instance.to_dict()
# create an instance of ProjectSummaryCollection from a dict
project_summary_collection_from_dict = ProjectSummaryCollection.from_dict(project_summary_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


