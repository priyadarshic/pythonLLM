import base64

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)


# Ensure you have a video file named 'example_video.mp4' or provide the correct path.
video_file_path = "C:\\Users\\myclo\\Videos\\11903954_2160_3840_60fps.mp4"
video_mime_type = "video/mp4"


with open(video_file_path, "rb") as video_file:
    encoded_video = base64.b64encode(video_file.read()).decode("utf-8")

message = HumanMessage(
    content=[
        {"type": "text", "text": "Describe the first few frames of the video."},
        {
            "type": "media",
            "data": encoded_video,  # Use base64 string directly
            "mime_type": video_mime_type,
        },
    ]
)
response = llm.invoke([message])  # Uncomment to run
print(f"Response for video: {response.content}")