# SdkVersionDetailsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**project_key** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**environment_key** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**ld_latest_version** | **str** |  | [optional] 
**eol_status** | **str** | The end of life (EOL) status of the SDK version. Possible values are: &lt;br/&gt;- &lt;code&gt;EolAllClear&lt;/code&gt;: the SDK version is current&lt;br/&gt;- &lt;code&gt;EolNear&lt;/code&gt;: the SDK version is approaching EOL&lt;br/&gt;- &lt;code&gt;EolPast&lt;/code&gt;: the SDK version is past EOL&lt;br/&gt;- &lt;code&gt;MajorVersionAvailable&lt;/code&gt;: a new major version is available but the current version is not near EOL&lt;br/&gt;- &lt;code&gt;EolUnknown&lt;/code&gt;: the EOL status cannot be determined. | [optional] 
**latest_release_url** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**relay_version** | **str** |  | [optional] 
**relay_eol_status** | **str** | The end of life status of the Relay Proxy version. Only present when the SDK connects through a Relay Proxy. Uses the same values as &lt;code&gt;eolStatus&lt;/code&gt;. | [optional] 
**relay_latest_version** | **str** |  | [optional] 
**relay_latest_release_url** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.sdk_version_details_rep import SdkVersionDetailsRep

# TODO update the JSON string below
json = "{}"
# create an instance of SdkVersionDetailsRep from a JSON string
sdk_version_details_rep_instance = SdkVersionDetailsRep.from_json(json)
# print the JSON string representation of the object
print(SdkVersionDetailsRep.to_json())

# convert the object into a dict
sdk_version_details_rep_dict = sdk_version_details_rep_instance.to_dict()
# create an instance of SdkVersionDetailsRep from a dict
sdk_version_details_rep_from_dict = SdkVersionDetailsRep.from_dict(sdk_version_details_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


