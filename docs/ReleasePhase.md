# ReleasePhase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The phase ID | 
**name** | **str** | The release phase name | 
**complete** | **bool** | Whether this phase is complete | 
**creation_date** | **int** |  | 
**completion_date** | **int** |  | [optional] 
**completed_by** | [**CompletedBy**](CompletedBy.md) |  | [optional] 
**audiences** | [**List[ReleaseAudience]**](ReleaseAudience.md) | A logical grouping of one or more environments that share attributes for rolling out changes | 
**status** | **str** |  | [optional] 
**started** | **bool** | Whether or not this phase has started | [optional] 
**started_date** | **int** |  | [optional] 
**configuration** | **object** |  | [optional] 

## Example

```python
from launchdarkly_api.models.release_phase import ReleasePhase

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasePhase from a JSON string
release_phase_instance = ReleasePhase.from_json(json)
# print the JSON string representation of the object
print(ReleasePhase.to_json())

# convert the object into a dict
release_phase_dict = release_phase_instance.to_dict()
# create an instance of ReleasePhase from a dict
release_phase_from_dict = ReleasePhase.from_dict(release_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


