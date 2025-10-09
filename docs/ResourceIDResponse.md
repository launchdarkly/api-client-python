# ResourceIDResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**project_key** | **str** |  | [optional] 
**environment_key** | **str** |  | [optional] 
**flag_key** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.resource_id_response import ResourceIDResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceIDResponse from a JSON string
resource_id_response_instance = ResourceIDResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceIDResponse.to_json())

# convert the object into a dict
resource_id_response_dict = resource_id_response_instance.to_dict()
# create an instance of ResourceIDResponse from a dict
resource_id_response_from_dict = ResourceIDResponse.from_dict(resource_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


