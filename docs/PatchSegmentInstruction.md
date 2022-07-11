# PatchSegmentInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of change to make to the user&#39;s removal date from this segment | 
**user_key** | **str** | A unique key used to represent the user | 
**target_type** | **str** | The segment&#39;s target type | 
**value** | **int** | The time, in Unix milliseconds, when the user should be removed from this segment. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;addExpireUserTargetDate&lt;/code&gt; or &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 
**version** | **int** | The version of the segment to update. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


