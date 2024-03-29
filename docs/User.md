# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The user key. This is the only mandatory user attribute. | [optional] 
**secondary** | **str** | If provided, used with the user key to generate a variation in percentage rollouts | [optional] 
**ip** | **str** | The user&#39;s IP address | [optional] 
**country** | **str** | The user&#39;s country | [optional] 
**email** | **str** | The user&#39;s email | [optional] 
**first_name** | **str** | The user&#39;s first name | [optional] 
**last_name** | **str** | The user&#39;s last name | [optional] 
**avatar** | **str** | An absolute URL to an avatar image. | [optional] 
**name** | **str** | The user&#39;s full name | [optional] 
**anonymous** | **bool** | Whether the user is anonymous. If true, this user does not appear on the Contexts list in the LaunchDarkly user interface. | [optional] 
**custom** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Any other custom attributes for this user. Custom attributes contain any other user data that you would like to use to conditionally target your users. | [optional] 
**private_attrs** | **[str]** | A list of attribute names that are marked as private. You can use these attributes in targeting rules and segments. If you are using a server-side SDK, the SDK will not send the private attribute back to LaunchDarkly. If you are using a client-side SDK, the SDK will send the private attribute back to LaunchDarkly for evaluation. However, the SDK won&#39;t send the attribute to LaunchDarkly in events data, LaunchDarkly won&#39;t store the private attribute, and the private attribute will not appear on the Contexts list. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


