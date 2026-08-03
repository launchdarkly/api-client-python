# ContextKindEnvironmentObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_key** | **str** | The environment key | 
**last_seen** | **int** |  | 

## Example

```python
from launchdarkly_api.models.context_kind_environment_observation import ContextKindEnvironmentObservation

# TODO update the JSON string below
json = "{}"
# create an instance of ContextKindEnvironmentObservation from a JSON string
context_kind_environment_observation_instance = ContextKindEnvironmentObservation.from_json(json)
# print the JSON string representation of the object
print(ContextKindEnvironmentObservation.to_json())

# convert the object into a dict
context_kind_environment_observation_dict = context_kind_environment_observation_instance.to_dict()
# create an instance of ContextKindEnvironmentObservation from a dict
context_kind_environment_observation_from_dict = ContextKindEnvironmentObservation.from_dict(context_kind_environment_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


