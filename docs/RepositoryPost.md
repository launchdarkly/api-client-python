# RepositoryPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The repository name | 
**source_link** | **str** | A URL to access the repository | [optional] 
**commit_url_template** | **str** | A template for constructing a valid URL to view the commit | [optional] 
**hunk_url_template** | **str** | A template for constructing a valid URL to view the hunk | [optional] 
**type** | **str** | The type of repository. If not specified, the default value is &lt;code&gt;custom&lt;/code&gt;. | [optional] 
**default_branch** | **str** | The repository&#39;s default branch. If not specified, the default value is &lt;code&gt;main&lt;/code&gt;. | [optional] 

## Example

```python
from launchdarkly_api.models.repository_post import RepositoryPost

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryPost from a JSON string
repository_post_instance = RepositoryPost.from_json(json)
# print the JSON string representation of the object
print(RepositoryPost.to_json())

# convert the object into a dict
repository_post_dict = repository_post_instance.to_dict()
# create an instance of RepositoryPost from a dict
repository_post_from_dict = RepositoryPost.from_dict(repository_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


