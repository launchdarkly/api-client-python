# Webhooks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**items** | [**List[Webhook]**](Webhook.md) | An array of webhooks | 

## Example

```python
from launchdarkly_api.models.webhooks import Webhooks

# TODO update the JSON string below
json = "{}"
# create an instance of Webhooks from a JSON string
webhooks_instance = Webhooks.from_json(json)
# print the JSON string representation of the object
print(Webhooks.to_json())

# convert the object into a dict
webhooks_dict = webhooks_instance.to_dict()
# create an instance of Webhooks from a dict
webhooks_from_dict = Webhooks.from_dict(webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


