# ReleaseStep

One step in a phase's rollout schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_index** | **int** | Zero-based index of this step. | [readonly] 
**allocation** | **int** | Thousandths of a percent. &#x60;100000&#x60; is 100%, and &#x60;10000&#x60; is 10%. Guarded releases cannot exceed &#x60;50000&#x60;, preserving a control group.  | 
**duration_millis** | **int** |  | 
**started_at** | **int** | Start of the step in Unix milliseconds. | [optional] [readonly] 
**ended_at** | **int** | End of the step in Unix milliseconds. | [optional] [readonly] 

## Example

```python
from launchdarkly_api.models.release_step import ReleaseStep

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseStep from a JSON string
release_step_instance = ReleaseStep.from_json(json)
# print the JSON string representation of the object
print(ReleaseStep.to_json())

# convert the object into a dict
release_step_dict = release_step_instance.to_dict()
# create an instance of ReleaseStep from a dict
release_step_from_dict = ReleaseStep.from_dict(release_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


