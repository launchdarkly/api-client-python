# VersionsRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_versions** | **List[int]** | A list of all valid API versions. To learn more about our versioning, read [Versioning](https://launchdarkly.com/docs/api#versioning). | 
**latest_version** | **int** |  | 
**current_version** | **int** |  | 
**beta** | **bool** | Whether the version of the API currently is use is a beta version. This is always &lt;code&gt;true&lt;/code&gt; if you add the &lt;code&gt;LD-API-Version: beta&lt;/code&gt; header to your request. | [optional] 

## Example

```python
from launchdarkly_api.models.versions_rep import VersionsRep

# TODO update the JSON string below
json = "{}"
# create an instance of VersionsRep from a JSON string
versions_rep_instance = VersionsRep.from_json(json)
# print the JSON string representation of the object
print(VersionsRep.to_json())

# convert the object into a dict
versions_rep_dict = versions_rep_instance.to_dict()
# create an instance of VersionsRep from a dict
versions_rep_from_dict = VersionsRep.from_dict(versions_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


