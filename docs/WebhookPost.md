# WebhookPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the remote webhook | 
**sign** | **bool** | If sign is false, the webhook does not include a signature header, and the secret can be omitted. | 
**on** | **bool** | Whether or not this webhook is enabled. | 
**name** | **str** | A human-readable name for your webhook | [optional] 
**secret** | **str** | If sign is true, and the secret attribute is omitted, LaunchDarkly automatically generates a secret for you. | [optional] 
**statements** | [**StatementPostList**](StatementPostList.md) |  | [optional] 
**tags** | **[str]** | List of tags for this webhook | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


