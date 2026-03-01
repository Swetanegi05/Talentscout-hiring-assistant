import streamlit as st
from openai import OpenAI

# Configure OpenAI client (using OpenRouter as the key is an OpenRouter key: sk-or-v1-...)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"],
)

def generate_questions(tech_stack):
    try:
        prompt = f"""You are a senior technical recruiter. Generate 3 to 5 high-quality, challenging technical interview questions based specifically on the following tech stack. Keep them concise.
        
Tech Stack: {tech_stack}
Generate the questions."""
        
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating questions. Please check your API key. Details: {e}"

# Set page config
st.set_page_config(page_title="TalentScout - AI Hiring Assistant", page_icon="🤖", layout="wide")

st.title("🤖 TalentScout - AI Hiring Assistant")
st.markdown("Welcome! I'm here to gather some information and generate custom interview questions for you.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm TalentScout. Could you please provide your **Full Name**?"}]
if "step" not in st.session_state:
    st.session_state.step = 0
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {
        "Full Name": "",
        "Email": "",
        "Phone Number": "",
        "Years of Experience": "",
        "Current Role": "",
        "Tech Stack": ""
    }
if "finished" not in st.session_state:
    st.session_state.finished = False

# Sidebar for Candidate Summary
with st.sidebar:
    st.header("📋 Candidate Summary")
    st.markdown("---")
    for key, value in st.session_state.candidate_info.items():
        st.write(f"**{key}:** {value if value else 'Pending...'}")
    
    st.markdown("---")
    if st.button("Finish Process", disabled=st.session_state.finished):
        st.session_state.finished = True
        st.session_state.messages.append({"role": "assistant", "content": "Thank you for sharing your details with TalentScout! Your session is now finished."})
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input logic
if not st.session_state.finished:
    if prompt := st.chat_input("Type your answer here..."):
        # Add user response to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Process answer based on current step
        step = st.session_state.step
        
        with st.chat_message("assistant"):
            if step == 0:
                st.session_state.candidate_info["Full Name"] = prompt
                next_prompt = "Great! What is your **Email address**?"
                st.markdown(next_prompt)
                st.session_state.messages.append({"role": "assistant", "content": next_prompt})
                st.session_state.step += 1
                
            elif step == 1:
                st.session_state.candidate_info["Email"] = prompt
                next_prompt = "Got it. Please provide your **Phone Number**."
                st.markdown(next_prompt)
                st.session_state.messages.append({"role": "assistant", "content": next_prompt})
                st.session_state.step += 1
                
            elif step == 2:
                st.session_state.candidate_info["Phone Number"] = prompt
                next_prompt = "Thanks. How many **Years of Experience** do you have?"
                st.markdown(next_prompt)
                st.session_state.messages.append({"role": "assistant", "content": next_prompt})
                st.session_state.step += 1
                
            elif step == 3:
                st.session_state.candidate_info["Years of Experience"] = prompt
                next_prompt = "Excellent. What is your **Current Role**?"
                st.markdown(next_prompt)
                st.session_state.messages.append({"role": "assistant", "content": next_prompt})
                st.session_state.step += 1
                
            elif step == 4:
                st.session_state.candidate_info["Current Role"] = prompt
                next_prompt = "Finally, could you list your primary **Tech Stack**?"
                st.markdown(next_prompt)
                st.session_state.messages.append({"role": "assistant", "content": next_prompt})
                st.session_state.step += 1
                
            elif step == 5:
                st.session_state.candidate_info["Tech Stack"] = prompt
                st.markdown("Thank you! Generating your technical interview questions based on your stack...")
                st.session_state.messages.append({"role": "assistant", "content": "Thank you! Generating your technical interview questions based on your stack..."})
                
                with st.spinner("Thinking..."):
                    questions = generate_questions(prompt)
                    
                st.markdown("### Technical Interview Questions\n" + questions)
                st.session_state.messages.append({"role": "assistant", "content": "### Technical Interview Questions\n" + questions})
                
                st.markdown("We have collected all necessary information. You can review your summary in the sidebar or click 'Finish Process'.")
                st.session_state.messages.append({"role": "assistant", "content": "We have collected all necessary information. You can review your summary in the sidebar or click 'Finish Process'."})
                st.session_state.step += 1
                
        st.rerun()

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray; font-size: small;'>*Privacy Note: Your data is collected solely for the interview generation process and is not persistently stored.*</div>", unsafe_allow_html=True)
