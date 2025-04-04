# ModelConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human readable name of the model | 
**key** | **str** | Unique key for the model | 
**id** | **str** | Identifier for the model, for use with third party providers | 
**_global** | **bool** | Whether the model is global | 
**tags** | **[str]** |  | 
**version** | **int** |  | 
**access** | [**AiConfigsAccess**](AiConfigsAccess.md) |  | [optional] 
**icon** | **str** | Icon for the model | [optional] 
**provider** | **str** | Provider for the model | [optional] 
**params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**custom_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**cost_per_input_token** | **float** | Cost per input token in USD | [optional] 
**cost_per_output_token** | **float** | Cost per output token in USD | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


