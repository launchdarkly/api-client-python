# PatchSegmentInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**user_key** | **str** | A unique key used to represent the user | 
**target_type** | **str** | A segment&#39;s target type. Must be either &lt;code&gt;included&lt;/code&gt; or &lt;code&gt;excluded&lt;/code&gt; | 
**value** | **int** | Schedule user target expiration on a segment by including a timestamp | [optional] 
**version** | **int** | Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


