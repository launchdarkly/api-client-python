# Projects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A link to this resource. | 
**items** | [**List[Project]**](Project.md) | List of projects. | 
**total_count** | **int** |  | [optional] 

## Example

```python
from launchdarkly_api.models.projects import Projects

# TODO update the JSON string below
json = "{}"
# create an instance of Projects from a JSON string
projects_instance = Projects.from_json(json)
# print the JSON string representation of the object
print(Projects.to_json())

# convert the object into a dict
projects_dict = projects_instance.to_dict()
# create an instance of Projects from a dict
projects_from_dict = Projects.from_dict(projects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


