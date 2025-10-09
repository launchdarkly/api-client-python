# SubscriptionPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for your audit log subscription. | 
**statements** | [**List[StatementPost]**](StatementPost.md) |  | [optional] 
**on** | **bool** | Whether or not you want your subscription to actively send events. | [optional] 
**tags** | **List[str]** | An array of tags for this subscription. | [optional] 
**config** | **Dict[str, object]** | The unique set of fields required to configure an audit log subscription integration of this type. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; at https://github.com/launchdarkly/integration-framework/tree/main/integrations for a full list of fields for the integration you wish to configure. | 
**url** | **str** | Slack webhook receiver URL. Only necessary for legacy Slack webhook integrations. | [optional] 
**api_key** | **str** | Datadog API key. Only necessary for legacy Datadog webhook integrations. | [optional] 

## Example

```python
from launchdarkly_api.models.subscription_post import SubscriptionPost

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPost from a JSON string
subscription_post_instance = SubscriptionPost.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPost.to_json())

# convert the object into a dict
subscription_post_dict = subscription_post_instance.to_dict()
# create an instance of SubscriptionPost from a dict
subscription_post_from_dict = SubscriptionPost.from_dict(subscription_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


