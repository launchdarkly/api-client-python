# SubscriptionPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for your audit log subscription. | 
**config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The unique set of fields required to configure an audit log subscription integration of this type. Refer to the &lt;code&gt;formVariables&lt;/code&gt; field in the corresponding &lt;code&gt;manifest.json&lt;/code&gt; at https://github.com/launchdarkly/integration-framework/tree/main/integrations for a full list of fields for the integration you wish to configure. | 
**statements** | [**StatementPostList**](StatementPostList.md) |  | [optional] 
**on** | **bool** | Whether or not you want your subscription to actively send events. | [optional] 
**tags** | **[str]** | An array of tags for this subscription. | [optional] 
**url** | **str** | Slack webhook receiver URL. Only necessary for legacy Slack webhook integrations. | [optional] 
**api_key** | **str** | Datadog API key. Only necessary for legacy Datadog webhook integrations. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


