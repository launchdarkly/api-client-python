# EnvironmentReleaseStepInput

One step of a phase's rollout schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | **int** | Thousandths of a percent. &#x60;100000&#x60; is 100%, and &#x60;10000&#x60; is 10%. Guarded releases cannot exceed &#x60;50000&#x60;, preserving a control group. Each step&#39;s allocation must be greater than the previous step&#39;s.  In a progressive release, an allocation of N% serves the target variation to N% of the phase&#39;s contexts and the original variation to the rest. In a guarded release, it serves the target variation to N%, the original variation to another N% as the measured control group, and the original variation to the rest without measuring them.  | 
**duration_millis** | **int** |  | 

## Example

```python
from launchdarkly_api.models.environment_release_step_input import EnvironmentReleaseStepInput

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleaseStepInput from a JSON string
environment_release_step_input_instance = EnvironmentReleaseStepInput.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleaseStepInput.to_json())

# convert the object into a dict
environment_release_step_input_dict = environment_release_step_input_instance.to_dict()
# create an instance of EnvironmentReleaseStepInput from a dict
environment_release_step_input_from_dict = EnvironmentReleaseStepInput.from_dict(environment_release_step_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


