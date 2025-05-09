import streamlit as st
import random
import yagmail
import time

from app import main

# Initialize session state
if 'otp_sent' not in st.session_state:
    st.session_state['otp_sent'] = False
if 'generated_otp' not in st.session_state:
    st.session_state['generated_otp'] = None
if 'email' not in st.session_state:
    st.session_state['email'] = ""
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'otp_sent_time' not in st.session_state:
    st.session_state['otp_sent_time'] = 0

# Wrap everything into a function
def login():
    def send_otp_email(receiver_email, otp):
        sender_email = "aaryaborakhade@gmail.com"
        sender_password = "nmszgmoedqdhgazz"

        try:
            yag = yagmail.SMTP(sender_email, sender_password)
            subject = "Your OTP Code"
            contents = f"Your OTP code is {otp}. It will expire in 2 minutes."
            yag.send(to=receiver_email, subject=subject, contents=contents)
            return True
        except Exception as e:
            st.error(f"Error sending email: {e}")
            return False

    st.markdown("<p style='font-size:30px; font-weight:bold;'>🔐 Login</p>", unsafe_allow_html=True)

    if not st.session_state['authenticated']:
        # Email input and Send OTP button
        st.session_state['email'] = st.text_input("Enter your email")
        if st.button("Send OTP"):
            if st.session_state['email']:
                otp = random.randint(100000, 999999)
                success = send_otp_email(st.session_state['email'], otp)
                if success:
                    st.session_state['generated_otp'] = otp
                    st.session_state['otp_sent'] = True
                    st.session_state['otp_sent_time'] = time.time()
                    st.success("OTP has been sent to your email.")
            else:
                st.warning("Please enter your email first.")

        # OTP input and Verify OTP button
        entered_otp = st.text_input("Enter OTP", type="password")
        if st.button("Verify OTP"):
            if not st.session_state['otp_sent']:
                st.warning("OTP has not been sent yet.")
            else:
                time_elapsed = time.time() - st.session_state['otp_sent_time']
                if time_elapsed > 120:
                    st.error("OTP expired. Please resend.")
                    st.session_state['otp_sent'] = False
                elif entered_otp == str(st.session_state['generated_otp']):
                    st.session_state['authenticated'] = True
                    st.success("✅ OTP Verified. You are logged in.")
                else:
                    st.error("❌ Incorrect OTP.")

        if st.session_state['otp_sent']:
            if st.button("Resend OTP"):
                st.session_state['otp_sent'] = False
                st.experimental_rerun()

    else:
        st.success(f"Welcome {st.session_state['email']}! 🎉 You are logged in.")



