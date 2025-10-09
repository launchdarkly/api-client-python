# Environments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The number of environments returned | [optional] 
**items** | [**List[Environment]**](Environment.md) | An array of environments | 

## Example

```python
from launchdarkly_api.models.environments import Environments

# TODO update the JSON string below
json = "{}"
# create an instance of Environments from a JSON string
environments_instance = Environments.from_json(json)
# print the JSON string representation of the object
print(Environments.to_json())

# convert the object into a dict
environments_dict = environments_instance.to_dict()
# create an instance of Environments from a dict
environments_from_dict = Environments.from_dict(environments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


