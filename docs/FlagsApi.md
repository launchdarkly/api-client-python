# swagger_client.FlagsApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_feature_flag**](FlagsApi.md#delete_feature_flag) | **DELETE** /flags/{projectKey}/{featureFlagKey} | Delete a feature flag by ID
[**get_feature_flag**](FlagsApi.md#get_feature_flag) | **GET** /flags/{projectKey}/{featureFlagKey} | Get a single feature flag by key.
[**get_feature_flag_status**](FlagsApi.md#get_feature_flag_status) | **GET** /flag-statuses/{projectKey}/{environmentKey} | Get a list of statuses for all feature flags
[**get_feature_flag_statuses**](FlagsApi.md#get_feature_flag_statuses) | **GET** /flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey} | Get a list of statuses for all feature flags
[**get_feature_flags**](FlagsApi.md#get_feature_flags) | **GET** /flags/{projectKey} | Get a list of all features in the given project.
[**patch_feature_flag**](FlagsApi.md#patch_feature_flag) | **PATCH** /flags/{projectKey}/{featureFlagKey} | Modify a feature flag by ID
[**post_feature_flag**](FlagsApi.md#post_feature_flag) | **POST** /flags/{projectKey} | Create a feature flag


# **delete_feature_flag**
> delete_feature_flag(project_key, feature_flag_key)

Delete a feature flag by ID

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try: 
    # Delete a feature flag by ID
    api_instance.delete_feature_flag(project_key, feature_flag_key)
except ApiException as e:
    print("Exception when calling FlagsApi->delete_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag**
> FeatureFlag get_feature_flag(project_key, feature_flag_key, environment_key_query=environment_key_query)

Get a single feature flag by key.

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key_query = 'environment_key_query_example' # str | The environment key (optional)

try: 
    # Get a single feature flag by key.
    api_response = api_instance.get_feature_flag(project_key, feature_flag_key, environment_key_query=environment_key_query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagsApi->get_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key_query** | **str**| The environment key | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_status**
> FeatureFlagStatuses get_feature_flag_status(project_key, environment_key)

Get a list of statuses for all feature flags

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key

try: 
    # Get a list of statuses for all feature flags
    api_response = api_instance.get_feature_flag_status(project_key, environment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagsApi->get_feature_flag_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 

### Return type

[**FeatureFlagStatuses**](FeatureFlagStatuses.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_statuses**
> FeatureFlagStatus get_feature_flag_statuses(project_key, environment_key, feature_flag_key)

Get a list of statuses for all feature flags

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try: 
    # Get a list of statuses for all feature flags
    api_response = api_instance.get_feature_flag_statuses(project_key, environment_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagsApi->get_feature_flag_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**FeatureFlagStatus**](FeatureFlagStatus.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flags**
> FeatureFlags get_feature_flags(project_key, environment_key_query=environment_key_query, tag=tag)

Get a list of all features in the given project.

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key_query = 'environment_key_query_example' # str | The environment key (optional)
tag = 'tag_example' # str | Filter by tag. A tag can be used to group flags across projects. (optional)

try: 
    # Get a list of all features in the given project.
    api_response = api_instance.get_feature_flags(project_key, environment_key_query=environment_key_query, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagsApi->get_feature_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key_query** | **str**| The environment key | [optional] 
 **tag** | **str**| Filter by tag. A tag can be used to group flags across projects. | [optional] 

### Return type

[**FeatureFlags**](FeatureFlags.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_feature_flag**
> FeatureFlag patch_feature_flag(project_key, feature_flag_key, patch_delta)

Modify a feature flag by ID

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
patch_delta = [swagger_client.PatchDelta()] # list[PatchDelta] | http://jsonpatch.com/

try: 
    # Modify a feature flag by ID
    api_response = api_instance.patch_feature_flag(project_key, feature_flag_key, patch_delta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagsApi->patch_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **patch_delta** | [**list[PatchDelta]**](PatchDelta.md)| http://jsonpatch.com/ | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_flag**
> post_feature_flag(project_key, feature_flag_body)

Create a feature flag

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
api_instance = swagger_client.FlagsApi()
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_body = swagger_client.FeatureFlagBody() # FeatureFlagBody | Create a new feature flag

try: 
    # Create a feature flag
    api_instance.post_feature_flag(project_key, feature_flag_body)
except ApiException as e:
    print("Exception when calling FlagsApi->post_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_body** | [**FeatureFlagBody**](FeatureFlagBody.md)| Create a new feature flag | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

