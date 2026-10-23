# ObservabilityAlertSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**alert_id** | **int** |  | 

## Example

```python
from launchdarkly_api.models.observability_alert_source import ObservabilityAlertSource

# TODO update the JSON string below
json = "{}"
# create an instance of ObservabilityAlertSource from a JSON string
observability_alert_source_instance = ObservabilityAlertSource.from_json(json)
# print the JSON string representation of the object
print(ObservabilityAlertSource.to_json())

# convert the object into a dict
observability_alert_source_dict = observability_alert_source_instance.to_dict()
# create an instance of ObservabilityAlertSource from a dict
observability_alert_source_from_dict = ObservabilityAlertSource.from_dict(observability_alert_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


