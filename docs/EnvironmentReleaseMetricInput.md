# EnvironmentReleaseMetricInput

A metric to monitor across every phase of a guarded release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_key** | **str** |  | 
**auto_rollback** | **bool** | Whether a regression on this metric automatically reverts the release. When &#x60;false&#x60;, a detected regression pauses the release instead: it reports &#x60;waiting&#x60; with reason &#x60;waiting_regression_detected&#x60; and does not advance until the regression is dismissed or the release is stopped.  | [optional] [default to False]

## Example

```python
from launchdarkly_api.models.environment_release_metric_input import EnvironmentReleaseMetricInput

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseMetricInput from a JSON string
environment_release_metric_input_instance = EnvironmentReleaseMetricInput.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseMetricInput.to_json())

# convert the object into a dict
environment_release_metric_input_dict = environment_release_metric_input_instance.to_dict()
# create an instance of EnvironmentReleaseMetricInput from a dict
environment_release_metric_input_from_dict = EnvironmentReleaseMetricInput.from_dict(environment_release_metric_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


