# MemberImportItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | An error message, including CSV line number, if the &lt;code&gt;status&lt;/code&gt; is &lt;code&gt;error&lt;/code&gt; | [optional] 
**status** | **str** | Whether this member can be successfully imported (&lt;code&gt;success&lt;/code&gt;) or not (&lt;code&gt;error&lt;/code&gt;). Even if the status is &lt;code&gt;success&lt;/code&gt;, members are only added to a team on a &lt;code&gt;201&lt;/code&gt; response. | 
**value** | **str** | The email address for the member requested to be added to this team. May be blank or an error, such as &#39;invalid email format&#39;, if the email address cannot be found or parsed. | 

## Example

```python
from launchdarkly_api.models.member_import_item import MemberImportItem

# TODO update the JSON string below
json = "{}"
# create an instance of MemberImportItem from a JSON string
member_import_item_instance = MemberImportItem.from_json(json)
# print the JSON string representation of the object
print(MemberImportItem.to_json())

# convert the object into a dict
member_import_item_dict = member_import_item_instance.to_dict()
# create an instance of MemberImportItem from a dict
member_import_item_from_dict = MemberImportItem.from_dict(member_import_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


