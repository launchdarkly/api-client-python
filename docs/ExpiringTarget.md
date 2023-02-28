# ExpiringTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of this expiring target | 
**version** | **int** | The version of this expiring target | 
**expiration_date** | **int** |  | 
**context_kind** | **str** | The context kind of the context to be removed | 
**context_key** | **str** | A unique key used to represent the context to be removed | 
**resource_id** | [**ResourceId**](ResourceId.md) |  | 
**target_type** | **str** | A segment&#39;s target type, &lt;code&gt;included&lt;/code&gt; or &lt;code&gt;excluded&lt;/code&gt;. Included when expiring targets are updated on a segment. | [optional] 
**variation_id** | **str** | A unique ID used to represent the flag variation. Included when expiring targets are updated on a feature flag. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


