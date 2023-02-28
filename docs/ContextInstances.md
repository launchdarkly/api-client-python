# ContextInstances


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** | The environment ID | 
**items** | [**[ContextInstanceRecord]**](ContextInstanceRecord.md) | A collection of context instances. Can include multiple versions of context instances that have the same &lt;code&gt;id&lt;/code&gt;, but different &lt;code&gt;applicationId&lt;/code&gt;s. | 
**links** | [**{str: (Link,)}**](Link.md) | The location and content type of related resources | [optional] 
**total_count** | **int** | The number of unique context instances | [optional] 
**continuation_token** | **str** | An obfuscated string that references the last context instance on the previous page of results. You can use this for pagination, however, we recommend using the &lt;code&gt;next&lt;/code&gt; link instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


