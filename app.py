import streamlit as st
import pandas as pd
from datetime import datetime, date
from streamlit_autorefresh import st_autorefresh


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MediQueue | Smart Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SESSION STATE
# ============================================================

if "appointments" not in st.session_state:
    st.session_state.appointments = []

if "page" not in st.session_state:
    st.session_state.page = "Home"


# ============================================================
# HOSPITAL IMAGES
# ============================================================

hospital_images = [
    (
        "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1600&q=85",
        "Modern Healthcare",
        "Quality healthcare with advanced facilities"
    ),
    (
        "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=1600&q=85",
        "Expert Doctors",
        "Experienced doctors for better patient care"
    ),
    (
        "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1600&q=85",
        "Smart Healthcare",
        "Technology-enabled hospital management"
    ),
    (
        "https://images.unsplash.com/photo-1538108149393-fbbd81895907?auto=format&fit=crop&w=1600&q=85",
        "Patient Care",
        "Simple and comfortable healthcare experience"
    ),
    (
        "https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=1600&q=85",
        "Trusted Service",
        "Making hospital visits easier and faster"
    )
]


# ============================================================
# DOCTORS
# ============================================================

doctors = {

    "General Medicine": [
        ["Dr. Ravi Kumar", "General Physician", "12 Years", 400],
        ["Dr. Sneha Reddy", "Internal Medicine", "9 Years", 450],
        ["Dr. Karthik Rao", "General Physician", "8 Years", 400]
    ],

    "Cardiology": [
        ["Dr. Priya Sharma", "Cardiologist", "15 Years", 800],
        ["Dr. Arjun Rao", "Interventional Cardiologist", "11 Years", 900],
        ["Dr. Meena Kapoor", "Cardiologist", "10 Years", 850]
    ],

    "Dermatology": [
        ["Dr. Anitha Reddy", "Dermatologist", "10 Years", 600],
        ["Dr. Meena Rao", "Cosmetic Dermatologist", "8 Years", 650]
    ],

    "Pediatrics": [
        ["Dr. Kumar Singh", "Child Specialist", "13 Years", 500],
        ["Dr. Divya Patel", "Pediatrician", "7 Years", 450]
    ],

    "Orthopedics": [
        ["Dr. Raj Malhotra", "Orthopedic Surgeon", "14 Years", 700],
        ["Dr. Kiran Rao", "Joint Replacement Specialist", "10 Years", 750]
    ],

    "Neurology": [
        ["Dr. Vikram Singh", "Neurologist", "16 Years", 1000],
        ["Dr. Neha Kapoor", "Neuro Physician", "10 Years", 900]
    ],

    "ENT": [
        ["Dr. Ajay Kumar", "ENT Specialist", "11 Years", 550],
        ["Dr. Lakshmi Rao", "ENT Surgeon", "9 Years", 600]
    ]
}


# ============================================================
# TIME SLOTS
# ============================================================

time_slots = [
    "09:00 AM",
    "09:30 AM",
    "10:00 AM",
    "10:30 AM",
    "11:00 AM",
    "11:30 AM",
    "12:00 PM",
    "12:30 PM",
    "01:00 PM - 02:00 PM | LUNCH BREAK",
    "02:00 PM",
    "02:30 PM",
    "03:00 PM",
    "03:30 PM",
    "04:00 PM",
    "04:30 PM - 05:00 PM | DOCTOR BREAK",
    "05:00 PM",
    "05:30 PM",
    "06:00 PM"
]


# ============================================================
# TOP HEADER
# ============================================================

top1, top2, top3 = st.columns([2.5, 5, 2.5])

with top1:
    st.title("🏥 MediQueue")

with top2:
    st.caption("Smart Hospital OP Booking & Queue Management")

with top3:
    st.write("")


# ============================================================
# NAVIGATION MENU
# ============================================================

menu1, menu2, menu3, menu4, menu5, menu6 = st.columns(6)

with menu1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

with menu2:
    if st.button("📝 Book OP", use_container_width=True):
        st.session_state.page = "Book Appointment"
        st.rerun()

with menu3:
    if st.button("👨‍⚕️ Doctors", use_container_width=True):
        st.session_state.page = "Doctors"
        st.rerun()

with menu4:
    if st.button("📋 Queue", use_container_width=True):
        st.session_state.page = "Queue"
        st.rerun()

with menu5:
    if st.button("📅 History", use_container_width=True):
        st.session_state.page = "History"
        st.rerun()

with menu6:
    if st.button("📊 Analytics", use_container_width=True):
        st.session_state.page = "Analytics"
        st.rerun()


st.divider()


page = st.session_state.page


# ============================================================
# HOME PAGE
# ============================================================

