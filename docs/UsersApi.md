# swagger_client.UsersApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{projectKey}/{environmentKey}/{userKey} | Delete a user by ID
[**get_search_users**](UsersApi.md#get_search_users) | **GET** /user-search/{projectKey}/{environmentKey} | Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.
[**get_user**](UsersApi.md#get_user) | **GET** /users/{projectKey}/{environmentKey}/{userKey} | Get a user by key.
[**get_users**](UsersApi.md#get_users) | **GET** /users/{projectKey}/{environmentKey} | List all users in the environment. Includes the total count of users. In each page, there will be up to &#39;limit&#39; users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.


# **delete_user**
> delete_user(project_key, environment_key, user_key)

Delete a user by ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key
user_key = 'user_key_example' # str | The user's key

try: 
    # Delete a user by ID
    api_instance.delete_user(project_key, environment_key, user_key)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 
 **user_key** | **str**| The user&#39;s key | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_users**
> Users get_search_users(project_key, environment_key, q=q, limit=limit, offset=offset, after=after)

Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key
q = 'q_example' # str | Search query (optional)
limit = 3.4 # float | Pagination limit (optional)
offset = 3.4 # float | Specifies the first item to return in the collection (optional)
after = 789 # int | A unix epoch time in milliseconds specifying the maximum last time a user requested a feature flag (optional)

try: 
    # Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.
    api_response = api_instance.get_search_users(project_key, environment_key, q=q, limit=limit, offset=offset, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 
 **q** | **str**| Search query | [optional] 
 **limit** | **float**| Pagination limit | [optional] 
 **offset** | **float**| Specifies the first item to return in the collection | [optional] 
 **after** | **int**| A unix epoch time in milliseconds specifying the maximum last time a user requested a feature flag | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(project_key, environment_key, user_key)

Get a user by key.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key
user_key = 'user_key_example' # str | The user's key

try: 
    # Get a user by key.
    api_response = api_instance.get_user(project_key, environment_key, user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 
 **user_key** | **str**| The user&#39;s key | 

### Return type

[**User**](User.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> Users get_users(project_key, environment_key, limit=limit)

List all users in the environment. Includes the total count of users. In each page, there will be up to 'limit' users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key
limit = 3.4 # float | Pagination limit (optional)

try: 
    # List all users in the environment. Includes the total count of users. In each page, there will be up to 'limit' users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.
    api_response = api_instance.get_users(project_key, environment_key, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 
 **limit** | **float**| Pagination limit | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

