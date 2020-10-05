# launchdarkly_api.AccessTokensApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](AccessTokensApi.md#delete_token) | **DELETE** /tokens/{tokenId} | Delete an access token by ID.
[**get_token**](AccessTokensApi.md#get_token) | **GET** /tokens/{tokenId} | Get a single access token by ID.
[**get_tokens**](AccessTokensApi.md#get_tokens) | **GET** /tokens | Returns a list of tokens in the account.
[**patch_token**](AccessTokensApi.md#patch_token) | **PATCH** /tokens/{tokenId} | Modify an access token by ID.
[**post_token**](AccessTokensApi.md#post_token) | **POST** /tokens | Create a new token.
[**reset_token**](AccessTokensApi.md#reset_token) | **POST** /tokens/{tokenId}/reset | Reset an access token&#39;s secret key with an optional expiry time for the old key.


# **delete_token**
> delete_token(token_id)

Delete an access token by ID.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AccessTokensApi(launchdarkly_api.ApiClient(configuration))
token_id = 'token_id_example' # str | The access token ID.

try:
    # Delete an access token by ID.
    api_instance.delete_token(token_id)
except ApiException as e:
    print("Exception when calling AccessTokensApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The access token ID. | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> Token get_token(token_id)

Get a single access token by ID.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AccessTokensApi(launchdarkly_api.ApiClient(configuration))
token_id = 'token_id_example' # str | The access token ID.

try:
    # Get a single access token by ID.
    api_response = api_instance.get_token(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The access token ID. | 

### Return type

[**Token**](Token.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> Tokens get_tokens(show_all=show_all)

Returns a list of tokens in the account.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AccessTokensApi(launchdarkly_api.ApiClient(configuration))
show_all = true # bool | If set to true, and the authentication access token has the \"Admin\" role, personal access tokens for all members will be retrieved. (optional)

try:
    # Returns a list of tokens in the account.
    api_response = api_instance.get_tokens(show_all=show_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->get_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_all** | **bool**| If set to true, and the authentication access token has the \&quot;Admin\&quot; role, personal access tokens for all members will be retrieved. | [optional] 

### Return type

[**Tokens**](Tokens.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_token**
> Token patch_token(token_id, patch_delta)

Modify an access token by ID.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AccessTokensApi(launchdarkly_api.ApiClient(configuration))
token_id = 'token_id_example' # str | The access token ID.
patch_delta = [launchdarkly_api.PatchOperation()] # list[PatchOperation] | Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/'

try:
    # Modify an access token by ID.
    api_response = api_instance.patch_token(token_id, patch_delta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->patch_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The access token ID. | 
 **patch_delta** | [**list[PatchOperation]**](PatchOperation.md)| Requires a JSON Patch representation of the desired changes to the project. &#39;http://jsonpatch.com/&#39; | 

### Return type

[**Token**](Token.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_token**
> Token post_token(token_body)

Create a new token.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AccessTokensApi(launchdarkly_api.ApiClient(configuration))
token_body = launchdarkly_api.TokenBody() # TokenBody | Create a new access token.

try:
    # Create a new token.
    api_response = api_instance.post_token(token_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->post_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_body** | [**TokenBody**](TokenBody.md)| Create a new access token. | 

### Return type

[**Token**](Token.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_token**
> Token reset_token(token_id, expiry=expiry)

Reset an access token's secret key with an optional expiry time for the old key.

### Example
```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AccessTokensApi(launchdarkly_api.ApiClient(configuration))
token_id = 'token_id_example' # str | The access token ID.
expiry = 789 # int | An expiration time for the old token key, expressed as a Unix epoch time in milliseconds. By default, the token will expire immediately. (optional)

try:
    # Reset an access token's secret key with an optional expiry time for the old key.
    api_response = api_instance.reset_token(token_id, expiry=expiry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokensApi->reset_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The access token ID. | 
 **expiry** | **int**| An expiration time for the old token key, expressed as a Unix epoch time in milliseconds. By default, the token will expire immediately. | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

