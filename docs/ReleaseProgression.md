# ReleaseProgression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | 
**completed_at** | **int** |  | [optional] 
**flag_key** | **str** | The flag key | 
**active_phase_id** | **str** | The ID of the currently active release phase | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 

## Example

```python
from launchdarkly_api.models.release_progression import ReleaseProgression

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseProgression from a JSON string
release_progression_instance = ReleaseProgression.from_json(json)
# print the JSON string representation of the object
print(ReleaseProgression.to_json())

# convert the object into a dict
release_progression_dict = release_progression_instance.to_dict()
# create an instance of ReleaseProgression from a dict
release_progression_from_dict = ReleaseProgression.from_dict(release_progression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


