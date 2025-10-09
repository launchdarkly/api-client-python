# ProjectSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this project | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**key** | **str** | The project key | 
**name** | **str** | The project name | 

## Example

```python
from launchdarkly_api.models.project_summary import ProjectSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSummary from a JSON string
project_summary_instance = ProjectSummary.from_json(json)
# print the JSON string representation of the object
print(ProjectSummary.to_json())

# convert the object into a dict
project_summary_dict = project_summary_instance.to_dict()
# create an instance of ProjectSummary from a dict
project_summary_from_dict = ProjectSummary.from_dict(project_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


