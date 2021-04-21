# launchdarkly_api.FeatureFlagsApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_feature_flag**](FeatureFlagsApi.md#copy_feature_flag) | **POST** /flags/{projectKey}/{featureFlagKey}/copy | Copies the feature flag configuration from one environment to the same feature flag in another environment.
[**delete_approval_request**](FeatureFlagsApi.md#delete_approval_request) | **DELETE** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{approvalRequestId} | Delete an approval request for a feature flag config
[**delete_feature_flag**](FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /flags/{projectKey}/{featureFlagKey} | Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.
[**delete_flag_config_scheduled_changes**](FeatureFlagsApi.md#delete_flag_config_scheduled_changes) | **DELETE** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{scheduledChangeId} | Delete a scheduled change on a feature flag in an environment.
[**flags_project_key_environment_key_feature_flag_key_dependent_flags_get**](FeatureFlagsApi.md#flags_project_key_environment_key_feature_flag_key_dependent_flags_get) | **GET** /flags/{projectKey}/{environmentKey}/{featureFlagKey}/dependent-flags | Get dependent flags for the flag in the environment specified in path parameters
[**flags_project_key_feature_flag_key_dependent_flags_get**](FeatureFlagsApi.md#flags_project_key_feature_flag_key_dependent_flags_get) | **GET** /flags/{projectKey}/{featureFlagKey}/dependent-flags | Get dependent flags across all environments for the flag specified in the path parameters
[**get_approval_request**](FeatureFlagsApi.md#get_approval_request) | **GET** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{approvalRequestId} | Get a single approval request for a feature flag config
[**get_approval_requests**](FeatureFlagsApi.md#get_approval_requests) | **GET** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests | Get all approval requests for a feature flag config
[**get_expiring_user_targets**](FeatureFlagsApi.md#get_expiring_user_targets) | **GET** /flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey} | Get expiring user targets for feature flag
[**get_feature_flag**](FeatureFlagsApi.md#get_feature_flag) | **GET** /flags/{projectKey}/{featureFlagKey} | Get a single feature flag by key.
[**get_feature_flag_status**](FeatureFlagsApi.md#get_feature_flag_status) | **GET** /flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey} | Get the status for a particular feature flag.
[**get_feature_flag_status_across_environments**](FeatureFlagsApi.md#get_feature_flag_status_across_environments) | **GET** /flag-status/{projectKey}/{featureFlagKey} | Get the status for a particular feature flag across environments
[**get_feature_flag_statuses**](FeatureFlagsApi.md#get_feature_flag_statuses) | **GET** /flag-statuses/{projectKey}/{environmentKey} | Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.
[**get_feature_flags**](FeatureFlagsApi.md#get_feature_flags) | **GET** /flags/{projectKey} | Get a list of all features in the given project.
[**get_flag_config_scheduled_change**](FeatureFlagsApi.md#get_flag_config_scheduled_change) | **GET** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{scheduledChangeId} | Get a scheduled change on a feature flag by id.
[**get_flag_config_scheduled_changes**](FeatureFlagsApi.md#get_flag_config_scheduled_changes) | **GET** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | Get all scheduled workflows for a feature flag by key.
[**get_flag_config_scheduled_changes_conflicts**](FeatureFlagsApi.md#get_flag_config_scheduled_changes_conflicts) | **POST** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes-conflicts | Lists conflicts between the given instructions and any existing scheduled changes for the feature flag. The actual HTTP verb should be REPORT, not POST.
[**patch_expiring_user_targets**](FeatureFlagsApi.md#patch_expiring_user_targets) | **PATCH** /flags/{projectKey}/{featureFlagKey}/expiring-user-targets/{environmentKey} | Update, add, or delete expiring user targets on feature flag
[**patch_feature_flag**](FeatureFlagsApi.md#patch_feature_flag) | **PATCH** /flags/{projectKey}/{featureFlagKey} | Perform a partial update to a feature.
[**patch_flag_config_scheduled_change**](FeatureFlagsApi.md#patch_flag_config_scheduled_change) | **PATCH** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes/{scheduledChangeId} | Updates an existing scheduled-change on a feature flag in an environment.
[**post_apply_approval_request**](FeatureFlagsApi.md#post_apply_approval_request) | **POST** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{approvalRequestId}/apply | Apply approval request for a feature flag config
[**post_approval_request**](FeatureFlagsApi.md#post_approval_request) | **POST** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{approvalRequestId} | Create an approval request for a feature flag config
[**post_feature_flag**](FeatureFlagsApi.md#post_feature_flag) | **POST** /flags/{projectKey} | Creates a new feature flag.
[**post_flag_config_scheduled_changes**](FeatureFlagsApi.md#post_flag_config_scheduled_changes) | **POST** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/scheduled-changes | Creates a new scheduled change for a feature flag.
[**post_review_approval_request**](FeatureFlagsApi.md#post_review_approval_request) | **POST** /projects/{projectKey}/flags/{featureFlagKey}/environments/{environmentKey}/approval-requests/{approvalRequestId}/review | Review approval request for a feature flag config


# **copy_feature_flag**
> FeatureFlag copy_feature_flag(project_key, feature_flag_key, feature_flag_copy_body)

Copies the feature flag configuration from one environment to the same feature flag in another environment.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
feature_flag_copy_body = launchdarkly_api.FeatureFlagCopyBody() # FeatureFlagCopyBody | Copy feature flag configurations between environments.

try:
    # Copies the feature flag configuration from one environment to the same feature flag in another environment.
    api_response = api_instance.copy_feature_flag(project_key, feature_flag_key, feature_flag_copy_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->copy_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **feature_flag_copy_body** | [**FeatureFlagCopyBody**](FeatureFlagCopyBody.md)| Copy feature flag configurations between environments. | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_approval_request**
> delete_approval_request(project_key, environment_key, feature_flag_key, approval_request_id, approval_request_config_body=approval_request_config_body)

Delete an approval request for a feature flag config

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
approval_request_id = 'approval_request_id_example' # str | The approval request ID
approval_request_config_body = launchdarkly_api.ApprovalRequestConfigBody() # ApprovalRequestConfigBody | Create a new approval request (optional)

try:
    # Delete an approval request for a feature flag config
    api_instance.delete_approval_request(project_key, environment_key, feature_flag_key, approval_request_id, approval_request_config_body=approval_request_config_body)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->delete_approval_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **approval_request_id** | **str**| The approval request ID | 
 **approval_request_config_body** | [**ApprovalRequestConfigBody**](ApprovalRequestConfigBody.md)| Create a new approval request | [optional] 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feature_flag**
> delete_feature_flag(project_key, feature_flag_key)

Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.
    api_instance.delete_feature_flag(project_key, feature_flag_key)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->delete_feature_flag: %s\n" % e)
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

# **delete_flag_config_scheduled_changes**
> delete_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, scheduled_change_id)

Delete a scheduled change on a feature flag in an environment.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
scheduled_change_id = 'scheduled_change_id_example' # str | The id of the scheduled change

try:
    # Delete a scheduled change on a feature flag in an environment.
    api_instance.delete_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key, scheduled_change_id)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->delete_flag_config_scheduled_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **scheduled_change_id** | **str**| The id of the scheduled change | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flags_project_key_environment_key_feature_flag_key_dependent_flags_get**
> DependentFlagsByEnvironment flags_project_key_environment_key_feature_flag_key_dependent_flags_get(project_key, environment_key, feature_flag_key)

Get dependent flags for the flag in the environment specified in path parameters

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Get dependent flags for the flag in the environment specified in path parameters
    api_response = api_instance.flags_project_key_environment_key_feature_flag_key_dependent_flags_get(project_key, environment_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->flags_project_key_environment_key_feature_flag_key_dependent_flags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**DependentFlagsByEnvironment**](DependentFlagsByEnvironment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flags_project_key_feature_flag_key_dependent_flags_get**
> MultiEnvironmentDependentFlags flags_project_key_feature_flag_key_dependent_flags_get(project_key, feature_flag_key)

Get dependent flags across all environments for the flag specified in the path parameters

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Get dependent flags across all environments for the flag specified in the path parameters
    api_response = api_instance.flags_project_key_feature_flag_key_dependent_flags_get(project_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->flags_project_key_feature_flag_key_dependent_flags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**MultiEnvironmentDependentFlags**](MultiEnvironmentDependentFlags.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_request**
> ApprovalRequests get_approval_request(project_key, feature_flag_key, environment_key, approval_request_id)

Get a single approval request for a feature flag config

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
approval_request_id = 'approval_request_id_example' # str | The approval request ID

try:
    # Get a single approval request for a feature flag config
    api_response = api_instance.get_approval_request(project_key, feature_flag_key, environment_key, approval_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_approval_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **approval_request_id** | **str**| The approval request ID | 

### Return type

[**ApprovalRequests**](ApprovalRequests.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_requests**
> ApprovalRequests get_approval_requests(project_key, feature_flag_key, environment_key)

Get all approval requests for a feature flag config

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.

try:
    # Get all approval requests for a feature flag config
    api_response = api_instance.get_approval_requests(project_key, feature_flag_key, environment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_approval_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 

### Return type

[**ApprovalRequests**](ApprovalRequests.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expiring_user_targets**
> UserTargetingExpirationForFlags get_expiring_user_targets(project_key, environment_key, feature_flag_key)

Get expiring user targets for feature flag

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Get expiring user targets for feature flag
    api_response = api_instance.get_expiring_user_targets(project_key, environment_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_expiring_user_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**UserTargetingExpirationForFlags**](UserTargetingExpirationForFlags.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag**
> FeatureFlag get_feature_flag(project_key, feature_flag_key, env=env)

Get a single feature flag by key.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
env = ['env_example'] # list[str] | By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env=[\"production\"] will restrict the returned configurations to just your production environment. (optional)

try:
    # Get a single feature flag by key.
    api_response = api_instance.get_feature_flag(project_key, feature_flag_key, env=env)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **env** | [**list[str]**](str.md)| By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env&#x3D;[\&quot;production\&quot;] will restrict the returned configurations to just your production environment. | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_status**
> FeatureFlagStatus get_feature_flag_status(project_key, environment_key, feature_flag_key)

Get the status for a particular feature flag.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Get the status for a particular feature flag.
    api_response = api_instance.get_feature_flag_status(project_key, environment_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_feature_flag_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**FeatureFlagStatus**](FeatureFlagStatus.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_status_across_environments**
> FeatureFlagStatusAcrossEnvironments get_feature_flag_status_across_environments(project_key, feature_flag_key)

Get the status for a particular feature flag across environments

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.

try:
    # Get the status for a particular feature flag across environments
    api_response = api_instance.get_feature_flag_status_across_environments(project_key, feature_flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_feature_flag_status_across_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 

### Return type

[**FeatureFlagStatusAcrossEnvironments**](FeatureFlagStatusAcrossEnvironments.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flag_statuses**
> FeatureFlagStatuses get_feature_flag_statuses(project_key, environment_key)

Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.

try:
    # Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.
    api_response = api_instance.get_feature_flag_statuses(project_key, environment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_feature_flag_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 

### Return type

[**FeatureFlagStatuses**](FeatureFlagStatuses.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feature_flags**
> FeatureFlags get_feature_flags(project_key, env=env, summary=summary, archived=archived, limit=limit, offset=offset, filter=filter, sort=sort, tag=tag)

Get a list of all features in the given project.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
env = ['env_example'] # list[str] | By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env=[\"production\"] will restrict the returned configurations to just your production environment. (optional)
summary = true # bool | By default in api version >= 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary=0 to include these fields for each flag returned. (optional)
archived = true # bool | When set to 1, only archived flags will be included in the list of flags returned.  By default, archived flags are not included in the list of flags. (optional)
limit = 8.14 # float | The number of objects to return. Defaults to -1, which returns everything. (optional)
offset = 8.14 # float | Where to start in the list. This is for use with pagination. For example, an offset of 10 would skip the first 10 items and then return the next limit items. (optional)
filter = 'filter_example' # str | A comma-separated list of filters. Each filter is of the form field:value. (optional)
sort = 'sort_example' # str | A comma-separated list of fields to sort by. A field prefixed by a - will be sorted in descending order. (optional)
tag = 'tag_example' # str | Filter by tag. A tag can be used to group flags across projects. (optional)

try:
    # Get a list of all features in the given project.
    api_response = api_instance.get_feature_flags(project_key, env=env, summary=summary, archived=archived, limit=limit, offset=offset, filter=filter, sort=sort, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_feature_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **env** | [**list[str]**](str.md)| By default, each feature will include configurations for each environment. You can filter environments with the env query parameter. For example, setting env&#x3D;[\&quot;production\&quot;] will restrict the returned configurations to just your production environment. | [optional] 
 **summary** | **bool**| By default in api version &gt;&#x3D; 1, flags will _not_ include their list of prerequisites, targets or rules.  Set summary&#x3D;0 to include these fields for each flag returned. | [optional] 
 **archived** | **bool**| When set to 1, only archived flags will be included in the list of flags returned.  By default, archived flags are not included in the list of flags. | [optional] 
 **limit** | **float**| The number of objects to return. Defaults to -1, which returns everything. | [optional] 
 **offset** | **float**| Where to start in the list. This is for use with pagination. For example, an offset of 10 would skip the first 10 items and then return the next limit items. | [optional] 
 **filter** | **str**| A comma-separated list of filters. Each filter is of the form field:value. | [optional] 
 **sort** | **str**| A comma-separated list of fields to sort by. A field prefixed by a - will be sorted in descending order. | [optional] 
 **tag** | **str**| Filter by tag. A tag can be used to group flags across projects. | [optional] 

### Return type

[**FeatureFlags**](FeatureFlags.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_config_scheduled_change**
> FeatureFlagScheduledChange get_flag_config_scheduled_change(project_key, feature_flag_key, environment_key, scheduled_change_id)

Get a scheduled change on a feature flag by id.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
scheduled_change_id = 'scheduled_change_id_example' # str | The id of the scheduled change

try:
    # Get a scheduled change on a feature flag by id.
    api_response = api_instance.get_flag_config_scheduled_change(project_key, feature_flag_key, environment_key, scheduled_change_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_flag_config_scheduled_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **scheduled_change_id** | **str**| The id of the scheduled change | 

### Return type

[**FeatureFlagScheduledChange**](FeatureFlagScheduledChange.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_config_scheduled_changes**
> FeatureFlagScheduledChanges get_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key)

Get all scheduled workflows for a feature flag by key.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.

try:
    # Get all scheduled workflows for a feature flag by key.
    api_response = api_instance.get_flag_config_scheduled_changes(project_key, feature_flag_key, environment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_flag_config_scheduled_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 

### Return type

[**FeatureFlagScheduledChanges**](FeatureFlagScheduledChanges.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_config_scheduled_changes_conflicts**
> FeatureFlagScheduledChangesConflicts get_flag_config_scheduled_changes_conflicts(project_key, feature_flag_key, environment_key, flag_config_scheduled_changes_conflicts_body)

Lists conflicts between the given instructions and any existing scheduled changes for the feature flag. The actual HTTP verb should be REPORT, not POST.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
flag_config_scheduled_changes_conflicts_body = launchdarkly_api.FlagConfigScheduledChangesConflictsBody() # FlagConfigScheduledChangesConflictsBody | Used to determine if a semantic patch will result in conflicts with scheduled changes on a feature flag.

try:
    # Lists conflicts between the given instructions and any existing scheduled changes for the feature flag. The actual HTTP verb should be REPORT, not POST.
    api_response = api_instance.get_flag_config_scheduled_changes_conflicts(project_key, feature_flag_key, environment_key, flag_config_scheduled_changes_conflicts_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->get_flag_config_scheduled_changes_conflicts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **flag_config_scheduled_changes_conflicts_body** | [**FlagConfigScheduledChangesConflictsBody**](FlagConfigScheduledChangesConflictsBody.md)| Used to determine if a semantic patch will result in conflicts with scheduled changes on a feature flag. | 

### Return type

[**FeatureFlagScheduledChangesConflicts**](FeatureFlagScheduledChangesConflicts.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_expiring_user_targets**
> UserTargetingExpirationForFlags patch_expiring_user_targets(project_key, environment_key, feature_flag_key, semantic_patch_with_comment)

Update, add, or delete expiring user targets on feature flag

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
semantic_patch_with_comment = NULL # object | Requires a Semantic Patch representation of the desired changes to the resource. 'https://apidocs.launchdarkly.com/reference#updates-via-semantic-patches'. The addition of comments is also supported.

try:
    # Update, add, or delete expiring user targets on feature flag
    api_response = api_instance.patch_expiring_user_targets(project_key, environment_key, feature_flag_key, semantic_patch_with_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->patch_expiring_user_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **semantic_patch_with_comment** | **object**| Requires a Semantic Patch representation of the desired changes to the resource. &#39;https://apidocs.launchdarkly.com/reference#updates-via-semantic-patches&#39;. The addition of comments is also supported. | 

### Return type

[**UserTargetingExpirationForFlags**](UserTargetingExpirationForFlags.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_feature_flag**
> FeatureFlag patch_feature_flag(project_key, feature_flag_key, patch_comment)

Perform a partial update to a feature.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
patch_comment = launchdarkly_api.PatchComment() # PatchComment | Requires a JSON Patch representation of the desired changes to the project, and an optional comment. 'http://jsonpatch.com/' Feature flag patches also support JSON Merge Patch format. 'https://tools.ietf.org/html/rfc7386' The addition of comments is also supported.

try:
    # Perform a partial update to a feature.
    api_response = api_instance.patch_feature_flag(project_key, feature_flag_key, patch_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->patch_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **patch_comment** | [**PatchComment**](PatchComment.md)| Requires a JSON Patch representation of the desired changes to the project, and an optional comment. &#39;http://jsonpatch.com/&#39; Feature flag patches also support JSON Merge Patch format. &#39;https://tools.ietf.org/html/rfc7386&#39; The addition of comments is also supported. | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_flag_config_scheduled_change**
> FeatureFlagScheduledChange patch_flag_config_scheduled_change(project_key, feature_flag_key, flag_config_scheduled_changes_patch_body, environment_key, scheduled_change_id)

Updates an existing scheduled-change on a feature flag in an environment.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
flag_config_scheduled_changes_patch_body = launchdarkly_api.FlagConfigScheduledChangesPatchBody() # FlagConfigScheduledChangesPatchBody | Update scheduled changes on a feature flag.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
scheduled_change_id = 'scheduled_change_id_example' # str | The id of the scheduled change

try:
    # Updates an existing scheduled-change on a feature flag in an environment.
    api_response = api_instance.patch_flag_config_scheduled_change(project_key, feature_flag_key, flag_config_scheduled_changes_patch_body, environment_key, scheduled_change_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->patch_flag_config_scheduled_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **flag_config_scheduled_changes_patch_body** | [**FlagConfigScheduledChangesPatchBody**](FlagConfigScheduledChangesPatchBody.md)| Update scheduled changes on a feature flag. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **scheduled_change_id** | **str**| The id of the scheduled change | 

### Return type

[**FeatureFlagScheduledChange**](FeatureFlagScheduledChange.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_apply_approval_request**
> ApprovalRequests post_apply_approval_request(project_key, feature_flag_key, environment_key, approval_request_id, approval_request_apply_config_body)

Apply approval request for a feature flag config

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
approval_request_id = 'approval_request_id_example' # str | The approval request ID
approval_request_apply_config_body = launchdarkly_api.ApprovalRequestApplyConfigBody() # ApprovalRequestApplyConfigBody | Apply an approval request

try:
    # Apply approval request for a feature flag config
    api_response = api_instance.post_apply_approval_request(project_key, feature_flag_key, environment_key, approval_request_id, approval_request_apply_config_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->post_apply_approval_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **approval_request_id** | **str**| The approval request ID | 
 **approval_request_apply_config_body** | [**ApprovalRequestApplyConfigBody**](ApprovalRequestApplyConfigBody.md)| Apply an approval request | 

### Return type

[**ApprovalRequests**](ApprovalRequests.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_approval_request**
> ApprovalRequest post_approval_request(project_key, feature_flag_key, environment_key, approval_request_id, approval_request_config_body=approval_request_config_body)

Create an approval request for a feature flag config

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
approval_request_id = 'approval_request_id_example' # str | The approval request ID
approval_request_config_body = launchdarkly_api.ApprovalRequestConfigBody() # ApprovalRequestConfigBody | Create a new approval request (optional)

try:
    # Create an approval request for a feature flag config
    api_response = api_instance.post_approval_request(project_key, feature_flag_key, environment_key, approval_request_id, approval_request_config_body=approval_request_config_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->post_approval_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **approval_request_id** | **str**| The approval request ID | 
 **approval_request_config_body** | [**ApprovalRequestConfigBody**](ApprovalRequestConfigBody.md)| Create a new approval request | [optional] 

### Return type

[**ApprovalRequest**](ApprovalRequest.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feature_flag**
> FeatureFlag post_feature_flag(project_key, feature_flag_body, clone=clone)

Creates a new feature flag.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_body = launchdarkly_api.FeatureFlagBody() # FeatureFlagBody | Create a new feature flag.
clone = 'clone_example' # str | The key of the feature flag to be cloned. The key identifies the flag in your code.  For example, setting clone=flagKey will copy the full targeting configuration for all environments (including on/off state) from the original flag to the new flag. (optional)

try:
    # Creates a new feature flag.
    api_response = api_instance.post_feature_flag(project_key, feature_flag_body, clone=clone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->post_feature_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_body** | [**FeatureFlagBody**](FeatureFlagBody.md)| Create a new feature flag. | 
 **clone** | **str**| The key of the feature flag to be cloned. The key identifies the flag in your code.  For example, setting clone&#x3D;flagKey will copy the full targeting configuration for all environments (including on/off state) from the original flag to the new flag. | [optional] 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_flag_config_scheduled_changes**
> FeatureFlagScheduledChange post_flag_config_scheduled_changes(project_key, flag_config_scheduled_changes_post_body, feature_flag_key, environment_key)

Creates a new scheduled change for a feature flag.

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
flag_config_scheduled_changes_post_body = launchdarkly_api.FlagConfigScheduledChangesPostBody() # FlagConfigScheduledChangesPostBody | Create scheduled changes on a feature flag.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.

try:
    # Creates a new scheduled change for a feature flag.
    api_response = api_instance.post_flag_config_scheduled_changes(project_key, flag_config_scheduled_changes_post_body, feature_flag_key, environment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->post_flag_config_scheduled_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **flag_config_scheduled_changes_post_body** | [**FlagConfigScheduledChangesPostBody**](FlagConfigScheduledChangesPostBody.md)| Create scheduled changes on a feature flag. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 

### Return type

[**FeatureFlagScheduledChange**](FeatureFlagScheduledChange.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_review_approval_request**
> ApprovalRequests post_review_approval_request(project_key, feature_flag_key, environment_key, approval_request_id, approval_request_review_config_body)

Review approval request for a feature flag config

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
api_instance = launchdarkly_api.FeatureFlagsApi(launchdarkly_api.ApiClient(configuration))
project_key = 'project_key_example' # str | The project key, used to tie the flags together under one project so they can be managed together.
feature_flag_key = 'feature_flag_key_example' # str | The feature flag's key. The key identifies the flag in your code.
environment_key = 'environment_key_example' # str | The environment key, used to tie together flag configuration and users under one environment so they can be managed together.
approval_request_id = 'approval_request_id_example' # str | The approval request ID
approval_request_review_config_body = launchdarkly_api.ApprovalRequestReviewConfigBody() # ApprovalRequestReviewConfigBody | Review an approval request

try:
    # Review approval request for a feature flag config
    api_response = api_instance.post_review_approval_request(project_key, feature_flag_key, environment_key, approval_request_id, approval_request_review_config_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureFlagsApi->post_review_approval_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_key** | **str**| The project key, used to tie the flags together under one project so they can be managed together. | 
 **feature_flag_key** | **str**| The feature flag&#39;s key. The key identifies the flag in your code. | 
 **environment_key** | **str**| The environment key, used to tie together flag configuration and users under one environment so they can be managed together. | 
 **approval_request_id** | **str**| The approval request ID | 
 **approval_request_review_config_body** | [**ApprovalRequestReviewConfigBody**](ApprovalRequestReviewConfigBody.md)| Review an approval request | 

### Return type

[**ApprovalRequests**](ApprovalRequests.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

