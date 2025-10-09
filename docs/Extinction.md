# Extinction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revision** | **str** | The identifier for the revision where flag became extinct. For example, a commit SHA. | 
**message** | **str** | Description of the extinction. For example, the commit message for the revision. | 
**time** | **int** |  | 
**flag_key** | **str** | The feature flag key | 
**proj_key** | **str** | The project key | 

## Example

```python
from launchdarkly_api.models.extinction import Extinction

# TODO update the JSON string below
json = "{}"
# create an instance of Extinction from a JSON string
extinction_instance = Extinction.from_json(json)
# print the JSON string representation of the object
print(Extinction.to_json())

# convert the object into a dict
extinction_dict = extinction_instance.to_dict()
# create an instance of Extinction from a dict
extinction_from_dict = Extinction.from_dict(extinction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


