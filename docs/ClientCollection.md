# ClientCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**items** | [**List[Client]**](Client.md) | List of client objects | 

## Example

```python
from launchdarkly_api.models.client_collection import ClientCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCollection from a JSON string
client_collection_instance = ClientCollection.from_json(json)
# print the JSON string representation of the object
print(ClientCollection.to_json())

# convert the object into a dict
client_collection_dict = client_collection_instance.to_dict()
# create an instance of ClientCollection from a dict
client_collection_from_dict = ClientCollection.from_dict(client_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


