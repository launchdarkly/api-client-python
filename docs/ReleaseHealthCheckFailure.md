# ReleaseHealthCheckFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**ReleaseHealthCheckKind**](ReleaseHealthCheckKind.md) |  | 
**metric_key** | **str** | The metric key associated with a metric event check. | [optional] 
**message** | **str** | A description of the failed health check. | 

## Example

```python
from launchdarkly_api.models.release_health_check_failure import ReleaseHealthCheckFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseHealthCheckFailure from a JSON string
release_health_check_failure_instance = ReleaseHealthCheckFailure.from_json(json)
# print the JSON string representation of the object
print(ReleaseHealthCheckFailure.to_json())

# convert the object into a dict
release_health_check_failure_dict = release_health_check_failure_instance.to_dict()
# create an instance of ReleaseHealthCheckFailure from a dict
release_health_check_failure_from_dict = ReleaseHealthCheckFailure.from_dict(release_health_check_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