if page == "Home":

    # Automatic image slider
    refresh_count = st_autorefresh(
        interval=5000,
        key="hospital_slider"
    )

    image_index = refresh_count % len(hospital_images)

    image_url, image_title, image_description = (
        hospital_images[image_index]
    )

    st.image(
        image_url,
        use_container_width=True
    )

    st.title(
        f"🏥 {image_title}"
    )

    st.write(
        image_description
    )

    st.divider()

    # --------------------------------------------------------
    # WELCOME
    # --------------------------------------------------------

    st.header("Welcome to MediQueue 👋")

    st.write(
        "MediQueue is a smart hospital OP booking and "
        "queue management system designed to make hospital "
        "visits faster, easier and more organized."
    )

    st.write("")


    # --------------------------------------------------------
    # STATISTICS
    # --------------------------------------------------------

    total_appointments = len(
        st.session_state.appointments
    )

    waiting = sum(
        1
        for appointment in st.session_state.appointments
        if appointment["Status"] == "Waiting"
    )

    cancelled = sum(
        1
        for appointment in st.session_state.appointments
        if appointment["Status"] == "Cancelled"
    )

    total_doctors = sum(
        len(items)
        for items in doctors.values()
    )


    st.header("📊 Hospital Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📅 Appointments",
            total_appointments
        )

    with c2:
        st.metric(
            "⏳ Waiting Patients",
            waiting
        )

    with c3:
        st.metric(
            "👨‍⚕️ Doctors",
            total_doctors
        )

    with c4:
        st.metric(
            "❌ Cancelled",
            cancelled
        )


    st.divider()


    # --------------------------------------------------------
    # SERVICES
    # --------------------------------------------------------

    st.header("✨ Our Services")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            """
            ### 📝 OP Appointment

            Book your hospital OP appointment
            without waiting in long queues.
            """
        )

    with c2:
        st.success(
            """
            ### 👨‍⚕️ Doctor Selection

            Select your preferred department
            and doctor based on specialization.
            """
        )

    with c3:
        st.warning(
            """
            ### ⏳ Queue Management

            View your token and estimated
            waiting position easily.
            """
        )


    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info(
            """
            ### 🎟️ Smart Token

            Get an automatic appointment token
            after successful booking.
            """
        )

    with c2:
        st.success(
            """
            ### 📅 Appointment History

            View and manage all your
            previous appointments.
            """
        )

    with c3:
        st.warning(
            """
            ### 📊 Analytics

            Analyze hospital appointments
            by department and doctor.
            """
        )


    st.divider()


    # --------------------------------------------------------
    # TIMINGS
    # --------------------------------------------------------

    st.header("🕐 OP Timings")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success(
            """
            **🌅 Morning OP**

            09:00 AM – 01:00 PM
            """
        )

    with c2:
        st.warning(
            """
            **🍴 Lunch Break**

            01:00 PM – 02:00 PM
            """
        )

    with c3:
        st.info(
            """
            **🌇 Evening OP**

            02:00 PM – 06:00 PM
            """
        )


# ============================================================
# BOOK APPOINTMENT
# ============================================================

elif page == "Book Appointment":

    st.header("📝 Book OP Appointment")

    st.write(
        "Fill in the patient details and select an available slot."
    )

    st.divider()

    with st.form("appointment_form"):

        c1, c2 = st.columns(2)

        with c1:

            patient_name = st.text_input(
                "👤 Patient Name"
            )

            age = st.number_input(
                "🎂 Age",
                min_value=1,
                max_value=120,
                value=20
            )

            phone = st.text_input(
                "📱 Phone Number"
            )

            department = st.selectbox(
                "🏥 Department",
                list(doctors.keys())
            )


        with c2:

            doctor_data_list = doctors[department]

            doctor_names = [
                item[0]
                for item in doctor_data_list
            ]

            selected_doctor = st.selectbox(
                "👨‍⚕️ Doctor",
                doctor_names
            )

            selected_doctor_data = next(
                item
                for item in doctor_data_list
                if item[0] == selected_doctor
            )

            st.info(
                f"""
                **Specialization:** {selected_doctor_data[1]}

                **Experience:** {selected_doctor_data[2]}

                **Consultation Fee:** ₹{selected_doctor_data[3]}
                """
            )

            appointment_date = st.date_input(
                "📅 Appointment Date",
                min_value=date.today()
            )

            selected_slot = st.selectbox(
                "🕐 OP Time Slot",
                time_slots
            )


        submitted = st.form_submit_button(
            "🎟️ Confirm Appointment",
            use_container_width=True
        )


    if submitted:

        if not patient_name.strip():

            st.error(
                "Please enter patient name."
            )

        elif not phone.isdigit() or len(phone) != 10:

            st.error(
                "Please enter a valid 10-digit phone number."
            )

        elif "LUNCH BREAK" in selected_slot:

            st.error(
                "Lunch break slot cannot be booked."
            )

        elif "DOCTOR BREAK" in selected_slot:

            st.error(
                "Doctor break slot cannot be booked."
            )

        else:

            duplicate = any(
                appointment["Doctor"] == selected_doctor
                and appointment["Date"] == str(appointment_date)
                and appointment["Slot"] == selected_slot
                and appointment["Status"] == "Waiting"
                for appointment in st.session_state.appointments
            )

            if duplicate:

                st.error(
                    "This doctor is already booked for the selected slot."
                )

            else:

                token = (
                    len(st.session_state.appointments)
                    + 1
                )

                new_appointment = {

                    "Token": token,

                    "Patient": patient_name,

                    "Age": age,

                    "Phone": phone,

                    "Department": department,

                    "Doctor": selected_doctor,

                    "Date": str(appointment_date),

                    "Slot": selected_slot,

                    "Booking Time":
                        datetime.now().strftime("%H:%M"),

                    "Status": "Waiting"
                }

                st.session_state.appointments.append(
                    new_appointment
                )

                st.success(
                    "🎉 Appointment booked successfully!"
                )

                st.balloons()

                st.divider()

                st.header("🎟️ Appointment Confirmation")

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "Token Number",
                        f"#{token}"
                    )

                    st.write(
                        f"👤 **Patient:** {patient_name}"
                    )

                    st.write(
                        f"🎂 **Age:** {age}"
                    )

                with c2:

                    st.write(
                        f"🏥 **Department:** {department}"
                    )

                    st.write(
                        f"👨‍⚕️ **Doctor:** {selected_doctor}"
                    )

                    st.write(
                        f"📅 **Date:** {appointment_date}"
                    )

                    st.write(
                        f"🕐 **Slot:** {selected_slot}"
                    )

                st.info(
                    f"💰 Consultation Fee: ₹{selected_doctor_data[3]}"
                )


