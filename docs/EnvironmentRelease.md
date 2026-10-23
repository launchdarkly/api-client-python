# EnvironmentRelease

A flag release in one environment, made up of one or more ordered phases. The top-level status is derived from the phases: it reflects the active phase, reports `waiting` between successfully completed phases, and reports the terminal outcome of the release. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**status_reason** | [**ReleaseStatusReason**](ReleaseStatusReason.md) |  | [optional] 
**project_key** | **str** |  | 
**environment_key** | **str** |  | 
**flag_key** | **str** |  | 
**original_variation_id** | **UUID** | ID of the variation the release started from. | 
**original_variation_value** | **object** | The value of the variation. This may be a string, boolean, number, JSON object, or array. | 
**target_variation_id** | **UUID** | ID of the variation being released. | 
**target_variation_value** | **object** | The value of the variation. This may be a string, boolean, number, JSON object, or array. | 
**randomization_unit** | **str** | Key of the context kind the release randomizes on. | 
**cleanup_behavior** | [**CleanupBehavior**](CleanupBehavior.md) |  | 
**kind** | [**ReleaseType**](ReleaseType.md) |  | 
**metrics** | [**List[ReleaseMetric]**](ReleaseMetric.md) |  | 
**phases** | [**List[EnvironmentReleasePhase]**](EnvironmentReleasePhase.md) |  | 
**current_phase_index** | **int** | Zero-based index of the active phase. Null before the first phase, between phases, and after the release reaches a terminal status. | 
**advancement_mode** | [**EnvironmentReleaseAdvancementMode**](EnvironmentReleaseAdvancementMode.md) |  | 
**created_at** | **int** | Creation time in Unix milliseconds. | 
**started_at** | **int** | Start of the first phase in Unix milliseconds. Absent until a phase has started. | [optional] [readonly] 
**ended_at** | **int** | End of the last started phase in Unix milliseconds. Present only after the release reaches a terminal status of &#x60;completed&#x60; or &#x60;reverted&#x60;. | [optional] [readonly] 
**links** | [**Dict[str, EnvironmentReleaseLink]**](EnvironmentReleaseLink.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.environment_release import EnvironmentRelease

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentRelease from a JSON string
environment_release_instance = EnvironmentRelease.from_json(json)
# print the JSON string representation of the object
print(EnvironmentRelease.to_json())

# convert the object into a dict
environment_release_dict = environment_release_instance.to_dict()
# create an instance of EnvironmentRelease from a dict
environment_release_from_dict = EnvironmentRelease.from_dict(environment_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


