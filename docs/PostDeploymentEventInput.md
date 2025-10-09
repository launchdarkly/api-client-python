# PostDeploymentEventInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_key** | **str** | The project key | 
**environment_key** | **str** | The environment key | 
**application_key** | **str** | The application key. This defines the granularity at which you want to view your insights metrics. Typically it is the name of one of the GitHub repositories that you use in this project.&lt;br/&gt;&lt;br/&gt;LaunchDarkly automatically creates a new application each time you send a unique application key. | 
**application_name** | **str** | The application name. This defines how the application is displayed | [optional] 
**application_kind** | **str** | The kind of application. Default: &lt;code&gt;server&lt;/code&gt; | [optional] 
**version** | **str** | The application version. You can set the application version to any string that includes only letters, numbers, periods (&lt;code&gt;.&lt;/code&gt;), hyphens (&lt;code&gt;-&lt;/code&gt;), or underscores (&lt;code&gt;_&lt;/code&gt;).&lt;br/&gt;&lt;br/&gt;We recommend setting the application version to at least the first seven characters of the SHA or to the tag of the GitHub commit for this deployment. | 
**version_name** | **str** | The version name. This defines how the version is displayed | [optional] 
**event_type** | **str** | The event type | 
**event_time** | **int** |  | [optional] 
**event_metadata** | **Dict[str, object]** | A JSON object containing metadata about the event | [optional] 
**deployment_metadata** | **Dict[str, object]** | A JSON object containing metadata about the deployment | [optional] 

## Example

```python
from launchdarkly_api.models.post_deployment_event_input import PostDeploymentEventInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostDeploymentEventInput from a JSON string
post_deployment_event_input_instance = PostDeploymentEventInput.from_json(json)
# print the JSON string representation of the object
print(PostDeploymentEventInput.to_json())

# convert the object into a dict
post_deployment_event_input_dict = post_deployment_event_input_instance.to_dict()
# create an instance of PostDeploymentEventInput from a dict
post_deployment_event_input_from_dict = PostDeploymentEventInput.from_dict(post_deployment_event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


