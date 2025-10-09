# OauthClientPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of your new LaunchDarkly OAuth 2.0 client. | [optional] 
**redirect_uri** | **str** | The redirect URI for your new OAuth 2.0 application. This should be an absolute URL conforming with the standard HTTPS protocol. | [optional] 
**description** | **str** | Description of your OAuth 2.0 client. | [optional] 

## Example

```python
from launchdarkly_api.models.oauth_client_post import OauthClientPost

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientPost from a JSON string
oauth_client_post_instance = OauthClientPost.from_json(json)
# print the JSON string representation of the object
print(OauthClientPost.to_json())

# convert the object into a dict
oauth_client_post_dict = oauth_client_post_instance.to_dict()
# create an instance of OauthClientPost from a dict
oauth_client_post_from_dict = OauthClientPost.from_dict(oauth_client_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


