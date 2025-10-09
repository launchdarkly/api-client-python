# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | 
**id** | **str** | The ID of this webhook | 
**name** | **str** | A human-readable name for this webhook | [optional] 
**url** | **str** | The URL to which LaunchDarkly sends an HTTP POST payload for this webhook | 
**secret** | **str** | The secret for this webhook | [optional] 
**statements** | [**List[Statement]**](Statement.md) | Represents a Custom role policy, defining a resource kinds filter the webhook responds to. | [optional] 
**on** | **bool** | Whether or not this webhook is enabled | 
**tags** | **List[str]** | List of tags for this webhook | 
**access** | [**Access**](Access.md) |  | [optional] 

## Example

```python
from launchdarkly_api.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


