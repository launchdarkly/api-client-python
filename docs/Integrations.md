# Integrations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) |  | [optional] 
**items** | [**List[Integration]**](Integration.md) |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.integrations import Integrations

# TODO update the JSON string below
json = "{}"
# create an instance of Integrations from a JSON string
integrations_instance = Integrations.from_json(json)
# print the JSON string representation of the object
print(Integrations.to_json())

# convert the object into a dict
integrations_dict = integrations_instance.to_dict()
# create an instance of Integrations from a dict
integrations_from_dict = Integrations.from_dict(integrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


