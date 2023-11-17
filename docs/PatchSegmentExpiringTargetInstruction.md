# PatchSegmentExpiringTargetInstruction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of change to make to the context&#39;s removal date from this segment | 
**context_key** | **str** | A unique key used to represent the context | 
**context_kind** | **str** | The kind of context | 
**target_type** | **str** | The segment&#39;s target type | 
**value** | **int** | The time, in Unix milliseconds, when the context should be removed from this segment. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;addExpiringTarget&lt;/code&gt; or &lt;code&gt;updateExpiringTarget&lt;/code&gt;. | [optional] 
**version** | **int** | The version of the expiring target to update. Optional and only used if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpiringTarget&lt;/code&gt;. If included, update will fail if version doesn&#39;t match current version of the expiring target. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


