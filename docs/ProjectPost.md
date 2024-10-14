# ProjectPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A human-friendly name for the project. | 
**key** | **str** | A unique key used to reference the project in your code. | 
**include_in_snippet_by_default** | **bool** | Whether or not flags created in this project are made available to the client-side JavaScript SDK by default. | [optional] 
**default_client_side_availability** | [**DefaultClientSideAvailabilityPost**](DefaultClientSideAvailabilityPost.md) |  | [optional] 
**tags** | **[str]** | Tags for the project | [optional] 
**environments** | [**[EnvironmentPost]**](EnvironmentPost.md) | Creates the provided environments for this project. If omitted default environments will be created instead. | [optional] 
**naming_convention** | [**NamingConvention**](NamingConvention.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


