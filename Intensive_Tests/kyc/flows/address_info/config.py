
from Intensive_Tests.kyc.config import Field_types, KYC_Choices




class Localization_Address_Info:

    city_title="City"
    area_title="Area"
    block_title="Block"
    street_title="Street"
    house_title="House"
    mobile_number_title="Mobile number"    


class KYC_Fields:
    
    class City:
        trigger_Title=Localization_Address_Info.gender_title
        choice= KYC_Choices.Personal_info.gender
        type=Field_types.selection
        is_visible=True
        #Means that if there are 4 elements with same ID, we don't compare with text, but we click on index from here. 
        #Ex.: 0 instead of "No_Childen", no need to compare text we can directly click element index 0
        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id

    
    class Area:
        trigger_Title=Localization_Address_Info.first_name_title
        choice= KYC_Choices.Personal_info.first_name
        type=Field_types.input
        is_visible=True


        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id

    class Block:
        trigger_Title=Localization_Address_Info.middle_name_title
        choice= KYC_Choices.Personal_info.middle_name
        type=Field_types.input
        is_visible=True


        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
        
    class Street:
        trigger_Title=Localization_Address_Info.family_name_title
        choice= KYC_Choices.Personal_info.family_name
        type=Field_types.input
        is_visible=True

        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
        
    class House:
        trigger_Title=Localization_Address_Info.mother_name_title
        choice= KYC_Choices.Personal_info.mother_name
        type=Field_types.input
        is_visible=True


        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
    
    class Mobile_number:
        trigger_Title=Localization_Address_Info.are_you_married_title
        choice= KYC_Choices.Personal_info.are_you_married
        type=Field_types.selection
        is_visible=True


        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id

    class Spouse_name:
        trigger_Title=Localization_Address_Info.spouse_title
        choice= KYC_Choices.Personal_info.spouse_name
        type=Field_types.input
        
        is_visible=True if KYC_Choices.Personal_info.are_you_married == "Yes" else False


        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
        
        
    class How_many_children:
        trigger_Title=Localization_Address_Info.How_many_children_title
        choice= KYC_Choices.Personal_info.how_many_children
        type=Field_types.selection
        
        is_visible=True

        #Means that if there are 4 elements with same ID, we don't compare with text, but we click on index from here. 
        #Ex.: 0 instead of "No_Childen", no need to compare text we can directly click element index 0
        mapped_by_index=True
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
    
    class Child_1:
        trigger_Title=Localization_Address_Info.children_box_title
        choice= KYC_Choices.Personal_info.child1_name
        type=Field_types.input
        
        is_visible=True if KYC_Choices.Personal_info.how_many_children >0 else False

        mapped_by_index=True
        index=0
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id    
    
    class Child_2:
        trigger_Title=Localization_Address_Info.children_box_title
        choice= KYC_Choices.Personal_info.child2_name
        type=Field_types.input
        
        is_visible=True if KYC_Choices.Personal_info.how_many_children >1 else False

        mapped_by_index=True
        index=1
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id    
    
    class Child_3:
        trigger_Title=Localization_Address_Info.children_box_title
        choice= KYC_Choices.Personal_info.child3_name
        type=Field_types.input
        
        is_visible=True if KYC_Choices.Personal_info.how_many_children >2 else False

        mapped_by_index=True
        index=2
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id    
    
    class Child_4:
        trigger_Title=Localization_Address_Info.children_box_title
        choice= KYC_Choices.Personal_info.child4_name
        type=Field_types.input
        
        is_visible=True if KYC_Choices.Personal_info.how_many_children >3 else False

        mapped_by_index=True
        index=3
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id  
          
    class Child_5:
        trigger_Title=Localization_Address_Info.children_box_title
        choice= KYC_Choices.Personal_info.child5_name
        type=Field_types.input
        
        is_visible=True if KYC_Choices.Personal_info.how_many_children ==5 else False

        mapped_by_index=True
        index=4
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id    

    class Birth_date:
        trigger_Title=Localization_Address_Info.Birth_date_title
        choice_day= KYC_Choices.Personal_info.birth_date[0:2]
        choice_month=KYC_Choices.Personal_info.birth_date[3:5]
        choice_year= KYC_Choices.Personal_info.birth_date[6:10]
        
        type=Field_types.date_picker
        
        is_visible=True

        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id    
        
    class Nationality:
        trigger_Title=Localization_Address_Info.Nationality_title
        choice=KYC_Choices.Personal_info.nationality
        
        type=Field_types.list_picker
        
        is_visible=True
        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
        
    class Country_of_birth:
        trigger_Title=Localization_Address_Info.Country_of_birth_title
        choice=KYC_Choices.Personal_info.country_of_birth
        
        type=Field_types.list_picker
        
        is_visible=True
        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
        
    class Civil_id:
        trigger_Title=Localization_Address_Info.civil_id_title
        choice=KYC_Choices.Personal_info.civil_id
        
        type=Field_types.input
        
        is_visible=True
        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id

    class Civil_id_serial:
        trigger_Title=Localization_Address_Info.civil_id_serial_title
        choice=KYC_Choices.Personal_info.civil_id_serial
        
        type=Field_types.input
        
        is_visible=True
        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id

    class Civil_id_expiry:
        trigger_Title=Localization_Address_Info.civil_id_expiry_title

        choice_day= KYC_Choices.Personal_info.civil_id_expiry[0:2]
        choice_month=KYC_Choices.Personal_info.civil_id_expiry[3:5]
        choice_year= KYC_Choices.Personal_info.civil_id_expiry[6:10]
        type=Field_types.date_picker
        
        is_visible=True
        mapped_by_index=False
        
        id=type.id
        parent_class=type.parent_class
        parent_id=type.parent_id
