# StatementPostData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Whether this statement should allow or deny actions on the resources. | 
**resources** | **[str]** | Resource specifier strings | [optional] 
**not_resources** | **[str]** | Targeted resources are the resources NOT in this list. The &lt;code&gt;resources&lt;/code&gt; field must be empty to use this field. | [optional] 
**actions** | **[str]** | Actions to perform on a resource | [optional] 
**not_actions** | **[str]** | Targeted actions are the actions NOT in this list. The &lt;code&gt;actions&lt;/code&gt; field must be empty to use this field. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


