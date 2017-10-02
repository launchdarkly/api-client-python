# swagger_client.EnvironmentsApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environment**](EnvironmentsApi.md#delete_environment) | **DELETE** /environments/{projectKey}/{environmentKey} | Delete an environment by ID
[**get_environment**](EnvironmentsApi.md#get_environment) | **GET** /environments/{projectKey}/{environmentKey} | Get an environment by key.
[**patch_environment**](EnvironmentsApi.md#patch_environment) | **PATCH** /environments/{projectKey}/{environmentKey} | Modify an environment by ID
[**post_environment**](EnvironmentsApi.md#post_environment) | **POST** /environments/{projectKey} | Create an environment


# **delete_environment**
> delete_environment(project_key, environment_key)

Delete an environment by ID

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
api_instance = swagger_client.EnvironmentsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key

try: 
    # Delete an environment by ID
    api_instance.delete_environment(project_key, environment_key)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->delete_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> Environment get_environment(project_key, environment_key)

Get an environment by key.

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
api_instance = swagger_client.EnvironmentsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key

try: 
    # Get an environment by key.
    api_response = api_instance.get_environment(project_key, environment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->get_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 

### Return type

[**Environment**](Environment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_environment**
> patch_environment(project_key, environment_key, patch_delta)

Modify an environment by ID

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
api_instance = swagger_client.EnvironmentsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key
patch_delta = [swagger_client.PatchDelta()] # list[PatchDelta] | http://jsonpatch.com/

try: 
    # Modify an environment by ID
    api_instance.patch_environment(project_key, environment_key, patch_delta)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->patch_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 
 **patch_delta** | [**list[PatchDelta]**](PatchDelta.md)| http://jsonpatch.com/ | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_environment**
> post_environment(project_key, environment_body)

Create an environment

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
api_instance = swagger_client.EnvironmentsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_body = swagger_client.EnvironmentBody() # EnvironmentBody | New environment

try: 
    # Create an environment
    api_instance.post_environment(project_key, environment_body)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->post_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_body** | [**EnvironmentBody**](EnvironmentBody.md)| New environment | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

