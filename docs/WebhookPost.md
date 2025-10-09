# WebhookPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-readable name for your webhook | [optional] 
**url** | **str** | The URL of the remote webhook | 
**secret** | **str** | If sign is true, and the secret attribute is omitted, LaunchDarkly automatically generates a secret for you. | [optional] 
**statements** | [**List[StatementPost]**](StatementPost.md) |  | [optional] 
**sign** | **bool** | If sign is false, the webhook does not include a signature header, and the secret can be omitted. | 
**on** | **bool** | Whether or not this webhook is enabled. | 
**tags** | **List[str]** | List of tags for this webhook | [optional] 

## Example

```python
from launchdarkly_api.models.webhook_post import WebhookPost

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPost from a JSON string
webhook_post_instance = WebhookPost.from_json(json)
# print the JSON string representation of the object
print(WebhookPost.to_json())

# convert the object into a dict
webhook_post_dict = webhook_post_instance.to_dict()
# create an instance of WebhookPost from a dict
webhook_post_from_dict = WebhookPost.from_dict(webhook_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


