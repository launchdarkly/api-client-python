# ResourceId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_key** | **str** | The environment key | [optional] 
**flag_key** | **str** | Deprecated, use &lt;code&gt;key&lt;/code&gt; instead | [optional] 
**key** | **str** | The key of the flag or segment | [optional] 
**kind** | **str** |  | [optional] 
**project_key** | **str** | The project key | [optional] 

## Example

```python
from launchdarkly_api.models.resource_id import ResourceId

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceId from a JSON string
resource_id_instance = ResourceId.from_json(json)
# print the JSON string representation of the object
print(ResourceId.to_json())

# convert the object into a dict
resource_id_dict = resource_id_instance.to_dict()
# create an instance of ResourceId from a dict
resource_id_from_dict = ResourceId.from_dict(resource_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


