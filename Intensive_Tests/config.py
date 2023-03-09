from Intensive_Tests.pending_dashboard.flows.kyc.config import Localization_pending_dashboard_kyc as pending_dashboard_localization
from Intensive_Tests.pending_dashboard.config import IDS as pending_dashboard_ids
from Intensive_Tests.kyc.config import IDS as personal_info_ids
from Intensive_Tests.kyc.flows.personal_info.config import Localization_Personal_Info as personal_info_localization


class Application_screens:
    
    Pending_Dashboard=pending_dashboard_ids,pending_dashboard_localization
    Personal_info_blue=personal_info_ids.Blue_Screen,personal_info_localization.Blue_Screen
    Personal_info=personal_info_ids,personal_info_localization
    