import random
import string
from Intensive_Tests.enums import limits


class KYC_Choices:
    
    class Personal_info:
        
        # gender_options=["Male", "Female"]
        gender="Male"
        
        first_name="Roy"
        middle_name="N"
        family_name="Braish"

        mother_name="Mother"
        
        # are_you_married_options=["Yes", "No"]
        are_you_married="No"
        spouse_name="Spouse"
        
        # How_many_children=["0","1","2","3","4","5"]
        how_many_children=0
        
        child1_name="Child one"
        child2_name="Child two"
        child3_name="Child three"
        child4_name="Child four"
        child5_name="Child five"
        

        birth_date="10/04/2000"
        nationality="Kuwait"
        country_of_birth="Lebanon"
        
        
        civil_id=''.join(random.choice(string.digits) for i in range(limits.CIVIL_ID))
        civil_id_serial=''.join(random.choice(string.digits) for i in range(limits.CIVIL_ID_SERIAL))
        civil_id_expiry="10/04/2055"
        
    class Address_info:
        city_title="City"
        area_title="Area"
        block_title="Block"
        street_title="Street"
        house_title="House"
        mobile_number_title="Mobile number"    

class IDS:
    
    class Blue_Screen:
        title="neo.nbkc.smartwealth.demo:id/tv_title"
        description="neo.nbkc.smartwealth.demo:id/tv_info"
        start_button="neo.nbkc.smartwealth.demo:id/btn"
    
    input_fields="neo.nbkc.smartwealth.demo:id/etValue"
    selection_fields="neo.nbkc.smartwealth.demo:id/tvContent"
    date_picker_fields="neo.nbkc.smartwealth.demo:id/imgCalendar"
    
    date_picker_year_id="android:id/date_picker_header_year"
    date_picker_single_year_id="android:id/text1"

    selection_parent_id="neo.nbkc.smartwealth.demo:id/dropdown"
    input_parent_id="neo.nbkc.smartwealth.demo:id/card"
    date_picker_parent_id="neo.nbkc.smartwealth.demo:id/datePicker"
    date_picker_month_parent_id="android:id/month_view"  
  
    date_picker_month_next="android:id/next"
    date_picker_month_back="android:id/prev"


    date_picker_ok_button="android:id/button1"
    submit_button="neo.nbkc.smartwealth.demo:id/submitButton"
    
    
    class list_picker:
        list_picker_field="neo.nbkc.smartwealth.demo:id/imgArrow"
        list_picker_parent_id="neo.nbkc.smartwealth.demo:id/listPicker"
        list_picker_country_id="neo.nbkc.smartwealth.demo:id/tvTitle"
        scroller_parent_id="neo.nbkc.smartwealth.demo:id/fastScrollerView"
        scroller_letter_class="android.widget.TextView"
        
    class classes:
        selection_class="android.widget.FrameLayout"
        date_picker_class="android.widget.FrameLayout"
        input_class="android.view.ViewGroup"
        date_picker_month_class="android.view.View"
        list_picker_class="android.widget.FrameLayout"
    
class Field_types:

    class selection:
        id=IDS.selection_fields
        parent_class=IDS.classes.selection_class
        parent_id=IDS.selection_parent_id
    
    class input:
        id=IDS.input_fields
        parent_class=IDS.classes.input_class
        parent_id=IDS.input_parent_id
    
    class date_picker:
        id=IDS.date_picker_fields
        parent_class=IDS.classes.date_picker_class
        parent_id=IDS.date_picker_parent_id
        ok_button_id=IDS.date_picker_ok_button
        
        class year:
            id=IDS.date_picker_year_id
            single_year_id=IDS.date_picker_single_year_id
            parent_class=IDS.classes.date_picker_class
            parent_id=IDS.date_picker_parent_id
        
        class month:
            parent_id=IDS.date_picker_month_parent_id
            class_name=IDS.classes.date_picker_month_class
            next_button_id=IDS.date_picker_month_next
            back_button_id=IDS.date_picker_month_back
    
    class list_picker:
        id=IDS.list_picker.list_picker_field
        parent_id=IDS.list_picker.list_picker_parent_id
        single_country_id=IDS.list_picker.list_picker_country_id
        parent_class=IDS.classes.list_picker_class
        class scroller:
            parent_id=IDS.list_picker.scroller_parent_id
            values_class_name=IDS.list_picker.scroller_letter_class
        