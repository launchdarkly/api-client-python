# TriggerPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_key** | **str** | The unique identifier of the integration you intend to set your trigger up with. \&quot;generic-trigger\&quot; should be used for integrations not explicitly supported. | 
**comment** | **str** |  | [optional] 
**instructions** | [**[Instruction]**](Instruction.md) | The action to perform when triggering. It should pass an array with a single {\&quot;kind\&quot;: &lt;flag_action&gt;} object. Currently supported flag actions are \&quot;turnFlagOn\&quot; and \&quot;turnFlagOff\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


