# FlagInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The ID of the variation or rollout of the flag to use. Use \&quot;fallthrough\&quot; for the default targeting behavior when the flag is on. | 
**flag_config_version** | **int** | The flag version | 
**not_in_experiment_variation_id** | **str** | The ID of the variation to route traffic not part of the experiment analysis to. Defaults to variation ID of baseline treatment, if set. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


