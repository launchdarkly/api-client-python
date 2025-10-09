# ProjectRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The ID of this project | 
**key** | **str** | The key of this project | 
**include_in_snippet_by_default** | **bool** | Whether or not flags created in this project are made available to the client-side JavaScript SDK by default | 
**default_client_side_availability** | [**ClientSideAvailability**](ClientSideAvailability.md) |  | [optional] 
**name** | **str** | A human-friendly name for the project | 
**access** | [**Access**](Access.md) |  | [optional] 
**tags** | **List[str]** | A list of tags for the project | 
**default_release_pipeline_key** | **str** | The key of the default release pipeline for this project | [optional] 
**environments** | [**List[Environment]**](Environment.md) | A list of environments for the project | 

## Example

```python
from launchdarkly_api.models.project_rep import ProjectRep

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRep from a JSON string
project_rep_instance = ProjectRep.from_json(json)
# print the JSON string representation of the object
print(ProjectRep.to_json())

# convert the object into a dict
project_rep_dict = project_rep_instance.to_dict()
# create an instance of ProjectRep from a dict
project_rep_from_dict = ProjectRep.from_dict(project_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


