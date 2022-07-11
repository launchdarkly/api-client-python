# FlagLinkPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The flag link key | [optional] 
**integration_key** | **str** | The integration key for an integration whose &lt;code&gt;manifest.json&lt;/code&gt; includes the &lt;code&gt;flagLink&lt;/code&gt; capability, if this is a flag link for an existing integration. Do not include for URL flag links. | [optional] 
**timestamp** | **int** |  | [optional] 
**deep_link** | **str** | The URL for the external resource you are linking the flag to | [optional] 
**title** | **str** | The title of the flag link | [optional] 
**description** | **str** | The description of the flag link | [optional] 
**metadata** | **{str: (str,)}** | The metadata required by this integration in order to create a flag link, if this is a flag link for an existing integration. Defined in the integration&#39;s &lt;code&gt;manifest.json&lt;/code&gt; file under &lt;code&gt;flagLink&lt;/code&gt;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


