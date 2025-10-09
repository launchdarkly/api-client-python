# StatementPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **List[str]** | Resource specifier strings | [optional] 
**not_resources** | **List[str]** | Targeted resources are the resources NOT in this list. The &lt;code&gt;resources&lt;/code&gt; field must be empty to use this field. | [optional] 
**actions** | **List[str]** | Actions to perform on a resource | [optional] 
**not_actions** | **List[str]** | Targeted actions are the actions NOT in this list. The &lt;code&gt;actions&lt;/code&gt; field must be empty to use this field. | [optional] 
**effect** | **str** | Whether this statement should allow or deny actions on the resources. | 

## Example

```python
from launchdarkly_api.models.statement_post import StatementPost

# TODO update the JSON string below
json = "{}"
# create an instance of StatementPost from a JSON string
statement_post_instance = StatementPost.from_json(json)
# print the JSON string representation of the object
print(StatementPost.to_json())

# convert the object into a dict
statement_post_dict = statement_post_instance.to_dict()
# create an instance of StatementPost from a dict
statement_post_from_dict = StatementPost.from_dict(statement_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


