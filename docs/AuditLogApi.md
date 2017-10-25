# swagger_client.AuditLogApi

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_entries**](AuditLogApi.md#get_audit_log_entries) | **GET** /auditlog | Fetch a list of all audit log entries
[**get_audit_log_entry**](AuditLogApi.md#get_audit_log_entry) | **GET** /auditlog/{resourceId} | Get an audit log entry by ID


# **get_audit_log_entries**
> AuditLogEntries get_audit_log_entries()

Fetch a list of all audit log entries

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
api_instance = swagger_client.AuditLogApi()

try: 
    # Fetch a list of all audit log entries
    api_response = api_instance.get_audit_log_entries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogApi->get_audit_log_entries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogEntries**](AuditLogEntries.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_entry**
> AuditLogEntry get_audit_log_entry(resource_id)

Get an audit log entry by ID

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
api_instance = swagger_client.AuditLogApi()
resource_id = 'resource_id_example' # str | The resource ID

try: 
    # Get an audit log entry by ID
    api_response = api_instance.get_audit_log_entry(resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogApi->get_audit_log_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The resource ID | 

### Return type

[**AuditLogEntry**](AuditLogEntry.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

