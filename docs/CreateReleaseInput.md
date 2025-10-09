# CreateReleaseInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_variation_id** | **str** | The variation id to release to across all phases | [optional] 
**release_pipeline_key** | **str** | The key of the release pipeline to attach the flag to | 

## Example

```python
from launchdarkly_api.models.create_release_input import CreateReleaseInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReleaseInput from a JSON string
create_release_input_instance = CreateReleaseInput.from_json(json)
# print the JSON string representation of the object
print(CreateReleaseInput.to_json())

# convert the object into a dict
create_release_input_dict = create_release_input_instance.to_dict()
# create an instance of CreateReleaseInput from a dict
create_release_input_from_dict = CreateReleaseInput.from_dict(create_release_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


