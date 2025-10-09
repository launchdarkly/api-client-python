# RootResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | 

## Example

```python
from launchdarkly_api.models.root_response import RootResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RootResponse from a JSON string
root_response_instance = RootResponse.from_json(json)
# print the JSON string representation of the object
print(RootResponse.to_json())

# convert the object into a dict
root_response_dict = root_response_instance.to_dict()
# create an instance of RootResponse from a dict
root_response_from_dict = RootResponse.from_dict(root_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