# ============================================================
# DOCTORS
# ============================================================

elif page == "Doctors":

    st.header("👨‍⚕️ Our Doctors")

    st.write(
        "Choose from our experienced doctors across different departments."
    )

    st.divider()

    for department, doctor_list in doctors.items():

        st.subheader(
            f"🏥 {department}"
        )

        columns = st.columns(
            len(doctor_list)
        )

        for column, doctor in zip(
            columns,
            doctor_list
        ):

            with column:

                st.info(
                    f"""
                    ### 👨‍⚕️ {doctor[0]}

                    **Specialization**

                    {doctor[1]}

                    **Experience**

                    ⭐ {doctor[2]}

                    **Consultation**

                    ₹{doctor[3]}
                    """
                )


# ============================================================
# QUEUE
# ============================================================

elif page == "Queue":

    st.header("📋 Current OP Queue")

    st.write(
        "View patients currently waiting for consultation."
    )

    st.divider()

    waiting = [
        appointment
        for appointment in st.session_state.appointments
        if appointment["Status"] == "Waiting"
    ]

    if not waiting:

        st.success(
            "🎉 No patients are currently waiting."
        )

    else:

        queue_df = pd.DataFrame(
            waiting
        )

        st.dataframe(
            queue_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.header("⏳ Estimated Waiting Time")

        for position, appointment in enumerate(
            waiting,
            start=1
        ):

            wait_time = (
                position - 1
            ) * 10

            c1, c2, c3 = st.columns(3)

            with c1:
                st.write(
                    f"🎟️ **Token #{appointment['Token']}**"
                )

            with c2:
                st.write(
                    f"👤 **{appointment['Patient']}**"
                )

            with c3:
                st.write(
                    f"⏳ **{wait_time} minutes**"
                )


# ============================================================
# HISTORY
# ============================================================

elif page == "History":

    st.header("📅 Appointment History")

    if not st.session_state.appointments:

        st.info(
            "No appointments found."
        )

    else:

        history_df = pd.DataFrame(
            st.session_state.appointments
        )

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        active = [
            appointment
            for appointment in st.session_state.appointments
            if appointment["Status"] == "Waiting"
        ]

        if active:

            token_options = [
                appointment["Token"]
                for appointment in active
            ]

            selected_token = st.selectbox(
                "Select appointment to cancel",
                token_options
            )

            if st.button(
                "❌ Cancel Appointment",
                use_container_width=True
            ):

                for appointment in st.session_state.appointments:

                    if (
                        appointment["Token"]
                        == selected_token
                    ):

                        appointment["Status"] = "Cancelled"

                st.success(
                    "Appointment cancelled successfully."
                )

                st.rerun()


        csv_data = history_df.to_csv(
            index=False
        )

        st.download_button(
            "📥 Download Appointment History",
            csv_data,
            "mediqueue_appointments.csv",
            "text/csv",
            use_container_width=True
        )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    st.header("📊 Hospital Analytics")

    if not st.session_state.appointments:

        st.info(
            "Book some appointments to generate analytics."
        )

    else:

        df = pd.DataFrame(
            st.session_state.appointments
        )

        # Department
        st.subheader(
            "🏥 Appointments by Department"
        )

        department_data = (
            df["Department"]
            .value_counts()
        )

        st.bar_chart(
            department_data
        )


        # Doctor
        st.subheader(
            "👨‍⚕️ Appointments by Doctor"
        )

        doctor_data = (
            df["Doctor"]
            .value_counts()
        )

        st.bar_chart(
            doctor_data
        )


        # Status
        st.subheader(
            "📋 Appointment Status"
        )

        status_data = (
            df["Status"]
            .value_counts()
        )

        st.bar_chart(
            status_data
        )


        # Date
        st.subheader(
            "📅 Appointments by Date"
        )

        date_data = (
            df["Date"]
            .value_counts()
            .sort_index()
        )

        st.line_chart(
            date_data
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🏥 MediQueue | Smart Hospital OP Booking & Queue Management"
)