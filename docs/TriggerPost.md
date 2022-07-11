# TriggerPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_key** | **str** | The unique identifier of the integration for your trigger. Use &lt;code&gt;generic-trigger&lt;/code&gt; for integrations not explicitly supported. | 
**comment** | **str** | Optional comment describing the trigger | [optional] 
**instructions** | [**[Instruction]**](Instruction.md) | The action to perform when triggering. This should be an array with a single object that looks like &lt;code&gt;{\&quot;kind\&quot;: \&quot;flag_action\&quot;}&lt;/code&gt;. Supported flag actions are &lt;code&gt;turnFlagOn&lt;/code&gt; and &lt;code&gt;turnFlagOff&lt;/code&gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


