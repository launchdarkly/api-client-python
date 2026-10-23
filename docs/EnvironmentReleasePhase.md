# EnvironmentReleasePhase

One ordered phase of an environment release.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**phase_index** | **int** | Zero-based index of this phase. | [readonly] 
**rule_id** | **str** | ID of the flag rule for this phase. New public-API releases always have a rule ID. &#x60;null&#x60; is retained only when reading a historical release that ran on the default rule.  | 
**description** | **str** | The description of the flag rule when this release was created. Omitted for default-rule phases.  | [optional] [readonly] 
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**status_reason** | [**ReleaseStatusReason**](ReleaseStatusReason.md) |  | [optional] 
**steps** | [**List[ReleaseStep]**](ReleaseStep.md) |  | 
**current_step_index** | **int** | Zero-based index of the step the phase is on. Omitted until the first step starts. Once the phase completes or reverts, it stays at the last step that started, unlike &#x60;currentPhaseIndex&#x60;, which becomes &#x60;null&#x60; when the release reaches a terminal status.  | [optional] [readonly] 
**started_at** | **int** | Start of the phase in Unix milliseconds. | [optional] [readonly] 
**ended_at** | **int** | End of the phase in Unix milliseconds. | [optional] [readonly] 
**metric_statuses** | [**Dict[str, ReleaseMetricStatus]**](ReleaseMetricStatus.md) | Per-phase metric status keyed by metric key. Empty for progressive releases. Metric definitions and monitoring preferences live once in the parent release&#39;s &#x60;metrics&#x60; array.  | [readonly] 

## Example

```python
from launchdarkly_api.models.environment_release_phase import EnvironmentReleasePhase

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentReleasePhase from a JSON string
environment_release_phase_instance = EnvironmentReleasePhase.from_json(json)
# print the JSON string representation of the object
print(EnvironmentReleasePhase.to_json())

# convert the object into a dict
environment_release_phase_dict = environment_release_phase_instance.to_dict()
# create an instance of EnvironmentReleasePhase from a dict
environment_release_phase_from_dict = EnvironmentReleasePhase.from_dict(environment_release_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


