# SegmentBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the segment | 
**key** | **str** | A unique key used to reference the segment | 
**description** | **str** | A description of the segment&#39;s purpose | [optional] 
**tags** | **[str]** | Tags for the segment | [optional] 
**unbounded** | **bool** | Whether to create a standard segment (&lt;code&gt;false&lt;/code&gt;) or a big segment (&lt;code&gt;true&lt;/code&gt;). Standard segments include rule-based and smaller list-based segments. Big segments include larger list-based segments and synced segments. Only use a big segment if you need to add more than 15,000 individual targets. | [optional] 
**unbounded_context_kind** | **str** | For big segments, the targeted context kind. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


