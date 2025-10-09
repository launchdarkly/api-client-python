# ProjectPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the project. | 
**key** | **str** | A unique key used to reference the project in your code. | 
**include_in_snippet_by_default** | **bool** | Whether or not flags created in this project are made available to the client-side JavaScript SDK by default. | [optional] 
**default_client_side_availability** | [**DefaultClientSideAvailabilityPost**](DefaultClientSideAvailabilityPost.md) |  | [optional] 
**tags** | **List[str]** | Tags for the project | [optional] 
**environments** | [**List[EnvironmentPost]**](EnvironmentPost.md) | Creates the provided environments for this project. If omitted default environments will be created instead. | [optional] 
**naming_convention** | [**NamingConvention**](NamingConvention.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.project_post import ProjectPost

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPost from a JSON string
project_post_instance = ProjectPost.from_json(json)
# print the JSON string representation of the object
print(ProjectPost.to_json())

# convert the object into a dict
project_post_dict = project_post_instance.to_dict()
# create an instance of ProjectPost from a dict
project_post_from_dict = ProjectPost.from_dict(project_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


