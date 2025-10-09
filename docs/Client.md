# Client


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**name** | **str** | Client name | 
**description** | **str** | Client description | [optional] 
**account_id** | **str** | The account ID the client is registered under | 
**client_id** | **str** | The client&#39;s unique ID | 
**client_secret** | **str** | The client secret. This will only be shown upon creation. | [optional] 
**redirect_uri** | **str** | The client&#39;s redirect URI | 
**creation_date** | **int** |  | 

## Example

```python
from launchdarkly_api.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print(Client.to_json())

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_from_dict = Client.from_dict(client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


