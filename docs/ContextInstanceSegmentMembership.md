# ContextInstanceSegmentMembership


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the segment | 
**key** | **str** | A unique key used to reference the segment | 
**description** | **str** | A description of the segment&#39;s purpose | 
**unbounded** | **bool** | Whether this is an unbounded/big segment | 
**external** | **str** | If the segment is a Synced Segment the name of the external source&#39; | 
**is_member** | **bool** | Whether the context is a member of this segment, either by explicit inclusion or by rule matching | 
**is_individually_targeted** | **bool** | Whether the context is explicitly included in this segment | 
**is_rule_targeted** | **bool** | Whether the context is captured by this segment&#39;s rules. The value of this field is undefined if the context is also explicitly included (isIndividuallyTargeted &#x3D; true). | 
**links** | [**{str: (Link,)}**](Link.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


