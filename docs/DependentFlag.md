# DependentFlag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The flag name | [optional] 
**key** | **str** | The flag key | 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**site** | [**Link**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.dependent_flag import DependentFlag

# TODO update the JSON string below
json = "{}"
# create an instance of DependentFlag from a JSON string
dependent_flag_instance = DependentFlag.from_json(json)
# print the JSON string representation of the object
print(DependentFlag.to_json())

# convert the object into a dict
dependent_flag_dict = dependent_flag_instance.to_dict()
# create an instance of DependentFlag from a dict
dependent_flag_from_dict = DependentFlag.from_dict(dependent_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


