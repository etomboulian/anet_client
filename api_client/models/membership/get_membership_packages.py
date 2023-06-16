from api_client.models.base import Root, Body, ResponseTypes


class MembershipPackage(Body):
    package_name: str
    package_id: int
    modified_date_time: str
    description: str
    package_category_name: str
    package_status: str
    catalog_description: str
    eligibility_percentage: bool
    site_name: str
    usage_fee_name: str
    package_start_date: str
    specific_end_date: str
    specific_number_of_days: int
    specific_time_period: str
    force_expiration_date: str
    specific_renew_period: bool
    force_auto_renew: bool
    max_sellable_uses: int
    max_timeperiods: int
    max_uses: int
    max_uses_per_day: int
    max_uses_per_week: int
    membership_expire_warn_days: int
    family_membership: bool
    all_family_members: bool
    select_family_members: bool
    auto_allocate_to_immediate_family_members: bool
    family_member_count_min: int
    family_member_count_max: int
    family_member_age_min: int
    max_passes: int
    residency_type: str
    package_gender: str
    ages_min: int
    ages_max: int
    new_alternate_key_type_links_names: str
    new_alternate_key_status_links_names: str
    renewable_membership: bool
    membership_discount: bool
    qualify_member_registration_dates: bool
    hide_on_internet: bool
    available_as_prerequisite: bool
    after_scan_print_receipt: bool
    cancellation_options: str
    disable_transfer_usage_fee: bool
    disable_renew_usage_fee: bool
    automatic_cancellation: str
    selected_entry_points: str
    qualify_commission_option: bool


class GetMembershipPackagesResponse(Root):
    body: list[MembershipPackage]

    class APIProperties:
        paginated = True
        sortable = True
        endpoint = 'membershippackages'
        response_type = ResponseTypes.LIST
