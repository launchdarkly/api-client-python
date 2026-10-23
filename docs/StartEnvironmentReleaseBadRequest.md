# StartEnvironmentReleaseBadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**failing_checks** | [**List[ReleaseHealthCheckFailure]**](ReleaseHealthCheckFailure.md) | Present when &#x60;code&#x60; is &#x60;health_checks_failed&#x60;. | [optional] 

## Example

```python
from launchdarkly_api.models.start_environment_release_bad_request import StartEnvironmentReleaseBadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartEnvironmentReleaseBadRequest from a JSON string
start_environment_release_bad_request_instance = StartEnvironmentReleaseBadRequest.from_json(json)
# print the JSON string representation of the object
print(StartEnvironmentReleaseBadRequest.to_json())

# convert the object into a dict
start_environment_release_bad_request_dict = start_environment_release_bad_request_instance.to_dict()
# create an instance of StartEnvironmentReleaseBadRequest from a dict
start_environment_release_bad_request_from_dict = StartEnvironmentReleaseBadRequest.from_dict(start_environment_release_bad_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


