# SeriesListRepFloat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **Dict[str, object]** | The location and content type of related resources | 
**metadata** | **List[Dict[str, object]]** | Metadata about each series | 
**series** | **List[Dict[str, float]]** | An array of data points with timestamps. Each element of the array is an object with a &#39;time&#39; field, whose value is the timestamp, and one or more key fields. If there are multiple key fields, they are labeled &#39;0&#39;, &#39;1&#39;, and so on, and are explained in the &lt;code&gt;metadata&lt;/code&gt;. | 

## Example

```python
from launchdarkly_api.models.series_list_rep_float import SeriesListRepFloat

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesListRepFloat from a JSON string
series_list_rep_float_instance = SeriesListRepFloat.from_json(json)
# print the JSON string representation of the object
print(SeriesListRepFloat.to_json())

# convert the object into a dict
series_list_rep_float_dict = series_list_rep_float_instance.to_dict()
# create an instance of SeriesListRepFloat from a dict
series_list_rep_float_from_dict = SeriesListRepFloat.from_dict(series_list_rep_float_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


