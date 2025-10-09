# Destinations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**items** | [**List[Destination]**](Destination.md) | An array of Data Export destinations | [optional] 

## Example

```python
from launchdarkly_api.models.destinations import Destinations

# TODO update the JSON string below
json = "{}"
# create an instance of Destinations from a JSON string
destinations_instance = Destinations.from_json(json)
# print the JSON string representation of the object
print(Destinations.to_json())

# convert the object into a dict
destinations_dict = destinations_instance.to_dict()
# create an instance of Destinations from a dict
destinations_from_dict = Destinations.from_dict(destinations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


