# ValuePut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setting** | **object** | The variation value to set for the context. Must match the flag&#39;s variation type. | [optional] 
**comment** | **str** | Optional comment describing the change | [optional] 

## Example

```python
from launchdarkly_api.models.value_put import ValuePut

# TODO update the JSON string below
json = "{}"
# create an instance of ValuePut from a JSON string
value_put_instance = ValuePut.from_json(json)
# print the JSON string representation of the object
print(ValuePut.to_json())

# convert the object into a dict
value_put_dict = value_put_instance.to_dict()
# create an instance of ValuePut from a dict
value_put_from_dict = ValuePut.from_dict(value_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


