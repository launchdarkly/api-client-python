# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from launchdarkly_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from launchdarkly_api.model.access_denied_reason_rep import AccessDeniedReasonRep
from launchdarkly_api.model.access_denied_rep import AccessDeniedRep
from launchdarkly_api.model.access_rep import AccessRep
from launchdarkly_api.model.access_token_post import AccessTokenPost
from launchdarkly_api.model.action_input_rep import ActionInputRep
from launchdarkly_api.model.action_output_rep import ActionOutputRep
from launchdarkly_api.model.all_variations_summary import AllVariationsSummary
from launchdarkly_api.model.approval_condition_input_rep import ApprovalConditionInputRep
from launchdarkly_api.model.approval_condition_output_rep import ApprovalConditionOutputRep
from launchdarkly_api.model.approval_settings import ApprovalSettings
from launchdarkly_api.model.audit_log_entry_listing_rep import AuditLogEntryListingRep
from launchdarkly_api.model.audit_log_entry_listing_rep_collection import AuditLogEntryListingRepCollection
from launchdarkly_api.model.audit_log_entry_rep import AuditLogEntryRep
from launchdarkly_api.model.authorized_app_data_rep import AuthorizedAppDataRep
from launchdarkly_api.model.big_segment_target import BigSegmentTarget
from launchdarkly_api.model.branch_collection_rep import BranchCollectionRep
from launchdarkly_api.model.branch_rep import BranchRep
from launchdarkly_api.model.clause import Clause
from launchdarkly_api.model.client_side_availability import ClientSideAvailability
from launchdarkly_api.model.client_side_availability_post import ClientSideAvailabilityPost
from launchdarkly_api.model.condition_base_output_rep import ConditionBaseOutputRep
from launchdarkly_api.model.condition_input_rep import ConditionInputRep
from launchdarkly_api.model.condition_output_rep import ConditionOutputRep
from launchdarkly_api.model.confidence_interval_rep import ConfidenceIntervalRep
from launchdarkly_api.model.conflict import Conflict
from launchdarkly_api.model.conflict_output_rep import ConflictOutputRep
from launchdarkly_api.model.copied_from_env import CopiedFromEnv
from launchdarkly_api.model.create_copy_flag_config_approval_request_request import CreateCopyFlagConfigApprovalRequestRequest
from launchdarkly_api.model.create_flag_config_approval_request_request import CreateFlagConfigApprovalRequestRequest
from launchdarkly_api.model.custom_properties import CustomProperties
from launchdarkly_api.model.custom_property import CustomProperty
from launchdarkly_api.model.custom_role import CustomRole
from launchdarkly_api.model.custom_role_post import CustomRolePost
from launchdarkly_api.model.custom_role_post_data import CustomRolePostData
from launchdarkly_api.model.custom_roles import CustomRoles
from launchdarkly_api.model.custom_workflow_input_rep import CustomWorkflowInputRep
from launchdarkly_api.model.custom_workflow_meta import CustomWorkflowMeta
from launchdarkly_api.model.custom_workflow_output_rep import CustomWorkflowOutputRep
from launchdarkly_api.model.custom_workflow_stage_meta import CustomWorkflowStageMeta
from launchdarkly_api.model.custom_workflows_listing_output_rep import CustomWorkflowsListingOutputRep
from launchdarkly_api.model.default_client_side_availability_post import DefaultClientSideAvailabilityPost
from launchdarkly_api.model.defaults import Defaults
from launchdarkly_api.model.dependent_flag import DependentFlag
from launchdarkly_api.model.dependent_flag_environment import DependentFlagEnvironment
from launchdarkly_api.model.dependent_flags_by_environment import DependentFlagsByEnvironment
from launchdarkly_api.model.derived_attribute import DerivedAttribute
from launchdarkly_api.model.destination import Destination
from launchdarkly_api.model.destination_post import DestinationPost
from launchdarkly_api.model.destinations import Destinations
from launchdarkly_api.model.environment import Environment
from launchdarkly_api.model.environment_post import EnvironmentPost
from launchdarkly_api.model.execution_output_rep import ExecutionOutputRep
from launchdarkly_api.model.experiment_allocation_rep import ExperimentAllocationRep
from launchdarkly_api.model.experiment_enabled_period_rep import ExperimentEnabledPeriodRep
from launchdarkly_api.model.experiment_environment_setting_rep import ExperimentEnvironmentSettingRep
from launchdarkly_api.model.experiment_info_rep import ExperimentInfoRep
from launchdarkly_api.model.experiment_metadata_rep import ExperimentMetadataRep
from launchdarkly_api.model.experiment_rep import ExperimentRep
from launchdarkly_api.model.experiment_results_rep import ExperimentResultsRep
from launchdarkly_api.model.experiment_stats_rep import ExperimentStatsRep
from launchdarkly_api.model.experiment_time_series_slice import ExperimentTimeSeriesSlice
from launchdarkly_api.model.experiment_time_series_variation_slice import ExperimentTimeSeriesVariationSlice
from launchdarkly_api.model.experiment_time_series_variation_slices import ExperimentTimeSeriesVariationSlices
from launchdarkly_api.model.experiment_totals_rep import ExperimentTotalsRep
from launchdarkly_api.model.expiring_user_target_error import ExpiringUserTargetError
from launchdarkly_api.model.expiring_user_target_get_response import ExpiringUserTargetGetResponse
from launchdarkly_api.model.expiring_user_target_item import ExpiringUserTargetItem
from launchdarkly_api.model.expiring_user_target_patch_response import ExpiringUserTargetPatchResponse
from launchdarkly_api.model.extinction import Extinction
from launchdarkly_api.model.extinction_collection_rep import ExtinctionCollectionRep
from launchdarkly_api.model.extinction_list_post import ExtinctionListPost
from launchdarkly_api.model.feature_flag import FeatureFlag
from launchdarkly_api.model.feature_flag_body import FeatureFlagBody
from launchdarkly_api.model.feature_flag_config import FeatureFlagConfig
from launchdarkly_api.model.feature_flag_scheduled_change import FeatureFlagScheduledChange
from launchdarkly_api.model.feature_flag_scheduled_changes import FeatureFlagScheduledChanges
from launchdarkly_api.model.feature_flag_status import FeatureFlagStatus
from launchdarkly_api.model.feature_flag_status_across_environments import FeatureFlagStatusAcrossEnvironments
from launchdarkly_api.model.feature_flag_statuses import FeatureFlagStatuses
from launchdarkly_api.model.feature_flags import FeatureFlags
from launchdarkly_api.model.flag_config_approval_request_response import FlagConfigApprovalRequestResponse
from launchdarkly_api.model.flag_config_approval_requests_response import FlagConfigApprovalRequestsResponse
from launchdarkly_api.model.flag_copy_config_environment import FlagCopyConfigEnvironment
from launchdarkly_api.model.flag_copy_config_post import FlagCopyConfigPost
from launchdarkly_api.model.flag_global_attributes_rep import FlagGlobalAttributesRep
from launchdarkly_api.model.flag_listing_rep import FlagListingRep
from launchdarkly_api.model.flag_scheduled_changes_input import FlagScheduledChangesInput
from launchdarkly_api.model.flag_status_rep import FlagStatusRep
from launchdarkly_api.model.flag_summary import FlagSummary
from launchdarkly_api.model.forbidden_error_rep import ForbiddenErrorRep
from launchdarkly_api.model.form_variable_config import FormVariableConfig
from launchdarkly_api.model.hunk_rep import HunkRep
from launchdarkly_api.model.instruction import Instruction
from launchdarkly_api.model.instructions import Instructions
from launchdarkly_api.model.integration_metadata import IntegrationMetadata
from launchdarkly_api.model.integration_status import IntegrationStatus
from launchdarkly_api.model.invalid_request_error_rep import InvalidRequestErrorRep
from launchdarkly_api.model.ip_list import IpList
from launchdarkly_api.model.json_patch import JSONPatch
from launchdarkly_api.model.last_seen_metadata import LastSeenMetadata
from launchdarkly_api.model.link import Link
from launchdarkly_api.model.member import Member
from launchdarkly_api.model.member_data_rep import MemberDataRep
from launchdarkly_api.model.member_permission_grant_summary_rep import MemberPermissionGrantSummaryRep
from launchdarkly_api.model.member_summary_rep import MemberSummaryRep
from launchdarkly_api.model.member_team_summary_rep import MemberTeamSummaryRep
from launchdarkly_api.model.members import Members
from launchdarkly_api.model.method_not_allowed_error_rep import MethodNotAllowedErrorRep
from launchdarkly_api.model.metric_collection_rep import MetricCollectionRep
from launchdarkly_api.model.metric_listing_rep import MetricListingRep
from launchdarkly_api.model.metric_post import MetricPost
from launchdarkly_api.model.metric_rep import MetricRep
from launchdarkly_api.model.metric_seen import MetricSeen
from launchdarkly_api.model.modification import Modification
from launchdarkly_api.model.multi_environment_dependent_flag import MultiEnvironmentDependentFlag
from launchdarkly_api.model.multi_environment_dependent_flags import MultiEnvironmentDependentFlags
from launchdarkly_api.model.new_member_form import NewMemberForm
from launchdarkly_api.model.new_member_form_list_post import NewMemberFormListPost
from launchdarkly_api.model.not_found_error_rep import NotFoundErrorRep
from launchdarkly_api.model.parent_resource_rep import ParentResourceRep
from launchdarkly_api.model.patch_failed_error_rep import PatchFailedErrorRep
from launchdarkly_api.model.patch_operation import PatchOperation
from launchdarkly_api.model.patch_segment_instruction import PatchSegmentInstruction
from launchdarkly_api.model.patch_segment_request import PatchSegmentRequest
from launchdarkly_api.model.patch_with_comment import PatchWithComment
from launchdarkly_api.model.permission_grant_collection_rep import PermissionGrantCollectionRep
from launchdarkly_api.model.permission_grant_input import PermissionGrantInput
from launchdarkly_api.model.permission_grant_rep import PermissionGrantRep
from launchdarkly_api.model.post_approval_request_apply_request import PostApprovalRequestApplyRequest
from launchdarkly_api.model.post_approval_request_review_request import PostApprovalRequestReviewRequest
from launchdarkly_api.model.post_flag_scheduled_changes_input import PostFlagScheduledChangesInput
from launchdarkly_api.model.prerequisite import Prerequisite
from launchdarkly_api.model.project import Project
from launchdarkly_api.model.project_listing_rep import ProjectListingRep
from launchdarkly_api.model.project_post import ProjectPost
from launchdarkly_api.model.projects import Projects
from launchdarkly_api.model.pub_nub_detail_rep import PubNubDetailRep
from launchdarkly_api.model.put_branch import PutBranch
from launchdarkly_api.model.rate_limited_error_rep import RateLimitedErrorRep
from launchdarkly_api.model.reference_rep import ReferenceRep
from launchdarkly_api.model.relay_auto_config_collection_rep import RelayAutoConfigCollectionRep
from launchdarkly_api.model.relay_auto_config_post import RelayAutoConfigPost
from launchdarkly_api.model.relay_auto_config_rep import RelayAutoConfigRep
from launchdarkly_api.model.repository_collection_rep import RepositoryCollectionRep
from launchdarkly_api.model.repository_post import RepositoryPost
from launchdarkly_api.model.repository_rep import RepositoryRep
from launchdarkly_api.model.resource_access import ResourceAccess
from launchdarkly_api.model.resource_id_response import ResourceIDResponse
from launchdarkly_api.model.review_output_rep import ReviewOutputRep
from launchdarkly_api.model.review_response import ReviewResponse
from launchdarkly_api.model.rollout import Rollout
from launchdarkly_api.model.root_response import RootResponse
from launchdarkly_api.model.rule import Rule
from launchdarkly_api.model.schedule_condition_input_rep import ScheduleConditionInputRep
from launchdarkly_api.model.schedule_condition_output_rep import ScheduleConditionOutputRep
from launchdarkly_api.model.sdk_list_rep import SdkListRep
from launchdarkly_api.model.sdk_version_list_rep import SdkVersionListRep
from launchdarkly_api.model.sdk_version_rep import SdkVersionRep
from launchdarkly_api.model.segment_body import SegmentBody
from launchdarkly_api.model.segment_metadata import SegmentMetadata
from launchdarkly_api.model.segment_user_list import SegmentUserList
from launchdarkly_api.model.segment_user_state import SegmentUserState
from launchdarkly_api.model.series_list_rep import SeriesListRep
from launchdarkly_api.model.series_metadata_rep import SeriesMetadataRep
from launchdarkly_api.model.series_time_slice_rep import SeriesTimeSliceRep
from launchdarkly_api.model.source_flag import SourceFlag
from launchdarkly_api.model.stage_input_rep import StageInputRep
from launchdarkly_api.model.stage_output_rep import StageOutputRep
from launchdarkly_api.model.statement import Statement
from launchdarkly_api.model.statement_post import StatementPost
from launchdarkly_api.model.statement_post_data import StatementPostData
from launchdarkly_api.model.statement_post_list import StatementPostList
from launchdarkly_api.model.statement_rep import StatementRep
from launchdarkly_api.model.statistic_collection_rep import StatisticCollectionRep
from launchdarkly_api.model.statistic_rep import StatisticRep
from launchdarkly_api.model.statistics_root import StatisticsRoot
from launchdarkly_api.model.status_conflict_error_rep import StatusConflictErrorRep
from launchdarkly_api.model.subject_data_rep import SubjectDataRep
from launchdarkly_api.model.target import Target
from launchdarkly_api.model.target_resource_rep import TargetResourceRep
from launchdarkly_api.model.team_collection_rep import TeamCollectionRep
from launchdarkly_api.model.team_patch_input import TeamPatchInput
from launchdarkly_api.model.team_post_input import TeamPostInput
from launchdarkly_api.model.team_rep import TeamRep
from launchdarkly_api.model.title_rep import TitleRep
from launchdarkly_api.model.token import Token
from launchdarkly_api.model.token_data_rep import TokenDataRep
from launchdarkly_api.model.tokens import Tokens
from launchdarkly_api.model.unauthorized_error_rep import UnauthorizedErrorRep
from launchdarkly_api.model.url_matchers import UrlMatchers
from launchdarkly_api.model.url_post import UrlPost
from launchdarkly_api.model.user import User
from launchdarkly_api.model.user_attribute_names_rep import UserAttributeNamesRep
from launchdarkly_api.model.user_flag_setting import UserFlagSetting
from launchdarkly_api.model.user_flag_settings import UserFlagSettings
from launchdarkly_api.model.user_record import UserRecord
from launchdarkly_api.model.user_record_rep import UserRecordRep
from launchdarkly_api.model.user_segment import UserSegment
from launchdarkly_api.model.user_segment_rule import UserSegmentRule
from launchdarkly_api.model.user_segments import UserSegments
from launchdarkly_api.model.users import Users
from launchdarkly_api.model.value_put import ValuePut
from launchdarkly_api.model.variation import Variation
from launchdarkly_api.model.variation_or_rollout_rep import VariationOrRolloutRep
from launchdarkly_api.model.variation_summary import VariationSummary
from launchdarkly_api.model.versions_rep import VersionsRep
from launchdarkly_api.model.webhook import Webhook
from launchdarkly_api.model.webhook_post import WebhookPost
from launchdarkly_api.model.webhooks import Webhooks
from launchdarkly_api.model.weighted_variation import WeightedVariation
