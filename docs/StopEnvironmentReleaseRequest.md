# StopEnvironmentReleaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | [**EnvironmentReleaseResolution**](EnvironmentReleaseResolution.md) |  | 
**comment** | **str** | Optional comment written to the flag&#39;s audit-log entry. | [optional] 

## Example

```python
from launchdarkly_api.models.stop_environment_release_request import StopEnvironmentReleaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopEnvironmentReleaseRequest from a JSON string
stop_environment_release_request_instance = StopEnvironmentReleaseRequest.from_json(json)
# print the JSON string representation of the object
print(StopEnvironmentReleaseRequest.to_json())

# convert the object into a dict
stop_environment_release_request_dict = stop_environment_release_request_instance.to_dict()
# create an instance of StopEnvironmentReleaseRequest from a dict
stop_environment_release_request_from_dict = StopEnvironmentReleaseRequest.from_dict(stop_environment_release_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


