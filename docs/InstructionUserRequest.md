# InstructionUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The type of change to make to the removal date for this user from individual targeting for this flag. | 
**flag_key** | **str** | The flag key | 
**variation_id** | **str** | ID of a variation on the flag | 
**value** | **int** | The time, in Unix milliseconds, when LaunchDarkly should remove the user from individual targeting for this flag. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;addExpireUserTargetDate&lt;/code&gt; or &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 
**version** | **int** | The version of the flag variation to update. You can retrieve this by making a GET request for the flag. Required if &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;updateExpireUserTargetDate&lt;/code&gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


