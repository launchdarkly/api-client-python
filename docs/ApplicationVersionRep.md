# ApplicationVersionRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**Access**](Access.md) |  | [optional] 
**links** | [**Dict[str, Link]**](Link.md) | The location and content type of related resources | [optional] 
**version** | **int** | Version of the application version | [optional] 
**auto_added** | **bool** | Whether the application version was automatically created, because it was included in a context when a LaunchDarkly SDK evaluated a feature flag, or if the application version was created through the LaunchDarkly UI or REST API.  | 
**creation_date** | **int** |  | [optional] 
**key** | **str** | The unique identifier of this application version | 
**name** | **str** | The name of this version | 
**supported** | **bool** | Whether this version is supported. Only applicable if the application &lt;code&gt;kind&lt;/code&gt; is &lt;code&gt;mobile&lt;/code&gt;. | [optional] 

## Example

```python
from launchdarkly_api.models.application_version_rep import ApplicationVersionRep

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVersionRep from a JSON string
application_version_rep_instance = ApplicationVersionRep.from_json(json)
# print the JSON string representation of the object
print(ApplicationVersionRep.to_json())

# convert the object into a dict
application_version_rep_dict = application_version_rep_instance.to_dict()
# create an instance of ApplicationVersionRep from a dict
application_version_rep_from_dict = ApplicationVersionRep.from_dict(application_version_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


