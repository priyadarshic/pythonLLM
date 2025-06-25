import base64
import cv2
import numpy as np
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash-preview-image-generation")

message = {
    "role": "user",
    "content": "Generate a photorealistic image of a cuddly cat wearing a hat.",
}

response_ai = llm.invoke(
    [message], generation_config=dict(response_modalities=["TEXT", "IMAGE"]),
)


def _get_image_base64(response: AIMessage) -> None:
    image_block = next(
        block
        for block in response.content
        if isinstance(block, dict) and block.get("image_url")
    )
    return image_block["image_url"].get("url").split(",")[-1]


# image_base64 = _get_image_base64(response_ai)
# print(image_base64)
decoded_bytes = base64.b64decode(_get_image_base64(response_ai))

np_array = np.frombuffer(decoded_bytes, np.uint8)
image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

cv2.imwrite("decoded_image.jpg", image)
cv2.imshow("Decoded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
