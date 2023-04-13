# SeriesListRep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The location and content type of related resources | 
**metadata** | [**[SeriesMetadataRep]**](SeriesMetadataRep.md) | Metadata about each series | 
**series** | [**[SeriesTimeSliceRep]**](SeriesTimeSliceRep.md) | An array of data points with timestamps. Each element of the array is an object with a &#39;time&#39; field, whose value is the timestamp, and one or more key fields. If there are multiple key fields, they are labeled &#39;0&#39;, &#39;1&#39;, and so on, and are explained in the &lt;code&gt;metadata&lt;/code&gt;. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


