# UrlPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**substring** | **str** |  | [optional] 
**pattern** | **str** |  | [optional] 

## Example

```python
from launchdarkly_api.models.url_post import UrlPost

# TODO update the JSON string below
json = "{}"
# create an instance of UrlPost from a JSON string
url_post_instance = UrlPost.from_json(json)
# print the JSON string representation of the object
print(UrlPost.to_json())

# convert the object into a dict
url_post_dict = url_post_instance.to_dict()
# create an instance of UrlPost from a dict
url_post_from_dict = UrlPost.from_dict(url_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


