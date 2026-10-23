# DataExportSeriesListRep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **Dict[str, object]** | The location and content type of related resources | 
**metadata** | **List[Dict[str, object]]** | Metadata about each series | 
**series** | **List[Dict[str, int]]** | An array of data points with timestamps. Each element of the array is an object with a &#39;time&#39; field, whose value is the timestamp, and one or more key fields. If there are multiple key fields, they are labeled &#39;0&#39;, &#39;1&#39;, and so on, and are explained in the &lt;code&gt;metadata&lt;/code&gt;. | 
**data_through** | **str** | The end of the latest hour written by this source&#39;s usage pipeline, as an RFC 3339 UTC timestamp. It is measured across all accounts, not only yours, and usage after this time is not counted yet. Omitted when the watermark is unavailable. | [optional] 
**delayed** | **bool** | Whether this source&#39;s usage pipeline is late: it wrote every hour of the 24 hours ending at &lt;code&gt;dataThrough&lt;/code&gt;, and more than three hours have passed since &lt;code&gt;dataThrough&lt;/code&gt;. Always &lt;code&gt;false&lt;/code&gt; for a source with gaps in those 24 hours, where gaps usually mean no usage rather than a stalled pipeline. Omitted when &lt;code&gt;dataThrough&lt;/code&gt; is omitted. | [optional] 

## Example

```python
from launchdarkly_api.models.data_export_series_list_rep import DataExportSeriesListRep

# TODO update the JSON string below
json = "{}"
# create an instance of DataExportSeriesListRep from a JSON string
data_export_series_list_rep_instance = DataExportSeriesListRep.from_json(json)
# print the JSON string representation of the object
print(DataExportSeriesListRep.to_json())

# convert the object into a dict
data_export_series_list_rep_dict = data_export_series_list_rep_instance.to_dict()
# create an instance of DataExportSeriesListRep from a dict
data_export_series_list_rep_from_dict = DataExportSeriesListRep.from_dict(data_export_series_list_rep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


