# EnvironmentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**key** | **str** | A project-unique key for the environment | 
**name** | **str** | A human-friendly name for the environment | 
**color** | **str** | The color used to indicate this environment in the UI | 

## Example

```python
from launchdarkly_api.models.environment_summary import EnvironmentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentSummary from a JSON string
environment_summary_instance = EnvironmentSummary.from_json(json)
# print the JSON string representation of the object
print(EnvironmentSummary.to_json())

# convert the object into a dict
environment_summary_dict = environment_summary_instance.to_dict()
# create an instance of EnvironmentSummary from a dict
environment_summary_from_dict = EnvironmentSummary.from_dict(environment_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


