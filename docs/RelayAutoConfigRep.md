# RelayAutoConfigRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | A human-friendly name for the Relay Proxy configuration | 
**policy** | [**[Statement]**](Statement.md) | A description of what environments and projects the Relay Proxy should include or exclude | 
**full_key** | **str** | The Relay Proxy configuration key | 
**display_key** | **str** | The last few characters of the Relay Proxy configuration key, displayed in the LaunchDarkly UI | 
**creation_date** | **int** |  | 
**last_modified** | **int** |  | 
**creator** | [**MemberSummary**](MemberSummary.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


